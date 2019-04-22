from django.shortcuts import render
from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from app import models
from django.core.paginator import Paginator, EmptyPage  # 分页类
import os


# Create your views here.


def MainPage(req, pagenum=1):
    sql = '''select app_user_upload.userID_id, 
            app_user_upload.datetime, 
            app_user_upload.content, 
            app_user_upload.title, 
            app_user_upload.Picture, 
            app_user_upload.num,
            app_user.userNickname, 
            app_user.userPicture,
            app_user.userID 
            from app_user, app_user_upload 
            where app_user.userID = app_user_upload.userID_id
            order by app_user_upload.num desc'''
    content = models.User.objects.raw(sql)
    Page = toNextPage(int(pagenum), content, 5)  # 调用分页函数（页码， content， 每页展示数量）
    page_sum = range(1, Page['total_page'] + 1)
    C_dict = {'posts': Page['dataList'],
              'nowPage': Page['nowPage'],
              'total_page': Page['total_page'],
              'page_sum': page_sum
              }
    return render(req, 'mainPage.html', C_dict)


def login_register(req):  # 登录注册页面
    return render(req, 'login&registe.html')


def register_page(req):  # 注册
    useraccount = req.POST.get('account')
    userpassword = req.POST.get('pass_word')
    # try:
    data = ['这家伙很懒，什么都没有留下', '\\static\\img\\tolerant.jpg']
    userObj = models.User(userAccount=useraccount, userPassword=userpassword, userNickname=useraccount, userQQ='',
                          userSign=data[0], userPicture=data[1])
    try:
        userObj.save()
        req.session['account'] = useraccount
        return HttpResponseRedirect('/logindPage/')
    except:  # 账号注册重复了从这儿走
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'a', max_age=1)
        return resp


def logind(req, pagenum=1):  # 进入用户主界面之前的参数设置
    print('-------------------------------------------')
    try:
        account = req.session.get('account')
        accountMass = models.User.objects.get(userAccount=account)
        userid = accountMass.userID
        USER_Nickname = accountMass.userNickname
        USER_sign = accountMass.userSign
        USER_picture = accountMass.userPicture
        like_obj = models.user_attention.objects.filter(attentions=userid)
        like_num = len(like_obj)
        fans_obj = models.user_attention.objects.filter(attentiond=userid)
        fans_num = len(fans_obj)
        boke_obj = models.USER_upload.objects.filter(userID=userid)
        boke_num = len(boke_obj)
        sql1 = '''
            select distinct tab4.*, app_user_attention.attentiond from(
                select tabledislike.dislike, table2.* from
                (
                    select tab1.num, tablelike.lik, tab1.* from
                    (
                        select distinct tab1.*, 
                            app_post_like.num_id, 
                            app_post_like.userID_id, 
                            app_post_like.is_like 
                        from 
                        (
                            select app_user_upload.datetime, 
                                app_user_upload.content, 
                                app_user_upload.title, 
                                app_user_upload.Picture, 
                                app_user_upload.num,
                                app_user.userNickname, 
                                app_user.userPicture,
                                app_user.userID 
                            from app_user, app_user_upload 
                            where app_user.userID = app_user_upload.userID_id
                            order by app_user_upload.num desc
                        ) tab1 
                        LEFT JOIN app_post_like  
                        on app_post_like.userID_id = %d and tab1.num = app_post_like.num_id 
                    ) tab1
                    left join
                    (
                        select count(liketab.is_like) lik, 
                            liketab.num_id 
                        from 
                        ( 
                            select app_post_like.num_id, 
                                app_post_like.is_like 
                            from app_post_like where app_post_like.is_like = 1
                        ) liketab 
                        group by liketab.num_id
                    ) tablelike  
                    on tab1.num = tablelike.num_id
                ) table2 left join
                    (
                        select count(disliketab.is_like) dislike, 
                                disliketab.num_id 
                        from 
                            ( 
                                select app_post_like.num_id, 
                                    app_post_like.is_like 
                                from app_post_like 
                                where app_post_like.is_like = 0
                            ) disliketab 
                        group by disliketab.num_id
                    ) tabledislike 
                    on table2.num = tabledislike.num_id
            ) tab4 left join 
            app_user_attention 
            on tab4.userID = app_user_attention.attentiond 
            and app_user_attention.attentions_id = %d
            ''' % (userid, userid)
        content = models.User.objects.raw(sql1)
        Page = toNextPage(int(pagenum), content, 3)
        page_sum = range(1, Page['total_page'] + 1)
        print('______________________', userid)
        try:
            sql3 = '''
                    select app_user.userNickname,
                           app_user.userID 
                    from app_user_attention, app_user 
                    where app_user_attention.attentiond = app_user.userID 
                          and app_user_attention.attentions_id = %d
                  ''' % userid
            lik_obj = models.User.objects.raw(sql3)
        except:
            lik_obj = None
        try:
            sql4 = '''
                    select app_user.userNickname, 
                           app_user.userID 
                    from app_user_attention, app_user 
                    where app_user_attention.attentions_id = app_user.userID 
                          and app_user_attention.attentiond = %d
                   ''' % userid
            liked_obj = models.User.objects.raw(sql4)
        except:
            liked_obj = None
        user_sett = {
            'USER_Nickname': USER_Nickname,
            'USER_sign': USER_sign,
            'USER_picture': USER_picture,
            'posts': Page['dataList'],
            'nowPage': Page['nowPage'],
            'total_page': Page['total_page'],
            'page_sum': page_sum,
            'like_num': like_num,
            'fans': fans_num,
            'boke': boke_num,
            'lik': lik_obj,
            'liked': liked_obj
        }
        return render(req, 'logindPage.html', user_sett)
    except:  # 登录失效的处理
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def logintoLPage(req):  # 登录
    account = req.POST.get('account')
    password = str(req.POST.get('password'))
    try:
        the_user = models.User.objects.get(userAccount=account)
        if password == the_user.userPassword:
            req.session['account'] = account
            return HttpResponseRedirect('/logindPage/')  # 登陆成功，进入主界面设置函数)
        else:
            return render(req, '')  # 自设置错误
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'b', max_age=1)
        return resp


