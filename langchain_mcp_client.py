import asyncio
from dotenv import load_dotenv
load_dotenv()
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

async def main():
    async with MultiServerMCPClient() as client:
        await client.initialize()
        print("client initialized")
        agent = create_react_agent(llm,client.tools)
        result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in New York and what is 54 + 2 * 3?"}]})
        print(result["messages"][-1].content)


