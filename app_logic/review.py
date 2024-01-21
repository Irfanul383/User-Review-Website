from typing import List


class Review:
    review_id: int = None
    topic_id: int
    creator_id: int
    content: str
    category: str
    is_anonymous: bool
    topic_answers: List[int]
    is_draft: bool
    is_text_based: bool

    def __init__(self, review_id, topic_id, creator_id, content, category=None, is_anonymous=False, topic_answers=None, is_draft=False, is_text_based=False):
        """

        :param topic_id: the topic of the review (TBD).
        :param content: the content of the review.
        :param is_anonymous: determines if the review is anonymous or not.
        """
        self.review_id = review_id
        self.topic_id = topic_id
        self.creator_id = creator_id
        self.content = content
        self.category = category
        self.is_anonymous = is_anonymous
        self.topic_answers = topic_answers
        self.is_draft = is_draft
        self.is_text_based = is_text_based
