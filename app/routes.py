from app import app
from flask import render_template


@app.route('/')

@app.route ('/Home')
def Home():
    return  render_template('Home.html', title="Home")


@app.route ('/lab1')
def lab1():
    return  render_template('lab1.html', title="Lab 1")

@app.route ('/lab2')
def lab2():
    return  render_template('lab2.html', title="Lab 2")