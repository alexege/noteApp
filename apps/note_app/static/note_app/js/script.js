//Prevent elements from propagating
function StopEventPropagation(event) { 
    if (event.stopPropagation) { 
        event.stopPropagation(); 
    } 
    else if(window.event) { 
        window.event.cancelBubble=true; 
    } 
}

// Search bar functionality
function searchFunction() {
    var searchbox = document.getElementById("myInput");
    var filter = searchbox.value.toUpperCase();
    var list = document.getElementById("notes_component");
    var items = list.getElementsByClassName("accordion");

    for (i = 0; i < items.length; i++) {
        var a = items[i].getElementsByClassName("note")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            items[i].style.display = "";
        } else {
            items[i].style.display = "none";
        }
    }
}

// Display comment configuration menu
function showMenu(comment){
    comment.parentNode.querySelector('.comment_menu').style.display = "block";
    // comment.parentNode.style.border = "2px solid #09d6ef";
}

// Hide comment configuration menu
function hideMenu(comment){
    comment.parentNode.querySelector('.comment_menu').style.display = "none";
    // comment.parentNode.style.border = "0px solid #09d6ef";
}

// Indent comment
$(document).on('click', '.fa-indent', function(e){
    var comment_id = this.closest('.comment').getAttribute('comment_id')
    var note_id = this.closest('.note_body').getAttribute('note_id');
    e.preventDefault();
    $.ajax({
        url: `comment/${comment_id}/indent`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            togglePanelDisplay(note_id);
            addClickListener();
        }
    })
})

// Outdent comment
$(document).on('click', '.fa-outdent', function(e){
    var comment_id = this.closest('.comment').getAttribute('comment_id')
    var note_id = this.closest('.note_body').getAttribute('note_id');
    e.preventDefault();
    $.ajax({
        url: `comment/${comment_id}/outdent`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            togglePanelDisplay(note_id);
            addClickListener();
        }
    })
})


// Show/Hide Navbar Dropdown
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
    }
  }

// Toggle Light/Dark Mode
function toggleLightDark(){
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        if (currentTheme === 'dark') {
            toggleSwitch.checked = true;
        }
    }

    function switchTheme(e) {
        if (e.target.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }
        else {        document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }
    }
    toggleSwitch.addEventListener('change', switchTheme, false);
}

//Delete Note
function delete_note(note_id){
    $.ajax({
        url: `note/delete/${note_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#notes_component').html(serverResponse);
            addClickListener();
        }
    })
}

function del_comment(comment_id){
    console.log("Comment ID:", comment_id);
    document.getElementById('deleteModal').style.display = "block";
    document.getElementById('modal_confirm').setAttribute('onclick', `confirm_del_comment(${comment_id})`);
    document.getElementById('modal_message').innerHTML = '';
    document.getElementById('modal_message').append('Are you sure you wish to delete this comment?');
}

function confirm_del_comment(comment_id){
    document.getElementById('deleteModal').style.display = "none";
    delete_comment(comment_id);
}

function del_note(note_id){
    document.getElementById('deleteModal').style.display = "block";
    document.getElementById('modal_confirm').setAttribute('onclick', `confirm_del_note(${note_id})`);
    document.getElementById('modal_message').innerHTML = '';
    document.getElementById('modal_message').append('Are you sure you wish to delete this note?');
}

function confirm_del_note(comment_id){
    document.getElementById('deleteModal').style.display = "none";
    delete_note(comment_id);
}

function del_notebook(notebook_id){
    document.getElementById('deleteModal').style.display = "block";
    document.getElementById('modal_confirm').setAttribute('onclick', `confirm_del_notebook(${notebook_id})`);
    document.getElementById('modal_message').innerHTML = '';
    document.getElementById('modal_message').append('Are you sure you wish to delete this notebook?');
}

function confirm_del_notebook(notebook_id){
    document.getElementById('deleteModal').style.display = "none";
    delete_notebook(notebook_id);
}

function del_category(category_id){
    document.getElementById('deleteModal').style.display = "block";
    document.getElementById('modal_confirm').setAttribute('onclick', `confirm_del_category(${category_id})`);
    document.getElementById('modal_message').innerHTML = '';
    document.getElementById('modal_message').append('Are you sure you wish to delete this category?');
}

function confirm_del_category(category_id){
    document.getElementById('deleteModal').style.display = "none";
    delete_category(category_id);
}

function no(){
    document.getElementById('deleteModal').style.display = "none";
}

// Delete Comment
function delete_comment(comment_id){

    var element = document.getElementById(`comment_${comment_id}`);
    var note_id = element.closest('.note_body').getAttribute('note_id');
    var note = element.closest('.note_body');

    if(!comment_id){
        comment_id = note.getAttribute('note_id');
    }

    $.ajax({
        url:`comment/delete/${comment_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            togglePanelDisplay(note_id);
            addClickListener();
        }
    })
}

