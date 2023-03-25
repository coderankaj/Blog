from blog import app, engine, Base
from blog import  db


if __name__ == '__main__':
    app.run(debug=True, threaded=True)