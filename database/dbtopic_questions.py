from database.db import use_db, db
from typing import List
from app_logic.TopicQuestion import TopicQuestion

@use_db
def create_topic_question(topic_questions: List[TopicQuestion], topic_id: int) -> List[TopicQuestion]:
    params = []
    for topic_question in topic_questions:
        params.append([topic_question.question, topic_id])

    results = db.executemany('INSERT INTO topic_question VALUES (?, ?)', params).fetchall()
    topic_questions = [TopicQuestion(question=result[0], topic_id=result[1]) for result in results]
    return topic_questions
