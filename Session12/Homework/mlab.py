import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds023480.mlab.com:23480/ryantest

host = "ds023480.mlab.com"
port = 23480
db_name = "ryantest"
user_name = "admin"
password = "04042204"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
