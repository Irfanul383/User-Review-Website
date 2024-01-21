from typing import List
from .TopicQuestion import *
class Topic:
    topic_id: int
    creator_id: int
    title: str
    topic_questions: List[TopicQuestion]
    is_anonymous: bool

    def __init__(self, topic_id, title, creator_id, is_anonymous=False, topic_questions=None):
        """

        :param content: the content of the review.
        :param is_anonymous: determines if the review is anonymous or not.
        """
        self.topic_id = topic_id
        self.title = title
        self.creator_id = creator_id
        self.is_anonymous = is_anonymous
        self.topic_questions = topic_questions
