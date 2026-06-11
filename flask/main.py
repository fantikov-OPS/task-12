from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
   return str(datetime.now())


def world():
   return 'World!'

if __name__ == '__main__':
   app.add_url_rule('/world', 'world',world)
   print(app.url_map)
   app.run(port=8080)