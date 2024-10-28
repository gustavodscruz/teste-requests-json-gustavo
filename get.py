# Install the Appwrite SDK
# pip install appwrite

from appwrite.client import Client
from appwrite.services.databases import Databases

# Initialize the Appwrite client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Your Appwrite endpoint
client.set_project('671e7c2a00080871ec57')           # Your project ID
client.set_key('standard_ab8122587f06b6515cd303fca72cab497a5f1aaf87a4ed136ab2fa52c8a8ae6a82262ef3e664d14bd77565b0f8c360c77a3cc625f6e76b3e123293c3d41e5c1a028760992a12b98dc96a8ecf2b72878947b884fb1fd0801e69432df8eed5cb1bfd8b8eae2d7c93da09582de1ca849e0515f14003b62f4e4245e57f6b73c7a0be')  # Your API key

# Initialize the Databases service
databases = Databases(client)

# ID of the database and collection in Appwrite
database_id = '671e7d31000aa5a6082a'
collection_id = '671e7d3a002f2ec859a4'

# Function to fetch documents from the collection
def fetch_documents():
    try:
        response = databases.list_documents(
            database_id=database_id,
            collection_id=collection_id
        )
        documents = response['documents']
        for doc in documents:
            print(doc)
    except Exception as e:
        print(f"Falha ao buscar documentos: {str(e)}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.json()}")

# Fetch and print documents
fetch_documents()