# coding=utf-8

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
  return  render_template('index.tpl.html', heading=u'Flask 的 render_template 送出來的一段文字...')
