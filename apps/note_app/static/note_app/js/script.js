// var acc = document.getElementsByClassName("accordion");
// var i;

// for (i = 0; i < acc.length; i++) {
//   acc[i].addEventListener("click", function() {
//     /* Toggle between adding and removing the "active" class,
//     to highlight the button that controls the panel */
//     this.classList.toggle("active");

//     /* Toggle between hiding and showing the active panel */
//     var panel = this.nextElementSibling;
//     if (panel.style.display === "block") {
//       panel.style.display = "none";
//     } else {
//       panel.style.display = "block";
//     }
//   });
// }


function edit_note(ele){
    var current_note = ele.parentElement;
    console.log(ele.parentElement.getAttribute('id'))
    
    var note_title = document.createElement("input");
    note_title.setAttribute('name','note_title');
    note_title.setAttribute('value', current_note.getAttribute('title'))
    note_title.setAttribute('name', 'title');
    
    var note_content = document.createElement("input");
    note_content.setAttribute('value', current_note.getAttribute('content'))
    note_content.setAttribute('name', 'content');
    
    var edit_form = document.createElement("form");
    edit_form.setAttribute('method','POST');
    edit_form.setAttribute('action','note/update/' + current_note.getAttribute('id'));

    var update_button = document.createElement("button");
    update_button.setAttribute("value", "update")
    update_button.innerText = "Update"

    // edit_form.append("{% csrf_token %}"|safe);
    var csrf = document.getElementById('csrf');
    var cloned_csrf = csrf.cloneNode(true);
    edit_form.append(cloned_csrf);
    edit_form.append(note_title);
    edit_form.append(note_content);
    edit_form.append(update_button);

    var replaceBody = document.querySelector('note_content')

    current_note.append(edit_form);
    // var theDiv = document.getElementById("<ID_OF_THE_DIV>");
    // var content = document.createTextNode("<YOUR_CONTENT>");
    // theDiv.appendChild(content);
}

function toggleEdit(note_comment_id){
    console.log("Toggling Edit");
    console.log(note_comment_id);
    var parent = document.getElementById('note_comment_' + note_comment_id);
    if (parent.nextElementSibling.style.display === "none") {
        parent.style.display = "none";
        parent.nextElementSibling.style.display = "block";
    } else {
        parent.style.display = "block";
        parent.nextElementSibling.style.display = "none";
    }
}

$(document).ready(function(){
    var acc = document.getElementsByClassName("accordion");
    console.log(acc.length);
    var i;

    for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
        panel.style.display = "none";
        } else {
        panel.style.display = "block";
        }
    });
    }


    // AutoSize TextAreas
    var textarea = document.querySelector('textarea');

    textarea.addEventListener('keydown', autosize);
                
    function autosize(){
    var el = this;
    setTimeout(function(){
        el.style.cssText = 'height:auto; padding:0';
        // for box-sizing other than "content-box" use:
        // el.style.cssText = '-moz-box-sizing:content-box';
        el.style.cssText = 'height:' + el.scrollHeight + 'px';
    },0);
    }

});



// // sidenav
// function openNav() {
//     document.getElementById("mySidenav").style.width = "25vw";
//     document.getElementById("main").style.marginLeft = "25vw";
//   }
  
//   function closeNav() {
//     document.getElementById("mySidenav").style.width = "0";
//     document.getElementById("main").style.marginLeft= "0";
//   }

//Side Nav Script
var toggle = true;
function openNav() {
  if (toggle){
    document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-left" id="toggle_button"></i>';
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    toggle = false;
  } else {
    document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-right" id="toggle_button"></i>';
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    toggle = true;
  }
}
