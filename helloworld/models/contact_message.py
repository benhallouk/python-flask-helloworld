from helloworld import db

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    message = db.Column(db.String(120), unique=False)
    
    # Example of how to use one to many
    #----------------------------------
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    # add the user class it should contains something like that
    # messages = db.relationship('ContactMessage', backref='user', lazy='dynamic')

    # Example of using many to many
    #----------------------------------
    # tags = db.Table('bookmark_tag',
    #    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    #    db.Column('bookmark_id', db.Integer, db.ForeignKey('bookmark.id'))
    # )
    
    # Then in relationship
    # _tags = db.relationship('Tag', secondary=tags, backref= db.backref('bookmarks', lazy='dynamic'))

    def __repr__(self):
        return '<ContactMessage %r>' % self.name

db.create_all()