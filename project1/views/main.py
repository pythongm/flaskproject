"""
author:gm
c_date:2021/1/23 11:28
u_date:2021/1/23 11:28
reversion:1.0
file_name:main
"""
from flask import render_template, Blueprint

mainbp = Blueprint("main", __name__)
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


@mainbp.route("/")
def index():
    books = list
    return render_template("index.html", **locals())


@mainbp.route("/<int:pk>")
def detail(pk):
    for b in list:
        if b["id"] == pk:
            article = b["article"]
    return render_template("detail.html", **locals())