function openCloseAccordion(source){
    // Toggle open/close accordion elements
    var list = document.getElementById(`${source}`);
    var acc = list.getElementsByClassName("accordion");
    var i;
    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
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

//Add new Notebook
$(document).on('submit', '.notebook_add_form', function(e){
    e.preventDefault();
    $.ajax({
        url: `notebook/add`,
        method: 'POST',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("Added a new notebook");
            $('#mySidenav').html(serverResponse);
            
            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks")

            //Give focus to category input
            $('#add_notebook_input').focus();
        }
    })
})

//Toggle Edit Notebook
function edit_notebook(e){
    var form = e.parentNode.querySelector('.notebook_edit_form');
    if(form.style.display === "block"){
        form.style.display = "none";
    } else {
        form.style.display = "block"
    }
}

//Edit Notebook
$(document).on('submit', '.notebook_edit_form', function(e){
    var notebook_id = this.closest('.notebook').getAttribute('id');
    e.preventDefault();
    $.ajax({
        url:`/notes/notebook/edit/${notebook_id}`,
        method: 'POST',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#mySidenav').html(serverResponse);
            console.log("Successfully edited notebook");

            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks");
        }
    })
})

//Delete Notebook
function delete_notebook(notebook_id){
    $.ajax({
        url: `/notes/notebook/delete/${notebook_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#mySidenav').html(serverResponse);
            
            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks");
        }
    })
}

//Add Category
$(document).on('submit', '.category_add_form', function(e){
    e.preventDefault();

    // check if contained within public notebooks or not.
    var container = this.closest('.public_notebooks');

    notebook_id = this.closest('.notebook').getAttribute('id');
    $.ajax({
        url: `category/add/${notebook_id}`,
        method: 'POST',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#mySidenav').html(serverResponse);
            
            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks");

            elements = document.getElementsByClassName(`notebook${notebook_id}`);
            for(var i = 0; i < elements.length; i++){
                elements[i].querySelector('.accordion').classList.toggle('active');
            }

            //Toggle acitve elements to be open
            var sidenav = document.getElementById('mySidenav');
            var notebooks = sidenav.querySelectorAll('.active');

            if(container != null){
                notebooks[1].nextElementSibling.style.display = 'block';
                //Grab focus of private notebook input field
                $(`#private_category_input_${notebook_id}`).focus();
            } else {
                notebooks[0].nextElementSibling.style.display = 'block';
                //Grab focus of public notebook input field
                $(`#public_category_input_${notebook_id}`).focus();
            }
        }
    })
})

