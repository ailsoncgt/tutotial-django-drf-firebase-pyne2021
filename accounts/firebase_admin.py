import firebase_admin
from firebase_admin import credentials, auth

from django.conf import settings

cred = credentials.Certificate(settings.FIREBASE_CONFIG_FILE)
firebase_admin.initialize_app(cred)

def get_auth():
    return auth

