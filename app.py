# This file is the entry point to the server.
import sys
import os
from bottle import run, route, TEMPLATE_PATH, redirect, request, template

from database import db
from app_logic import logic

# Prevents python from generating cache files
sys.dont_write_bytecode = True

# Appends the path to your interfaces directory to Bottle's template search path
interfaces_dir = os.path.join(os.getcwd(), 'interfaces')
TEMPLATE_PATH.append(interfaces_dir)

# default route to login page
@route("/")
def redirect_to_login_page():
    return redirect("/login")
# login page route
@route("/login")
def show_login_page():
    return template("login", error_message=None, has_error=None)

# login page logic for error handling
@route("/login", method="post")
def handle_login():
    a = logic.handle_login(request.forms.get('username'), request.forms.get('password'))
    if a[0]:
        return redirect("/topic_list")
    else:
        return template("login", error_message=a[1], has_error=a[2])

# logout page route
@route("/logout")
def logout():
    logic.handle_logout()
    return redirect("/login")

# register page route
@route("/register")
def show_register_page():
    return template("register", error_message=None, has_error=None)

# login page logic for error handling 
@route("/register", method="post")
def handle_register():
    a = logic.handle_register(request.forms.get('wanted_username'), request.forms.get('wanted_password'))
    if a[0]:
        return template("login", error_message=a[1], has_error=a[2])
    else:
        return template("register", error_message=a[1], has_error=a[2])

@route("/reviews")
def show_reviews():
    return template("review_list")

@route("/reviews_list/<topic_id>")
def review_list(topic_id):
    return template("review_list")

@route("/post_review")
def post_review():
    return template("post_review")

@route("/post_review", method="post")
def handle_post_review():
    #takes the answer to questions and gives them to logic to handle
    rating1 = request.forms.get('rating1')
    rating2 = request.forms.get('rating2')
    rating3 = request.forms.get('rating3')
    # needs to be implemented
    topic_ID = 1
    # also needs to be implemented
    is_anonymous = 0
    logic.handle_post_review(topic_ID, rating1, rating2, rating3, is_anonymous)
    return redirect("/topic_list")


@route("/post_topic")
def post_topic():
    return template("post_topic")


# Access the 'topic_name' parameter from the URL
@route("/post_topic/<topic_name>")
def topic_page(topic_name):
    return f"Topic Page for {topic_name}"

# Handle the post request with the topic name
@route("/post_topic", method="post")
def handle_post_topic():
    topic_name = request.forms.get('topic_name')
    #discuss with group, is this hadnler and its page needed?

@route("/topic_list")
def topic_list():
    return template("topic_list")

@route("/write_review/<topic_id>")
def write_review():
    return template("write_review")

@route("/write_review/<topic_id>", method="post")
def handle_write_review(topic_id):
    review_content = request.forms.get('reviewContent')
    is_anonymous = request.forms.get('anonymous')
    logic.handle_write_review(topic_id, request.forms.get('creator_id'), request.forms.get('content'),
                              request.forms.get('category'), request.forms.get('is_anonymous'),
                              request.forms.get('topic_answers'),
                              request.forms.get('is_draft'), request.forms.get('is_text_based'))
    return redirect("/topic_list")

@route("/write_topic")
def write_topic():
    return template("write_topic")

@route("/write_topic", method="post")
def handle_write_topic():
    topic_content = request.forms.get('topicContent')
    question1 = request.forms.get('question1')
    question2 = request.forms.get('question2')
    question3 = request.forms.get('question3')
    logic.handle_create_topic (topic_content, question1, question2, question3)
    return redirect("/topic_list")

# Server information
hostname = 'localhost'
port = 8080

# Sets up the database
db.setup()

if __name__ == "__main__":
    run(host=hostname, port=port, debug=True)
