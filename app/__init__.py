from flask import Flask
# make use of datastore database in Google Cloud platform
from google.cloud import datastore


# This __name__ is needed so that Flask knows where to look for resources such
# as templates and static files.
app = Flask(__name__)
datastore_client = datastore.Client()


# In fact, we can put routes'code here. However, in order to have a good
# structure for the project we separate it from app initialization and database
# connection code.
from app import routes
