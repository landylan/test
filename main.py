# coding=utf-8

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
  return  '這是由 Flask 的 render_template 丟出來的一個頁面。。。'
