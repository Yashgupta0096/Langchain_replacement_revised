from xagent import Dispatcher, Planner, Actor
from xagent.dispatcher import Task
from xagent.actor import ToolServer
from config import Config
from services.run_log import RunLogsManager
from typings.agent import AgentWithConfigsOutput

class DialogueAgentWithToolsXAgent:
    def __init__(
        self,
        name: str,
        agent_with_configs: AgentWithConfigsOutput,
        system_message: SystemMessage,
        model: ChatOpenAI,
        tools: List[any],
        session_id: str,
        sender_name: str,
        is_memory: bool = False,
        run_logs_manager: Optional[RunLogsManager] = None,
        **tool_kwargs,
    ) -> None:
        self.tools = tools
        self.session_id = session_id
        self.sender_name = sender_name
        self.is_memory = is_memory
        self.run_logs_manager = run_logs_manager

    def send(self) -> str:
        memory: ToolServer

        memory = ToolServer(
            'memory',
            session_id=str(self.session_id),
            url=Config.TOOL_SERVER_URL,
            api_key=Config.TOOL_SERVER_API_KEY,
            return_messages=True,
        )

        memory.human_name = self.sender_name
        memory.ai_name = self.agent_with_configs.agent.name
        memory.auto_save = False

        callbacks = []

        if self.run_logs_manager:
            callbacks.append(self.run_logs_manager.get_agent_callback_handler())

        task = Task(
            task_type='chat',
            task_id=str(self.session_id),
            content="\n".join(self.message_history + [self.prefix]),
            tools=self.tools,
            memory=memory,
            configs=self.agent_with_configs.configs,
            callbacks=callbacks,
        )

        dispatcher = Dispatcher([task])
        planner = Planner()
        actor = Actor()

        dispatcher.dispatch(planner, actor)

        res = task.get_result()

        return res
