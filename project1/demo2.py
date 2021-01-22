"""
author:gm
c_date:2021/1/22 9:37
u_date:2021/1/22 9:37
reversion:1.0
file_name:demo2
"""

from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "欢迎来到Flask首页"


@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到Flask{pk}"


if __name__ == '__main__':
    app.run(host="192.168.11.6", port="6789", debug=True)

