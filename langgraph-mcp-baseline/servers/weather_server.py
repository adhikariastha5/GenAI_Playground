from mcp.server.fastmcp import FastMCPServer
import httpx

server = FastMCPServer("weather")

@server.tool()
def get_weather(city: str) -> str:
    # Fake weather for demo
    return f"The weather in {city} is sunny 25°C."

if __name__ == "__main__":
    server.run()
