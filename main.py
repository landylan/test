# coding=utf-8

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
  return  render_template('index.tpl.html', heading=u'Flask 的 render_template 送出來的一段文字...')

if __name__ == "__main__":
  app.run(port=80, debug=True)