"""
author:gm
c_date:2021/1/22 11:38
u_date:2021/1/22 11:38
reversion:1.0
file_name:demo4
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from project1.views.main import mainbp
from project1.views.user import userbp


app = Flask(__name__)
app.secret_key = "11111111111111111111111111111111"
app.register_blueprint(mainbp)
app.register_blueprint(userbp)


if __name__ == '__main__':
    app.run(debug=True)
