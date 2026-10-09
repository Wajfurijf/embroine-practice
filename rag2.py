from sentence_transformers import SentenceTransformer
import numpy as np

model=SentenceTransformer('all-MiniLM-L6-v2')

documents=[
    "Dogs are allowed in the office on fridays",
    "Pets can come to work on Furry Fridays",
    "Remote work policy allows 3 days work from home"
]

embeddings=model.encode(documents)

sim_1_2=np.dot(embeddings[0], embeddings[1])
sim_2_3=np.dot(embeddings[1], embeddings[2])
sim_1_3=np.dot(embeddings[0], embeddings[2])

print(f"Dogs and Pets : {sim_1_2*100:.1f}% similar")
print(f"Pets and Remote : {sim_2_3*100:.1f}% similar")
print(f"Dogs and Remote : {sim_1_3*100:.1f}% similar")

