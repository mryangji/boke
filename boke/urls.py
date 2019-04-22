"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage),
    path('<int:pagenum>/', views.MainPage),
    path('login&register/', views.login_register),  # 登录注册页面
    path('register/', views.register_page),  # 注册
    path('logindPage/<str:pagenum>/', views.logind),  # 进入用户主界面之前的参数设置
    path('logindPage/', views.logind),  # 进入用户主界面之前的参数设置
    path('logintoPage/', views.logintoLPage),  # 登录
    path('Judgment/', views.Judgment),  # 判断账户状态
    path('user_setting/', views.Usersteeing),  # 进入用户设置页面参数设置
    path('userPict_change/', views.userPict_change),  # 设置界面图片保存回显
    path('save_user/', views.Save_setting),  # 保存用户设置
    path('Upload/', views.Upload),  # 发布博文
    path('U_pict_upload/', views.U_pict_upload),  # 发图片
    path('replay/<str:num>/', views.Replay_page),  # 进入回复页面
    path('replay/<str:num>/<int:pagenum>/', views.Replay_page),
    path('replay_post/<str:num>/<int:pagenum>/', views.Replay_post),  # 回复内容保存
    path('like/', views.Like),  # 点赞
    path('dislike/', views.disLike),  # 踩它
    path('attention/', views.Attention),  # 加关注
    path('myboke/', views.Myboke),  # 展示个人博文
    path('myboke/<int:pagenum>/', views.Myboke),
    path('del/', views.Del),  # 删除博文
    path('chaxun/', views.chaxun),
    path('permass/<str:userid>/', views.permass),

    path('out/', views.OUT),  # 退出当前账户，删除session
    path('sendfile/', views.asd),
    path('aaaa/', views.aaaa),
    path('bbb/', views.bbb),
]
