# LangGraph MCP Baseline (Django + OpenAI)

This is a baseline implementation of an **AI agent using LangGraph** with a **Django backend**.  
It exposes a simple `/api/chat/` endpoint where you can send user messages and receive responses powered by OpenAI.  

---

## 📦 Features
- Uses **LangGraph** to define a simple agent workflow  
- Backend built with **Django REST Framework**  
- Compatible with **uv** (no pip required)  
- Loads **OpenAI API key** securely from `.env`  
- Minimal setup — easy to extend into a full MCP agent  

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/langgraph-mcp-baseline.git
cd langgraph-mcp-baseline
```

### 2. Create and activate environment
```bash
uv venv langgraph-mcp-baseline
source langgraph-mcp-baseline/bin/activate
```
### 3. Install dependencies
```bash
uv pip install django djangorestframework langgraph langchain langchain-community openai python-dotenv
```
### 4. Add openAI key
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=sk-yourkeyhere
```
### 5. Run migrations
```bash
python manage.py migrate
```
### 6. Start the dev server
```bash
python manage.py runserver
```
## API Usage

### Endpoint

`POST /api/chat/`

```bash
curl -X POST http://127.0.0.1:8000/api/chat/ \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, agent!"}'
```

### Example response
```json
{
  "output": "Hello! I'm your LangGraph agent, ready to assist."
}
```

### Project Structure
```bash
langgraph-mcp-baseline/
├── agents/
│   └── agent.py          # LangGraph agent definition
├── api/
│   └── views.py          # API endpoint using Django REST Framework
├── langgraph_backend/
│   └── settings.py       # Django settings
├── manage.py
├── main.py
├── README.md
└── .env
```