//const { ipcRenderer } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
var input_value = document.getElementById('input_SteamID');
var response = document.getElementById('value_js');

//ipcRenderer.on('message', function (event, text) {
//    var response = document.getElementById('value_js');
//    console.log(text)
//    response.innerHTML = text;
//});

function pythcall(x) {
    const childPython = spawn(path_extraResources + "\\extraResources\\backend\\csgovaluecalculator.exe", [input_value.value]);
    //const childPython = spawn(__dirname + "\\extraResources\\backend\\csgovaluecalculator.exe", [input_value.value]);
    //const childPython = spawn("python", ["csgovaluecalculator.py", input_value.value]);

    childPython.stdout.on('data', (data) => {
        response.innerHTML = `${data}`
    });

    childPython.stderr.on('data', (data) => {
        response.innerHTML = `A fatal error was detected. Please restart the app. `
    });
}

function myFonction() {
    response.innerHTML = "Searching, please wait...";
    var path_extraResources = path.dirname(__dirname);
    if(isNaN(input_value.value)){ 
        if(input_value.value.substring(0, 4) == "http"){
            response.innerHTML = "SteamID profile link detected, please wait...";
            pythcall();
        }else{
            response.innerHTML = "Format not valid: " + input_value.value;
        }
    }else{
        if(parseInt(input_value.value) > 9999999999999999){
            response.innerHTML = "SteamID format detected, please wait...";
            pythcall();
        }else{
            response.innerHTML = "Format not valid: " + input_value.value;
        }
     }
}
