from db import DBClientPerson, DBClientKeys
from db import Session


# session = Session()
# client = DBClientPerson(session)
# print(client.get_person_by_id(1))
# client.add_person("ilyas", "Niyazov", True, 2, [4, 9])
# print(client.get_person_by_id(1))

session = Session()
key_client = DBClientKeys(session)
print(key_client.get_keys_by_id(1))
key_client.add_keys(1, "01239000", 100)
print(key_client.get_keys_by_id(1))

