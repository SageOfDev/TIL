var Links = {
    setColor:function(color){
        // var alist = document.querySelectorAll('a');
        // var i = 0;
        // while(i < alist.length){
        // alist[i].style.color = color;
        // i = i + 1;
        // }
        $('a').css('color', color); // 모든 'a'태그를 jQuery로  처리하겠다는 뜻
    }
}
var Body = {
    setColor:function(color){
        //document.querySelector('body').style.color = color;
        $('body').css('color', color);
    },
    setBackgroundColor:function(color){
        //document.querySelector('body').style.backgroundColor = color;
        $('body').css('backgroundColor', color);
    }
}
function nightDayHandler(self){
    var target = document.querySelector('body')
    if (self.value === 'night'){ 
    Body.setBackgroundColor('black')
    Body.setColor('white')
    self.value = 'day'
    
    Links.setColor('powderblue');
    } else {
    Body.setBackgroundColor('white')
    Body.setColor('black')
    self.value = 'night'

    Links.setColor('blue');
    }
}