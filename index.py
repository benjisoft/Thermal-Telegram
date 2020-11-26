import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Use a service account
cred = credentials.Certificate('path/to/serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create an Event for notifying main thread.
callback_done = threading.Event()

# Define printing function
def tPrint(printing):
    command = './print.sh ' + printing
    os.system(command)
    return True

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        tPrint({doc.data.printing})
    callback_done.set()

doc_ref = db.collection(u'requests')

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)