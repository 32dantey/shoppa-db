from django.urls import path
from .views import UserSerializerListView

urlpatterns = [
    path('', UserSerializerListView.as_view()),
]