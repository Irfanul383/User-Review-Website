from database.db import use_db, db
from typing import List
from app_logic.topic import Topic
from app_logic.TopicQuestion import TopicQuestion
from .dbtopic_questions import create_topic_question


@use_db
def create_topic(creator_id, title, topic_questions) -> Topic:
    # Create topic questions first
    create_topic_params = [creator_id, title]

    created_topic = db.execute("INSERT INTO topic VALUES (?, ?)", create_topic_params)
    topic_id = created_topic.lastrowid

    created_topic_questions: List[TopicQuestion] = []

    if topic_questions is not None:
        # Create the topic questions with the associated topic id
        created_topic_questions = create_topic_question(topic_questions, topic_id)

    return Topic(
        topic_id=topic_id,
        title=title,
        creator_id=creator_id,
        topic_questions=created_topic_questions
    )

@use_db
def get_topics() -> List[Topic]:
    topics = db.executemany("SELECT rowid, * FROM topic").fetchall()

    return [
        Topic(
            topic_id=topic[0],
            creator_id=topic[1],
            title=topic[2]
        )
        for topic in topics
    ]
