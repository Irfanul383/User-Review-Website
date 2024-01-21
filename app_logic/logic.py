import sys
import os

#just to make sure the entire project is in scope while importing
grandparent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, grandparent_dir)


from session_management import user
import database.dbtopic as dbtopic
from .TopicQuestion import TopicQuestion
from .review import Review
import database.dbreview as dbreview
def handle_login(username, password):
    """
    Authenticates the user based on the provided username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        list: A list containing:
            - A boolean indicating success or failure of the login.
            - A message string or None detailing the result.
            - A boolean indicating if there's an alert or None.
    """
    if not user.check_username_exists(username):
        return [False, "Username does not exist", True]
    if not user.match_password(username, password):
        return [False, "Incorrect password", True]
    if user.is_logged_in(username):
        return [False, "User is already logged in", True]
    else:
        user.login_user(username)
        return [True, None, None]


def handle_register(username, password):
    """
    Registers a new user with the given username and password.

    Args:
        username (str): The desired username.
        password (str): The desired password.

    Returns:
        list: A list containing:
            - A boolean indicating success or failure of the registration.
            - A message string detailing the result.
            - A boolean indicating if there's an alert.
    """
    if user.check_username_exists(username):
        return [False, "Username already exists", True]
    else:
        user.create_user(username, password)
        return [True, "register successful", True]


def handle_logout():
    """
    Logs out the current user.

    Returns:
        bool: Always returns True.
    """
    user.logout_user()
    return True


def handle_write_review(review_id, topic_id, creator_id, content, category=None, is_anonymous=False,
                        topic_answers=None, is_draft=False, is_text_based=False):
    # If topic_answers is None, initialize it as an empty list

    if topic_answers is None:
        topic_answers = []

    new_review = Review(review_id, topic_id, creator_id, content, category, is_anonymous,
                        topic_answers, is_draft, is_text_based)

    dbreview.create_review(creator_id, new_review)

    print("Review written")



def handle_create_topic(content, q1, q2, q3):
    #discuss algorithm to find creatorID with group
    #is it a database task or logic or session managment?
    #for now all ID's are 1
    creatorID = 1
    topic_questions = [TopicQuestion(creatorID, q1),
                       TopicQuestion(creatorID, q2),
                       TopicQuestion(creatorID, q3)]
    dbtopic.create_topic(creatorID, content, topic_questions)
    print("topic created")

def handle_post_review(topicID, a1, a2, a3, anonymousflag):
    #wait for app.py to pass topic ID
    #tell imanuel to also have create review take anonymous flag as an argument
    #tell imanuel to provide clarification on how to call his creat review
    #for different purposes such as post or write review
    print("this is not implemented yet")



def handle_search():
    pass
