"""
Recommendation algorithm for the Credit Card Recommendation Engine.
This file defines the logic for matching user preferences with suitable credit cards.
"""

class RecommendationEngine:
    """
    Class to handle the recommendation algorithm for credit cards.
    """
    def __init__(self, card_database=None):
        """
        Initialize the recommendation engine.
        
        Args:
            card_database: Database of credit cards (optional)
        """
        self.card_database = card_database
        self.weight_factors = self._define_weight_factors()
        
    def _define_weight_factors(self):
        """
        Define weight factors for different criteria in the recommendation algorithm.
        Returns a dictionary with criteria and their weights.
        """
        return {
            # Eligibility factors (highest weight as these are requirements)
            "income_eligibility": 10.0,
            "age_eligibility": 10.0,
            "credit_score_eligibility": 10.0,
            "employment_type_match": 8.0,
            
            # Fee preferences
            "annual_fee_match": 7.0,
            "fee_waiver_match": 6.0,
            
            # Reward preferences
            "reward_type_match": 8.0,
            "reward_rate_value": 7.0,
            "spending_category_match": 8.0,
            
            # Travel preferences
            "travel_benefits_match": 6.0,
            "lounge_access_match": 5.0,
            "forex_markup_value": 5.0,
            
            # Lifestyle preferences
            "fuel_benefits_match": 4.0,
            "dining_benefits_match": 4.0,
            "shopping_benefits_match": 4.0,
            "entertainment_benefits_match": 4.0,
            
            # Bank preferences
            "preferred_bank_match": 3.0,
            "existing_relationship_match": 4.0,
            
            # Card tier preferences
            "card_tier_match": 5.0,
            
            # Additional factors
            "popularity_score": 2.0,
            "complementary_to_existing_cards": 3.0
        }
    
    def recommend_cards(self, user_preferences, limit=5):
        """
        Recommend credit cards based on user preferences.
        
        Args:
            user_preferences: Dictionary containing user preferences
            limit: Maximum number of recommendations to return
            
        Returns:
            Dictionary containing recommended cards, match scores, and match reasons
        """
        if not self.card_database:
            return {"error": "Card database not initialized"}
        
        # Filter cards based on eligibility criteria
        eligible_cards = self._filter_eligible_cards(user_preferences)
        
        # Score each eligible card
        scored_cards = self._score_cards(eligible_cards, user_preferences)
        
        # Sort cards by score in descending order
        sorted_cards = sorted(scored_cards, key=lambda x: x["total_score"], reverse=True)
        
        # Limit the number of recommendations
        top_cards = sorted_cards[:limit]
        
        # Format the results
        results = {
            "recommended_cards": [card["card_id"] for card in top_cards],
            "match_scores": {card["card_id"]: card["total_score"] for card in top_cards},
            "match_reasons": {card["card_id"]: card["match_reasons"] for card in top_cards}
        }
        
        return results
    
    def _filter_eligible_cards(self, user_preferences):
        """
        Filter cards based on eligibility criteria.
        
        Args:
            user_preferences: Dictionary containing user preferences
            
        Returns:
            List of eligible cards
        """
        eligible_cards = []
        
        for card in self.card_database:
            # Check income eligibility
            if user_preferences.get("annual_income", 0) < card.get("min_income", 0):
                continue
            
            # Check age eligibility
            user_age = user_preferences.get("age", 0)
            if user_age < card.get("min_age", 0) or (card.get("max_age", 100) > 0 and user_age > card.get("max_age", 100)):
                continue
            
            # Check credit score eligibility if provided
            user_credit_score = user_preferences.get("credit_score", "Don't Know")
            if user_credit_score != "Don't Know":
                # Extract the minimum value from the credit score range
                if user_credit_score == "Below 650":
                    min_credit_score = 600
                elif user_credit_score == "650-700":
                    min_credit_score = 650
                elif user_credit_score == "700-750":
                    min_credit_score = 700
                elif user_credit_score == "750-800":
                    min_credit_score = 750
                elif user_credit_score == "Above 800":
                    min_credit_score = 800
                else:
                    min_credit_score = 0
                
                if min_credit_score < card.get("credit_score_required", 0):
                    continue
            
            # Check employment type eligibility
            user_employment = user_preferences.get("employment_type", "")
            if user_employment and card.get("employment_type") and user_employment not in card.get("employment_type", []):
                continue
            
            # Add card to eligible list
            eligible_cards.append(card)
        
        return eligible_cards
    
    def _score_cards(self, eligible_cards, user_preferences):
        """
        Score each eligible card based on user preferences.
        
        Args:
            eligible_cards: List of eligible cards
            user_preferences: Dictionary containing user preferences
            
        Returns:
            List of cards with scores and match reasons
        """
        scored_cards = []
        
        for card in eligible_cards:
            score_details = {
                "card_id": card["card_id"],
                "card_name": card["card_name"],
                "scores": {},
                "match_reasons": [],
                "total_score": 0.0
            }
            
            # Score based on fee preferences
            self._score_fee_preferences(score_details, card, user_preferences)
            
            # Score based on reward preferences
            self._score_reward_preferences(score_details, card, user_preferences)
            
            # Score based on travel preferences
            self._score_travel_preferences(score_details, card, user_preferences)
            
            # Score based on lifestyle preferences
            self._score_lifestyle_preferences(score_details, card, user_preferences)
            
            # Score based on bank preferences
            self._score_bank_preferences(score_details, card, user_preferences)
            
            # Score based on card tier preferences
            self._score_card_tier_preferences(score_details, card, user_preferences)
            
            # Score based on additional factors
            self._score_additional_factors(score_details, card, user_preferences)
            
            # Calculate total score
            total_score = sum(score_details["scores"].values())
            score_details["total_score"] = total_score
            
            scored_cards.append(score_details)
        
        return scored_cards
    
    def _score_fee_preferences(self, score_details, card, user_preferences):
        """
        Score card based on fee preferences.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        fee_preference = user_preferences.get("fee_preference", "")
        
        # Score based on annual fee
        annual_fee_score = 0.0
        if fee_preference == "No annual fee" and card.get("annual_fee", 0) == 0:
            annual_fee_score = self.weight_factors["annual_fee_match"]
            score_details["match_reasons"].append("No annual fee")
        elif fee_preference == "Low annual fee with better benefits" and 0 < card.get("annual_fee", 0) <= 1000:
            annual_fee_score = self.weight_factors["annual_fee_match"] * 0.8
            score_details["match_reasons"].append("Low annual fee")
        elif fee_preference == "Don't mind higher fees for premium benefits" and card.get("annual_fee", 0) > 1000:
            annual_fee_score = self.weight_factors["annual_fee_match"] * 0.9
            score_details["match_reasons"].append("Premium card with higher fee")
        
        score_details["scores"]["annual_fee"] = annual_fee_score
        
        # Score based on fee waiver
        if card.get("fee_waiver_condition", ""):
            monthly_spend = self._parse_monthly_spend(user_preferences.get("monthly_card_spend", ""))
            annual_spend = monthly_spend * 12
            
            # Simple check if annual spend might meet waiver condition
            # In a real implementation, this would be more sophisticated
            if annual_spend >= 100000:  # Assuming ₹1 lakh is a common threshold
                score_details["scores"]["fee_waiver"] = self.weight_factors["fee_waiver_match"]
                score_details["match_reasons"].append("Likely eligible for fee waiver based on spending")
    
    def _score_reward_preferences(self, score_details, card, user_preferences):
        """
        Score card based on reward preferences.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        reward_preference = user_preferences.get("reward_preference", "")
        
        # Score based on reward type
        reward_type_score = 0.0
        if reward_preference == "Cashback" and card.get("cashback_rate", 0) > 0:
            reward_type_score = self.weight_factors["reward_type_match"]
            score_details["match_reasons"].append(f"Offers cashback at {card.get('cashback_rate')}%")
        elif reward_preference == "Reward Points" and card.get("reward_rate", 0) > 0:
            reward_type_score = self.weight_factors["reward_type_match"]
            score_details["match_reasons"].append(f"Offers reward points at {card.get('reward_rate')} points per ₹100")
        elif reward_preference == "Air Miles" and "travel" in card.get("reward_categories", []):
            reward_type_score = self.weight_factors["reward_type_match"]
            score_details["match_reasons"].append("Offers air miles or travel rewards")
        elif reward_preference == "Discounts" and any(cat in ["shopping", "dining", "entertainment"] for cat in card.get("reward_categories", [])):
            reward_type_score = self.weight_factors["reward_type_match"]
            score_details["match_reasons"].append("Offers discounts on shopping, dining, or entertainment")
        elif reward_preference == "No preference":
            reward_type_score = self.weight_factors["reward_type_match"] * 0.5
        
        score_details["scores"]["reward_type"] = reward_type_score
        
        # Score based on spending categories
        spending_category_score = 0.0
        user_categories = user_preferences.get("primary_spending_categories", [])
        card_categories = card.get("reward_categories", [])
        
        # Calculate overlap between user categories and card categories
        if user_categories and card_categories:
            # Normalize category names for comparison
            normalized_user_categories = [self._normalize_category(cat) for cat in user_categories]
            normalized_card_categories = [self._normalize_category(cat) for cat in card_categories]
            
            # Count matches
            matches = sum(1 for cat in normalized_user_categories if cat in normalized_card_categories)
            
            if matches > 0:
                # Score based on percentage of user categories matched
                match_percentage = matches / len(normalized_user_categories)
                spending_category_score = self.weight_factors["spending_category_match"] * match_percentage
                
                if match_percentage >= 0.7:
                    score_details["match_reasons"].append("Excellent match for your spending categories")
                elif match_percentage >= 0.4:
                    score_details["match_reasons"].append("Good match for your spending categories")
                else:
                    score_details["match_reasons"].append("Matches some of your spending categories")
        
        score_details["scores"]["spending_category"] = spending_category_score
    
    def _score_travel_preferences(self, score_details, card, user_preferences):
        """
        Score card based on travel preferences.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        travel_frequency = user_preferences.get("travel_frequency", "")
        lounge_importance = user_preferences.get("lounge_access_importance", "")
        international_transactions = user_preferences.get("international_transactions", False)
        
        # Score based on travel benefits
        travel_score = 0.0
        if travel_frequency == "Frequently" and card.get("travel_benefits", False):
            travel_score = self.weight_factors["travel_benefits_match"]
            score_details["match_reasons"].append("Excellent travel benefits for frequent travelers")
        elif travel_frequency == "Occasionally" and card.get("travel_benefits", False):
            travel_score = self.weight_factors["travel_benefits_match"] * 0.7
            score_details["match_reasons"].append("Good travel benefits for occasional travelers")
        elif travel_frequency == "Rarely" and card.get("travel_benefits", False):
            travel_score = self.weight_factors["travel_benefits_match"] * 0.3
        
        score_details["scores"]["travel_benefits"] = travel_score
        
        # Score based on lounge access
        lounge_score = 0.0
        if lounge_importance == "Very important" and card.get("lounge_access", False):
            lounge_score = self.weight_factors["lounge_access_match"]
            visits = card.get("lounge_access_count", 0)
            if visits > 0:
                score_details["match_reasons"].append(f"Offers {visits} complimentary lounge visits per year")
            else:
                score_details["match_reasons"].append("Offers airport lounge access")
        elif lounge_importance == "Somewhat important" and card.get("lounge_access", False):
            lounge_score = self.weight_factors["lounge_access_match"] * 0.7
            score_details["match_reasons"].append("Offers airport lounge access")
        elif lounge_importance == "Not important":
            lounge_score = 0.0
        
        score_details["scores"]["lounge_access"] = lounge_score
        
        # Score based on forex markup
        forex_score = 0.0
        if international_transactions and card.get("forex_markup", 0) <= 2.0:
            forex_score = self.weight_factors["forex_markup_value"]
            score_details["match_reasons"].append(f"Low forex markup at {card.get('forex_markup')}%")
        elif international_transactions and card.get("forex_markup", 0) <= 3.5:
            forex_score = self.weight_factors["forex_markup_value"] * 0.5
            score_details["match_reasons"].append("Reasonable forex markup")
        
        score_details["scores"]["forex_markup"] = forex_score
    
    def _score_lifestyle_preferences(self, score_details, card, user_preferences):
        """
        Score card based on lifestyle preferences.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        user_categories = user_preferences.get("primary_spending_categories", [])
        
        # Score based on fuel benefits
        if "Fuel" in user_categories and card.get("fuel_surcharge_waiver", False):
            score_details["scores"]["fuel_benefits"] = self.weight_factors["fuel_benefits_match"]
            score_details["match_reasons"].append("Offers fuel surcharge waiver")
        
        # Score based on dining benefits
        if "Dining" in user_categories and card.get("dining_benefits", False):
            score_details["scores"]["dining_benefits"] = self.weight_factors["dining_benefits_match"]
            score_details["match_reasons"].append("Offers dining benefits or discounts")
        
        # Score based on shopping benefits
        if "Shopping" in user_categories and card.get("shopping_benefits", False):
            score_details["scores"]["shopping_benefits"] = self.weight_factors["shopping_benefits_match"]
            score_details["match_reasons"].append("Offers shopping benefits or discounts")
        
        # Score based on entertainment benefits
        if "Entertainment" in user_categories and card.get("movie_benefits", False):
            score_details["scores"]["entertainment_benefits"] = self.weight_factors["entertainment_benefits_match"]
            score_details["match_reasons"].append("Offers movie or entertainment benefits")
    
    def _score_bank_preferences(self, score_details, card, user_preferences):
        """
        Score card based on bank preferences.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        preferred_banks = user_preferences.get("preferred_banks", [])
        existing_relationships = user_preferences.get("existing_relationship", [])
        
        # Score based on preferred banks
        if preferred_banks and card.get("issuer", "") in preferred_banks:
            score_details["scores"]["preferred_bank"] = self.weight_factors["preferred_bank_match"]
            score_details["match_reasons"].append(f"Card from your preferred bank: {card.get('issuer')}")
        
        # Score based on existing relationships
        if existing_relationships and card.get("issuer", "") in existing_relationships:
            score_details["scores"]["existing_relationship"] = self.weight_factors["existing_relationship_match"]
            score_details["match_reasons"].append(f"You have an existing relationship with {card.get('issuer')}")
    
    def _score_card_tier_preferences(self, score_details, card, user_preferences):
        """
        Score card based on card tier preferences.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        preferred_tier = user_preferences.get("preferred_card_tier", "")
        
        if preferred_tier and self._normalize_tier(card.get("card_tier", "")) == self._normalize_tier(preferred_tier):
            score_details["scores"]["card_tier"] = self.weight_factors["card_tier_match"]
            score_details["match_reasons"].append(f"Matches your preferred card tier: {preferred_tier}")
    
    def _score_additional_factors(self, score_details, card, user_preferences):
        """
        Score card based on additional factors.
        
        Args:
            score_details: Dictionary to store score details
            card: Card to score
            user_preferences: User preferences
        """
        # Score based on popularity
        popularity = card.get("popularity_score", 0)
        if popularity > 7:
            score_details["scores"]["popularity"] = self.weight_factors["popularity_score"]
            score_details["match_reasons"].append("Highly popular card with excellent user ratings")
        elif popularity > 5:
            score_details["scores"]["popularity"] = self.weight_factors["popularity_score"] * 0.7
            score_details["match_reasons"].append("Well-rated card with good user feedback")
        
        # Score based on complementary to existing cards
        # This would require knowledge of user's existing cards and their features
        # Simplified implementation for now
        existing_cards = user_preferences.get("existing_cards", False)
        if not existing_cards:
            # If user has no existing cards, give slight boost to entry-level cards
            if self._normalize_tier(card.get("card_tier", "")) == "basic":
                score_details["scores"]["complementary"] = self.weight_factors["complementary_to_existing_cards"]
                score_details["match_reasons"].append("Good starter card for first-time users")
    
    def _parse_monthly_spend(self, spend_range):
        """
        Parse monthly spend range to a numeric value.
        
        Args:
            spend_range: String representing spend range
            
        Returns:
            Numeric value representing the average of the range
        """
        if spend_range == "Less than ₹10,000":
            return 5000
        elif spend_range == "₹10,000 - ₹25,000":
            return 17500
        elif spend_range == "₹25,000 - ₹50,000":
            return 37500
        elif spend_range == "₹50,000 - ₹1,00,000":
            return 75000
        elif spend_range == "More than ₹1,00,000":
            return 150000
        else:
            return 0
    
    def _normalize_category(self, category):
        """
        Normalize category name for comparison.
        
        Args:
            category: Category name
            
        Returns:
            Normalized category name
        """
        category = category.lower()
        
        # Map similar categories
        if category in ["grocery", "groceries"]:
            return "groceries"
        elif category in ["dining", "restaurant", "restaurants", "food"]:
            return "dining"
        elif category in ["shopping", "retail", "online shopping"]:
            return "shopping"
        elif category in ["travel", "airline", "airlines", "hotel", "hotels"]:
            return "travel"
        elif category in ["fuel", "petrol", "gas", "diesel"]:
            return "fuel"
        elif category in ["entertainment", "movie", "movies", "theatre"]:
            return "entertainment"
        elif category in ["bill", "bills", "bill payments", "utility", "utilities"]:
            return "bills"
        else:
            return category
    
    def _normalize_tier(self, tier):
        """
        Normalize card tier for comparison.
        
        Args:
            tier: Card tier
            
        Returns:
            Normalized tier
        """
        tier = tier.lower()
        
        if tier in ["basic", "entry-level", "basic/entry-level", "standard"]:
            return "basic"
        elif tier in ["gold", "classic", "gold/classic"]:
            return "gold"
        elif tier in ["platinum", "premium", "platinum/premium"]:
            return "platinum"
        elif tier in ["signature", "infinite", "super premium", "super premium/signature/infinite"]:
            return "signature"
        else:
            return tier


