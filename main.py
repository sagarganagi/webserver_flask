from os import name
from flask import Flask, render_template, request, redirect
import csv
from markupsafe import escape

app = Flask(__name__)
print(__name__)


@app.route('/')
def stat_fun():
  return render_template('index.html')
# @app.route('/about.html')
# def stat_fun1():
#   return render_template('about.html')
@app.route('/submit_form' , methods=["post", "get"])
def submit_form():
  print(request.method)

  if request.method == "POST":
    print(request.form.to_dict)
    data=request.form.to_dict()
    write_to_csv(data)
  print("here visited")
  return redirect('thankyou.html')

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    print("hudshgljbslh")
    email=data['email']
    print(email)
    subject=data['subject']
    message=data["message"]
    file=database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
  with open('database.csv',newline='\n', mode='a') as database1:
    print("hudshgljbslh")
    email=data['email']
    print(email)
    subject=data['subject']
    message=data["message"]
    csv_writer=csv.writer(database1, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])
    # file=database.write(f'\n {email}, {subject}, {message}')



@app.route("/<string:user1>")
def user(user1):
  print('user1')
  return render_template(user1)
