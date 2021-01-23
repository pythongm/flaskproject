"""
author:gm
c_date:2021/1/22 11:38
u_date:2021/1/22 11:38
reversion:1.0
file_name:demo4
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "11111111111111111111111111111111"

list = [
    {
        "id": 1,
        "name": "盗墓笔记",
        "info": "讲述一个老九门的故事",
        "article": [
            {
                "title": "第一章",
                "content": "111111",
            },
            {
                "title": "第二章",
                "content": "222222",
            },
            {
                "title": "第三章",
                "content": "333333",
            },
            {
                "title": "第四章",
                "content": "444444",
            },
        ]
    },
    {
        "id": 2,
        "name": "斗破苍穹",
        "info": "讲述一个玄幻世界的故事",
        "article": [
            {
                "title": "第一章",
                "content": "111111",
            },
            {
                "title": "第二章",
                "content": "222222",
            },
            {
                "title": "第三章",
                "content": "333333",
            },
            {
                "title": "第四章",
                "content": "444444",
            },
        ]
    }
]
users = [
    {
        "email": "123456@qq.com",
        "password": "123456"
    }
]


@app.route("/")
def index():
    books = list
    return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
    for b in list:
        if b["id"] == pk:
            article = b["article"]
    return render_template("detail.html", **locals())


@app.route("/login", methods=["GET", "POST"])
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
                return redirect(url_for("index"))
        flash("用户名或密码错误")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("email")
    return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
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
                return redirect(url_for('regist'))
        if password != password2:
            flash("两次密码不一致")
            return redirect(url_for('regist'))
        users.append({
            "email": email,
            "password": password
        })
        print("当前用户有", users)
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
