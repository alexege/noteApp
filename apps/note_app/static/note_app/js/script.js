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


function edit_note(ele, event){
    
    var note = ele.parentNode.parentNode.parentNode.querySelector('#update_form')
    if(note.style.display == "block"){
        note.style.display = "none";
    } else {
        note.style.display = "block";
    }

    // var current_note = ele.parentElement;
    // console.log(ele.parentElement.getAttribute('id'))
    
    // var note_title = document.createElement("input");
    // note_title.setAttribute('name','note_title');
    // note_title.setAttribute('value', current_note.getAttribute('title'))
    // note_title.setAttribute('name', 'title');
    // note_title.setAttribute('class', 'propagating_input');
    
    // var note_content = document.createElement("input");
    // note_content.setAttribute('value', current_note.getAttribute('content'))
    // note_content.setAttribute('name', 'content');
    // note_content.setAttribute('class', 'propagating_input');
    
    // var edit_form = document.createElement("form");
    // edit_form.setAttribute('method','POST');
    // edit_form.setAttribute('action','note/update/' + current_note.getAttribute('id'));

    // var update_button = document.createElement("button");
    // update_button.setAttribute("value", "update")
    // update_button.innerText = "Update"

    // // edit_form.append("{% csrf_token %}"|safe);
    // var csrf = document.getElementById('csrf');
    // var cloned_csrf = csrf.cloneNode(true);
    // edit_form.append(cloned_csrf);
    // edit_form.append(note_title);
    // edit_form.append(note_content);
    // edit_form.append(update_button);

    // var replaceBody = document.querySelector('note_content')

    // current_note.append(edit_form);
    // // var theDiv = document.getElementById("<ID_OF_THE_DIV>");
    // // var content = document.createTextNode("<YOUR_CONTENT>");
    // // theDiv.appendChild(content);

    // $(".propagating_input").on('click', function(e){
    //     console.log("Stopping Propagation");
    //     e.stopPropagation();
    // })

    // $(".propagating_input").on('keydown', function(e){
    //     if(e.key === ' ' || e.key === 'Spacebar'){
    //         // e.preventDefault();
    //         e.stopPropagation();
    //         console.log("Space was clicked");
    //     }
    //     // console.log("Stopping Propagation");
    //     // e.stopPropagation();
    // })

    // // Disable edit form inputs from propagating accordion collapse
    // $(".edit_form").on('click', function(e){
    //     console.log("Clicking a form")
    //     e.stopPropagation();
    //     e.preventDefault();
    // })
    // $(".edit_form").on("keydown", function(e){
    //     if (e.key === ' ' || e.key === 'Spacebar') {
    //         // ' ' is standard, 'Spacebar' was used by IE9 and Firefox < 37
    //         // e.preventDefault()
    //         e.stopPropagation();
    //         console.log('Space pressed')
    //       }
    // })

    event.stopPropagation();
}

function togglePrivacy(ele, event){
    console.log(ele.getAttribute('privacy'));
    privacy = ele.getAttribute('privacy');
    if(privacy){
        console.log("Private")
        privacy = false;
    } else {
        privacy = true;
        console.log("Public")
    }
    event.stopPropagation();
}

