# api.py
from ninja import NinjaAPI, Schema

api = NinjaAPI()

class AddRequest(Schema):
    a: float
    b: float

class AddResponse(Schema):
    result: float

@api.get("/health")
def health(request):
    return {"status": "ok"}

@api.post("/echo")
def echo(request, message: str, meta: dict = None):
    return {"received": {"message": message, "meta": meta or {}}}

@api.post("/add", response=AddResponse)
def add(request, payload: AddRequest):
    return {"result": payload.a + payload.b}
