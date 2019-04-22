from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key = True)
    userAccount = models.CharField(max_length = 30, unique = True)
    userPassword = models.CharField(max_length = 30)
    userNickname = models.CharField(max_length = 30, null=True)
    userQQ = models.CharField(max_length = 30, null = True)
    userSign = models.CharField(max_length = 200, null = True)
    userPicture = models.CharField(max_length = 200, null = True)

class USER_upload(models.Model):
    userID = models.ForeignKey('User', to_field = 'userID', on_delete = models.CASCADE, null = True) 
    title = models.CharField(max_length = 100)
    datetime = models.DateTimeField(auto_now=True, null=True)
    content = models.CharField(max_length = 1000)
    Picture = models.CharField(max_length = 200)
    num = models.AutoField(primary_key = True)

class Replays(models.Model):
    replay_num = models.AutoField(primary_key = True)
    num = models.ForeignKey('USER_upload', to_field = 'num', on_delete = models.CASCADE, null = True)
    replay = models.CharField(max_length = 1000)
    replay_date = models.DateTimeField(auto_now=True, null=True)
    userID = models.ForeignKey('User', to_field = 'userID', on_delete = models.CASCADE, null = True)

class Post_like(models.Model):
    num = models.ForeignKey('USER_upload', to_field = 'num', on_delete = models.CASCADE, null = True)
    userID = models.ForeignKey('User', to_field = 'userID', on_delete = models.CASCADE, null = True) 
    is_like = models.BooleanField(null=True)

class user_attention(models.Model):
    attentions = models.ForeignKey('User', to_field = 'userID', on_delete = models.CASCADE, null = True)
    attentiond = models.CharField(max_length = 30, null=True)