//Delete Category
function delete_category(category_id){
    event.stopPropagation();
    var element = document.getElementById(category_id);
    notebook_id = element.closest('.notebook').getAttribute('id');
    $.ajax({
        url: `category/delete/${category_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#mySidenav').html(serverResponse);
            
            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks");

            elements = document.getElementsByClassName(`notebook${notebook_id}`);
            for(var i = 0; i < elements.length; i++){
                elements[i].querySelector('.accordion').classList.toggle('active');
            }

            //Toggle active elements to be open
            var sidenav = document.getElementById('mySidenav');
            var notebooks = sidenav.querySelectorAll('.active');

            notebooks[0].nextElementSibling.style.display = 'block';
        }
    })
}

function togglePrivacy(e){
    event.stopPropagation()
    e.classList.toggle('fa-lock-open');
    e.classList.toggle('fa-lock');
    notebook_id = e.getAttribute('note_id');

    $.ajax({
        url:`notebook/${notebook_id}/privacy`,
        method:'get',
        success: function(serverResponse){
            $('#mySidenav').html(serverResponse);

            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks");
        }
    })
}

// Toggle open/close accordion elements
function addClickListener(){
    var list = document.getElementById("notes_component");
    var acc = list.getElementsByClassName("accordion");
    for (var i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");

            /* Toggle between hiding and showing the active panel */
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
            panel.style.display = "none";
            localStorage.clear();
            } else {
            panel.style.display = "block";
            }
        });
    }
}

//Set this element's active toggle to display the panel
function togglePanelDisplay(note_id){
    var note = document.querySelector(`#note${note_id}`);
    note.querySelector('button').classList.toggle('active');
    var panel = note.querySelector('.panel')
    if(panel.style.display === "block"){
        panel.style.display = "none";
    } else {
        panel.style.display = "block";
    }
}

// On add new note form submission
$(document).on('submit', '.new_note_form', function(e){
    var notebook_name = this.getAttribute('notebook_name');
    console.log("Notebook:", notebook_name);
    e.preventDefault();
    $.ajax({
        url:`note/add/${notebook_name}`,
        data: $(this).serialize(),
        method: 'POST',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);
            
            addClickListener();
        }
    })
})

// On update note form submission
$(document).on('submit', '.note_update_form', function(e){
    e.preventDefault();
    var note_id = this.closest('.note_body').getAttribute('note_id');
    $.ajax({
        url:`note/edit/${note_id}`,
        data: $(this).serialize(),
        method: 'POST',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);
            
            addClickListener();
        }
    })
})

// Add Comment
$(document).on('submit', '.new_comment_form', function(e){
    e.preventDefault();
    var formNumber = this.getAttribute('id');
    var note_id = this.parentNode.parentNode.getAttribute('note_id');
    var data = new FormData($('.new_comment_form').get(0));

    $.ajax({
        url:'comment/add/' + note_id,
        method: 'POST',
        headers: { "X-CSRFToken": '{{csrf_token}}' },
        data: data,
        data: $(this).serialize(),
        cache: false,
        // processData: false,
        // contentType: false,
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            togglePanelDisplay(note_id);
            addClickListener();

            //Focus new comment textarea
            document.getElementById('note' + note_id).querySelector('.note_textarea').focus();
        }
    })
})

// Edit Comment
$(document).on('submit', '.comment_edit_form', function(e){
    e.preventDefault();
    var comment_id = this.parentNode.querySelector('li').getAttribute('comment_id');
    var note_id = this.closest('.note_body').getAttribute('note_id');

    $.ajax({
        url:'comment/edit/' + comment_id,
        data: $(this).serialize(),
        method: 'POST',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            togglePanelDisplay(note_id);
            addClickListener();
        }
    })
})

//Dynamically view notes of a specific category
function view_category(notebook, category){
    $.ajax({
        url: `/notes/selected_notes/${notebook}/${category}`,
        method: 'get',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            addClickListener();
        }
    })
}

function view_sidenav(){
    $.ajax({
        url: `/notes/sidenav`,
        method: 'get',
        success: function(serverResponse){
            $('#mySidenav').html(serverResponse);
            openCloseAccordion("notebooks");
            openCloseAccordion("public_notebooks");
        }
    })
}

//Dynamically view notes of a specific category

function view_all_notebook_categories(notebook){
    console.log("Notebook: ", notebook);
    $.ajax({
        url: `/notes/view/${notebook}`,
        method: 'get',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            addClickListener();
        }
    })
}

function showAllNotes(){
    $.ajax({
        url: `/notes/all_notes`,
        method: 'get',
        success: function(serverResponse){
            $("#notes_component").html(serverResponse);

            addClickListener();
        }
    })
}

// //Dynamically view notes of a specific category
// function view_public_category(category){
//     $.ajax({
//         url: `/notes/public/${category}`,
//         method: 'get',
//         success: function(serverResponse){
//             $("#notes_component").html(serverResponse);

//             addClickListener();
//         }
//     })
// }

//Toggle edit note form
function edit_note(event, element){
    event.stopPropagation();
    var note = element.closest('.note_body').querySelector('.note_update_form')
    if(note.style.display == "block"){
        note.style.display = "none";
    } else {
        note.style.display = "block";
    }
}

