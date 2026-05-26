from knowledge_base import KNOWLEDGE_BASE

def get_user_symptoms(valid_symptoms):
    """Prompts the user for symptoms and validates the input."""
    print("Please enter your symptoms separated by commas.")
    print(f"Available symptoms: {', '.join(valid_symptoms)}")
    
    while True:
        user_input = input("\nYour symptoms: ").strip()
        
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        
        # Clean and format the input to match the knowledge base (Title Case)
        input_symptoms = [s.strip().title() for s in user_input.split(',')]
        
        # Input Validation
        invalid_symptoms = [s for s in input_symptoms if s not in valid_symptoms]
        if invalid_symptoms:
            print(f"Error: Unrecognized symptoms: {', '.join(invalid_symptoms)}")
            print("Please only use symptoms from the available list and ensure correct spelling.")
            continue
        
        return input_symptoms

def infer_disease(user_symptoms, rules):
    """Applies IF-THEN rules to match symptoms to diseases."""
    user_symptoms_set = set(user_symptoms)
    possible_diseases = []

    for rule in rules:
        conditions_set = set(rule["conditions"])
        # IF all conditions in the rule are a subset of the user's symptoms, THEN conclude disease
        if conditions_set.issubset(user_symptoms_set):
            possible_diseases.append(rule["conclusion"])

    return possible_diseases
 
def main():
    print("="*45)
    print(" Medical Diagnosis Rule-Based Expert System ")
    print("="*45)
    
    valid_symptoms = KNOWLEDGE_BASE["facts"]["symptoms"]
    rules = KNOWLEDGE_BASE["rules"]

    # 1: Accept symptoms as input
    user_symptoms = get_user_symptoms(valid_symptoms)
    
    print("\nAnalyzing symptoms against the knowledge base...")
    
    # 2: Apply rules
    detected_diseases = infer_disease(user_symptoms, rules)

    # 3: Display possible illness
    print("\n" + "="*20 + " RESULTS " + "="*20)
    if detected_diseases:
        print("Based on the symptoms provided, possible conditions include:")
        for disease in detected_diseases:
            print(f"➔ {disease}")
    else:
        print("No exact matching diseases found in the knowledge base.")
        print("➔ Diagnosis inconclusive based on current rules.")
    print("="*49)

if __name__ == "__main__":
    main()