from unittest import TestCase
from database.dbtopic_questions import create_topic_question
from app_logic.TopicQuestion import TopicQuestion


class DBReview(TestCase):
    def handle_create_topic_question(self):
        creator_id = 1
        topic_id = 2
        topic_question_params = [
            TopicQuestion(creator_id, "Question 1"),
            TopicQuestion(creator_id, "Question 2"),
            TopicQuestion(creator_id, "Question 3")
        ]

        result = create_topic_question(topic_question_params, topic_id)
        self.assertEqual(result.rowcount, 1)