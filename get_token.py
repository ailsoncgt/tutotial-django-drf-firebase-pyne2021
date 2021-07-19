import pyrebase

config = {
    "apiKey": "AIzaSyAkKHAEyPyXDZ1Vz9xGzYTw4wAejsXySog",
    "authDomain": "pyne-9bd56.firebaseapp.com",
    "databaseURL": "https://pyne-9bd56.firebaseio.com",
    "projectId": "pyne-9bd56",
    "storageBucket": "pyne-9bd56.appspot.com",
    "messagingSenderId": "940937104065"
}

firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
email = 'ailsoncgt@gmail.com'
password = 'pynordeste10'
user = auth.sign_in_with_email_and_password(email, password)
print(user['idToken'], user['localId'])