from xagent import Dispatcher, Planner, Actor
from xagent.dispatcher import Task
from xagent.actor import ToolServer
from config import Config
from services.voice import speech_to_text, text_to_speech
from postgres import PostgresChatMessageHistory
from services.pubsub import ChatPubSubService
from services.run_log import RunLogsManager
from typings.config import AccountSettings, AccountVoiceSettings
from utils.system_message import SystemMessageBuilder

class ConversationalAgentXAgent:
    def run(
        self,
        settings: AccountSettings,
        voice_settings: AccountVoiceSettings,
        chat_pubsub_service: ChatPubSubService,
        agent_with_configs: AgentWithConfigsOutput,
        tools,
        prompt: str,
        voice_url: str,
        history: PostgresChatMessageHistory,
        human_message_id: str,
        run_logs_manager: RunLogsManager,
        pre_retrieved_context: str,
    ):
        memory = ToolServer(
            'memory',
            session_id=str(self.session_id),
            url=Config.TOOL_SERVER_URL,
            api_key=Config.TOOL_SERVER_API_KEY,
            return_messages=True,
        )

        memory.human_name = self.sender_name
        memory.ai_name = agent_with_configs.agent.name

        system_message = SystemMessageBuilder(
            agent_with_configs, pre_retrieved_context
        ).build()

        res: str

        try:
            if voice_url:
                configs = agent_with_configs.configs
                prompt = speech_to_text(voice_url, configs, voice_settings)

            task = Task(
                task_type='conversation',
                task_id=str(self.session_id),
                content=prompt,
                tools=tools,
                memory=memory,
                configs=configs,
                callbacks=[run_logs_manager.get_agent_callback_handler()],
            )

            dispatcher = Dispatcher([task])
            planner = Planner()
            actor = Actor()

            dispatcher.dispatch(planner, actor)

            res = task.get_result()

        except Exception as err:
            # handle error
            pass

        try:
            configs = agent_with_configs.configs
            voice_url = None
            if "Voice" in configs.response_mode:
                voice_url = text_to_speech(res, configs, voice_settings)
                
        except Exception as err:
            # handle error
            pass

        ai_message = history.create_ai_message(
            res,
            human_message_id,
            agent_with_configs.agent.id,
            voice_url,
        )

        chat_pubsub_service.send_chat_message(chat_message=ai_message)

        return res
