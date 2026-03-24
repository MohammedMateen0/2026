## Day 18 — Convolutional Neural Networks (CNN Basics)

CNNs are designed for image data and use local filters to extract features.

---

Max Pooling

Max Pooling reduces spatial dimensions while keeping important features.

Example:

Input (4×4)

1 3 2 4
5 6 1 2
7 2 8 3
1 4 2 9

After 2×2 max pooling:

6 4
7 9

---

Purpose

- Reduce computation
- Extract dominant features
- Provide translation invariance

---

Output Shape Example

Input: (1, 28, 28)
After pooling: (1, 14, 14)

---

Key Concept

CNNs preserve spatial structure, unlike fully connected neural networks.