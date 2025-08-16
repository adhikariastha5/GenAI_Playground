# Flask + MCP Demo Setup

## 1. Install dependencies
This project uses a virtual environment created with uv or pip.
If you don’t have uv installed, you can also use pip.

### Option A: with uv (recommended)
uv sync

### Option B: with pip
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install flask httpx "mcp[cli]"

---

## 2. Start the Flask API
Run this in one terminal:

    python app.py

This starts the Flask API on http://127.0.0.1:5000

---

## 3. Configure Cline (VS Code)
Edit the file:

    ~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json

Add this section (update the path if needed):

{
  "mcpServers": {
    "flask-tools": {
      "command": "<absolute_path_to_project>/.venv/bin/python",
      "args": ["mcp_server.py"],
      "cwd": "<absolute_path_to_project>"
    }
  }
}

---

## 4. Use in Cline
Reload VS Code → Open Cline.

Now you can run commands like:

    @tool health
    @tool add a=2 b=5
    @tool echo message="Hello world"

---

## Notes
- Only **app.py** (the Flask API) must be running manually.
- Cline will automatically launch **mcp_server.py** in the background.
