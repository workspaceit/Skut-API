from django.urls import path, include
from areas import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.AreaList.as_view()),
    path('<uuid:guid>/', views.AreaDetail.as_view())
]