# Example of how to use the RecommendationEngine class
if __name__ == "__main__":
    # Sample card database (in a real implementation, this would come from a database)
    sample_cards = [
        {
            "card_id": "hdfc001",
            "card_name": "HDFC Regalia Gold",
            "issuer": "HDFC Bank",
            "card_type": "rewards",
            "card_tier": "Gold",
            "annual_fee": 1000,
            "interest_rate": 42.0,
            "reward_rate": 4.0,
            "reward_categories": ["travel", "dining", "shopping"],
            "lounge_access": True,
            "lounge_access_count": 8,
            "fuel_surcharge_waiver": True,
            "min_income": 600000,
            "min_age": 21,
            "credit_score_required": 750,
            "employment_type": ["Salaried", "Self-employed Professional"],
            "popularity_score": 8.5
        },
        {
            "card_id": "sbi001",
            "card_name": "SBI SimplyCLICK",
            "issuer": "SBI Card",
            "card_type": "cashback",
            "card_tier": "Basic",
            "annual_fee": 499,
            "interest_rate": 45.0,
            "cashback_rate": 1.25,
            "reward_categories": ["online shopping", "entertainment"],
            "lounge_access": False,
            "fuel_surcharge_waiver": True,
            "min_income": 300000,
            "min_age": 21,
            "credit_score_required": 700,
            "employment_type": ["Salaried", "Self-employed Professional", "Business Owner"],
            "popularity_score": 7.8
        }
    ]
    
    # Sample user preferences
    sample_preferences = {
        "annual_income": 800000,
        "employment_type": "Salaried",
        "age": 30,
        "credit_score": 780,
        "primary_spending_categories": ["Online Shopping", "Dining", "Travel"],
        "monthly_card_spend": "₹25,000 - ₹50,000",
        "international_transactions": True,
        "fee_preference": "Low annual fee with better benefits",
        "reward_preference": "Reward Points",
        "travel_frequency": "Occasionally",
        "lounge_access_importance": "Somewhat important",
        "preferred_banks": ["HDFC Bank", "ICICI Bank"],
        "existing_relationship": ["HDFC Bank"],
        "existing_cards": True,
        "preferred_card_tier": "Gold/Classic"
    }
    
    # Initialize recommendation engine with sample card database
    engine = RecommendationEngine(sample_cards)
    
    # Get recommendations
    recommendations = engine.recommend_cards(sample_preferences)
    
    # Print recommendations
    print("Recommended Cards:")
    for i, card_id in enumerate(recommendations["recommended_cards"]):
        print(f"\n{i+1}. {next((card['card_name'] for card in sample_cards if card['card_id'] == card_id), 'Unknown')}")
        print(f"   Match Score: {recommendations['match_scores'][card_id]:.2f}")
        print(f"   Match Reasons:")
        for reason in recommendations["match_reasons"][card_id]:
            print(f"   - {reason}")
