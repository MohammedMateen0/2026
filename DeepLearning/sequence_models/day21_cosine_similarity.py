import numpy as np
def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
query=np.array([0.2,0.1,0.7])
clause1=np.array([0.21,0.09,0.68])
clause2=np.array([0.9,0.1,0.1])
sim1 = cosine_similarity(query, clause1)
sim2 = cosine_similarity(query, clause2)

print("Similarity with clause1:", sim1)
print("Similarity with clause2:", sim2)