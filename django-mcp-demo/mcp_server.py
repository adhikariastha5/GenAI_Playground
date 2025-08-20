# mcp_server.py
import os
import httpx
from typing import TypedDict, Optional
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession

print("Starting Django MCP server...")

API_BASE = os.environ.get("DJANGO_API_URL", "http://127.0.0.1:8000/api")

mcp = FastMCP("Django-Ninja Tools")

class AddResult(TypedDict):
    result: float

# ----------------------
# Tools
# ----------------------
@mcp.tool()
def health(ctx: Context[ServerSession, None]) -> str:
    """Check health of the Django API."""
    try:
        r = httpx.get(f"{API_BASE}/health", timeout=5)
        r.raise_for_status()
        return r.json().get("status", "unknown")
    except Exception as e:
        return f"Error connecting to Django API: {e}"

@mcp.tool()
def echo(message: str, meta: Optional[dict] = None) -> dict:
    """Echo back a message via Django API."""
    payload = {"message": message, "meta": meta or {}}
    try:
        r = httpx.post(f"{API_BASE}/echo", json=payload, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def add(a: float, b: float) -> AddResult:
    """Add two numbers via Django API."""
    try:
        r = httpx.post(f"{API_BASE}/add", json={"a": a, "b": b}, timeout=5)
        r.raise_for_status()
        data = r.json()
        return {"result": float(data.get("result", 0))}
    except Exception as e:
        return {"error": str(e)}

# ----------------------
# Prompts
# ----------------------
@mcp.prompt()
def hello_prompt(ctx: Context, name: str = "world") -> str:
    """Simple test prompt to verify MCP integration."""
    return f"Hello, {name}! Django MCP server is alive 🚀"

# ----------------------
# Entry Point
# ----------------------
if __name__ == "__main__":
    print("Running MCP server with tools: health, echo, add and prompt: hello_prompt")
    mcp.run()
