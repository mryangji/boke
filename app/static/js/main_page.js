windowheight = window.innerHeight
window.onload = function() {
	var nu = getid('page_in').value
	var num = 'page_'+ nu
	page_obj = getid(num)
	page_obj.style.backgroundColor = '#e5e5e5'
}

window.onscroll = function(){
	menu_obj = getid('menu_div')
}

function zhanneisousuo() {
	sousuo_obj = getid('sousuo');
	sousuo_obj.style.backgroundColor = "#d4dee3"
}

function zhanneisousuo_() {
	sousuo_obj = getid('sousuo');
	sousuo_obj.style.backgroundColor = "transparent"
}

function getid(s) {
	return document.getElementById(s)
}



// function getElementViewTop(element){
// 	　　var actualTop = element.offsetTop;
// 		alert(actualTop)
// 	　　var current = element.offsetParent;
// 	　　while (current !== null){ 
// 			actualTop += current.offsetTop;
// 			current = current.offsetParent;
// 	　　}
// 		var elementScrollTop=0;
// 	　　if (document.compatMode == "BackCompat"){
// 			elementScrollTop=document.body.scrollTop;
// 	　　} else {
// 			elementScrollTop=document.documentElement.scrollTop; 
// 	　　}
// 		alert(actualTop)
// 		return actualTop;
// 	　//　return actualTop-elementScrollTop;
// 	}
function getScroll()
	{
		var top;
		if (document.documentElement && document.documentElement.scrollTop) {
			top = document.documentElement.scrollTop;
		} else if (document.body) {
			top = document.body.scrollTop;
		}
		return { 'top': top }
	}
	var nav = document.getElementById('menu_div'); 

	var posTop = 332; 

	window.addEventListener('scroll',function(){
		var scrollTop = getScroll().top;
		if(posTop>=30 && posTop-scrollTop <= 30) 
			nav.className = 'absu fixed';
		else nav.className = 'absu';
	},false);
