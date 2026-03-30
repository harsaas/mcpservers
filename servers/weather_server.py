from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "Always Hot as hell"

if __name__ == "__main__":
    mcp.run(transport="sse")
#sse - server sent events, a protocol for pushing updates from a server to a client in real-time via http. In this case, the weather server can use sse to send real-time weather updates to clients that are subscribed to the weather updates.