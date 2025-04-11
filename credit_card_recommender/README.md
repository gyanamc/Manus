# Credit Card Recommendation Engine - India

A web-based application that recommends the most suitable credit cards for users in India based on their preferences and financial profile.

## Local Installation Instructions

Follow these steps to run the Credit Card Recommendation Engine locally:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. **Download and extract the project files**
   - Download the `credit_card_recommender.zip` file
   - Extract the contents to a folder on your computer

2. **Install required dependencies**
   ```bash
   cd credit_card_recommender
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to http://127.0.0.1:5000
   - You should see the Credit Card Recommendation Engine interface

## System Overview

This recommendation engine helps users find the most suitable credit cards based on their personal preferences and financial profile. The system:

1. Collects user information through a multi-step form
2. Processes this information using a sophisticated recommendation algorithm
3. Presents personalized credit card recommendations with detailed information and match reasons

## Features

- **Comprehensive Database**: Contains 16 credit cards from major Indian banks
- **Personalized Recommendations**: Uses a sophisticated algorithm that considers eligibility criteria and user preferences
- **User-Friendly Interface**: Multi-step form that collects detailed preferences in an intuitive way
- **Detailed Results**: Shows match scores, specific reasons for recommendations, and comprehensive card information
- **Mobile-Responsive Design**: Works well on both desktop and mobile devices

## Project Structure

- `app.py`: Main Flask application file
- `data/`: Contains credit card database and research information
- `src/`: Source code for the recommendation engine and database handling
- `static/`: Static files (JavaScript, CSS)
- `templates/`: HTML templates
- `tests/`: Test scripts for the recommendation engine
- `documentation.md`: Comprehensive system documentation

## Troubleshooting

- **Port already in use**: If port 5000 is already in use, modify the port number in `app.py` (line 115)
- **Module not found errors**: Ensure you have installed all required dependencies
- **Database issues**: Check that the `data/credit_cards.json` file exists and is properly formatted

## License

This project is for demonstration purposes only. The credit card information is based on research and may not reflect current offerings from banks.

## Contact

For any questions or issues, please refer to the documentation or create an issue in the project repository.
