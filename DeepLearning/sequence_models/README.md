# Day 19 - Sequence Models (RNN & LSTM)

## 1. Recurrent Neural Network (RNN)

### Concept
RNNs process sequences step-by-step while maintaining a hidden state.

**Formula:**
h_t = f(Wx_t + Uh_{t-1})

- h_t: hidden state (memory)
- x_t: input at time t
- h_{t-1}: previous hidden state

---

## 2. Vanishing Gradient Problem

During Backpropagation Through Time (BPTT):

Gradients are repeatedly multiplied across time steps.

If weights < 1:
Gradient → exponentially decreases → approaches 0

### Result:
- Model forgets earlier inputs
- Cannot learn long-term dependencies

Example:
Sequence length = 500 → early information lost

---

## 3. Long Short-Term Memory (LSTM)

LSTM solves vanishing gradient using a **cell state (C_t)** and **gates**.

---

### Forget Gate
f_t = σ(W_f [h_{t-1}, x_t])

- Decides what to remove from memory

---

### Input Gate
i_t = σ(W_i [h_{t-1}, x_t])

- Decides what new information to store

---

### Candidate Memory
C~_t = tanh(W_c [h_{t-1}, x_t])

---

### Cell State Update
C_t = f_t * C_{t-1} + i_t * C~_t

- Additive update → prevents gradient vanishing

---

### Output Gate
h_t = o_t * tanh(C_t)

---

## 4. Key Insight

RNN:
- Memory overwritten → gradients vanish

LSTM:
- Memory preserved via controlled gates
- Additive updates allow stable gradient flow

---

## 5. When to Use

- RNN → short sequences
- LSTM → long dependencies
- GRU → lighter alternative
- Transformers → modern standard

---

## Status
✅ Concepts understood  
# Day 20 - Self-Attention & Transformers

## 1. Problem with RNN/LSTM

- Sequential processing → slow
- Cannot parallelize efficiently
- Long sequences → information loss (vanishing gradient)

Example:
A 40-page document → early information forgotten

---

## 2. Transformer Idea

Instead of reading tokens one by one:

→ Process all tokens simultaneously  
→ Learn relationships between every pair of words

---

## 3. Self-Attention Mechanism

Each word creates 3 vectors:
- Query (Q)
- Key (K)
- Value (V)

---

## 4. Attention Formula

Attention(Q, K, V) = softmax(QKᵀ / √d) V

---

## 5. Intuition

- Compare each word with every other word
- Assign importance scores
- Aggregate relevant information

Example:
"He" → attends to "landlord"  
"It" → attends to "deposit"

---

## 6. Why It Beats LSTM

| Feature | LSTM | Transformer |
|--------|------|------------|
| Processing | Sequential | Parallel |
| Long-range context | Weak | Strong |
| Speed | Slow | Fast (GPU optimized) |

---

## 7. Key Insight

Self-attention = dynamic weighting of relationships

Model decides:
- What to focus on
- What to ignore

---

## Status
✅ Understood core attention mechanism