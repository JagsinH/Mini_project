from flask import Flask, render_template, request
import requests

api_endpoint = "https://api.npoint.io/01f1d6378c69c2a581e2"
posts = requests.get(url=api_endpoint, verify=False).json()

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def hello():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/login")
def submitted():
    render_template('submitted.html')


if __name__ == "__main__":
    app.run(debug=True)