function toggleCategoryPrivacy(ele, event){
    privacy = ele.getAttribute('privacy');
    if(privacy){
        console.log("Private")
        privacy = false;
    } else {
        privacy = true;
        console.log("Public")
    }
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

function revealCategoryAddForm(){    
    document.querySelector(".category_add_form").style.opacity = 1;
}
function hideCategoryAddForm(){
    document.querySelector(".category_add_form").style.opacity = 0;
}

function jump(anchor){
    window.location.href = "#" + anchor;
    console.log("Jumping to ", window.location.href);
    history.replaceState(null,null,' ');
}

$(document).ready(function(){
  
    // var note = localStorage.getItem('target_note');
    // jump(note);

    // var current_note = localStorage.getItem('current_note');
    // location.href = current_note;
    // history.replaceState(null,null,url);
    console.log("target_note", typeof(localStorage.getItem('target_note')));
    console.log("target_note", localStorage.getItem('target_note'));
    if(localStorage.getItem('target_note') != null){

        target_id = localStorage.getItem('target_note');
        // console.log("target_note:",localStorage.getItem('target_note'));

        var element = document.getElementById(target_id);
        
        
        var a_tag = document.createElement('a');
        // a_tag.innerHTML = "This is a tag";
        a_tag.setAttribute('id', 'trigger');
        element.insertBefore(a_tag, element.childNodes[0]);
        element.childNodes[2].classList.toggle("active");
    }

    // Look to see if any notes are active
    var active_notes = document.querySelectorAll('.active');
    console.log("acitve_notes", active_notes);

    if(active_notes){
        console.log("Active notes found");
        jump('trigger');
        // element.childNodes[2].classList.toggle("active");
    
        // Toggle open or closed if active or not 
        var list_of_accordion_nodes = document.querySelectorAll(".accordion");
        for(i = 0; i < list_of_accordion_nodes.length; i++){
            var panel = list_of_accordion_nodes[i].nextElementSibling;
            if(list_of_accordion_nodes[i].classList.contains("active")){
                if (panel.style.display === "block") {
                    panel.style.display = "none";
                    } else {
                    panel.style.display = "block";
                    }
                // give panel focus
                panel.childNodes[3].querySelector('textarea').focus();
            }
        }
    } else {
        console.log("No active notes found")
    }



    $(".add_subnote_button").on('click', function(e){
        console.log("Adding subnote")
        var note = this.parentElement.parentElement.parentElement;
        console.log("note:", note)
        var note_id = note.getAttribute('id');
        localStorage.setItem('target_note', note_id);
        var a_tag = document.createElement('a');
        a_tag.setAttribute('id', 'trigger');
        note.insertBefore(a_tag, note.childNodes[0]);
    });

    // $(".update_subnote_button").on('click', function(e){
    //     console.log("Updating subnote")
    //     var note = this.parentElement.parentElement.parentElement;
    //     var note_id = note.getAttribute('id');
    //     localStorage.setItem('target_note', note_id);
    //     var a_tag = document.createElement('a');
    //     a_tag.setAttribute('id', 'trigger');
    //     note.insertBefore(a_tag, note.childNodes[0]);
    // })

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
        localStorage.clear();
        console.log("Clearing local storage")
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
    $('.togglePrivacy').on('click', function(e){
        var privacy = this.getAttribute('privacy');
        var Notebook = this;
        var category_id = this.getAttribute('custom_id');
        var notebook = this.parentNode;
        console.log("Category id: ", category_id);
        e.preventDefault()
        $.ajax({
            url: 'toggle_subcat_privacy/' + category_id,
            method: 'get',
            data: $(this).serialize(),
            success: function(serverResponse){
                console.log("privacy:",privacy)
                public_notes = document.getElementsByClassName("public_notebooks");
                public_notes[0].append(notebook);
                // console.log("privacytype:",typeof(privacy))
                // if(privacy == "False"){
                //     Notebook.privacy = "True";
                //     Notebook.save();
                //     console.log("This was false.")
                // } else {
                //     Notebook.privacy = "False";
                //     Notebook.save();
                //     console.log("This was True.")
                // }
                console.log("got successfully");
            }
        })
    });

    // // Add noteComment
    // $('.post-form').on('submit', function(event){
    //     console.log("__________Submitting the form___________");
    //     event.preventDefault();
    //     console.log(this);
    //     console.log(this.getAttribute('note_id'));
    //     note_id = this.getAttribute('note_id');

    //     $.ajax({
    //         url: `/notes/note/new_note_comment/${note_id}`,
    //         method: 'post',
    //         data: $(this).serialize(),
    //         success: function(serverResponse){
    //             console.log("Running ajax request");
    //             $(".note_comments_panel").html(serverResponse);
    //             document.querySelectorAll('.accordion')
    //             .forEach(input => input.addEventListener('click', function(){
    //                 this.firstElementChild.classList.toggle("active");
    //                 /* Toggle between hiding and showing the active panel */
    //                 console.log("input", input)
    //                 console.log("next:", this.nextElementSibling);
    //                 // var panel = input.firstElementChild.nextElementSibling;
    //                 var panel = this.nextElementSibling;
    //                 console.log(panel)
    //                 if (panel.style.display === "block") {
    //                 panel.style.display = "none";
    //                 } else {
    //                 panel.style.display = "block";
    //                 }
    //             }));
    //             console.log("SUCCESS");
    //             // console.log("------Server Response------");
    //             // console.log(serverResponse);
    //             // $("#note_comments_panel").html("Testing something");
    //         }
    //     })
    // })

    // // Submit new note using Ajax
    // $('#new_note_form').submit(function(e){
    //     console.log("Adding a new note with ajax.")
    //       e.preventDefault()

    //       title = document.getElementById("title_input").value;
    //       content = document.getElementById("content_input").value;
    //       privacy = document.getElementById("privacy_input").value;
    //       category = document.getElementById("category_input").value;
    //       upload_date = new Date().toJSON().slice(0,10);

    //       $.ajax({
    //         url: '/notes/note/add',
    //         method: 'post',
    //         data: $(this).serialize(),
    //         success: function(serverResponse){
    //             var note_layout = document.getElementById("note_template")
    //             // console.log(note_layout)
    //             var clone_note = note_layout.cloneNode(true);
    //             // console.log(clone_note)
    //             clone_note.addEventListener('click', function(){
    //                 this.firstElementChild.classList.toggle("active");
    //                 /* Toggle between hiding and showing the active panel */
    //                 var panel = this.firstElementChild.nextElementSibling;
    //                 console.log(panel)
    //                 if (panel.style.display === "block") {
    //                 panel.style.display = "none";
    //                 } else {
    //                 panel.style.display = "block";
    //                 }
    //             })
    //             $(".note_container").append(clone_note);
    //             document.getElementById("temp_note_title").innerHTML = title;
    //             document.getElementById("temp_note_content").innerHTML = content;
    //             // document.getElementById("temp_note_privacy").innerHTML = privacy;
    //             document.getElementById("temp_note_category").innerHTML = category;
    //             document.getElementById("upload_date").innerHTML = upload_date;
    //             // $(".note_container").append(clone_note);
    //         //   console.log("Received this from server: ", serverResponse)
    //           // $('.notes').html(serverResponse)
    //         //   $(".wrapper").html(serverResponse);
    //         }
    //       })
    //     })

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

// console.log("Start:", localStorage.getItem('sideNavToggle'))
if(localStorage.getItem('sideNavToggle') === null){
    localStorage.setItem('sideNavToggle', false)
}

// console.log("Currently, it's ", localStorage.getItem('sideNavToggle'))

if(localStorage.getItem('sideNavToggle') === 'false'){
    // console.log("it's false. Keep it closed!");
    localStorage.setItem('sideNavToggle', 'true')
} else {
    // console.log("it's true. Open it up!");
    localStorage.setItem('sideNavToggle', 'false')
}

if(localStorage.getItem('sideNavToggle') === 'true'){
    // console.log("sideNavToggle is true");
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
    // console.log("sideNavToggle is false");
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
