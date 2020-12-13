let textarea = document.getElementById("message_box")

// intervall set to 30 seconds, with a reset when keys are pressed.
// this is so that the user is not stressed when typing into chatt.

let timer = setTimeout(function(){
    location.reload();
}, 30000)

textarea.onkeydown = function(){

    clearTimeout(timer)

    timer = setTimeout(function(){
    location.reload();
}, 30000)
}