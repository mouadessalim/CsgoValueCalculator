const { ipcRenderer } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

ipcRenderer.on('message', function (event, text) {
    var response = document.getElementById('value_js');
    console.log(text)
    response.innerHTML = text;
});

function myFonction() {
    var input_value = document.getElementById('input_SteamID');
    var response = document.getElementById('value_js');
    response.innerHTML = "Searching ..."
    var path_extraResources = path.dirname(__dirname);
    const childPython = spawn(path_extraResources + "\\extraResources\\backend\\csgovaluecalculator.exe", [input_value.value]);
    //const childPython = spawn(__dirname + "\\extraResources\\backend\\csgovaluecalculator.exe", [input_value.value]);

    childPython.stdout.on('data', (data) => {
        response.innerHTML = `${data}`
    });

    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

}