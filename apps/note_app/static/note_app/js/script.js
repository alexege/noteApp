//Dynamically view notes of a specific category
function view_category(category){
    $.ajax({
        url: `/notes/${category}`,
        method: 'get',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            // Toggle open/close accordion elements
            var list = document.getElementById("notes_component");
            var acc = list.getElementsByClassName("accordion");
            var i;

            for (i = 0; i < acc.length; i++) {
            acc[i].addEventListener("click", function() {
                /* Toggle between adding and removing the "active" class, to highlight the button that controls the panel */
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
        }
    })
}

//Toggle edit form to edit a note
function edit_note(ele, event){
    var note = ele.parentNode.parentNode.parentNode.querySelector('#update_form')
    if(note.style.display == "block"){
        note.style.display = "none";
    } else {
        note.style.display = "block";
    }
    event.stopPropagation();
}

// function togglePrivacy(ele, event){
//     privacy = ele.getAttribute('privacy');
//     console.log("Privacy:", privacy)
//     if(privacy){
//         privacy = false;
//     } else {
//         privacy = true;
//     }
//     event.stopPropagation();
// }

function toggleEdit(note_comment_id){
    var parent = document.getElementById('comment_' + note_comment_id);
    if (parent.nextElementSibling.style.display === "none") {
        parent.style.display = "none";
        parent.nextElementSibling.style.display = "block";
    } else {
        parent.style.display = "block";
        parent.nextElementSibling.style.display = "none";
    }
}

function toggleCodeEdit(note_comment_id){
    console.log("Toggle code edit");
    var parent = document.getElementById('comment_' + note_comment_id);
    console.log("Comment:", parent.parentElement)
    var codeEditForm = parent.parentElement.querySelector('form');
    console.log("codeEditForm:", codeEditForm)

    if (codeEditForm.style.display === "none") {
        parent.style.display = "none";
        codeEditForm.style.display = "block";
    } else {
        parent.style.display = "block";
        codeEditForm.style.display = "none";
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
}

function revealCategoryAddForm(){    
    document.querySelector(".category_add_form").style.opacity = 1;
}
function hideCategoryAddForm(){
    document.querySelector(".category_add_form").style.opacity = 0;
}

function jump(anchor){
    window.location.href = "#" + anchor;
    history.replaceState(null,null,' ');
}


// Drag and Drop 
var starting_cell = null;
var starting_element = null;
var ending_cell = null;
var ending_element = null;
var starting_note_id = null;
var ending_note_id = null;

function dragStart(event, element) {
    starting_cell = element.parentNode;
    starting_element = element;
}

function allowDrop(event) {
  event.preventDefault();
}

function drop(event, element) {
    ending_element = element.querySelector('div');

    //If target element is not a div, climb parents until div is found.
    ending_cell = element.closest('div');

    console.log("starting_element_id:", starting_element.getAttribute('note_position_id'))
    console.log("ending_element_id:", ending_element.getAttribute('note_position_id'))

    starting_element_id = starting_element.getAttribute('note_position_id')
    ending_element_id = ending_element.getAttribute('note_position_id')

    $.ajax ({
        url: 'ajax/drag_and_drop/' + starting_element_id + '/' + ending_element_id,
        method: 'get',
        // data: $(this).serialize(),
        success: function(serverResponse){
            starting_element.setAttribute('note_position_id', ending_element_id)
            ending_element.setAttribute('note_position_id', starting_element_id)
        }
    });

    ending_cell.append(starting_element);
    starting_cell.append(ending_element);
}

//-------- Wait for page to load --------

$(document).ready(function(){

    // view_category();

    $.ajax({
        url:'ajax/all_notes_partial',
        method:'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            // Toggle open/close accordion elements
                var list = document.getElementById("notes_component");
                var acc = list.getElementsByClassName("accordion");
                var i;

                for (i = 0; i < acc.length; i++) {
                acc[i].addEventListener("click", function() {
                    /* Toggle between adding and removing the "active" class, to highlight the button that controls the panel */
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

        }
    });
  
    if(localStorage.getItem('target_note') != null){

        target_id = localStorage.getItem('target_note');
        var element = document.getElementById(target_id);
        var a_tag = document.createElement('a');

        if(element){
            a_tag.setAttribute('id', 'trigger');
            element.insertBefore(a_tag, element.childNodes[0]);
            element.childNodes[2].classList.toggle("active");
        }
    }

    // Look to see if any notes are active
    var active_notes = document.querySelectorAll('.active');

    if(active_notes){
        jump('trigger');
    
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
        var note_id = note.getAttribute('id');
        localStorage.setItem('target_note', note_id);
        var a_tag = document.createElement('a');
        a_tag.setAttribute('id', 'trigger');
        note.insertBefore(a_tag, note.childNodes[0]);
    });

    // $(".fa-lock-open").on('click', function(e){
    //     // console.log("lock opened: ", this.parentNode.parentNode.getAttribute('category_id'))

    //     category_id = this.getAttribute('custom_id')
    //     console.log("category:", category_id)
    //     $.ajax({
    //         url: `/notes/notebook/${category_id}/privacy`,
    //         method: 'get',
    //         success: function(serverResponse){
    //             $(".notebooks").html(serverResponse);
    //             console.log("Success")
    //             // element.setAttribute('onclick', element.getAttribute('onclick'));
                
    //         }
    //     })

    // })

// element that will be wrapped
var el = document.querySelectorAll('.code_format');
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

// Toggle open/close accordion elements
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class, to highlight the button that controls the panel */
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
});

//Side Nav Script
var toggle = true;

if(localStorage.getItem('sideNavToggle') === null){
    localStorage.setItem('sideNavToggle', false)
} else if(localStorage.getItem('sideNavToggle') === 'false'){
    localStorage.setItem('sideNavToggle', 'true')
} else {
    localStorage.setItem('sideNavToggle', 'false')
}

if(localStorage.getItem('sideNavToggle') === 'true'){
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
    if($(document).ready(function(){
        document.getElementById("toggle_button").innerHTML='<i class="fas fa-chevron-right" id="toggle_button"></i>';
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft= "0";
        toggle = true;
        localStorage.setItem('sideNavToggle', 'true');
    }));
}

function openNav() {
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