from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views
from django.conf.urls import url

urlpatterns = [
    
    # path('', views.home,name="home"),
    path('home/', views.HomeView.as_view()),
    path('', RedirectView.as_view(url='home/')),
    
    path('notice/', views.NoticeListView.as_view(),name="notice"),
    path('notice/<int:pk>', views.NoticeDetailListView.as_view()),
   
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/students")),
<<<<<<< HEAD
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<int:pk>/', views.profiledetailview),
    path('profiles/follow/<int:pk>',views.follow),
=======
    path('mypost/edit/<int:pk>', views.MyPostUpdateView.as_view(success_url="/students")),
    path('memories/albums/',views.AlbumsListView.as_view()),
    path('memories/albums/<int:pk>',views.AlbumsDetailView.as_view()),
   
>>>>>>> 0d49cea8e5ab538566f3a9dc1765ea1d84365c3a
    
    path('mypost/edit/<int:pk>', views.MyPostUpdateView.as_view(success_url="/students")),
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/students/mypost")),
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/students/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

<<<<<<< HEAD
    # path('about/', views.AboutView.as_view()),
    path('about/', views.about,name="about"),
    path('memories/',views.memories,name="memories"),
    path('memories/<int:pk>/',views.albumdetail),
=======
    path('profiles/', views.ProfileListView.as_view()),

    path('post/',views.PostsListView.as_view()), # All post of all users
    path('profiles/<int:pk>/post',views.OtherPostListView.as_view()),
    
    path('profiles/<int:pk>', views.ProfileDetailView.as_view()),
    path('profiles/<int:pk>/post',views.PostsListView.as_view()),

    path('profiles/follow/<int:pk>',views.follow),

    # path('about/', views.AboutView.as_view()),
    path('about/', views.about,name="about"),
    path('memories/', views.MemoriesListView.as_view(),name="memories"),
>>>>>>> 0d49cea8e5ab538566f3a9dc1765ea1d84365c3a
    
]
