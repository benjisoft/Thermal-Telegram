import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import threading
import time

# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

# Initialise Firebase variables
db = firestore.client()
doc_ref = db.collection(u'requests')

# Create an Event for notifying main thread.
callback_done = threading.Event()

# Define printing function
def tPrint(printing):
    command = './print.sh "' + str(printing) + '"'
    os.system(command)
    return True

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for change in changes:
        item = change.document.to_dict()
        if (change.type.name == "ADDED" and item["printed"] == False):
            if '"' in item["text"]:
                print("Fraudulent Code Execution Attempted")
            else:
                tPrint(item["text"])
            db.collection(u'requests').document(change.document.id).set({
                u'printed': True
            }, merge=True)
    callback_done.set()

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)

while True:
    time.sleep(1)