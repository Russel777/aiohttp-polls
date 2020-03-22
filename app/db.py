import os

from gino.ext.aiohttp import Gino

db = Gino()
DB_URL = os.getenv('DB_URL', 'postgresql://postgres@db:5432/postgres')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(), default='noname')
    email = db.Column(db.String())


class Poll(db.Model):
    __tablename__ = 'polls'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer(), primary_key=True)
    question_text = db.Column(db.String(), default='')
    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))


class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer(), primary_key=True)
    answer_text = db.Column(db.String(), default='')
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))


def init_db(app):
    app['config'] = {
        'gino': {'dsn': DB_URL},
    }
    db.init_app(app)
    app.middlewares.append(db)


async def create_db():
    await db.gino.create_all()


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.set_bind(DB_URL))
    loop.run_until_complete(create_db())
