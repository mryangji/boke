

$('#U_picture').change(function(){
    alert(this.files[0])
    picture_use = this.files[0]
    csrf_cookie = document.cookie.split(';')[0].split('=')[1]
    var for_data = new FormData()
    for_data.append('file',picture_use)
    // $.ajax({
    //     url:'/U_pict_upload/?name1=1',
    //     type:'GET',
    //     success:function(){
    //         alert('asdasdas')
    //     }
    // })

    $.ajax({
        async:true,
        url:'/U_pict_upload/',
        type:'POST',
        data: for_data,
        headers: {"X-CSRFToken":csrf_cookie},
        contentType:false,
        processData:false,
        success:function(){
            alert('asdasdas')
        }
    })
})

var title_obj = getid('input_title')
var textarea_obj = getid('U_content')
var picture_obj = getid('U_picture')

function check_title(){
    title = title_obj.value
    if (title == '' || title == null){
        return false
    }else{
        return true
    }
}

function check_content(){
    content = textarea_obj.value
    if (content == '' || content == null){
        return false
    }else{
        return true
    }
}

function check_pict(){
    picture = picture_obj.value
    if (picture == '' || picture == null){
        return false
    }else{
        return true
    }
}

function Check_upload(){
    return check_title() && (check_content() || check_pict())
}

function getid(s){
    return document.getElementById(s)
}

function like(s){
    // csrf_cookie = document.cookie.split(';')[0].split('=')[1]
    $.ajax({
        async:true,
        url:'/like/?is_like='+ String(s) ,
        type:'GET',
        success:function(res){
            d = 'like_div' + String(s)
            d2 = 'liked' + String(s)
            document.getElementById(d).className = 'displaynone'
            document.getElementById(d2).className = 'like_div'
        }
    })
}

function dislike(s){
    // csrf_cookie = document.cookie.split(';')[0].split('=')[1]
    $.ajax({
        async:true,
        url:'/dislike/?is_like='+ String(s) ,
        type:'GET',
        success:function(res){
            d = 'like_div' + String(s)
            d2 = 'disliked' + String(s)
            document.getElementById(d).className = 'displaynone'
            document.getElementById(d2).className = 'like_div'
        }
    })
}

function attentions(s, num){
    $.ajax({
        async:true,
        url:'/attention/?attention='+ String(s) ,
        type:'GET',
        success:function(res){
            if(res == 'true'){
                d = 'attention' + String(num)
                spanobj = getid(d)
                spanobj.innerText = '以关注'
                spanobj.className = 'attentiond'
            }else if (res == 'false'){
                tip_obj = document.createElement('div')
                tip_obj.className = 'tip'
                tip_obj.innerText = '已关注,请刷新后重试'
                document.body.appendChild(tip_obj)
                tip('tip')
            }
        }
    })
}

function tip(s){
    iid = '.'+s
	tipspan_obj = $(iid)
    tipspan_obj.fadeOut(2000)
}
 

function lik(s){
    x=event.clientX;
    y=event.clientY;
    lik_obj = getid(s)
    lik_obj.className = 'lik2'
    lik_obj.style.left = x +'px'
    lik_obj.style.top = y +'px'
}

function lik1(s){
    lik_obj = getid(s)
    lik_obj.className = 'lik1'
}