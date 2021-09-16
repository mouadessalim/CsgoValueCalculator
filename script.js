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
    var path_extraResources = path.dirname(__dirname);
    const childPython = spawn(path_extraResources + "\\extraResources\\backend\\csgovaluecalculator.exe", [input_value.value]);
    //const childPython = spawn(__dirname + "\\extraResources\\backend\\csgovaluecalculator.exe", [input_value.value]);
    //const childPython = spawn("python", ["csgovaluecalculator.py", input_value.value]);

    childPython.stdout.on('data', (data) => {
        response.innerHTML = `${data}`
    });

    childPython.stderr.on('data', (data) => {
        response.innerHTML = `A fatal error was detected. if this happen many of time, please contact me.`;
        fs.writeFileSync(process.env.APPDATA + "\\csgo-value-calculator\\logs.txt", `${data}`);
    });
}

function myFonction() {
    response.innerHTML = "Searching, please wait...";
    if(isNaN(input_value.value)){ 
        if(input_value.value.substring(0, 29) == "http://steamcommunity.com/id/"){
            response.innerHTML = "Steam profile custom link detected, please wait...";
            pythcall();
        }else if(input_value.value.substring(0, 30) == "https://steamcommunity.com/id/"){
            response.innerHTML = "Steam profile custom link detected, please wait...";
            pythcall();
        }else if(input_value.value.substring(0, 35) == "http://steamcommunity.com/profiles/"){
            response.innerHTML = "Steam profile link detected, please wait...";
            pythcall();
        }else if(input_value.value.substring(0, 36) == "https://steamcommunity.com/profiles/"){
            response.innerHTML = "Steam profile link detected, please wait...";
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
