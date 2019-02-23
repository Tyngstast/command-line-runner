from app import db 
from marshmallow import Schema, fields, validate

command_tags = db.Table('command_tags', 
    db.Column('tag_value', db.String, db.ForeignKey('tag.value'), primary_key=True),
    db.Column('command_id', db.Integer, db.ForeignKey('command.id'), primary_key=True)
)

class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    tags = db.relationship(
        'Tag',
        secondary=command_tags,
        back_populates='commands')

    def __init__(self, value, description):
        self.value = value
        self.description = description

    def __repr__(self):
        return 'Command(%r, %r, %r)' % (self.value, self.description, self.tags)

class Tag(db.Model):
    value = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    commands = db.relationship(
        'Command',
        secondary=command_tags,
        back_populates='tags')

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Tag(%r)' % self.value

class CommandSchema(Schema):
    tags = fields.Nested('TagSchema', many=True, exclude=('commands', ))
    class Meta:
        fields = ('id', 'value', 'description', 'tags')

class TagSchema(Schema):
    commands = fields.Nested(CommandSchema, many=True, exclude=('tags', ))
    class Meta:
        fields = ('value', 'commands')

command_schema = CommandSchema()
commands_schema = CommandSchema(many=True)
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
