from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views
from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'notice', views.NoticeViewSet)
router.register(r'branch', views.BranchViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'post', views.MyPostViewSet)
router.register(r'user', views.UsertViewSet)

urlpatterns = [
    path(r'api/',include(router.urls)),
    path(r'api-token-auth',obtain_jwt_token),
    
    # path('', views.home,name="home"),
    path('home/', views.HomeView.as_view()),
    path('', RedirectView.as_view(url='home/')),
    
    path('notice/', views.NoticeListView.as_view(),name="notice"),
    path('notice/<int:pk>', views.NoticeDetailListView.as_view()),
   
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/students")),
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<int:pk>/', views.profiledetailview),
    path('profiles/follow/<int:pk>',views.follow),
    
    path('mypost/edit/<int:pk>', views.MyPostUpdateView.as_view(success_url="/students")),
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/students/mypost")),
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/students/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

    # path('about/', views.AboutView.as_view()),
    path('about/', views.about,name="about"),
    path('memories/',views.memories,name="memories"),
    path('memories/<int:pk>/',views.albumdetail),
    
]
