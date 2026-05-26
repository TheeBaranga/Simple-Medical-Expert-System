# 1. Project Title
Medical Diagnosis Rule-Based Expert System

## 2. Project Description
This project is a simple AI-driven rule-based system designed to act as an initial medical diagnostic tool. It prompts users to input a series of symptoms, processes these inputs using predefined logic within a knowledge base, and outputs the most likely illness based on strict IF-THEN rules. 

## 3. Objectives
* To demonstrate the core concepts of Knowledge Representation using Python.
* To build a functional inference engine capable of subset-matching.
* To construct and visualize a semantic network linking patients, symptoms, and diseases.

## 4. Symptoms Used
The knowledge base currently recognizes the following symptoms:
* Fever, Headache, Cough, Chest Pain, Sneezing, Runny Nose, Fatigue, Sore Throat, Vomiting, Diarrhea

## 5. Diseases Detected
The system can infer the following medical conditions:
* Malaria
* Pneumonia
* Flu
* Food Poisoning

## 6. Rules Applied
The inference engine applies strict IF-THEN logic. Examples include:
* **Rule D1:** IF (Fever AND Headache AND Fatigue) THEN conclude **Malaria**.
* **Rule D2:** IF (Cough AND Chest Pain AND Fatigue) THEN conclude **Pneumonia**.
* **Rule D3:** IF (Sneezing AND Runny Nose AND Sore Throat) THEN conclude **Flu**.
* **Rule D4:** IF (Vomiting AND Diarrhea AND Fatigue) THEN conclude **Food Poisoning**.

## 7. Technologies Used
* **Language:** Python 3.x
* **Data Structures:** Python Dictionaries and Lists (for the Knowledge Base)
* **Visualization:** Draw.io 

## 8. How to Run the Program
1. Clone this repository to your local machine.
2. Ensure both `main.py` and `knowledge_base.py` are in the same directory.
3. Open your terminal or command prompt.
4. Run the script using the command:
   ```bash
   python main.py