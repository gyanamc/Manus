// Update the JavaScript in the index.html file to connect with the backend API

// Replace the getRecommendations function with this:
function getRecommendations() {
    // Validate the last step
    if (!validateStep(5)) {
        return;
    }
    
    // Get user preferences
    const preferences = getUserPreferences();
    
    // Show loading indicator
    const container = document.getElementById('recommendations-container');
    container.innerHTML = '<div class="text-center my-5"><div class="spinner-border text-primary" role="status"></div><p class="mt-3">Finding the best credit cards for you...</p></div>';
    
    // Show results section
    document.getElementById('preference-form').style.display = 'none';
    document.getElementById('results-section').style.display = 'block';
    document.getElementById('progress-bar').style.display = 'none';
    
    // Make API call to get recommendations
    fetch('/api/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displayRecommendations(data.recommendations);
        } else {
            container.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
        }
    })
    .catch(error => {
        container.innerHTML = `<div class="alert alert-danger">Error: ${error.message}</div>`;
    });
}

// Replace the displayRecommendations function with this:
function displayRecommendations(recommendations) {
    const container = document.getElementById('recommendations-container');
    container.innerHTML = '';
    
    if (recommendations.length === 0) {
        container.innerHTML = '<div class="alert alert-info">No credit cards match your preferences. Please try adjusting your criteria.</div>';
        return;
    }
    
    recommendations.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.className = 'card-result';
        
        const matchScore = Math.min(100, Math.round(card.match_score * 10));
        
        cardElement.innerHTML = `
            <div class="card-header d-flex justify-content-between align-items-center">
                <h4>${card.card_name}</h4>
                <div class="match-score">${matchScore}% Match</div>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-4 text-center mb-3">
                        <img src="${card.card_image_url}" alt="${card.card_name}" class="card-image mb-3">
                        <a href="${card.apply_url}" target="_blank" class="btn btn-success w-100">Apply Now</a>
                    </div>
                    <div class="col-md-8">
                        <p>${card.card_description}</p>
                        <h5>Why this card matches your preferences:</h5>
                        <div class="match-reasons mb-3">
                            ${card.match_reasons.map(reason => `<div class="match-reason">${reason}</div>`).join('')}
                        </div>
                        <h5>Key Features:</h5>
                        <div class="card-features">
                            <span class="feature-badge">Issuer: ${card.issuer}</span>
                            <span class="feature-badge">Annual Fee: ₹${card.annual_fee}</span>
                            ${card.reward_rate > 0 ? `<span class="feature-badge">Reward Rate: ${card.reward_rate}X</span>` : ''}
                            ${card.cashback_rate > 0 ? `<span class="feature-badge">Cashback: ${card.cashback_rate}%</span>` : ''}
                            ${card.lounge_access ? `<span class="feature-badge">Lounge Access: ${card.lounge_access_count} visits/year</span>` : ''}
                            <span class="feature-badge">Card Tier: ${card.card_tier}</span>
                        </div>
                        
                        <div class="accordion mt-4" id="accordion-${card.card_id}">
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-fees-${card.card_id}">
                                        Fees & Charges
                                    </button>
                                </h2>
                                <div id="collapse-fees-${card.card_id}" class="accordion-collapse collapse" data-bs-parent="#accordion-${card.card_id}">
                                    <div class="accordion-body">
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Joining Fee:</span>
                                                <span>₹${card.joining_fee}</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Annual Fee:</span>
                                                <span>₹${card.annual_fee}</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Interest Rate:</span>
                                                <span>${card.interest_rate}% p.a.</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Forex Markup:</span>
                                                <span>${card.forex_markup}%</span>
                                            </li>
                                            <li class="list-group-item">
                                                <span>Fee Waiver:</span>
                                                <span>${card.fee_waiver_condition || 'Not available'}</span>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-benefits-${card.card_id}">
                                        Benefits & Rewards
                                    </button>
                                </h2>
                                <div id="collapse-benefits-${card.card_id}" class="accordion-collapse collapse" data-bs-parent="#accordion-${card.card_id}">
                                    <div class="accordion-body">
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item">
                                                <strong>Welcome Benefits:</strong>
                                                <p>${card.welcome_benefits || 'None'}</p>
                                            </li>
                                            <li class="list-group-item">
                                                <strong>Reward Categories:</strong>
                                                <p>${card.reward_categories.join(', ')}</p>
                                            </li>
                                            <li class="list-group-item">
                                                <strong>Travel Benefits:</strong>
                                                <p>${card.travel_benefits ? 'Yes' : 'No'}</p>
                                            </li>
                                            <li class="list-group-item">
                                                <strong>Dining Benefits:</strong>
                                                <p>${card.dining_benefits ? 'Yes' : 'No'}</p>
                                            </li>
                                            <li class="list-group-item">
                                                <strong>Shopping Benefits:</strong>
                                                <p>${card.shopping_benefits ? 'Yes' : 'No'}</p>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-eligibility-${card.card_id}">
                                        Eligibility Criteria
                                    </button>
                                </h2>
                                <div id="collapse-eligibility-${card.card_id}" class="accordion-collapse collapse" data-bs-parent="#accordion-${card.card_id}">
                                    <div class="accordion-body">
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Minimum Income:</span>
                                                <span>₹${card.min_income.toLocaleString('en-IN')}/year</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Minimum Age:</span>
                                                <span>${card.min_age} years</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Credit Score Required:</span>
                                                <span>${card.credit_score_required}</span>
                                            </li>
                                            <li class="list-group-item">
                                                <span>Employment Types:</span>
                                                <span>${card.employment_type.join(', ')}</span>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        container.appendChild(cardElement);
    });
}
