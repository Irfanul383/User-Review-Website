from unittest import TestCase
from database.dbtopic import create_topic
from app_logic.topic import Topic


class DBTopic(TestCase):
    def handle_create_topic(self):
        topic_params = (1, "Sample topic", None)
        result = create_topic(*topic_params)
        created_topic: Topic = result['topic']

        # Assert that the topic content is correct
        self.assertEqual(created_topic.content, topic_params[1])

