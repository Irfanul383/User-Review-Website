from unittest import TestCase
from database.dbreview import create_review
from app_logic.review import Review


class DBReview(TestCase):
    def handle_create_review(self):
        review_params = (2, "Sample review")
        result = create_review(1, Review(*review_params))
        created_review: Review = result['review']

        # Assert that the topic id is correct
        self.assertEqual(created_review.topic_id, review_params[0])

        # Assert that the content is correct
        self.assertEqual(created_review.content, review_params[1])
