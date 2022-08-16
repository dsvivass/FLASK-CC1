from flaskr import create_app

app = create_app('default')

# Context is a dictionary that is used to store application-specific data.

app_context = app.app_context()
app_context.push()