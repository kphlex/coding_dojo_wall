from flask_app import app
from flask_app.controllers import nav_routes
from flask_app.controllers import content_routes




if __name__ == '__main__':
    app.run(debug=True)