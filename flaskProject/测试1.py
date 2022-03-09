import datetime
from time import strftime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/1")
def pr1():
    print("在控制台输出:  哈哈哈哈哈哈")
    return "这是return1+debug测试"


@app.route("/2")
def html1():
    nowtime = datetime.datetime.now()

    return render_template("测试1.html", var=nowtime)


@app.route("/3/<name>")
def welcome(name):
    return "你好,%s" % name


@app.route("/user/<int:id>")
def welcome2(id):
    return "你好,%d 号会员" %id


if __name__ == "__main":
    app.run(debug=True)
