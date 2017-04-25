from flask import Flask, render_template, request, flash, redirect
from wtforms import Form, TextField, SelectField, validators
from searcher import Searcher

class SearchForm(Form):
    text = TextField("text", [validators.required()])
    top = SelectField("top", [validators.required()],
                      choices = [(1,1), (2,2), (3,3), (5,5), (10,10), (15,15), (20,20)],
                      coerce=int)

app = Flask("goofle")
searcher = None

@app.route("/",methods=["GET"])
def index():
    form = SearchForm()
    return render_template("index.html", form=form)

@app.route("/result",methods=["POST"])
def result():
    form = SearchForm(request.form)
    if form.validate():
        words = form.text.data.split(" ")
        top = form.top.data
        results = searcher.search(words, top)
        return render_template("result.html", results=results)
    else:
        return redirect("/")

if __name__ == "__main__":
    searcher = Searcher()
    app.secret_key = "zzi0uj3NiiaTKJ1BkHBaJA=="
    app.config["SESSION_TYPE"] = "filesystem"
    app.run(debug = True, port = 8000)
