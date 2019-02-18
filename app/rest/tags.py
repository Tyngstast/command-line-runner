from flask_restful import Resource, reqparse, abort
from app.models import *
from app import db

class TagListResource(Resource):
    def get(self):
        tags = Tag.query.all()
        if not tags:
            return abort(404, message="No tags in database")

        return tags_schema.dump(tags)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tags', type=list, location='json')
        args = parser.parse_args(strict=True)

        tags = []
        for tag in args['tags']:
            if Tag.query.filter_by(value=tag).first():
                return abort(409, message="Tag already exists: %s" % tag)

            tags.append(Tag(tag))

        db.session.bulk_save_objects(tags)
        db.session.commit()

        return tags_schema.dump(tags), 201


class TagResource(Resource):
    def get(self, identifier: str):
        tag = Tag.query.filter_by(value=identifier).first()

        if not tag:
            return abort(404)

        return tag_schema.dump(tag, message="Tag not found")
    
    def delete(self, identifier: str):
        tag = Tag.query.filter_by(value=identifier).first()

        if not tag:
            return abort(404, message='Tag not found')

        db.session.delete(tag)
        db.session.commit()

        return '', 204