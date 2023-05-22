from db.client import DBClientPerson
from db.session import Session


session = Session()
client = DBClientPerson(session)
print(client.get_person_by_id(1))
client.add_person("biyaslan", "mokaev", True, 2, [4, 9])
print(client.get_person_by_id(1))
