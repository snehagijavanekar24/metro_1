from django.urls import path
from.import views

urlpatterns = [
    path('mp/',views.Member_API.as_view()),
    path('mp/<int:pk>/', views.Member_API.as_view())
]
