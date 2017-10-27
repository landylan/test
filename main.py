from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
  return  render_template("index.tpl.html", heading="這是由 Flask 的 render_template 丟出來的一個頁面。。。")
