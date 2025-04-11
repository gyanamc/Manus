"""
User preference input system for the Credit Card Recommendation Engine.
This file defines the structure and logic for collecting user preferences.
"""

class UserPreferenceInput:
    """
    Class to handle user preference input collection and validation.
    """
    def __init__(self):
        # Define the questions to ask users
        self.questions = self._define_questions()
        # Define validation rules for inputs
        self.validation_rules = self._define_validation_rules()
        
    def _define_questions(self):
        """
        Define the questions to ask users to collect their preferences.
        Returns a dictionary with question IDs and their details.
        """
        return {
            # Financial Information
            "annual_income": {
                "question": "What is your annual income (in ₹)?",
                "type": "number",
                "required": True,
                "help_text": "This helps us recommend cards you're eligible for."
            },
            "employment_type": {
                "question": "What is your employment status?",
                "type": "select",
                "options": ["Salaried", "Self-employed Professional", "Business Owner", 
                           "Student", "Retired", "Homemaker"],
                "required": True,
                "help_text": "Different cards are designed for different employment types."
            },
            "credit_score": {
                "question": "Do you know your credit score?",
                "type": "select",
                "options": ["Don't Know", "Below 650", "650-700", "700-750", "750-800", "Above 800"],
                "required": False,
                "help_text": "Your credit score affects your eligibility for certain cards."
            },
            
            # Demographic Information
            "age": {
                "question": "What is your age?",
                "type": "number",
                "required": True,
                "help_text": "You must be at least 18 years old to apply for most credit cards."
            },
            "residence_status": {
                "question": "What is your residence status?",
                "type": "select",
                "options": ["Indian Resident", "NRI", "Foreign National"],
                "required": True,
                "help_text": "Some cards are only available to residents of India."
            },
            
            # Spending Preferences
            "primary_spending_categories": {
                "question": "What are your primary spending categories? (Select all that apply)",
                "type": "multi_select",
                "options": ["Groceries", "Dining", "Shopping", "Travel", "Fuel", 
                           "Entertainment", "Bill Payments", "Online Shopping"],
                "required": True,
                "help_text": "We'll recommend cards with rewards for your spending habits."
            },
            "monthly_card_spend": {
                "question": "What is your estimated monthly spend on credit cards (in ₹)?",
                "type": "select",
                "options": ["Less than ₹10,000", "₹10,000 - ₹25,000", "₹25,000 - ₹50,000", 
                           "₹50,000 - ₹1,00,000", "More than ₹1,00,000"],
                "required": True,
                "help_text": "Higher spending may qualify you for better rewards and benefits."
            },
            "international_transactions": {
                "question": "Do you frequently make international transactions?",
                "type": "boolean",
                "required": True,
                "help_text": "Some cards offer better forex rates and international benefits."
            },
            
            # Feature Preferences
            "fee_preference": {
                "question": "What is your preference regarding annual fees?",
                "type": "select",
                "options": ["No annual fee", "Low annual fee with better benefits", 
                           "Don't mind higher fees for premium benefits"],
                "required": True,
                "help_text": "Many cards offer fee waivers based on spending thresholds."
            },
            "reward_preference": {
                "question": "What type of rewards do you prefer?",
                "type": "select",
                "options": ["Cashback", "Reward Points", "Air Miles", "Discounts", "No preference"],
                "required": True,
                "help_text": "Different cards offer different types of rewards."
            },
            "travel_frequency": {
                "question": "How frequently do you travel?",
                "type": "select",
                "options": ["Rarely", "Occasionally", "Frequently"],
                "required": True,
                "help_text": "Frequent travelers benefit from cards with travel perks."
            },
            "lounge_access_importance": {
                "question": "How important is airport lounge access to you?",
                "type": "select",
                "options": ["Not important", "Somewhat important", "Very important"],
                "required": True,
                "help_text": "Many premium cards offer complimentary airport lounge access."
            },
            
            # Additional Preferences
            "preferred_banks": {
                "question": "Do you have any preferred banks? (Select all that apply)",
                "type": "multi_select",
                "options": ["HDFC Bank", "SBI Card", "ICICI Bank", "Axis Bank", "Kotak Mahindra Bank", 
                           "RBL Bank", "IndusInd Bank", "IDFC FIRST Bank", "American Express", "No preference"],
                "required": False,
                "help_text": "Having an existing relationship with a bank may improve approval chances."
            },
            "existing_relationship": {
                "question": "Do you have any existing relationship with banks? (Select all that apply)",
                "type": "multi_select",
                "options": ["HDFC Bank", "SBI", "ICICI Bank", "Axis Bank", "Kotak Mahindra Bank", 
                           "RBL Bank", "IndusInd Bank", "IDFC FIRST Bank", "None"],
                "required": False,
                "help_text": "Having an existing relationship with a bank may improve approval chances."
            },
            "existing_cards": {
                "question": "Do you currently have any credit cards?",
                "type": "boolean",
                "required": True,
                "help_text": "This helps us recommend complementary cards."
            },
            "preferred_card_tier": {
                "question": "What tier of credit card are you looking for?",
                "type": "select",
                "options": ["Basic/Entry-level", "Gold/Classic", "Platinum/Premium", "Super Premium/Signature/Infinite"],
                "required": False,
                "help_text": "Higher tier cards typically offer better benefits but have stricter eligibility criteria."
            }
        }
    
    def _define_validation_rules(self):
        """
        Define validation rules for user inputs.
        Returns a dictionary with field IDs and their validation rules.
        """
        return {
            "annual_income": {
                "min": 0,
                "max": 100000000,  # 10 crore
                "error_message": "Please enter a valid annual income between 0 and 10 crore."
            },
            "age": {
                "min": 18,
                "max": 100,
                "error_message": "You must be at least 18 years old to apply for most credit cards."
            },
            "monthly_card_spend": {
                "min": 0,
                "error_message": "Please enter a valid monthly spend amount."
            }
        }
    
    def get_user_preferences(self):
        """
        Collect user preferences through a series of questions.
        Returns a dictionary with user preferences.
        
        Note: This is a placeholder method. In a real implementation, this would
        interact with a UI framework to collect user inputs.
        """
        # Placeholder for user preferences
        user_preferences = {}
        
        # In a real implementation, we would loop through self.questions
        # and collect user inputs for each question
        
        return user_preferences
    
    def validate_input(self, field_id, value):
        """
        Validate user input for a specific field.
        Returns True if valid, False otherwise.
        """
        if field_id not in self.validation_rules:
            return True
        
        rules = self.validation_rules[field_id]
        
        if "min" in rules and value < rules["min"]:
            return False
        
        if "max" in rules and value > rules["max"]:
            return False
        
        return True
    
    def get_error_message(self, field_id):
        """
        Get the error message for a specific field.
        """
        if field_id not in self.validation_rules:
            return "Invalid input."
        
        return self.validation_rules[field_id].get("error_message", "Invalid input.")
    
    def get_question_details(self, field_id):
        """
        Get the details for a specific question.
        """
        return self.questions.get(field_id, {})


# Example of how to use the UserPreferenceInput class
if __name__ == "__main__":
    preference_input = UserPreferenceInput()
    
    # Print all questions
    print("User Preference Questions:")
    for field_id, details in preference_input.questions.items():
        print(f"\n{details['question']}")
        if details['type'] == 'select' or details['type'] == 'multi_select':
            print(f"Options: {', '.join(details['options'])}")
        print(f"Help: {details['help_text']}")
