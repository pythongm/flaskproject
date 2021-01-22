"""
author:gm
c_date:2021/1/22 10:22
u_date:2021/1/22 10:22
reversion:1.0
file_name:demo3
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    name = "张三"
    age = 18
    return render_template("index.html", **locals())


if __name__ == '__main__':
    app.run(debug=True)

