# Medical ML Systems (Training Track)

## 📌 Purpose

This folder contains machine learning system architecture built during the 6-month Hyderabad AI/ML preparation plan.

Current Focus:

* Production-ready ML class design
* Modular pipeline structure
* Feature schema discipline (21-feature medical dataset)

## 🧠 Current Module

### MedicalClassifier

A clean class-based architecture for thyroid classification including:

* Preprocessing pipeline (schema validation + feature preparation)
* Training interface
* Prediction interface
* Future integration: SHAP explainability & deployment API

## 📊 Dataset Context

* Total Features: 21
* Numerical Features: 6 (real-valued)
* Binary Features: 15 (0/1 medical indicators)
* Task Type: Multi-class medical classification (thyroid condition)

## 🎯 Engineering Goals

* Avoid feature mismatch bugs (21 vs 12 issue faced earlier)
* Maintain consistent feature order
* Transition from notebook-style ML to production architecture
* Prepare for FastAPI deployment in later phases
