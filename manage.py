from helloworld import app, db
# from helloworld.models import User 
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    # data can be seeded in thatway
    # db.session.add(User(username='', email=''))
    # db.session.commit()
    print 'initialized the database'

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to drop the data"):
        db.drop_all()
        print 'Droped the database'

if __name__ == '__main__':
    manager.run()