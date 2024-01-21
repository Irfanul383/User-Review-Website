from typing import List
class TopicQuestion:

    topic_id: int
    question: str

    def __init__(self, topic_id, question=""):
        """
        :param topic_id: the ID of the topic to which the question belongs
        :param question: String containing the question
        """
        self.topic_id = topic_id
        self.question = question
