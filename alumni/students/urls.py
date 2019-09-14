from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailListView.as_view()),
    path('about/',views.about)
]
