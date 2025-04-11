"""
Test script for the Credit Card Recommendation Engine.
This file tests the recommendation engine with various user preference combinations.
"""

import sys
import os
import json
import unittest

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the recommendation engine and database
from src.recommendation_engine import RecommendationEngine
from src.credit_card_database import CreditCardDatabase

class TestRecommendationEngine(unittest.TestCase):
    """
    Test cases for the Credit Card Recommendation Engine.
    """
    
    def setUp(self):
        """
        Set up the test environment.
        """
        # Initialize the database and recommendation engine
        db_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'credit_cards.json')
        self.card_db = CreditCardDatabase(db_file)
        self.recommendation_engine = RecommendationEngine(self.card_db.get_all_cards())
    
    def test_high_income_premium_card_preference(self):
        """
        Test case for a high-income user who prefers premium cards.
        """
        # Define user preferences
        preferences = {
            "annual_income": 2000000,
            "employment_type": "Salaried",
            "credit_score": "750-800",
            "age": 35,
            "residence_status": "Indian Resident",
            "primary_spending_categories": ["Travel", "Dining", "Shopping"],
            "monthly_card_spend": "₹50,000 - ₹1,00,000",
            "international_transactions": True,
            "fee_preference": "Don't mind higher fees for premium benefits",
            "reward_preference": "Reward Points",
            "travel_frequency": "Frequently",
            "lounge_access_importance": "Very important",
            "preferred_banks": ["HDFC Bank", "ICICI Bank"],
            "existing_cards": True,
            "preferred_card_tier": "Platinum/Premium"
        }
        
        # Get recommendations
        recommendations = self.recommendation_engine.recommend_cards(preferences)
        
        # Verify that recommendations are returned
        self.assertTrue(len(recommendations["recommended_cards"]) > 0)
        
        # Verify that the top recommendation is a premium card
        top_card_id = recommendations["recommended_cards"][0]
        top_card = self.card_db.get_card_by_id(top_card_id)
        
        # Check if the top card is premium or super premium
        self.assertIn(top_card["card_tier"].lower(), ["premium", "super premium"])
        
        # Check if the top card has lounge access
        self.assertTrue(top_card["lounge_access"])
        
        # Check if the top card has travel benefits
        self.assertTrue(top_card["travel_benefits"])
        
        # Print the test results
        print("\nTest Case: High Income Premium Card Preference")
        print(f"Top Recommended Card: {top_card['card_name']} ({top_card['issuer']})")
        print(f"Match Score: {recommendations['match_scores'][top_card_id]:.2f}")
        print("Match Reasons:")
        for reason in recommendations["match_reasons"][top_card_id]:
            print(f"- {reason}")
    
    def test_low_income_no_fee_preference(self):
        """
        Test case for a low-income user who prefers no annual fee.
        """
        # Define user preferences
        preferences = {
            "annual_income": 350000,
            "employment_type": "Salaried",
            "credit_score": "700-750",
            "age": 25,
            "residence_status": "Indian Resident",
            "primary_spending_categories": ["Groceries", "Bill Payments", "Online Shopping"],
            "monthly_card_spend": "₹10,000 - ₹25,000",
            "international_transactions": False,
            "fee_preference": "No annual fee",
            "reward_preference": "Cashback",
            "travel_frequency": "Rarely",
            "lounge_access_importance": "Not important",
            "preferred_banks": [],
            "existing_cards": False,
            "preferred_card_tier": "Basic/Entry-level"
        }
        
        # Get recommendations
        recommendations = self.recommendation_engine.recommend_cards(preferences)
        
        # Verify that recommendations are returned
        self.assertTrue(len(recommendations["recommended_cards"]) > 0)
        
        # Verify that the top recommendation has no annual fee
        top_card_id = recommendations["recommended_cards"][0]
        top_card = self.card_db.get_card_by_id(top_card_id)
        
        # Check if the top card has no annual fee
        self.assertEqual(top_card["annual_fee"], 0)
        
        # Check if the top card is basic/entry-level
        self.assertIn(top_card["card_tier"].lower(), ["basic", "classic", "entry-level"])
        
        # Print the test results
        print("\nTest Case: Low Income No Fee Preference")
        print(f"Top Recommended Card: {top_card['card_name']} ({top_card['issuer']})")
        print(f"Match Score: {recommendations['match_scores'][top_card_id]:.2f}")
        print("Match Reasons:")
        for reason in recommendations["match_reasons"][top_card_id]:
            print(f"- {reason}")
    
    def test_online_shopper_preference(self):
        """
        Test case for a user who primarily shops online.
        """
        # Define user preferences
        preferences = {
            "annual_income": 600000,
            "employment_type": "Salaried",
            "credit_score": "700-750",
            "age": 28,
            "residence_status": "Indian Resident",
            "primary_spending_categories": ["Online Shopping", "Entertainment", "Food Delivery"],
            "monthly_card_spend": "₹25,000 - ₹50,000",
            "international_transactions": False,
            "fee_preference": "Low annual fee with better benefits",
            "reward_preference": "Cashback",
            "travel_frequency": "Occasionally",
            "lounge_access_importance": "Somewhat important",
            "preferred_banks": ["ICICI Bank", "Axis Bank"],
            "existing_cards": True,
            "preferred_card_tier": "Gold/Classic"
        }
        
        # Get recommendations
        recommendations = self.recommendation_engine.recommend_cards(preferences)
        
        # Verify that recommendations are returned
        self.assertTrue(len(recommendations["recommended_cards"]) > 0)
        
        # Verify that the top recommendation is good for online shopping
        top_card_id = recommendations["recommended_cards"][0]
        top_card = self.card_db.get_card_by_id(top_card_id)
        
        # Check if the top card has online shopping in reward categories
        online_shopping_related = any(
            category.lower() in ["online shopping", "online", "shopping", "e-commerce", "amazon"]
            for category in top_card["reward_categories"]
        )
        self.assertTrue(online_shopping_related)
        
        # Print the test results
        print("\nTest Case: Online Shopper Preference")
        print(f"Top Recommended Card: {top_card['card_name']} ({top_card['issuer']})")
        print(f"Match Score: {recommendations['match_scores'][top_card_id]:.2f}")
        print("Match Reasons:")
        for reason in recommendations["match_reasons"][top_card_id]:
            print(f"- {reason}")
    
    def test_travel_enthusiast_preference(self):
        """
        Test case for a user who travels frequently.
        """
        # Define user preferences
        preferences = {
            "annual_income": 1000000,
            "employment_type": "Self-employed Professional",
            "credit_score": "750-800",
            "age": 32,
            "residence_status": "Indian Resident",
            "primary_spending_categories": ["Travel", "Dining", "Fuel"],
            "monthly_card_spend": "₹50,000 - ₹1,00,000",
            "international_transactions": True,
            "fee_preference": "Low annual fee with better benefits",
            "reward_preference": "Air Miles",
            "travel_frequency": "Frequently",
            "lounge_access_importance": "Very important",
            "preferred_banks": [],
            "existing_cards": True,
            "preferred_card_tier": ""
        }
        
        # Get recommendations
        recommendations = self.recommendation_engine.recommend_cards(preferences)
        
        # Verify that recommendations are returned
        self.assertTrue(len(recommendations["recommended_cards"]) > 0)
        
        # Verify that the top recommendation is good for travel
        top_card_id = recommendations["recommended_cards"][0]
        top_card = self.card_db.get_card_by_id(top_card_id)
        
        # Check if the top card has travel in reward categories
        travel_related = any(
            category.lower() in ["travel", "airline", "hotel"]
            for category in top_card["reward_categories"]
        )
        self.assertTrue(travel_related)
        
        # Check if the top card has lounge access
        self.assertTrue(top_card["lounge_access"])
        
        # Print the test results
        print("\nTest Case: Travel Enthusiast Preference")
        print(f"Top Recommended Card: {top_card['card_name']} ({top_card['issuer']})")
        print(f"Match Score: {recommendations['match_scores'][top_card_id]:.2f}")
        print("Match Reasons:")
        for reason in recommendations["match_reasons"][top_card_id]:
            print(f"- {reason}")
    
    def test_specific_bank_preference(self):
        """
        Test case for a user who prefers a specific bank.
        """
        # Define user preferences
        preferences = {
            "annual_income": 800000,
            "employment_type": "Salaried",
            "credit_score": "700-750",
            "age": 30,
            "residence_status": "Indian Resident",
            "primary_spending_categories": ["Groceries", "Dining", "Shopping"],
            "monthly_card_spend": "₹25,000 - ₹50,000",
            "international_transactions": False,
            "fee_preference": "Low annual fee with better benefits",
            "reward_preference": "Reward Points",
            "travel_frequency": "Occasionally",
            "lounge_access_importance": "Somewhat important",
            "preferred_banks": ["HDFC Bank"],
            "existing_cards": True,
            "preferred_card_tier": "Gold/Classic"
        }
        
        # Get recommendations
        recommendations = self.recommendation_engine.recommend_cards(preferences)
        
        # Verify that recommendations are returned
        self.assertTrue(len(recommendations["recommended_cards"]) > 0)
        
        # Verify that the top recommendation is from the preferred bank
        top_card_id = recommendations["recommended_cards"][0]
        top_card = self.card_db.get_card_by_id(top_card_id)
        
        # Check if the top card is from HDFC Bank
        self.assertEqual(top_card["issuer"], "HDFC Bank")
        
        # Print the test results
        print("\nTest Case: Specific Bank Preference")
        print(f"Top Recommended Card: {top_card['card_name']} ({top_card['issuer']})")
        print(f"Match Score: {recommendations['match_scores'][top_card_id]:.2f}")
        print("Match Reasons:")
        for reason in recommendations["match_reasons"][top_card_id]:
            print(f"- {reason}")

if __name__ == "__main__":
    unittest.main()
