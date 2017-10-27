from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
  return  render_template("index.tpl.html", heading="這是由 Flask 的 render_template 丟出來的一個頁面。。。")
  
if __name__ == '__main__':
  app.run()