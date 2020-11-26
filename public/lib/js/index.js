const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");

var db = firebase.firestore();

function sendPrint(text) {
    db.collection("requests").doc().set({
        text: text,
        printed: false
    })
    .then(function() {
        console.log("Document successfully written!");
    })
    .catch(function(error) {
        console.error("Error writing document: ", error);
    });
}