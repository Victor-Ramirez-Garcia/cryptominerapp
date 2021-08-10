"""
Creates a simple cryptominerapp

"""
import flask
from flask.views import MethodView
from index import Index
from miner import Miner

app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/miner/',
                view_func=Miner.as_view('miner'),
                methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
