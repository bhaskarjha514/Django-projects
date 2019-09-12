from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    
    # path('', views.home,name="home"),
    path('home/', views.HomeView.as_view()),
    path('', RedirectView.as_view(url='home/')),
    path('notice/', views.NoticeListView.as_view(),name="notice"),
    path('notice/<int:pk>', views.NoticeDetailListView.as_view()),
   
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/students")),
   
    
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/students/mypost")),
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/students/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<int:pk>', views.ProfileDetailView.as_view()),
    path('profiles/follow/<int:pk>',views.follow),

    path('about/', views.AboutView.as_view()),
    
    

]
