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