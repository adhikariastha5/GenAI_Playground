from rest_framework.views import APIView
from rest_framework.response import Response
from agents.agent import graph

class AgentView(APIView):
    def post(self, request):
        user_input = request.data.get("input", "")
        result = graph.invoke({"input": user_input})
        # The graph returns a dict with "output"
        return Response({"output": result.get("output", "")})
