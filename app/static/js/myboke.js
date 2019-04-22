function delet(s){
    i = window.confirm('是否删除')
    if(i){
        $.ajax({
        async:true,
        url:'/del/?num='+ String(s) ,
        type:'GET',
        success:function(res){
            window.location.reload()
            }
        })
    }else{
        null
    }  
}