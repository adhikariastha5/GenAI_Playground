from django.urls import path
from .views import AgentView

urlpatterns = [
    path("chat/", AgentView.as_view(), name="agent-chat"),
]
