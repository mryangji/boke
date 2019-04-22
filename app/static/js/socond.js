var ball_list = []
var sep_i = 0
var Login_obj = document.getElementById('login_form')
var Digist_obj = document.getElementById('digist_form')
var login_obj = document.getElementById('login_1')
var digist_obj = document.getElementById('digist_1')
var body_obj = getid('content')

window.onload = function() {

	windowheight = window.innerHeight
	body_obj.style.height = windowheight + 'px'
	//			body_obj.style.backgroundSize = window.innerHeight 
	create()
	Int = window.setInterval('move()', 20)
}

$(document).ready(function(){
	tipspan_obj = $('#tip_span')
	tipspan_obj.fadeOut(3000) 
})

// $('#loginAcc').blur(function(){
// 	ACC_va = $('#loginAcc').val()
// 	$.ajax({
// 		url:'/login_Re/?name='+ACC_va,
// 		async:true,
// 		type:'GET',
// 		success:function(result){
// 			$('#loginAcc_span').html(result)
// 		}
// 	})
// })

Login_obj.onmousemove = function() {
	login_obj.style.display = 'block'
	//			Login_obj.style.backgroundColor = 'blue'
	Login_obj.style.color = 'white'
	digist_obj.style.display = 'none'
	Digist_obj.style.color = 'black'
	//			Digist_obj.style.backgroundColor = 'skyblue'
}
Digist_obj.onmouseover = function() {
	login_obj.style.display = 'none'
	digist_obj.style.display = 'block'
	Login_obj.style.color = 'black'
	Digist_obj.style.color = 'white'
}

function randomFrom(lowerValue, upperValue) {
	return Math.floor(Math.random() * (upperValue - lowerValue + 1) + lowerValue);
}

function create() {
	for(var i = 0; i < 10; i++) {
		div_obj = document.createElement('div')
		div_obj.className = 'ball'
		raX = randomFrom
		a = randomFrom(0, window.innerWidth)
		div_obj.style.top = window.innerHeight + 'px'
		div_obj.style.left = a + 'px'
		div_obj.speed = randomFrom(3, 8)
		div_obj.style.boxShadow = '-5px -5px 20px 0px' + ' ' + color() + ' ' + 'inset'
		div_obj.onclick = function() {
			window.clearInterval(Int)
			Top = div_obj.offsetTop
			Left = div_obj.offsetLeft
			sep(Top, Left)
			rem = window.setInterval('remove()', 20)
			//					sleep(2000)
			//					window.clearInterval(remove)
		}
		ball_list.push(div_obj)
		document.body.appendChild(div_obj)
	}
}

function sep(Top, Left) {
	for(var i = 0, len = ball_list.length; i < len; i++) {
		ball_list[i].top_ = (ball_list[i].offsetTop - Top) / 50;
		ball_list[i].left_ = (ball_list[i].offsetLeft - Left) / 50;
	}
}

function remove() {
	for(var i = 0, len = ball_list.length; i < len; i++) {
		ball_list[i].style.top = ball_list[i].offsetTop - ball_list[i].top_ + 'px';
		ball_list[i].style.left = ball_list[i].offsetLeft - ball_list[i].left_ + 'px';

	}
	sep_i++
	if(sep_i == 50) {
		window.clearInterval(rem)
	}
}

function move() {
	for(var i = 0, len = ball_list.length; i < len; i++) {
		top1 = ball_list[i].offsetTop - ball_list[i].speed
		if(top1 < -140) {
			top1 = window.innerHeight;
			ball_list[i].style.left = randomFrom(0, window.innerWidth) + 'px';
		}
		ball_list[i].style.top = top1 + 'px'

	}
}

function sleep(numberMillis) {
	var now = new Date();
	var exitTime = now.getTime() + numberMillis;
	while(true) {
		now = new Date();
		if(now.getTime() > exitTime)
			return;
	}
}

function chack_LACC() {
	laccspan_obj = getid('loginAcc_span')
	laccspan_obj.className = 'right'
	laccspan_obj.innerText = '√'
}

function chack_LPASS() {
	lpassspan_obj = getid('loginPass_span')
	lpassspan_obj.className = 'right'
	lpassspan_obj.innerText = '√'
}

function chack_DACC() {
	daccspan_obj = getid('digistAcc_span')
	dacc_obj = getid('digistAcc')
	//			alert(dacc_obj.value)
	reg = /[a-zA-Z]+\w*/
	res = reg.exec(dacc_obj.value)
	len_res = String(res).length
	//			alert(len_res)
	if(len_res >= 6 && len_res <= 18) {
		daccspan_obj.className = 'right';
		daccspan_obj.innerText = '√';
		return true;
	} else {
		daccspan_obj.className = 'wrong';
		daccspan_obj.innerText = '×';
		return false;
	}

}

function chack_DPAS() {
	dpasspan_obj = getid('digistPas_span')
	dpas_obj = getid('digistPas').value
	len_pasres = dpas_obj.length
	if(len_pasres >= 6 && len_pasres <= 18) {
		dpasspan_obj.className = 'right'
		dpasspan_obj.innerText = '√'
		return true;
	} else {
		dpasspan_obj.className = 'wrong'
		dpasspan_obj.innerText = '×'
		return false;
	}
}

function chack_DPASS() {
	dpassspan_obj = getid('digistPass_span')
	dpass_va = getid('digistPass').value
	dpas_va = getid('digistPas').value
	if(dpass_va == dpas_va && dpas_va != '') {
		dpassspan_obj.className = 'right'
		dpassspan_obj.innerText = '√'
		return true;
	} else {
		dpassspan_obj.className = 'wrong'
		dpassspan_obj.innerText = '×'
		return false;
	}

}

function chack_BOX() {
	box_obj = getid('check')
	if(box_obj.value == 'on') {
		return true;
	} else {
		return false;
	}
}

function ckacke_dig() {
	return chack_BOX() && chack_DPASS() && chack_DPAS() && chack_DACC()
}

function getid(s) {
	return document.getElementById(s);
}

function color() {
	a = randomFrom(0, 7)
	switch(a) {
		case 0:
			return 'green';
		case 1:
			return 'red';
		case 2:
			return 'yellow';
		case 3:
			return 'pink';
		case 4:
			return 'blue';
		case 5:
			return 'gold';
		case 6:
			return 'purple';
		case 7:
			return 'grey';
	}
}