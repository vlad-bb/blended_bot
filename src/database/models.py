from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, IntField, StringField


class Users(Document):
    user_id = IntField()
    first_name = StringField(null=False)
    last_name = StringField(null=True)
    username = StringField(null=True)
    language_code = StringField(null=False)
    created = DateTimeField(default=datetime.now)
    is_active = BooleanField(default=True)
    meta = {'allow_inheritance': True}


