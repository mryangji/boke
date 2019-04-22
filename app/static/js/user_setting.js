$('#picture_file').change(function(){
    // alert(this.files[0])
    picture_use = this.files[0]
    csrf_cookie = document.cookie.split(';')[0].split('=')[1]
    var for_data = new FormData()
    for_data.append('file',picture_use)
    $.ajax({
        async:true,
        url:'/userPict_change/',
        type:'POST',
        data: for_data,
        headers: {"X-CSRFToken":csrf_cookie},
        contentType:false,
        processData:false,
        success:function(res){
            $('#user_pict').attr('src',res)
        }
    })
})

function getid(s){
    return document.getElementById(s)
}

function CHECK_NAME(){
    Uname = getid('User_name').value
    var NAME = /^([\u4e00-\u9fa5]|[a-zA-Z]|[0-9])*$/
    // res = NAME.exec(Uname)
    res = NAME.test(Uname)
    // alert(res)
    if ( res ){
        return true
    }else{
        Uname_span = getid('tip')
        Uname_span.style.display = 'block'
        Uname_span.innerText = '昵称不能加特殊符号'
        tip()
        return false
    }
}

function tip(){
    tipspan_obj = $('#tip')
	tipspan_obj.fadeOut(2000) 
}

function CHECK_QQ(){
    UQQ = getid('user_QQ').value
    var QQ = /[0-9]*/
    res = QQ.exec(UQQ)   
    QQ_L = String(res).length
    if ( QQ_L == 0 || QQ_L >=5 && QQ_L <=11 ){
        return true
    }else{
        Uname_span = getid('tip')
        Uname_span.style.display = 'block'
        Uname_span.innerText = 'QQ输入错误'
        tip()
        return false
    } 
}

function CHECK_NAME_(){
    Uname = getid('User_name').value
    var NAME = /^([\u4e00-\u9fa5]|[a-zA-Z]|[0-9])*$/
    // res = NAME.exec(Uname)
    res = NAME.test(Uname)
    // alert(res)
    if ( res ){
        return true
    }else{
        return false
    }
}

function CHECK_QQ_(){
    UQQ = getid('user_QQ').value
    var QQ = /[0-9]*/
    res = QQ.exec(UQQ)   
    QQ_L = String(res).length
    if ( QQ_L == 0 || QQ_L >=5 && QQ_L <=11 ){
        return true
    }else{
        return false
    } 
}

function CHECKALL(){
    if (CHECK_NAME_() && CHECK_QQ_()){
        return true
    }else if(CHECK_NAME_() == false && CHECK_QQ_()){
        Uname_span = getid('tip')
        Uname_span.style.display = 'block'
        Uname_span.innerText = '昵称输入错误'
        tip()
        return false
    }else if(CHECK_NAME_() && CHECK_QQ_() == false){
        Uname_span = getid('tip')
        Uname_span.style.display = 'block'
        Uname_span.innerText = 'QQ输入错误'
        tip()
        return false
    }else{
        Uname_span = getid('tip')
        Uname_span.style.display = 'block'
        Uname_span.innerText = '昵称和QQ输入错误'
        tip()
        return false
    }
}

function Back(){
    window.history.back()
}