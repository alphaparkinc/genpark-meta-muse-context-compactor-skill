from client import MetaMuseContextCompactorClient
client = MetaMuseContextCompactorClient()
print(client.compact("Long context text "*50))