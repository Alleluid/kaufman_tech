console.log('loaded auth.js');
let btnToggle = $("button#toggle-hidden");
let inputPasswd = $("input#passwd")[0];
let isInputHidden = true;

btnToggle.click(toggle_hidden);

function toggle_hidden(){
    console.log("click");
    if (isInputHidden) {
        inputPasswd.type = "text";
        isInputHidden = false;
    } else {
        inputPasswd.type = "password";
        isInputHidden = true;
    }
}