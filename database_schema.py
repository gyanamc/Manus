"""
Database schema for the Credit Card Recommendation Engine.
This file defines the structure of the database that will store credit card information.
"""

class CreditCardSchema:
    """
    Schema for credit card information in the database.
    """
    def __init__(self):
        self.schema = {
            # Basic card information
            "card_id": "string",  # Unique identifier for the card
            "card_name": "string",  # Name of the credit card
            "issuer": "string",  # Bank or financial institution issuing the card
            "card_type": "string",  # Type of card (rewards, cashback, travel, etc.)
            "card_tier": "string",  # Basic, Gold, Platinum, etc.
            
            # Fees and charges
            "joining_fee": "float",  # One-time joining fee
            "annual_fee": "float",  # Annual fee
            "renewal_fee": "float",  # Renewal fee (if different from annual)
            "interest_rate": "float",  # Interest rate (APR)
            "interest_free_period": "integer",  # Interest-free period in days
            "forex_markup": "float",  # Foreign exchange markup percentage
            "cash_advance_fee": "float",  # Cash advance fee percentage
            "late_payment_fee": "float",  # Late payment fee
            "fee_waiver_condition": "string",  # Conditions for fee waiver
            
            # Rewards and benefits
            "reward_rate": "float",  # Reward points per ₹100 spent
            "cashback_rate": "float",  # Cashback percentage
            "reward_categories": "list",  # Categories with higher rewards
            "lounge_access": "boolean",  # Airport lounge access
            "lounge_access_count": "integer",  # Number of complimentary visits
            "fuel_surcharge_waiver": "boolean",  # Fuel surcharge waiver
            "movie_benefits": "boolean",  # Movie ticket benefits
            "dining_benefits": "boolean",  # Dining benefits
            "travel_benefits": "boolean",  # Travel benefits
            "shopping_benefits": "boolean",  # Shopping benefits
            "insurance_coverage": "boolean",  # Insurance coverage
            "welcome_benefits": "string",  # Welcome benefits description
            "milestone_benefits": "string",  # Milestone benefits description
            
            # Eligibility criteria
            "min_income": "float",  # Minimum annual income required
            "min_age": "integer",  # Minimum age required
            "max_age": "integer",  # Maximum age limit
            "credit_score_required": "integer",  # Minimum credit score required
            "employment_type": "list",  # Eligible employment types
            "residence_status": "list",  # Eligible residence status
            
            # Additional information
            "co_branded": "boolean",  # Whether it's a co-branded card
            "co_brand_partner": "string",  # Co-brand partner name
            "card_network": "string",  # Visa, Mastercard, RuPay, etc.
            "contactless": "boolean",  # Contactless payment feature
            "virtual_card": "boolean",  # Virtual card availability
            "card_description": "string",  # Detailed description of the card
            "card_image_url": "string",  # URL to card image
            "apply_url": "string",  # URL to apply for the card
            "popularity_score": "float",  # Popularity score (1-10)
        }

class UserPreferenceSchema:
    """
    Schema for user preferences in the recommendation system.
    """
    def __init__(self):
        self.schema = {
            # Basic user information
            "user_id": "string",  # Unique identifier for the user
            
            # Financial information
            "annual_income": "float",  # Annual income
            "employment_type": "string",  # Salaried, self-employed, business owner, etc.
            "credit_score": "integer",  # Credit score if known
            
            # Demographic information
            "age": "integer",  # Age of the user
            "residence_status": "string",  # Resident, NRI, etc.
            
            # Spending preferences
            "primary_spending_categories": "list",  # Main spending categories
            "monthly_card_spend": "float",  # Estimated monthly spend on card
            "international_transactions": "boolean",  # Frequent international transactions
            
            # Feature preferences
            "fee_preference": "string",  # Preference for annual fees (no fee, low fee, etc.)
            "reward_preference": "string",  # Preferred reward type (points, cashback, miles)
            "travel_frequency": "string",  # Frequency of travel (rarely, occasionally, frequently)
            "lounge_access_importance": "integer",  # Importance of lounge access (1-5)
            "fuel_spending": "boolean",  # Regular fuel spending
            "dining_spending": "boolean",  # Regular dining spending
            "shopping_spending": "boolean",  # Regular shopping spending
            "movie_spending": "boolean",  # Regular movie spending
            
            # Additional preferences
            "preferred_banks": "list",  # Preferred banks if any
            "existing_relationship": "list",  # Banks with existing relationship
            "existing_cards": "list",  # Existing credit cards
            "preferred_card_tier": "string",  # Preferred card tier
        }

class RecommendationResultSchema:
    """
    Schema for recommendation results.
    """
    def __init__(self):
        self.schema = {
            "user_id": "string",  # User ID for whom recommendation is generated
            "timestamp": "datetime",  # When the recommendation was generated
            "recommended_cards": "list",  # List of recommended card IDs
            "match_scores": "dict",  # Match scores for each recommended card
            "match_reasons": "dict",  # Reasons for recommending each card
        }

# Example of how to use the schemas
if __name__ == "__main__":
    card_schema = CreditCardSchema()
    user_schema = UserPreferenceSchema()
    result_schema = RecommendationResultSchema()
    
    print("Credit Card Schema Fields:")
    for field, data_type in card_schema.schema.items():
        print(f"  - {field}: {data_type}")
    
    print("\nUser Preference Schema Fields:")
    for field, data_type in user_schema.schema.items():
        print(f"  - {field}: {data_type}")
    
    print("\nRecommendation Result Schema Fields:")
    for field, data_type in result_schema.schema.items():
        print(f"  - {field}: {data_type}")
