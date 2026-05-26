
SYMPTOMS = [
    "Fever", "Headache", "Cough", "Chest Pain",
    "Sneezing", "Runny Nose", "Fatigue", "Sore Throat",
    "Vomiting", "Diarrhea"
]

DISEASES = ["Malaria", "Pneumonia", "Flu", "Food Poisoning"]


RULES = [
    {
        "id": "D1",
        "conditions": ["Fever", "Headache", "Fatigue"],
        "conclusion": "Malaria"
    },
    {
        "id": "D2",
        "conditions": ["Cough", "Chest Pain", "Fatigue"],
        "conclusion": "Pneumonia"
    },
    {
        "id": "D3",
        "conditions": ["Sneezing", "Runny Nose", "Sore Throat"],
        "conclusion": "Flu"
    },
    {
        "id": "D4",
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