"""
System architecture diagram for the Credit Card Recommendation Engine.
This file provides a textual representation of the system architecture.
"""

SYSTEM_ARCHITECTURE = """
+---------------------------------------------+
|        Credit Card Recommendation Engine    |
+---------------------------------------------+

+----------------+        +-------------------+
|                |        |                   |
| User Interface |<------>| Preference Input  |
|                |        | System            |
+----------------+        +-------------------+
        |                          |
        v                          v
+----------------+        +-------------------+
|                |        |                   |
| Recommendation |<------>| Credit Card       |
| Engine         |        | Database          |
|                |        |                   |
+----------------+        +-------------------+

Component Details:
-----------------

1. User Interface:
   - Collects user information and preferences
   - Displays recommended credit cards
   - Provides details about each recommended card
   - Allows filtering and sorting of recommendations

2. Preference Input System:
   - Validates user inputs
   - Handles different types of questions (select, multi-select, etc.)
   - Provides help text and guidance
   - Ensures data quality

3. Recommendation Engine:
   - Filters cards based on eligibility criteria
   - Scores cards based on user preferences
   - Uses weighted algorithm to rank cards
   - Provides match reasons for recommendations

4. Credit Card Database:
   - Stores comprehensive information about credit cards
   - Includes features, benefits, fees, eligibility criteria
   - Regularly updated with latest card information

Data Flow:
---------
1. User provides preferences through the User Interface
2. Preference Input System validates and processes the inputs
3. Recommendation Engine queries the Credit Card Database
4. Engine filters and scores cards based on user preferences
5. Ranked recommendations are returned to the User Interface
6. User Interface displays recommendations with details

Technology Stack:
---------------
- Backend: Python
- Database: JSON/CSV files (initial version)
- Frontend: HTML, CSS, JavaScript
- Deployment: Web-based application
"""

if __name__ == "__main__":
    print(SYSTEM_ARCHITECTURE)
