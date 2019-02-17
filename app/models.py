from app import db 

command_tags = db.Table('command_tags', 
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('command_id', db.Integer, db.ForeignKey('command.id'), primary_key=True)
)

class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    tags = db.relationship(
        "Tag",
        secondary=command_tags,
        back_populates="commands")

    def __init__(self, command, description):
        self.command = command
        self.description = description 

    def __repr__(self):
        return "Command(%r, %r)" % (self.command, self.description)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(20), unique=True, nullable=False)
    commands = db.relationship(
        "Command",
        secondary=command_tags,
        back_populates="tags")

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Tag(%r)" % self.value