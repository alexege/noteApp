$(document).ready(function(){
    // Hover
    $(".center-login-box").hover(function(){
        $(".corner").stop().animate({height: "250px", width: "250px"});
    }, function(){
        $(".corner").stop().animate({height: "50px", width: "50px"});
    });

})
