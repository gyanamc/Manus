"""
Main application file for the Credit Card Recommendation Engine.
This file connects the user interface with the recommendation engine.
"""

from flask import Flask, render_template, request, jsonify
import json
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the recommendation engine and database
from src.recommendation_engine import RecommendationEngine
from src.credit_card_database import CreditCardDatabase

app = Flask(__name__)

# Initialize the database and recommendation engine
db_file = os.path.join(os.path.dirname(__file__), 'data', 'credit_cards.json')
card_db = CreditCardDatabase(db_file)
recommendation_engine = RecommendationEngine(card_db.get_all_cards())

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def recommend():
    """API endpoint for getting credit card recommendations."""
    try:
        # Get user preferences from request
        user_preferences = request.json
        
        # Get recommendations
        recommendations = recommendation_engine.recommend_cards(user_preferences)
        
        # Get full card details for recommended cards
        recommended_cards = []
        for card_id in recommendations['recommended_cards']:
            card = card_db.get_card_by_id(card_id)
            if card:
                # Add match score and reasons
                card['match_score'] = recommendations['match_scores'][card_id]
                card['match_reasons'] = recommendations['match_reasons'][card_id]
                recommended_cards.append(card)
        
        return jsonify({
            'success': True,
            'recommendations': recommended_cards
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/cards', methods=['GET'])
def get_cards():
    """API endpoint for getting all credit cards."""
    try:
        return jsonify({
            'success': True,
            'cards': card_db.get_all_cards()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/card/<card_id>', methods=['GET'])
def get_card(card_id):
    """API endpoint for getting a specific credit card."""
    try:
        card = card_db.get_card_by_id(card_id)
        if card:
            return jsonify({
                'success': True,
                'card': card
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Card with ID {card_id} not found'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/issuers', methods=['GET'])
def get_issuers():
    """API endpoint for getting all credit card issuers."""
    try:
        issuers = list(set(card['issuer'] for card in card_db.get_all_cards()))
        return jsonify({
            'success': True,
            'issuers': issuers
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/types', methods=['GET'])
def get_types():
    """API endpoint for getting all credit card types."""
    try:
        types = list(set(card['card_type'] for card in card_db.get_all_cards()))
        return jsonify({
            'success': True,
            'types': types
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
