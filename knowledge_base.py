
SYMPTOMS = [
    "Fever", "Headache", "Cough", "Chest Pain",
    "Sneezing", "Runny Nose", "Fatigue", "Sore Throat",
    "Vomiting", "Diarrhea"
]

DISEASES = ["Malaria", "Pneumonia", "Flu", "Food Poisoning"]


RULES = [
    {
        "id": "A1",
        "conditions": ["Fever", "Headache", "Fatigue"],
        "conclusion": "Malaria"
    },
    {
        "id": "A2",
        "conditions": ["Cough", "Chest Pain", "Fatigue"],
        "conclusion": "Pneumonia"
    },
    {
        "id": "A3",
        "conditions": ["Sneezing", "Runny Nose", "Sore Throat"],
        "conclusion": "Flu"
    },
    {
        "id": "A4",
        "conditions": ["Vomiting", "Diarrhea", "Fatigue"],
        "conclusion": "Food Poisoning"
    },
]

KNOWLEDGE_BASE = {
    "facts": {
        "symptoms": SYMPTOMS,
        "diseases": DISEASES,
    },
    "rules": RULES,
}