//Toggles edit comment form
function toggleEdit(note_comment_id){
    var parent = document.getElementById('comment_' + note_comment_id);
    if (parent.nextElementSibling.style.display === "none") {
        parent.querySelector('.note_content').style.display = "none";
        parent.nextElementSibling.style.display = "block";
    } else {
        parent.querySelector('.note_content').style.display = "block";
        parent.nextElementSibling.style.display = "none";
    }
}

//Hide edit comment form
function hideEditForm(note_comment_id){
    var parent = document.getElementById('comment_' + note_comment_id);
    parent.querySelector('.note_content').style.display = "block";
    parent.nextElementSibling.style.display = "none";
}

// https://hackernoon.com/copying-text-to-clipboard-with-javascript-df4d4988697f
function copyToClipboard(ele){
    const el = document.createElement('textarea');
    el.value = ele.closest('.comment').querySelector('.note_content').innerText;
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

// Drag and Drop Notes
//Available functions: ondragstart, ondrag, ondragend, ondragenter, ondragover, ondragleave, ondrop
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
//   event.target.style.border = "2px solid lime";
}

function drop(event, element) {
    ending_element = element.querySelector('div');

    //If target element is not a div, climb parents until div is found.
    ending_cell = element.closest('div');
    starting_element_id = starting_element.getAttribute('note_position_id')
    ending_element_id = ending_element.getAttribute('note_position_id')

    $.ajax ({
        url: `ajax/drag_and_drop/${starting_element_id}/${ending_element_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            starting_element.setAttribute('note_position_id', ending_element_id)
            ending_element.setAttribute('note_position_id', starting_element_id)
        }
    });

    ending_cell.append(starting_element);
    starting_cell.append(ending_element);
}

// Drag and Drop Notebooks
//Available functions: ondragstart, ondrag, ondragend, ondragenter, ondragover, ondragleave, ondrop
var notebook_cell_start = null;
var notebook_start = null;
var notebook_cell_end = null;
var notebook_end = null;

var starting_notebook_id = null;
var ending_notebook_id = null;

function notebookDragStart(event, element) {
    notebook_cell_start = element.parentNode;
    notebook_start = element;
}

function notebookAllowDrop(event) {
  event.preventDefault();
//   event.target.style.border = "2px solid lime";
}

function notebookDrop(event, element) {
    notebook_end = element.querySelector('div');

    //If target element is not a div, climb parents until div is found.
    notebook_cell_end = element.closest('div');
    notebook_start_id = notebook_start.getAttribute('notebook_position_id')
    notebook_end_id = notebook_end.getAttribute('notebook_position_id')

    $.ajax ({
        url: `ajax/drag_and_drop_notebooks/${notebook_start_id}/${notebook_end_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            notebook_start.setAttribute('notebook_position_id', notebook_end_id)
            notebook_end.setAttribute('notebook_position_id', notebook_start_id)
        }
    });

    notebook_cell_end.append(notebook_start);
    notebook_cell_start.append(notebook_end);
}

//-------- Wait for page to load --------
$(document).ready(function(){
    // view_sidenav();

    openCloseAccordion("notebooks");
    openCloseAccordion("public_notebooks");

    toggleLightDark();
    view_category('All', 'All');


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

    // Toggle open or closed if active
    if(active_notes){
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

    $(document).on('click', '.close', function(event){
        no();
    })

    // Get the modal
    var modal = document.getElementById("deleteModal");
    $(document).on('click', function(event){
        if(event.target == modal) {
            modal.style.display = "none";
        }
    })

    if(document.getElementById('checkbox').checked){
        localStorage.setItem('darkToggle', 'dark');
    }
    if(localStorage.getItem('darkToggle') == 'dark'){
        document.getElementById('checkbox').checked = true;
    } else {
        document.getElementById('checkbox').checked = false;
    }

}); //End of document.ready();

//Side Nav Script
var toggle = true;
if(localStorage.getItem('sideNavToggle') === null){
    localStorage.setItem('sideNavToggle', false);
} else if(localStorage.getItem('sideNavToggle') === 'false'){
    localStorage.setItem('sideNavToggle', 'true');
} else {
    localStorage.setItem('sideNavToggle', 'false');
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