"""
Credit card database for the recommendation engine.
This file contains actual credit card data from major Indian banks.
"""

import json
import os

class CreditCardDatabase:
    """
    Class to manage the credit card database.
    """
    def __init__(self, db_file=None):
        """
        Initialize the credit card database.
        
        Args:
            db_file: Path to the database file (optional)
        """
        self.db_file = db_file
        self.cards = self._initialize_cards()
    
    def _initialize_cards(self):
        """
        Initialize the credit card database with actual card data.
        
        Returns:
            List of credit card dictionaries
        """
        # If database file exists, load from it
        if self.db_file and os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading database file: {e}")
                return self._create_default_cards()
        else:
            # Create default cards
            return self._create_default_cards()
    
    def _create_default_cards(self):
        """
        Create default credit card data based on research.
        
        Returns:
            List of credit card dictionaries
        """
        return [
            # HDFC Bank Cards
            {
                "card_id": "hdfc_regalia",
                "card_name": "HDFC Regalia Credit Card",
                "issuer": "HDFC Bank",
                "card_type": "rewards",
                "card_tier": "Premium",
                "joining_fee": 2500,
                "annual_fee": 2500,
                "renewal_fee": 2500,
                "interest_rate": 45.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 950,
                "fee_waiver_condition": "Annual fee waived on spending ₹3,00,000 in the previous year",
                "reward_rate": 4.0,
                "cashback_rate": 0.0,
                "reward_categories": ["travel", "dining", "shopping"],
                "lounge_access": True,
                "lounge_access_count": 12,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": True,
                "shopping_benefits": True,
                "insurance_coverage": True,
                "welcome_benefits": "10,000 reward points on spending ₹1,00,000 in the first 90 days",
                "milestone_benefits": "5,000 reward points on spending ₹8,00,000 in a year",
                "min_income": 1200000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 750,
                "employment_type": ["Salaried", "Self-employed Professional"],
                "residence_status": ["Indian Resident", "NRI"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "HDFC Regalia is a premium credit card offering comprehensive travel benefits, dining privileges, and reward points on all spends.",
                "card_image_url": "https://www.hdfcbank.com/content/api/contentstream-id/723fb80a-2dde-42a3-9793-7ae1be57c87f/b4fd4dcc-da0b-4789-a7a3-d897d67a9f32/Personal/Pay/Cards/Credit-Card/Credit-Cards/Regalia/regalia-card.png",
                "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-credit-card",
                "popularity_score": 8.7
            },
            {
                "card_id": "hdfc_millenia",
                "card_name": "HDFC Millenia Credit Card",
                "issuer": "HDFC Bank",
                "card_type": "rewards",
                "card_tier": "Gold",
                "joining_fee": 1000,
                "annual_fee": 1000,
                "renewal_fee": 1000,
                "interest_rate": 45.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 950,
                "fee_waiver_condition": "Annual fee waived on spending ₹1,00,000 in the previous year",
                "reward_rate": 5.0,
                "cashback_rate": 0.0,
                "reward_categories": ["online", "dining", "shopping"],
                "lounge_access": True,
                "lounge_access_count": 8,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "1,000 reward points on spending ₹1,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 600000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident", "NRI"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "HDFC Millenia Credit Card offers accelerated rewards on online spends, dining, and shopping, making it ideal for digital-first customers.",
                "card_image_url": "https://www.hdfcbank.com/content/api/contentstream-id/723fb80a-2dde-42a3-9793-7ae1be57c87f/1f31c4ad-e650-4de5-9f91-625a2e3c6a8e/Personal/Pay/Cards/Credit-Card/Credit-Cards/Millennia/millennia-card.png",
                "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/millennia-credit-card",
                "popularity_score": 8.5
            },
            {
                "card_id": "hdfc_moneyback",
                "card_name": "HDFC MoneyBack Credit Card",
                "issuer": "HDFC Bank",
                "card_type": "cashback",
                "card_tier": "Classic",
                "joining_fee": 500,
                "annual_fee": 500,
                "renewal_fee": 500,
                "interest_rate": 45.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 950,
                "fee_waiver_condition": "Annual fee waived on spending ₹50,000 in the previous year",
                "reward_rate": 2.0,
                "cashback_rate": 0.5,
                "reward_categories": ["groceries", "utility", "telecom"],
                "lounge_access": False,
                "lounge_access_count": 0,
                "fuel_surcharge_waiver": True,
                "movie_benefits": False,
                "dining_benefits": False,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 cashback on spending ₹5,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Mastercard",
                "contactless": True,
                "virtual_card": True,
                "card_description": "HDFC MoneyBack Credit Card offers cashback on everyday spends like groceries, utility bills, and telecom bills.",
                "card_image_url": "https://www.hdfcbank.com/content/api/contentstream-id/723fb80a-2dde-42a3-9793-7ae1be57c87f/5a3c9a2d-2e0c-4e1c-a9b7-f5e5e7c5c8c9/Personal/Pay/Cards/Credit-Card/Credit-Cards/MoneyBack/moneyback-card.png",
                "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/moneyback-credit-card",
                "popularity_score": 7.8
            },
            
            # SBI Cards
            {
                "card_id": "sbi_simplysave",
                "card_name": "SBI SimplySAVE Credit Card",
                "issuer": "SBI Card",
                "card_type": "rewards",
                "card_tier": "Classic",
                "joining_fee": 499,
                "annual_fee": 499,
                "renewal_fee": 499,
                "interest_rate": 45.0,
                "interest_free_period": 45,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹1,00,000 in the previous year",
                "reward_rate": 10.0,
                "cashback_rate": 0.0,
                "reward_categories": ["groceries", "dining", "entertainment", "utility"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "2,000 reward points on card activation",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "SBI SimplySAVE Credit Card offers accelerated rewards on everyday spends like groceries, dining, and entertainment.",
                "card_image_url": "https://www.sbicard.com/sbi-card-en/assets/media/images/personal/credit-cards/shopping/simplysave-sbi-card/simplysave-sbi-card.png",
                "apply_url": "https://www.sbicard.com/en/personal/credit-cards/shopping/simplysave-sbi-card.page",
                "popularity_score": 8.0
            },
            {
                "card_id": "sbi_simplyclick",
                "card_name": "SBI SimplyCLICK Credit Card",
                "issuer": "SBI Card",
                "card_type": "rewards",
                "card_tier": "Classic",
                "joining_fee": 499,
                "annual_fee": 499,
                "renewal_fee": 499,
                "interest_rate": 45.0,
                "interest_free_period": 45,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹1,00,000 in the previous year",
                "reward_rate": 10.0,
                "cashback_rate": 0.0,
                "reward_categories": ["online shopping", "entertainment", "food delivery"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": False,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 worth of Amazon gift card on card activation",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Mastercard",
                "contactless": True,
                "virtual_card": True,
                "card_description": "SBI SimplyCLICK Credit Card offers accelerated rewards on online spends, making it ideal for digital-first customers.",
                "card_image_url": "https://www.sbicard.com/sbi-card-en/assets/media/images/personal/credit-cards/shopping/simplyclick-sbi-card/simplyclick-sbi-card.png",
                "apply_url": "https://www.sbicard.com/en/personal/credit-cards/shopping/simplyclick-sbi-card.page",
                "popularity_score": 8.2
            },
            {
                "card_id": "sbi_prime",
                "card_name": "SBI Card PRIME",
                "issuer": "SBI Card",
                "card_type": "lifestyle",
                "card_tier": "Premium",
                "joining_fee": 2999,
                "annual_fee": 2999,
                "renewal_fee": 2999,
                "interest_rate": 45.0,
                "interest_free_period": 45,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 950,
                "fee_waiver_condition": "Annual fee waived on spending ₹3,00,000 in the previous year",
                "reward_rate": 5.0,
                "cashback_rate": 0.0,
                "reward_categories": ["dining", "entertainment", "travel", "shopping"],
                "lounge_access": True,
                "lounge_access_count": 12,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": True,
                "shopping_benefits": True,
                "insurance_coverage": True,
                "welcome_benefits": "5,000 reward points on card activation",
                "milestone_benefits": "10,000 bonus points on spending ₹6,00,000 in a year",
                "min_income": 1200000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 750,
                "employment_type": ["Salaried", "Self-employed Professional"],
                "residence_status": ["Indian Resident", "NRI"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "SBI Card PRIME is a premium lifestyle credit card offering comprehensive benefits across dining, entertainment, travel, and shopping.",
                "card_image_url": "https://www.sbicard.com/sbi-card-en/assets/media/images/personal/credit-cards/travel-and-fuel/sbi-card-prime/sbi-card-prime.png",
                "apply_url": "https://www.sbicard.com/en/personal/credit-cards/travel-and-fuel/sbi-card-prime.page",
                "popularity_score": 8.5
            },
            
            # ICICI Bank Cards
            {
                "card_id": "icici_amazon_pay",
                "card_name": "Amazon Pay ICICI Credit Card",
                "issuer": "ICICI Bank",
                "card_type": "cashback",
                "card_tier": "Classic",
                "joining_fee": 0,
                "annual_fee": 0,
                "renewal_fee": 0,
                "interest_rate": 44.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Lifetime free card",
                "reward_rate": 0.0,
                "cashback_rate": 5.0,
                "reward_categories": ["amazon", "online shopping", "utility"],
                "lounge_access": False,
                "lounge_access_count": 0,
                "fuel_surcharge_waiver": True,
                "movie_benefits": False,
                "dining_benefits": False,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 Amazon Pay balance on card activation",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": True,
                "co_brand_partner": "Amazon",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "Amazon Pay ICICI Credit Card offers unlimited 5% cashback on Amazon.in shopping for Prime members and 3% for non-Prime members.",
                "card_image_url": "https://www.icicibank.com/content/dam/icicibank/india/managed-assets/images/credit-card/amazon-pay-icici-bank-credit-card.png",
                "apply_url": "https://www.icicibank.com/personal-banking/cards/credit-cards/amazon-pay-credit-card",
                "popularity_score": 9.0
            },
            {
                "card_id": "icici_coral",
                "card_name": "ICICI Bank Coral Credit Card",
                "issuer": "ICICI Bank",
                "card_type": "rewards",
                "card_tier": "Classic",
                "joining_fee": 500,
                "annual_fee": 500,
                "renewal_fee": 500,
                "interest_rate": 44.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹1,50,000 in the previous year",
                "reward_rate": 2.0,
                "cashback_rate": 0.0,
                "reward_categories": ["dining", "entertainment", "utility"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "1,000 reward points on spending ₹10,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Mastercard",
                "contactless": True,
                "virtual_card": True,
                "card_description": "ICICI Bank Coral Credit Card is an entry-level rewards card offering benefits on dining, entertainment, and utility bill payments.",
                "card_image_url": "https://www.icicibank.com/content/dam/icicibank/india/managed-assets/images/credit-card/coral-credit-card.png",
                "apply_url": "https://www.icicibank.com/personal-banking/cards/credit-cards/coral-credit-card",
                "popularity_score": 7.5
            },
            {
                "card_id": "icici_emeralde",
                "card_name": "ICICI Bank Emeralde Credit Card",
                "issuer": "ICICI Bank",
                "card_type": "premium",
                "card_tier": "Super Premium",
                "joining_fee": 12000,
                "annual_fee": 12000,
                "renewal_fee": 12000,
                "interest_rate": 44.0,
                "interest_free_period": 50,
                "forex_markup": 2.0,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 950,
                "fee_waiver_condition": "Annual fee waived on spending ₹12,00,000 in the previous year",
                "reward_rate": 4.0,
                "cashback_rate": 0.0,
                "reward_categories": ["travel", "dining", "shopping", "entertainment"],
                "lounge_access": True,
                "lounge_access_count": 24,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": True,
                "shopping_benefits": True,
                "insurance_coverage": True,
                "welcome_benefits": "10,000 reward points on card activation",
                "milestone_benefits": "20,000 bonus points on spending ₹15,00,000 in a year",
                "min_income": 3000000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 800,
                "employment_type": ["Salaried", "Self-employed Professional"],
                "residence_status": ["Indian Resident", "NRI"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "ICICI Bank Emeralde Credit Card is a super premium card offering exclusive privileges including concierge services, golf benefits, and premium lounge access.",
                "card_image_url": "https://www.icicibank.com/content/dam/icicibank/india/managed-assets/images/credit-card/emeralde-credit-card.png",
                "apply_url": "https://www.icicibank.com/personal-banking/cards/credit-cards/emeralde-credit-card",
                "popularity_score": 8.8
            },
            
            # Axis Bank Cards
            {
                "card_id": "axis_ace",
                "card_name": "Axis Bank ACE Credit Card",
                "issuer": "Axis Bank",
                "card_type": "cashback",
                "card_tier": "Classic",
                "joining_fee": 499,
                "annual_fee": 499,
                "renewal_fee": 499,
                "interest_rate": 52.86,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹2,00,000 in the previous year",
                "reward_rate": 0.0,
                "cashback_rate": 5.0,
                "reward_categories": ["utility", "bill payments", "insurance"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": False,
                "dining_benefits": False,
                "travel_benefits": False,
                "shopping_benefits": False,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 cashback on spending ₹5,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "Axis Bank ACE Credit Card offers 5% cashback on bill payments, making it ideal for managing monthly expenses.",
                "card_image_url": "https://www.axisbank.com/images/default-source/default-album/ace-credit-card.jpg",
                "apply_url": "https://www.axisbank.com/retail/cards/credit-card/ace-credit-card",
                "popularity_score": 8.3
            },
            {
                "card_id": "axis_flipkart",
                "card_name": "Flipkart Axis Bank Credit Card",
                "issuer": "Axis Bank",
                "card_type": "cashback",
                "card_tier": "Classic",
                "joining_fee": 500,
                "annual_fee": 500,
                "renewal_fee": 500,
                "interest_rate": 52.86,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹2,00,000 in the previous year",
                "reward_rate": 0.0,
                "cashback_rate": 5.0,
                "reward_categories": ["flipkart", "online shopping", "travel", "dining"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 Flipkart voucher on card activation",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": True,
                "co_brand_partner": "Flipkart",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "Flipkart Axis Bank Credit Card offers unlimited 5% cashback on Flipkart and Myntra, and 4% on preferred partners including Swiggy and PVR.",
                "card_image_url": "https://www.axisbank.com/images/default-source/default-album/flipkart-axis-bank-credit-card.jpg",
                "apply_url": "https://www.axisbank.com/retail/cards/credit-card/flipkart-axis-bank-credit-card",
                "popularity_score": 8.7
            },
            
            # IDFC First Bank Cards
            {
                "card_id": "idfc_first_select",
                "card_name": "IDFC FIRST Select Credit Card",
                "issuer": "IDFC FIRST Bank",
                "card_type": "rewards",
                "card_tier": "Classic",
                "joining_fee": 0,
                "annual_fee": 0,
                "renewal_fee": 0,
                "interest_rate": 47.88,
                "interest_free_period": 50,
                "forex_markup": 1.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 600,
                "fee_waiver_condition": "Lifetime free card",
                "reward_rate": 10.0,
                "cashback_rate": 0.0,
                "reward_categories": ["dining", "shopping", "travel", "utility"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": True,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "2,000 reward points on spending ₹10,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 300000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "IDFC FIRST Select Credit Card is a lifetime free card offering 10X rewards on dining, shopping, and travel, with a low forex markup of 1.5%.",
                "card_image_url": "https://www.idfcfirstbank.com/content/dam/idfcfirstbank/images/personal-banking/cards/credit-cards/select-credit-card/select-credit-card.png",
                "apply_url": "https://www.idfcfirstbank.com/personal-banking/cards/credit-cards/select-credit-card",
                "popularity_score": 8.9
            },
            
            # American Express Cards
            {
                "card_id": "amex_membership_rewards",
                "card_name": "American Express Membership Rewards Credit Card",
                "issuer": "American Express",
                "card_type": "rewards",
                "card_tier": "Classic",
                "joining_fee": 1000,
                "annual_fee": 1000,
                "renewal_fee": 1000,
                "interest_rate": 42.0,
                "interest_free_period": 52,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹1,50,000 in the previous year",
                "reward_rate": 1.0,
                "cashback_rate": 0.0,
                "reward_categories": ["dining", "shopping", "travel", "entertainment"],
                "lounge_access": True,
                "lounge_access_count": 4,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": True,
                "shopping_benefits": True,
                "insurance_coverage": True,
                "welcome_benefits": "4,000 membership rewards points on spending ₹20,000 in the first 90 days",
                "milestone_benefits": "",
                "min_income": 600000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 750,
                "employment_type": ["Salaried", "Self-employed Professional"],
                "residence_status": ["Indian Resident", "NRI"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "American Express",
                "contactless": True,
                "virtual_card": True,
                "card_description": "American Express Membership Rewards Credit Card offers flexible rewards points that can be redeemed for a variety of options including travel, shopping, and dining.",
                "card_image_url": "https://www.americanexpress.com/content/dam/amex/in/benefits/MR_Card.png",
                "apply_url": "https://www.americanexpress.com/in/credit-cards/membership-rewards-card/",
                "popularity_score": 8.0
            },
            
            # RBL Bank Cards
            {
                "card_id": "rbl_shoprite",
                "card_name": "RBL Bank ShopRite Credit Card",
                "issuer": "RBL Bank",
                "card_type": "cashback",
                "card_tier": "Classic",
                "joining_fee": 0,
                "annual_fee": 0,
                "renewal_fee": 0,
                "interest_rate": 36.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 750,
                "fee_waiver_condition": "Lifetime free card",
                "reward_rate": 0.0,
                "cashback_rate": 5.0,
                "reward_categories": ["groceries", "shopping", "utility"],
                "lounge_access": False,
                "lounge_access_count": 0,
                "fuel_surcharge_waiver": True,
                "movie_benefits": False,
                "dining_benefits": False,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 cashback on spending ₹5,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 240000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Mastercard",
                "contactless": True,
                "virtual_card": True,
                "card_description": "RBL Bank ShopRite Credit Card is a lifetime free card offering 5% cashback on groceries and shopping.",
                "card_image_url": "https://www.rblbank.com/sites/default/files/shoprite-credit-card.png",
                "apply_url": "https://www.rblbank.com/credit-cards/shoprite-credit-card",
                "popularity_score": 7.5
            },
            
            # IndusInd Bank Cards
            {
                "card_id": "indusind_platinum",
                "card_name": "IndusInd Bank Platinum Credit Card",
                "issuer": "IndusInd Bank",
                "card_type": "rewards",
                "card_tier": "Platinum",
                "joining_fee": 1000,
                "annual_fee": 1000,
                "renewal_fee": 1000,
                "interest_rate": 36.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Annual fee waived on spending ₹1,50,000 in the previous year",
                "reward_rate": 2.0,
                "cashback_rate": 0.0,
                "reward_categories": ["dining", "shopping", "travel", "entertainment"],
                "lounge_access": True,
                "lounge_access_count": 8,
                "fuel_surcharge_waiver": True,
                "movie_benefits": True,
                "dining_benefits": True,
                "travel_benefits": True,
                "shopping_benefits": True,
                "insurance_coverage": True,
                "welcome_benefits": "2,000 reward points on card activation",
                "milestone_benefits": "",
                "min_income": 600000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 750,
                "employment_type": ["Salaried", "Self-employed Professional"],
                "residence_status": ["Indian Resident", "NRI"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "IndusInd Bank Platinum Credit Card offers comprehensive benefits across dining, shopping, travel, and entertainment.",
                "card_image_url": "https://www.indusind.com/content/dam/indusind/personal-banking/credit-cards/platinum-credit-card.jpg",
                "apply_url": "https://www.indusind.com/personal-banking/cards/credit-cards/platinum-credit-card.html",
                "popularity_score": 7.8
            },
            
            # Kotak Mahindra Bank Cards
            {
                "card_id": "kotak_811",
                "card_name": "Kotak 811 #DreamDifferent Credit Card",
                "issuer": "Kotak Mahindra Bank",
                "card_type": "cashback",
                "card_tier": "Classic",
                "joining_fee": 0,
                "annual_fee": 0,
                "renewal_fee": 0,
                "interest_rate": 42.0,
                "interest_free_period": 50,
                "forex_markup": 3.5,
                "cash_advance_fee": 2.5,
                "late_payment_fee": 900,
                "fee_waiver_condition": "Lifetime free card",
                "reward_rate": 0.0,
                "cashback_rate": 1.0,
                "reward_categories": ["dining", "shopping", "entertainment", "utility"],
                "lounge_access": False,
                "lounge_access_count": 0,
                "fuel_surcharge_waiver": True,
                "movie_benefits": False,
                "dining_benefits": False,
                "travel_benefits": False,
                "shopping_benefits": True,
                "insurance_coverage": False,
                "welcome_benefits": "₹500 cashback on spending ₹5,000 in the first 30 days",
                "milestone_benefits": "",
                "min_income": 240000,
                "min_age": 21,
                "max_age": 65,
                "credit_score_required": 700,
                "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
                "residence_status": ["Indian Resident"],
                "co_branded": False,
                "co_brand_partner": "",
                "card_network": "Visa",
                "contactless": True,
                "virtual_card": True,
                "card_description": "Kotak 811 #DreamDifferent Credit Card is a lifetime free card offering 1% cashback on all spends with no minimum spend requirement.",
                "card_image_url": "https://www.kotak.com/content/dam/Kotak/product_assets/credit_cards/811-dream-different-credit-card.jpg",
                "apply_url": "https://www.kotak.com/en/personal-banking/cards/credit-cards/811-dreamdifferent-credit-card.html",
                "popularity_score": 7.5
            }
        ]
    
    def save_to_file(self, file_path):
        """
        Save the credit card database to a file.
        
        Args:
            file_path: Path to save the database
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.cards, f, indent=4)
            print(f"Database saved to {file_path}")
            return True
        except Exception as e:
            print(f"Error saving database: {e}")
            return False
    
    def get_all_cards(self):
        """
        Get all credit cards in the database.
        
        Returns:
            List of all credit cards
        """
        return self.cards
    
    def get_card_by_id(self, card_id):
        """
        Get a credit card by its ID.
        
        Args:
            card_id: ID of the card to retrieve
            
        Returns:
            Credit card dictionary or None if not found
        """
        for card in self.cards:
            if card["card_id"] == card_id:
                return card
        return None
    
    def get_cards_by_issuer(self, issuer):
        """
        Get all credit cards from a specific issuer.
        
        Args:
            issuer: Name of the issuer
            
        Returns:
            List of credit cards from the issuer
        """
        return [card for card in self.cards if card["issuer"] == issuer]
    
    def get_cards_by_type(self, card_type):
        """
        Get all credit cards of a specific type.
        
        Args:
            card_type: Type of credit card
            
        Returns:
            List of credit cards of the specified type
        """
        return [card for card in self.cards if card["card_type"] == card_type]
    
    def get_cards_by_tier(self, tier):
        """
        Get all credit cards of a specific tier.
        
        Args:
            tier: Tier of credit card
            
        Returns:
            List of credit cards of the specified tier
        """
        return [card for card in self.cards if card["card_tier"] == tier]
    
    def get_cards_by_annual_income(self, income):
        """
        Get all credit cards eligible for a specific annual income.
        
        Args:
            income: Annual income
            
        Returns:
            List of eligible credit cards
        """
        return [card for card in self.cards if card["min_income"] <= income]
    
    def get_cards_with_lounge_access(self):
        """
        Get all credit cards with lounge access.
        
        Returns:
            List of credit cards with lounge access
        """
        return [card for card in self.cards if card["lounge_access"]]
    
    def get_cards_with_no_annual_fee(self):
        """
        Get all credit cards with no annual fee.
        
        Returns:
            List of credit cards with no annual fee
        """
        return [card for card in self.cards if card["annual_fee"] == 0]
    
    def get_cards_with_cashback(self):
        """
        Get all credit cards with cashback.
        
        Returns:
            List of credit cards with cashback
        """
        return [card for card in self.cards if card["cashback_rate"] > 0]
    
    def get_cards_with_rewards(self):
        """
        Get all credit cards with rewards.
        
        Returns:
            List of credit cards with rewards
        """
        return [card for card in self.cards if card["reward_rate"] > 0]
    
    def get_cards_for_category(self, category):
        """
        Get all credit cards with rewards for a specific category.
        
        Args:
            category: Spending category
            
        Returns:
            List of credit cards with rewards for the category
        """
        return [card for card in self.cards if category.lower() in [cat.lower() for cat in card["reward_categories"]]]


# Example of how to use the CreditCardDatabase class
if __name__ == "__main__":
    # Initialize the database
    db = CreditCardDatabase()
    
    # Save the database to a file
    db.save_to_file("/home/ubuntu/credit_card_recommender/data/credit_cards.json")
    
    # Print some statistics
    print(f"Total number of cards: {len(db.get_all_cards())}")
    print(f"Number of HDFC Bank cards: {len(db.get_cards_by_issuer('HDFC Bank'))}")
    print(f"Number of cashback cards: {len(db.get_cards_with_cashback())}")
    print(f"Number of cards with lounge access: {len(db.get_cards_with_lounge_access())}")
    print(f"Number of cards with no annual fee: {len(db.get_cards_with_no_annual_fee())}")
    print(f"Number of cards for dining: {len(db.get_cards_for_category('dining'))}")
