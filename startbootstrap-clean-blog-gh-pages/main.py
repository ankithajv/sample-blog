from flask import Flask , render_template
import requests


response = requests.get("https://api.npoint.io/c64c78bebbdf1b3f13e0")
posts = response.json()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # 1. Get the data from the API again
    # (In a real app, you might store this globally to save API calls, but this is fine for now)
    blog_url = "https://api.npoint.io/c64c78bebbdf1b3f13e0" # Make sure this matches your URL
    response = requests.get(blog_url)
    all_posts = response.json()
    
    # 2. Find the specific post with the matching ID
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
            
    # 3. Render the post.html template with the specific post data
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)



# CURRENTLY IN MY NPOINT DOESN'T HAVE "img-url" SO WE CANNOT SEE BACKGROUND IMAGE IN INDIVIDUAL POSTS.