def Judgment(req):  # 判断账户状态
    res = req.COOKIES.get('content')
    if res == 'a':
        return render(req, 'login&registe.html', {'content': '该账户已存在，请直接登录'})
    elif res == 'b':
        return render(req, 'login&registe.html', {'content': '账户或密码错误,请重新登陆'})
    elif res == 'c':
        return render(req, 'login&registe.html', {'content': '登录已失效,请重新登陆'})
    else:
        if req.POST.get('account'):
            return render(req, 'main_login.html')
        else:
            return render(req, 'login&registe.html')


def Usersteeing(req):  # 用户设置页面参数设置
    try:
        account = req.session.get('account')
        the_userObj = models.User.objects.get(userAccount=account)
        data = {'content': the_userObj.userPicture}
        return render(req, 'user_setting.html', data)
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def userPict_change(req):  # 图片保存回显
    print('aaaaaaaaaaaaaaaaaaaaaaaa')
    account = req.session.get('account')
    if account != '' and account is not None:
        fileobj = req.FILES.get('file')
        print('asdddddddddddddddddd',fileobj) 
        user_path = os.path.dirname(__file__) + os.sep + 'static\\user_picture\\' + account
        if not os.path.exists(user_path):
            os.makedirs(user_path)
        picture_path = user_path + os.sep + fileobj.name
        with open(picture_path, 'wb') as fw:
            for Pict in fileobj.chunks():
                fw.write(Pict) 
        return HttpResponse('/static/user_picture/' + account + os.sep + fileobj.name)
    else:  # session 失效走这里
        resp = HttpResponseRedirect('Judgment')
        resp.set_cookie('content', 'c', max_age=1)
        return resp

 
def Save_setting(req):  # 保存用户设置
    try:
        account = req.session.get('account')
        user_set = models.User.objects.get(userAccount=account)
        user_Nickname = req.POST.get('user_name')
        user_QQ = req.POST.get('user_QQ')
        user_Sign = req.POST.get('user_span')
        user_Pict = req.POST.get('user_pict')
        if user_Nickname != '':
            user_set.userNickname = user_Nickname
        if user_QQ != '':
            user_set.userQQ = user_QQ
        if user_Sign != '':
            user_set.userSign = user_Sign
        if user_Pict != '':
            user_set.userPicture = '/static/user_picture/' + account + os.sep + user_Pict
        user_set.save()
        return HttpResponseRedirect('/logindPage/')
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def Upload(req):  # 发布博文
    account = req.session.get('account')
    UserObj = models.User.objects.get(userAccount=account)
    U_title = req.POST.get('U_title')
    U_content = req.POST.get('U_content')
    U_picture = '/static/userUPload_pcit/' + account + '/' + req.POST.get('U_picture')
    USERUP_OBJ = models.USER_upload(userID=UserObj, title=U_title, Picture=U_picture, content=U_content)
    USERUP_OBJ.save()
    return HttpResponseRedirect('/logindPage/')


