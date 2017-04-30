from flask import Flask, render_template, request, flash, redirect
from wtforms import Form, TextField, SelectField, validators
from searcher import Searcher
from settings import Config

#create the app
app = Flask("goofle")

#connection with the database
my_searcher = None

#Search Form
#textfield for words
#selectfield for results count
class SearchForm(Form):
  text = TextField("text", [validators.required()])
  top = SelectField("top", [validators.required()],
                    choices = [(1,1), (2,2), (3,3), (5,5), (10,10), (15,15), (20,20)],
                    coerce=int)

#main page, searcher
@app.route("/",methods=["GET"])
def index():
  form = SearchForm()
  return render_template("index.html", form=form)

#results page
@app.route("/result",methods=["POST"])
def result():
  form = SearchForm(request.form)
  if form.validate():
    words = form.text.data.split(" ")
    top = form.top.data
    results = my_searcher.search(words, top)
    return render_template("result.html", results=results)
  else:
    return redirect("/")

#start the app
if __name__ == "__main__":
  my_searcher = Searcher(Config.MONGO_HOST,
                         Config.MONGO_PORT,
                         Config.MONGO_DB_NAME,
                         Config.MONGO_COLLECTION_NAME,
                         Config.MONGO_DB_USER,
                         Config.MONGO_DB_PWD)
  app.config.from_object('settings.Config')
  app.run(host=Config.APP_HOST, port=Config.APP_PORT)
