import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_visitor_to_cloud(visitor_data):
    # Save to Firestore collection 'visitors'
    db.collection('visitors').add(visitor_data)