def U_pict_upload(req):  # 发图片
    account = req.session.get('account')
    fileobj = req.FILES.get('file')
    print('asdddddddddddddddddd',fileobj) 
    user_path = os.path.dirname(__file__) + os.sep + 'static\\userUPload_pcit\\' + account
    if not os.path.exists(user_path):
        os.makedirs(user_path)
    picture_path = user_path + os.sep + fileobj.name
    with open(picture_path, 'wb') as fw:
        for Pict in fileobj.chunks():
            fw.write(Pict)
    return HttpResponse(None)


def Replay_page(req, num, pagenum=1):  # 回复页面
    try:
        account = req.session.get('account')
        accountMass = models.User.objects.get(userAccount=account)
        USER_Nickname = accountMass.userNickname
        USER_sign = accountMass.userSign
        USER_picture = accountMass.userPicture
        sql = '''
                select * 
                from app_user, app_replays 
                where app_user.userID = app_replays.userID_id
                and app_replays.num_id = %s''' % num
        content = models.User.objects.raw(sql)
        Page = toNextPage(int(pagenum), content, 3)
        page_sum = range(1, Page['total_page'] + 1)
        post_obj = models.USER_upload.objects.get(num=num)
        content = {'post': post_obj,
                   'USER_Nickname': USER_Nickname,
                   'USER_sign': USER_sign,
                   'USER_picture': USER_picture,
                   'posts': Page['dataList'],
                   'nowPage': Page['nowPage'],
                   'total_page': Page['total_page'],
                   'page_sum': page_sum,
                   'num': num
                   }
        return render(req, 'replay.html', content)
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def Replay_post(req, num, pagenum=1):  # 回复内容保存
    try:
        account = req.session.get('account')
        user_obj = models.User.objects.get(userAccount=account)
        post_obj = models.USER_upload.objects.get(num=num)
        replay = req.POST.get('R_content')
        replay_obj = models.Replays(num=post_obj, replay=replay, userID=user_obj)
        replay_obj.save()
        sql = '''
            select * 
            from app_user, app_replays 
            where app_user.userID = app_replays.userID_id'''
        content = models.User.objects.raw(sql)
        Page = toNextPage(int(pagenum), content, 3)
        return HttpResponseRedirect('/replay/' + str(num) + '/' + str(Page['total_page']) + '/')
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def Like(req):
    print('--------1111111-----------')
    num = req.GET.get('is_like')
    try:
        account = req.session.get('account')
        user_obj = models.User.objects.get(userAccount=account)
        upload_obj = models.USER_upload.objects.get(num=num)
        like_obj = models.Post_like(userID=user_obj, num=upload_obj, is_like=1)
        like_obj.save()
        return HttpResponse('true')
    except:
        return HttpResponse('false')


def disLike(req):
    print('--------22222-----------')
    num = req.GET.get('is_like')
    try:
        account = req.session.get('account')
        user_obj = models.User.objects.get(userAccount=account)
        upload_obj = models.USER_upload.objects.get(num=num)
        like_obj = models.Post_like(userID=user_obj, num=upload_obj, is_like=0)
        like_obj.save()
        return HttpResponse('true')
    except:
        return HttpResponse('false')


def Attention(req):
    attentiond_id = req.GET.get('attention')
    try:
        account = req.session.get('account')
        user_obj = models.User.objects.get(userAccount=account)
        userid = user_obj.userID
        try:
            attentiond_pbj = models.user_attention.objects.get(attentions=userid)
            if attentiond_pbj.attentiond == attentiond_id:
                return HttpResponse('false')
            else:
                attention_obj = models.user_attention(attentions=user_obj, attentiond=attentiond_id)
                attention_obj.save()
                return HttpResponse('true')
        except:
            attention_obj = models.user_attention(attentions=user_obj, attentiond=attentiond_id)
            attention_obj.save()
            return HttpResponse('true')
    except:
        return HttpResponse('false')


