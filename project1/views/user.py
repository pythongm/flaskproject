"""
author:gm
c_date:2021/1/23 11:28
u_date:2021/1/23 11:28
reversion:1.0
file_name:user
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash,Blueprint

userbp = Blueprint("user", __name__)
users = [
    {
        "email": "123456@qq.com",
        "password": "123456"
    }
]


@userbp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", **locals())
    elif request.method == "POST":
        user = None
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                session["email"] = email
                return redirect(url_for("main.index"))
        flash("用户名或密码错误")
        return redirect(url_for("user.login"))


@userbp.route("/logout")
def logout():
    session.pop("email")
    return redirect(url_for("main.index"))


@userbp.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html", **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        for u in users:
            if u["email"] == email:
                flash("邮箱已存在")
                return redirect(url_for('user.regist'))
        if password != password2:
            flash("两次密码不一致")
            return redirect(url_for('user.regist'))
        users.append({
            "email": email,
            "password": password
        })
        print("当前用户有", users)
        return redirect(url_for('user.login'))
