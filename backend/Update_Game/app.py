from api import app

if __name__ == '__main__':
    app.config.from_object('config.Config')
    app.run(debug=app.config['DEBUG'])
