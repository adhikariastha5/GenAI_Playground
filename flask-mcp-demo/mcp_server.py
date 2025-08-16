import os
import httpx
from typing import TypedDict, Optional

from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession

API_BASE = os.environ.get("FLASK_API_URL", "http://127.0.0.1:5000")

mcp = FastMCP("Flask Tools")

class AddResult(TypedDict):
    result: float

@mcp.tool()
def health(ctx: Context[ServerSession, None]) -> str:
    """
    Calls GET /health on the Flask API.
    """
    r = httpx.get(f"{API_BASE}/health", timeout=5)
    r.raise_for_status()
    return r.json().get("status", "unknown")

@mcp.tool()
def echo(message: str, meta: Optional[dict] = None) -> dict:
    """
    Calls POST /echo with a JSON body.
    """
    payload = {"message": message, "meta": meta or {}}
    r = httpx.post(f"{API_BASE}/echo", json=payload, timeout=5)
    r.raise_for_status()
    return r.json()

@mcp.tool()
def add(a: float, b: float) -> AddResult:
    """
    Calls POST /add with numbers a and b.
    Returns structured output: { "result": number }
    """
    r = httpx.post(f"{API_BASE}/add", json={"a": a, "b": b}, timeout=5)
    r.raise_for_status()
    data = r.json()
    if "result" not in data:
        # surface API error shape
        raise ValueError(f"API error: {data}")
    return {"result": float(data["result"])}

if __name__ == "__main__":
    import asyncio
    mcp.run()
