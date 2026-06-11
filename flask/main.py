from flask import Flask, redirect, url_for, request, render_template
from datetime import datetime
import csv
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.csv')


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

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f'Hello {guest}'

@app.route('/user/<name>')
def hello_user(name):
   if name == 'admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest = name))

@app.route('/my_word/<word>')
def my_word(word):
#   if len(word) % 2 == 0:
#      return word[::2]
#   else:
#      return word
   return word[::2] if len(word)%2==0 else word

@app.route('/success/<name>')
def success(name):
   return f'welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form.get('name')
   else:
      user = request.args.get('name')

   return redirect(url_for('success', name=user))


@app.route('/form', methods=['GET', 'POST'])
def user_form():
   if request.method == 'POST':
      firstname = request.form.get('firstname')
      lastname = request.form.get('lastname')
      age = request.form.get('age')

      file_exists = os.path.isfile(DATA_FILE)
      with open(DATA_FILE, 'a', encoding='utf-8', newline='') as f:
         writer = csv.writer(f)
         if not file_exists:
            writer.writerow(['firstname', 'lastname', 'age'])
         writer.writerow([firstname, lastname, age])

      return redirect(url_for('success', name=firstname))


if __name__ == '__main__':
   app.run(port=8080, debug=True)