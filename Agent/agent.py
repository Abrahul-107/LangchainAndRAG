from langchain.agents import AgentType, initialize_agent
from langchain.agents import load_tools  
from langchain_together import ChatTogether
from langchain_together import ChatTogether
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("API_KEY")
print(API_KEY)

chat = ChatTogether(
    together_api_key=API_KEY,
    model="meta-llama/Llama-3-70b-chat-hf",
)
# Load tools with the Together AI instance
tools = load_tools(['wikipedia', 'llm-math'], llm=chat)

# Initialize the agent with the tools and Together AI
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Run the agent with the query
ans_birth = agent.invoke("When was Elon musk born? Please provide just the year.What is his age right now in 2024, Please provide just the age with birth year.")
print(ans_birth)