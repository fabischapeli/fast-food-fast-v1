from flask import Flask
from app.v2.resources.menu import menu_api
from app.v2.resources.orders import orders_api
from app.v2.resources.users import users_api
from app.v2.resources.meals import meals_api

def create_app():
    from app.v2.models.createdb import main
    app = Flask(__name__)
    app.config.from_object('instance.v2.config.DevelopmentEnv')
    app.url_map.strict_slashes = False

    app.register_blueprint(menu_api, url_prefix='/api/v2')
    app.register_blueprint(orders_api, url_prefix='/api/v2')
    app.register_blueprint(users_api, url_prefix='/api/v2')
    app.register_blueprint(meals_api, url_prefix='/api/v2')
    main()

    @app.route('/', methods=['GET'])
    def index_info():
        return 'Welcome to Fast Food Fast Version 2'

    return app