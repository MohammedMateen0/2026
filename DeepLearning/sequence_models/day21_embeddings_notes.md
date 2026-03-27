# Day 21 - Word Embeddings & Cosine Similarity

## 1. Why Embeddings?

Neural networks cannot understand text directly.

### Problem with One-Hot Encoding:
- Very high dimensional (e.g., 50,000 words → 50,000 length vector)
- No semantic meaning

Example:
"Lease" and "Contract" → completely different vectors ❌

---

## 2. Dense Embeddings

Embedding models convert words into dense vectors:

Example:
"lease" → [0.12, -0.45, 0.89, ...]

- Typically 384–1536 dimensions
- Captures semantic meaning

---

## 3. Vector Space Intuition

Words with similar meaning are closer in space:

- "Lease" ≈ "Contract"
- "Landlord" ≈ "Tenant"
- "Apple" (fruit) far away

---

## 4. Cosine Similarity

Measures similarity between two vectors.

Formula:

cos(θ) = (A · B) / (||A|| ||B||)

---

## 5. Interpretation

- 1.0 → identical meaning
- 0.0 → unrelated
- -1.0 → opposite

---

## 6. Real-World Use (Your Project)

User Query:
"What happens if I break the contract?"

System:
- Convert query → embedding vector
- Convert document chunks → embeddings
- Compare using cosine similarity
- Retrieve most relevant clause

Example Match:
"Penalties for Early Lease Termination"

---

## 7. Key Insight

Embeddings turn language into geometry.

Similarity = distance in vector space

---

## Status
✅ Understood embeddings + similarity search