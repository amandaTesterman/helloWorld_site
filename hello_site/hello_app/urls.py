from django.urls import path

from hello_app.views import HelloWorldView
from hello_app.views import HelloNameView

urlpatterns = [
    path('world', HelloWorldView.as_view(), name='home'),
    path('<str:name>', HelloNameView.as_view()),
 
]