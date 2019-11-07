from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator

class Branch(models.Model):
    name = models.CharField(max_length=20, default="", choices=(("CSE","CSE"),("ME","ME"),("CIVIL","CIVIL"),("ECE","ECE"),("BBA","BBA"),("MBA","MBA")))
    hod = models.CharField(max_length=100)
    batch = models.CharField(max_length=30,default="")
    def __str__(self):
        return "%s" %self.name

class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="students/notice/images",blank=True,null=True)
    venue = models.TextField(null=True)
    contact_detail = models.TextField(null=True)
    

class Profile(models.Model):
    name = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=150, null=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    pic = models.ImageField(upload_to="students/profile/images",blank=True,null=True)
    description= models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20, default="single", choices=(("single","single"), ("married","married"), ("widow","widow"), ("sepreted","seprated"),("commited","commited"))) 
    gender = models.CharField(max_length=20, default="female", choices=(("male","male"),("female","female")))
    address = models.TextField(null=True)
    current_job = models.TextField(null=True)

    def __str__(self):
        # return "%s (%s)" % (self.user.username, self.branch)
        return "%s" %self.user.username
    # def __str__(self):
    #     return self.subject

class MyPost(models.Model):
    pic = models.ImageField(upload_to="students/profile/post",blank=True,null=True)
    subject = models.CharField(max_length = 200)   
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add = True)
    uploaded_by = models.ForeignKey(to=Profile, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" %self.subject

# class Memories(models.Model):
#     image = models.ImageField(upload_to="students/memories")
    # memoriesalbum = models.ForeignKey(to=MemoriesPic,on_delete=CASCADE)

# class MemoriesPic (models.Model):
#     image = models.ImageField(upload_to ="students/memories/Albums")

class Albums(models.Model):
    image = models.ImageField(upload_to ="students/memories/Albums")
    meetupplace = models.CharField(max_length =200)
    # MemoriesPic = models.OneToOneField(to=MemoriesPic, on_delete=CASCADE)
    def __str_(self):
        return self.meetupplace

class pictures(models.Model):
    album = models.ForeignKey(Albums,on_delete=CASCADE)
    pic = models.ImageField(upload_to="students/memories/Albums")
    picno = models.IntegerField(null = True)
    def __str_(self):
        return self.picno

class PostComment(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to=User, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add = True)
    flag = models.CharField(max_length=20, null=True,blank=True, choices=(("racist","racist"),("abusing","abusing")))
    def __str__(self):
        return "%s" %self.msg

class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=User, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return "%s" %self.liked_by

class FollowUser(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=Profile, on_delete=CASCADE, related_name ="followed_by")
    def __str__(self):
        return "%s" %self.followed_by

# Create your models here.
