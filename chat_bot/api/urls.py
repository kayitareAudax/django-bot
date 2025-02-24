from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.getData),
    path('chat/',include("chat_bot.api.chat.urls")),
    path('users/',include("chat_bot.api.users.urls"))
]