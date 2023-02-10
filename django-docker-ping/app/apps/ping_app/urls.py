from django.urls import include, path
from apps.ping_app.views import PingView

urlpatterns = [
    path('v1/ping/', PingView.as_view(), name='ping'),


]
