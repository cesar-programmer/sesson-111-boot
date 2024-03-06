export FLASK_APP=app/routes.py
export FLASK_ENV=development # this line is optional and can be removed if you want to run in production mode
# FLASK_ENV=development is used to run the app in debug mode

flask run --debug