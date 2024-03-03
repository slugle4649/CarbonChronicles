# Main Python code file to start up app

# Importing from website package
from website import create_webapp

# Generating app
app = create_webapp()

# If main is run direclty, web server is started and will run.
if __name__ == "__main__":

    # If debug is True, server will automatically rerun to account for changes in code.
    app.run(debug=True) # Debug will be set to false once production is over.