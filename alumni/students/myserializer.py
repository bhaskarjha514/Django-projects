from rest_framework import serializers
from .models import Branch, Notice, Profile, MyPost
from django.contrib.auth.models import User

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class MyPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyPost
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
