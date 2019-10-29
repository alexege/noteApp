function edit_note(){
    console.log(this.innerHTML())
}

// $(document).ready(function(){
//     var mousedown = false;
//     var mousedown_timer = '';
//     $('#button').mousedown(function(e) {
//         mousedown = true;
//         $('#log').text('mousedown...');
//         mousedown_timer = setTimeout(function () {
//             if(mousedown) {
//                 console.log(this)
//                 $('#edit_form').css({"display":"block"});
//                 $('#log').text('1 second');
//             }
//         }, 1000);
//     }).mouseup(function(e) {
//         mousedown = false;
//         clearTimeout(mousedown_timer);
//         $('#log').text('aborted');
//     });

// })