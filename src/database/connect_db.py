from mongoengine import connect
from dotenv import dotenv_values


config = dotenv_values(".env")

mongo_user = config.get('user')
mongodb_pass = config.get('pass')
db_name = config.get('db_name')
domain = config.get('domain')

"""
user=admin
pass=abc123
db_name=blended_2
domain=cluster0.j1abi6t.mongodb.net
"""

# connect to cluster on AtlasDB with connection string

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)