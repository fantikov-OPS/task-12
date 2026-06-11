from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def date_now():
   return str(datetime.now())

@app.route('/hello/<name>')
def hello_name(name):
   return f"Hello {name}"

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return f'Blog Number {postID}'

@app.route('/rev/<float:revNo>')
def revisoin(revNo):
   return f'Revision Number {revNo}'

@app.route('/path_to/<path:myPath>')
def my_path(myPath):
   return f'My path {myPath}'

@app.route('/two_pow/<int:twoNumber>')
def two_number(twoNumber):
   return str(2**twoNumber)

if __name__ == '__main__':
   print(app.url_map)
   app.run(port=8080)