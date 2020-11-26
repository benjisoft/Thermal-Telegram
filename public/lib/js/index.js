var db = firebase.firestore();

function sendPrint(text) {
    db.collection("requests").doc().set({
        text: text,
        printed: false
    })
    .then(function() {
        console.log("Document successfully written!");
        return true;
    })
    .catch(function(error) {
        console.error("Error writing document: ", error);
        return false;
    });
}