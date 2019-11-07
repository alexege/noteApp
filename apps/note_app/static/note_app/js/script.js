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
    console.log("Parent: ", parent);
    console.log("Sibling: ", parent.nextElementSibling);
    if (parent.nextElementSibling.style.display === "none") {
        parent.style.display = "none";
        parent.nextElementSibling.style.display = "block";
    } else {
        parent.style.display = "block";
        parent.nextElementSibling.style.display = "none";
    }
}

function toggleCodeEdit(note_comment_id){
    console.log("Toggling Code Edit");
    console.log(note_comment_id);
    var parent = document.getElementById('note_comment_' + note_comment_id);
    console.log("Parent: ", parent);
    console.log("Parent: ", parent.parentElement);
    if (parent.parentElement.nextElementSibling.style.display === "none") {
        parent.style.display = "none";
        parent.parentElement.nextElementSibling.style.display = "block";
    } else {
        parent.style.display = "block";
        parent.parentElement.nextElementSibling.style.display = "none";
    }
}

// https://hackernoon.com/copying-text-to-clipboard-with-javascript-df4d4988697f
function copyToClipboard(ele){

    const el = document.createElement('textarea');
    el.value = ele.parentNode.innerText;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);

    // console.log("ELEMENT: ", ele.parentElement)

    // /* Get the text field */
    // var copyText = ele.parentNode.innerHTML;
    // var copyTextNode = ele.parentElement.parentElement.parentElement;
    // console.log(copyTextNode)
    // ele.select()
    
    // // /* Select the text field */
    // // copyText.select();
    // // copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    
    // /* Copy the text inside the text field */
    // document.execCommand("copy");
    
    // /* Alert the copied text */
    // alert("Copied the text: " + copyText);
}

$(document).ready(function(){

// element that will be wrapped
var el = document.querySelectorAll('.code_format');
// console.log(el);

var i;
for (i = 0; i < el.length; i++) {

// create wrapper container
var wrapper = document.createElement('code');
wrapper.setAttribute('class', "language-css");

//   el[i].style.backgroundColor = "red";

  // insert wrapper before el in the DOM tree
  el[i].parentNode.insertBefore(wrapper, el[i]);
  
  // move el into wrapper
  wrapper.appendChild(el[i]);

}

// var code_elements = document.querySelectorAll('.code_format');
// var i = 0;
// for (i = 0; i < el.length; i++){
//     code_elements[i].parentNode.classList.add("language-css");
// }









    var acc = document.getElementsByClassName("accordion");
    // console.log(acc.length);
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

// if (localStorage.getItem('sideNavToggle') === null){
//     console.log("Does not exist in localstorage!");
//     localStorage.setItem('sideNavToggle', true);
//     console.log("sideNavToggle:", localStorage.getItem('sideNavToggle'));
//     toggle = false;
// } else {
//     localStorage.getItem('sideNavToggle');
//     toggle = true;
// }

// if (localStorage.getItem('sideNavToggle') === null){
//     localStorage.setItem('sideNavToggle', true);
//     toggle = false;
// } else {
//     localStorage.getItem('sideNavToggle');
//     toggle = true;
// }

// if(localStorage.getItem('sideNavToggle') == true){
//     console.log("sideNavToggle is true");
//     if($(document).ready(function(){
//         document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-left" id="toggle_button"></i>';
//         document.getElementById("mySidenav").style.width = "20vw";
//         document.getElementById("main").style.marginLeft = "20vw";
//         toggle = false;
//         // localStorage.setItem('sideNavToggle', false);
//     }));
// } else {
//     console.log("sideNavToggle is false");
//     if($(document).ready(function(){
//         document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-right" id="toggle_button"></i>';
//         document.getElementById("mySidenav").style.width = "0";
//         document.getElementById("main").style.marginLeft= "0";
//         toggle = true;
//         // localStorage.setItem('sideNavToggle', true);
//     }));
// }

console.log("Start:", localStorage.getItem('sideNavToggle'))
if(localStorage.getItem('sideNavToggle') === null){
    localStorage.setItem('sideNavToggle', false)
}

console.log("Currently, it's ", localStorage.getItem('sideNavToggle'))

if(localStorage.getItem('sideNavToggle') === 'false'){
    console.log("it's false. Keep it closed!");
    localStorage.setItem('sideNavToggle', 'true')
} else {
    console.log("it's true. Open it up!");
    localStorage.setItem('sideNavToggle', 'false')
}

if(localStorage.getItem('sideNavToggle') === 'true'){
    console.log("sideNavToggle is true");
    if($(document).ready(function(){
        document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-left" id="toggle_button"></i>';
        document.getElementById("mySidenav").style.width = "20vw";
        document.getElementById("mySidenav").style.transition = "0s";
        document.getElementById("main").style.marginLeft = "20vw";
        document.getElementById("main").style.transition = "0s";
        toggle = false;
        localStorage.setItem('sideNavToggle', 'false');
    }));
} else {
    console.log("sideNavToggle is false");
    if($(document).ready(function(){
        document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-right" id="toggle_button"></i>';
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft= "0";
        toggle = true;
        localStorage.setItem('sideNavToggle', 'true');
    }));
}

// console.log("toggle:", toggle)
function openNav() {
console.log("sideNavToggle", localStorage.getItem('sideNavToggle'))
document.getElementById("mySidenav").style.transition = "0.5s";
document.getElementById("main").style.transition = "0.5s";

  if (toggle){
    document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-left" id="toggle_button"></i>';
    document.getElementById("mySidenav").style.width = "20vw";
    document.getElementById("main").style.marginLeft = "20vw";
    toggle = false;
    localStorage.setItem('sideNavToggle', false);
} else {
    document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-right" id="toggle_button"></i>';
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    toggle = true;
    localStorage.setItem('sideNavToggle', true);
  }
}
