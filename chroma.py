import chromadb

client=chromadb.PersistentClient(path="./chroma_db")

collection=client.create_collection('docs')

docs=["Dogs are allowed in the office on fridays",
    "Pets can come to work on Furry Fridays",
    "Remote work policy allows 3 days work from home"]

for i, doc in enumerate(docs):
    collection.add(
        documents=[doc],
        ids=[f"doc_{i}"]
    )
query="Can i bring my dog to work"
results=collection.query(query_texts=[query], n_results=2)

print(results)
