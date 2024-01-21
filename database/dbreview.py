from typing import List

from database.db import use_db, db
from app_logic.review import Review


@use_db
def create_review(creator_id: int, review: Review):
    # TODO: The category attribute is assigned "NULL" for now; change it to an appropriate value later
    topic_answers = None
    if review.topic_answers is not None:
        result = []
        for point_rating in review.topic_answers:
            result.append(str(point_rating))
            topic_answers = ":".join(result)

    params = (review.topic_id, creator_id, review.content, topic_answers, review.category, review.is_anonymous, review.is_draft, review.is_text_based)
    executable = db.execute("INSERT INTO review VALUES (?,?,?,?,?,?,?,?)", params)
    result = executable.fetchone()
    review_id = executable.lastrowid

    return Review(
        review_id=review_id,
        topic_id=result[0],
        creator_id=result[1],
        content=result[2],
        topic_answers=result[3],
        category=result[4],
        is_anonymous=result[5],
        is_draft=result[6],
        is_text_based=result[7]
    )

@use_db
def get_reviews_for_topic(topic_id: int) -> List[Review]:
    param = (topic_id, )
    reviews = db.executemany("SELECT rowid, * FROM review WHERE topic_id = ?", param).fetchall() # TODO: See why there's no intellisense for the fetchall() method here

    return [
        Review(
            review_id=review[0],
            topic_id=review[1],
            creator_id=review[2],
            content=review[3],
            topic_answers=review[4],
            category=review[5],
            is_anonymous=review[6],
            is_draft=review[7],
            is_text_based=review[8]
        )
        for review in reviews
    ]
