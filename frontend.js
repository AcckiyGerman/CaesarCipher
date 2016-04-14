/*
This script takes  'message', put data in json format
send it to backend to encode/decode via XMLHTTPRequest
takes answer and put it back to the html
*/

//----------Binding forms and buttons
inputTextArea = document.getElementById('inputText');
inputRotArea = document.getElementById('ROTATE');
outputTextArea = document.getElementById('outputText');
tryToGuessArea = document.getElementById('tryToGuess');
copyButton = document.getElementById('COPY');
encodeRadioButton = document.getElementById('ENCODE');
decodeRadioButton = document.getElementById('DECODE');

//-----------Setting event listeners
inputTextArea.addEventListener('keyup', sendData);
inputRotArea.addEventListener('keyup', sendData);
encodeRadioButton.addEventListener('click', sendData);
decodeRadioButton.addEventListener('click', sendData);
copyButton.addEventListener('click', onCopy);

//---------------AJAX part---------------
//SENDING DATA
var xmlhttp = new XMLHttpRequest();
function sendData(event) {
    //let's get data from page
    input = inputTextArea.value;
    rotate = inputRotArea.value;
    decode = decodeRadioButton.checked;
    //check validity
    if (!input){
        outputTextArea.value = '\t\tPlease enter your message.';
        return
    }
    if (isNaN(rotate)) {
        outputTextArea.value = '\t\tROT must be a number!';
        return
    }
    //jsonize data
    var request = JSON.stringify({
        "message": input,
        "rotate": rotate,
        "decode": decode
        });
    console.log('request:'+request);
    sendToServer(request);
}
function sendToServer(request) {
    var params = 'REQUEST=' + encodeURIComponent(request)
    xmlhttp.open('POST', 'cgi-bin/index.py', true);
    xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xmlhttp.send(params);
}

//RECEIVING DATA
xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4){
        if (xmlhttp.status == 200){
            onResponse(xmlhttp.responseText); //handler for response
        }
    }
}
function onResponse(response){
    console.log('response:'+response);
    data = JSON.parse(response);
    outputText = data['outputtext'];
    frequencyDict = data['frequencydict'];
    tryToGuess = data['trytoguess'];
    //put data on page
    outputTextArea.value = outputText;
    drawDiagram(frequencyDict);
    tryToGuessArea.value = tryToGuess;
}

// copying data from output to input
function onCopy(event){
    event.preventDefault();
    console.log('copyButton pressed')
    inputTextArea.value = outputTextArea.value;
    sendData(event)
}

//Loading and adjusting canvas on witch we will draw diagram
var canvas = document.getElementById('Canvas');
var scene = canvas.getContext('2d');
scene.font = "14pt Arial";

function drawDiagram(frequencyDict) {
    //clearing canvas
    scene.clearRect(0, 0, canvas.width, canvas.height);
    //sorting symbols and finding max frequency value
    var symbols = new Array();
    var maxVal = 0;
    for (s in frequencyDict){
        symbols.push(s);
        val = frequencyDict[s];
        if (val > maxVal){
            maxVal = val;
        }
    }
    symbols.sort();
    //drawing lines
    scene.fillStyle = "blue";
    var step = canvas.height / maxVal;
    for (i=0; i<maxVal; i++){
        scene.fillRect(0, i*step, canvas.width, 1);
    }
    //drawing pikes
    var xPos = 0;
    var width = 30;
    for (n in symbols) { //this strange javascript enumerates indexes, not values, but ok
        s = symbols[n]; //we can get symbol anyway
        val = frequencyDict[s]
        xPos = n * width;
        scene.fillStyle = "orange";
        scene.fillRect(xPos, canvas.height, width - 5, -val*step);
        scene.fillStyle = "black";
        scene.fillText(s, xPos + 7, canvas.height - 5);
    }
}
// ----------hello to everyone who read that! :) --------------
