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
    path('mypost/edit/<int:pk>', views.MyPostUpdateView.as_view(success_url="/students")),
    path('memories/albums/',views.AlbumsListView.as_view()),
    path('memories/albums/<int:pk>',views.AlbumsDetailView.as_view()),
   
    
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/students/mypost")),
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/students/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

    path('profiles/', views.ProfileListView.as_view()),

    path('post/',views.PostsListView.as_view()), # All post of all users
    path('profiles/<int:pk>/post',views.OtherPostListView.as_view()),
    
    path('profiles/<int:pk>', views.ProfileDetailView.as_view()),
    path('profiles/<int:pk>/post',views.PostsListView.as_view()),

    path('profiles/follow/<int:pk>',views.follow),

    # path('about/', views.AboutView.as_view()),
    path('about/', views.about,name="about"),
    path('memories/', views.MemoriesListView.as_view(),name="memories"),
    
    
    

]