def Myboke(req, pagenum=1):
    try:
        account = req.session.get('account')
        accountMass = models.User.objects.get(userAccount=account)
        userid = accountMass.userID
        USER_Nickname = accountMass.userNickname
        USER_sign = accountMass.userSign
        USER_picture = accountMass.userPicture
        like_obj = models.user_attention.objects.filter(attentions=userid)
        like_num = len(like_obj)
        fans_obj = models.user_attention.objects.filter(attentiond=userid)
        fans_num = len(fans_obj)
        boke_obj = models.USER_upload.objects.filter(userID=userid)
        boke_num = len(boke_obj)
        bokes_obj = models.USER_upload.objects.filter(userID=userid)
        Page = toNextPage(int(pagenum), bokes_obj, 6)
        page_sum = range(1, Page['total_page'] + 1)
        content = {
            'USER_Nickname': USER_Nickname,
            'USER_sign': USER_sign,
            'USER_picture': USER_picture,
            'like_num': like_num,
            'fans': fans_num,
            'boke': boke_num,
            'bokes': Page['dataList'],
            'nowPage': Page['nowPage'],
            'total_page': Page['total_page'],
            'page_sum': page_sum
        }
        return render(req, 'myboke.html', content)
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def Del(req):
    try:
        account = req.session.get('account')
        accountMass = models.User.objects.get(userAccount=account)
        userid = accountMass.userID
        num = req.GET.get('num')
        print('^^^^^^^^^^^^^^^^^^^^', num)
        models.USER_upload.objects.get(num=num).delete()
        return HttpResponse('asd')
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def chaxun(req, list1=[], pagenum=1):
    try:
        account = req.session.get('account')
        accountMass = models.User.objects.get(userAccount=account)
        userid = accountMass.userID
        USER_Nickname = accountMass.userNickname
        USER_sign = accountMass.userSign
        USER_picture = accountMass.userPicture
        like_obj = models.user_attention.objects.filter(attentions=userid)
        like_num = len(like_obj)
        fans_obj = models.user_attention.objects.filter(attentiond=userid)
        fans_num = len(fans_obj)
        boke_obj = models.USER_upload.objects.filter(userID=userid)
        boke_num = len(boke_obj)
        reql = req.POST.get('chaxunre')
        if reql == '':
            return HttpResponseRedirect('/myboke/')
        res = '%'
        for r in reql:
            res += r + '%'
        sql = '''
                select * from app_user_upload 
                where app_user_upload.content 
                like '%s' or app_user_upload.title like '%s'
            ''' % (res, res)
        bokes_obj = models.USER_upload.objects.raw(sql)
        Page = toNextPage(int(pagenum), bokes_obj, 6)
        page_sum = range(1, Page['total_page'] + 1)
        content = {
            'USER_Nickname': USER_Nickname,
            'USER_sign': USER_sign,
            'USER_picture': USER_picture,
            'like_num': like_num,
            'fans': fans_num,
            'boke': boke_num,
            'bokes': Page['dataList'],
            'nowPage': Page['nowPage'],
            'total_page': Page['total_page'],
            'page_sum': page_sum
        }
        return render(req, 'myboke.html', content)
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def permass(req, userid):
    try:
        per_obj = models.User.objects.get(userID=int(userid))
        return render(req, 'permass.html', {'content': per_obj})
    except:
        resp = HttpResponseRedirect('/Judgment/')
        resp.set_cookie('content', 'c', max_age=1)
        return resp


def OUT(req):  # 退出当前账户，删除session
    req.session.clear()
    return HttpResponseRedirect('/')


def toNextPage(pagenum, objlist, pageN):  # 分页
    pageNa = Paginator(objlist, pageN)
    try:
        pageObj = pageNa.page(pagenum)  # 2 代表第几页数据
    except EmptyPage:
        pageObj = pageNa.page(1)  # 获得第一页数据
    context = dict()
    context['nowPage'] = pagenum  # 当前页码
    context['dataList'] = pageObj  # 页面显示的数据集
    context['total_page'] = pageNa.num_pages  # 总页数
    return context


def aaaa(req):
    return  render(req, 'fram.html')

def bbb(req):
    return render(req, 'login&registe.html')

def asd(req):
    return render(req, 'sendfile.html')