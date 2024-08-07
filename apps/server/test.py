from xagent import Dispatcher, Planner, Actor
from xagent.dispatcher import Task
from xagent.actor import ToolServer
from config import Config

def agent_factory():
    # Initialize XAgent components
    dispatcher = Dispatcher()
    planner = Planner()
    actor = Actor()

    # Initialize ToolServer
    tool_server = ToolServer('tools', url=Config.TOOL_SERVER_URL, api_key=Config.TOOL_SERVER_API_KEY)

    return dispatcher, planner, actor, tool_server

dispatcher, planner, actor, tool_server = agent_factory()

client = Client()

# Create task
task = Task(
    task_type='chat',
    task_id='test-task',
    content='Who is Leo DiCaprio\'s girlfriend? What is her current age raised to the 0.43 power?',
    tools=tool_server,
)

# Dispatch task to planner and actor
dispatcher.dispatch(planner, actor, task)

# Get result
result = task.get_result()

print(result)
