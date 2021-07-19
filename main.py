from app import app


# run the Flask application to make the server listen to a specific port
if __name__ == "__main__":
    # set debug to True in order to log helpful information for debugging
    app.run(debug=True)
