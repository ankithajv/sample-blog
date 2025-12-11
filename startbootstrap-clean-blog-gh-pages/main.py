from flask import Flask , render_template , request
import requests
import smtplib

response = requests.get("https://api.npoint.io/c64c78bebbdf1b3f13e0")
posts = response.json()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

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


@app.route("/contact" , methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"],data["email"],data["phone"],data["message"])

        return render_template("contact.html", msg_sent=True)
    
    return render_template("contact.html", msg_sent=False)


def send_email(name , email , phone , message):
    email_address = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

    with smtplib.SMTP("smtp.gmai.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL,OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL,OWN_EMAIL,email_message)
if __name__ == "__main__":
    app.run(debug=True)



# CURRENTLY IN MY NPOINT DOESN'T HAVE "img-url" SO WE CANNOT SEE BACKGROUND IMAGE IN INDIVIDUAL POSTS.


#CAN ALSO USE  

"""def contact():
    post_method = request.method
    match post_method:
        case "POST":
            print('ok post')
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            print(name, email, phone, message)
            return '<h1>Successfully sent your message!!!</h1>'
        case "GET":
            return render_template("contact.html")"""