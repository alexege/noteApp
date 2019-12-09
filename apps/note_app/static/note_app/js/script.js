function StopEventPropagation(event) { 
    if (event.stopPropagation) { 
        event.stopPropagation(); 
    } 
    else if(window.event) { 
        window.event.cancelBubble=true; 
    } 
}


// // Search bar functionality
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


//Indent
function showIndent(comment){
    comment.parentNode.querySelector('.comment_menu').style.display = "block";
}

// Outdent
function showOutdent(comment){
    comment.parentNode.querySelector('.comment_menu').style.display = "none";
}

//Indent comment
$(document).on('click', '.fa-indent', function(e){
    var comment_id = this.closest('.comment').getAttribute('comment_id')
    console.log("comment_id:", comment_id);
    var note_id = this.closest('.note_body').getAttribute('note_id');

    e.preventDefault();
    $.ajax({
        // url:`note/delete/${note_id}`,
        url: `comment/${comment_id}/indent`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("success");
            $("#notes_component").html(serverResponse);
            // $(".public_notebooks").html(serverResponse);

            //Set this element's active toggle to display the panel
            var note = document.querySelector(`#note${note_id}`);
            // var isActive = note.querySelector('button').classList.contains('active');
            note.querySelector('button').classList.toggle('active');
            console.log("note:", note);
            // console.log("isActive:", isActive);
            var panel = note.querySelector('.panel')
            if(panel.style.display === "block"){
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }

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

})

//outdent comment
$(document).on('click', '.fa-outdent', function(e){
    var comment_id = this.closest('.comment').getAttribute('comment_id')
    console.log("comment_id:", comment_id);
    var note_id = this.closest('.note_body').getAttribute('note_id');

    e.preventDefault();
    $.ajax({
        url: `comment/${comment_id}/outdent`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("success");
            $("#notes_component").html(serverResponse);
            // $(".public_notebooks").html(serverResponse);


            //Set this element's active toggle to display the panel
            var note = document.querySelector(`#note${note_id}`);
            // var isActive = note.querySelector('button').classList.contains('active');
            note.querySelector('button').classList.toggle('active');
            console.log("note:", note);
            // console.log("isActive:", isActive);
            var panel = note.querySelector('.panel')
            if(panel.style.display === "block"){
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }

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

})


// Show/Hide Navbar Dropdown

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
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

// Style
function getColorScheme(){
    var list_of_colors = ['font-color', 'primary-color', 'secondary-color', 'heading-color', 'background-color'];
    var list_of_default_colors = ['red', 'white', 'blue', 'purple', 'green'];
    //Check to see if all the colors stored in localStorage are null. If so, set them to their default colors.
    for(var i = 0; i < list_of_colors.length; i++){
        if(localStorage.getItem(`${list_of_colors[i]}`) == null){
            localStorage.setItem(`${list_of_colors[i]}`, `${list_of_default_colors[i]}`);
        }
    }
}

function changeFontColor(color){
    localStorage.setItem("font-color", color)
}
function changePrimaryColor(color){
    localStorage.setItem("primary-color", color)
}
function changeSecondaryColor(color){
    localStorage.setItem("secondary-color", color)
}
function changeheadingColor(color){
    localStorage.setItem("heading-color", color)
}
function changeBackgroundColor(color){
    localStorage.setItem("background-color", color)
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

// Delete Note
$(document).on('click', '.note_trashcan', function(e){
    // console.log("this.parent", this.closest(`.note_body`).getAttribute('note_id'));
    var note_id = this.closest('.note_body').getAttribute('note_id');
    console.log("note_id:", note_id);    
    e.preventDefault();
    e.stopPropagation(); //Doesn't seem to work
    $.ajax({
        url:`note/delete/${note_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("success");
            $("#notes_component").html(serverResponse);
            // $(".public_notebooks").html(serverResponse);

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

})

// Delete Comment
$(document).on('click', '.fa-trash', function(e){
    // console.log("this.parent", this.closest(`.note_body`).getAttribute('note_id'));
    var note_id = this.closest('.note_body').getAttribute('note_id');
    console.log("Clicking on a trash button");
    comment_id = this.parentNode.parentNode.getAttribute('comment_id')
    var note = this.closest('.note_body');
    console.log("note:", note);
    if(!comment_id){
        comment_id = note.getAttribute('note_id');
    }
    console.log("comment_id:", comment_id)
    e.preventDefault();
    e.stopPropagation(); //Doesn't seem to work
    $.ajax({
        url:`comment/delete/${comment_id}`,
        method: 'get',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("success");
            $("#notes_component").html(serverResponse);
            // $(".public_notebooks").html(serverResponse);


            //Set this element's active toggle to display the panel
            var note = document.querySelector(`#note${note_id}`);
            // var isActive = note.querySelector('button').classList.contains('active');
            note.querySelector('button').classList.toggle('active');
            console.log("note:", note);
            // console.log("isActive:", isActive);
            var panel = note.querySelector('.panel')
            if(panel.style.display === "block"){
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }


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

})

//Add new Notebook
$(document).on('submit', '.category_add_form', function(e){
    e.preventDefault();
    $.ajax({
        url: `notebook/add`,
        method: 'POST',
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("Added a new notebook");
            $('#mySidenav').html(serverResponse);
            
            // Toggle open/close accordion elements
            var list = document.getElementById("notebooks");
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
            
            // Toggle open/close accordion elements
            var list = document.getElementById("public_notebooks");
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

            //Give focus to category input
            $('#add_notebook_button').focus();
        }
    })
})

//Edit Notebook

//Delete Notebook
function delete_notebook(e){
    console.log("element:", e.closest('.notebook').getAttribute('id'));
    notebook_id = e.closest('.notebook').getAttribute('id');
    console.log("notebook_id", notebook_id);
    $.ajax({
        url: `/notes/notebook/delete/${notebook_id}`,
        method: 'get',
        // data: $(this).serialize(),
        success: function(serverResponse){
            console.log("Added a new notebook");
            $('#mySidenav').html(serverResponse);
            
            // Toggle open/close accordion elements
            var list = document.getElementById("notebooks");
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
            
            // Toggle open/close accordion elements
            var list = document.getElementById("public_notebooks");
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

function togglePrivacy(e){
    console.log("this:", e);
    console.log("this:", e.classList)
    e.classList.toggle('fa-lock-open');
    e.classList.toggle('fa-lock');

    notebook_id = e.getAttribute('note_id');
    console.log("notebook_id:", notebook_id);

    $.ajax({
        url:`notebook/${notebook_id}/privacy`,
        method:'get',
        success: function(serverResponse){
            console.log("Toggled Privacy");
            $('#mySidenav').html(serverResponse);
        }
    })

}

// // Toggle Notebook Privacy
// $(document).on('click', '.fa-lock, .fa-lock-open', function(e){
//     e.preventDefault();
//     e.stopPropagation(); //Doesn't seem to work
//     this.classList.toggle('fa-lock-open');
//     this.classList.toggle('fa-lock');
    
//     notebook_id = this.getAttribute('note_id')
//     $.ajax({
//         url:`notebook/${notebook_id}/privacy`,
//         method: 'get',
//         success: function(serverResponse){
//             console.log("success");
//             // $("#notebooks").html(serverResponse);
//             // $(".public_notebooks").html(serverResponse);
//             $("#mySidenav").html(serverResponse);

//             // Toggle open/close accordion elements
//             var list = document.getElementById("notebooks");
//             var acc = list.getElementsByClassName("accordion");
//             var i;
//             for (i = 0; i < acc.length; i++) {
//                 acc[i].addEventListener("click", function() {
//                     /* Toggle between adding and removing the "active" class, to highlight the button that controls the panel */
//                     this.classList.toggle("active");

//                     /* Toggle between hiding and showing the active panel */
//                     var panel = this.nextElementSibling;
//                     if (panel.style.display === "block") {
//                     panel.style.display = "none";
//                     localStorage.clear();
//                     console.log("Clearing local storage")
//                     } else {
//                     panel.style.display = "block";
//                     }
//                 });
//             }

//             // Toggle open/close accordion elements
//             var list = document.getElementById("public_notebooks");
//             var acc = list.getElementsByClassName("accordion");
//             var i;
//             for (i = 0; i < acc.length; i++) {
//                 acc[i].addEventListener("click", function() {
//                     /* Toggle between adding and removing the "active" class, to highlight the button that controls the panel */
//                     this.classList.toggle("active");

//                     /* Toggle between hiding and showing the active panel */
//                     var panel = this.nextElementSibling;
//                     if (panel.style.display === "block") {
//                     panel.style.display = "none";
//                     localStorage.clear();
//                     console.log("Clearing local storage")
//                     } else {
//                     panel.style.display = "block";
//                     }
//                 });
//             }
//         }
//     })

// })

// On add new note form submission
$(document).on('submit', '.new_note_form', function(e){
    e.preventDefault();
    console.log("add_new_note_form_submitted");
    $.ajax({
        url:'note/add',
        data: $(this).serialize(),
        method: 'POST',
        success: function(serverResponse){
            console.log("Posted successfully");
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

            //Focus new note textarea
            window.setTimeout(function ()
            {
                document.getElementById('title_input').focus();
            }, 2000);
        }
    })
})

// On add new comment form submission
$(document).on('submit', '.new_comment_form', function(e){
    e.preventDefault();
    console.log("this:", this);
    var note_id = this.parentNode.parentNode.getAttribute('note_id');
    console.log("note_id:", note_id)


    console.log("file:", $('.new_comment_form')[0])
    // var form_data = new FormData($('.new_comment_form').get(0))
    // form_data.append('file', $('.new_comment_form')[0])
    // var formData = new FormData();
    // formData.append('file1', myFile); 
    // const data_ = JSON.stringify(data)
    // formData.append('data', data_);
    // console.log("form_data:", form_data);
    
    $.ajax({
        url:'comment/add/' + note_id,
        data: $(this).serialize(),
        // data: form_data,
        method: 'POST',
        success: function(serverResponse){
            console.log("Posted successfully");
            $("#notes_component").html(serverResponse);

            //Set this element's active toggle to display the panel
            var note = document.querySelector(`#note${note_id}`);
            // var isActive = note.querySelector('button').classList.contains('active');
            note.querySelector('button').classList.toggle('active');
            console.log("note:", note);
            // console.log("isActive:", isActive);
            var panel = note.querySelector('.panel')
            if(panel.style.display === "block"){
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }

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

                //Focus new comment textarea
                document.getElementById('note' + note_id).querySelector('.note_textarea').focus();
            }
        }
    })
})

// On update edited comment form submission
$(document).on('submit', '.comment_edit_form', function(e){
    e.preventDefault();
    var comment_id = this.parentNode.querySelector('li').getAttribute('comment_id');
    var note_id = this.closest('.note_body').getAttribute('note_id');
    console.log("note_id:", note_id);
    $.ajax({
        url:'comment/edit/' + comment_id,
        data: $(this).serialize(),
        method: 'POST',
        success: function(serverResponse){
            console.log("Posted successfully");
            $("#notes_component").html(serverResponse);

            //Set this element's active toggle to display the panel
            var note = document.querySelector(`#note${note_id}`);
            console.log("note:", note)
            var isActive = note.querySelector('button').classList.contains('active');
            note.querySelector('button').classList.toggle('active');
            console.log("note:", note);
            console.log("isActive:", isActive);
            var panel = note.querySelector('.panel')
            if(panel.style.display === "block"){
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }

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
})

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

//Dynamically view notes of a specific category
function view_public_category(category){
    $.ajax({
        url: `/notes/public/${category}`,
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
        parent.querySelector('.note_content').style.display = "none";
        parent.nextElementSibling.style.display = "block";
    } else {
        // parent.style.display = "block";
        parent.querySelector('.note_content').style.display = "block";
        parent.nextElementSibling.style.display = "none";
    }
}

function hideEditForm(note_comment_id){
    var parent = document.getElementById('comment_' + note_comment_id);
    parent.querySelector('.note_content').style.display = "block";
    parent.nextElementSibling.style.display = "none";
}

// function toggleCodeEdit(note_comment_id){
//     console.log("Toggle code edit");
//     var parent = document.getElementById('comment_' + note_comment_id);
//     console.log("Comment:", parent.parentElement)
//     var codeEditForm = parent.parentElement.querySelector('form');
//     console.log("codeEditForm:", codeEditForm)

//     if (codeEditForm.style.display === "none") {
//         parent.style.display = "none";
//         codeEditForm.style.display = "block";
//     } else {
//         parent.style.display = "block";
//         codeEditForm.style.display = "none";
//     }
// }

// https://hackernoon.com/copying-text-to-clipboard-with-javascript-df4d4988697f
function copyToClipboard(ele){
    const el = document.createElement('textarea');
    // console.log("element:", ele.closest('.comment'));
    // el.value = ele.parentNode.querySelector('li').innerText;
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
    getColorScheme();
    toggleLightDark();
    view_category();

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