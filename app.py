from flask import Flask, request, jsonify
from flask_cors import CORS
from poker import simulate_draws, create_deck

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

@app.route('/api/calculate-probabilities', methods=['POST'])
def calculate_probabilities():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        initial_hand = data.get('initialHand', [])
        drawn_cards = data.get('drawnCards', [])
        
        # Validate input
        if not isinstance(initial_hand, list) or not isinstance(drawn_cards, list):
            return jsonify({"error": "Invalid input format"}), 400
            
        # Filter out empty/None values and validate card format
        initial_hand = [card for card in initial_hand if card and len(card) == 2]
        drawn_cards = [card for card in drawn_cards if card and len(card) == 2]
        
        deck = create_deck()
        num_simulations = 50000  # Reduced for faster response time
        
        probabilities = simulate_draws(initial_hand, drawn_cards, deck, num_simulations)
        
        # Convert probabilities to percentage strings
        formatted_probabilities = {
            hand: f"{prob * 100:.2f}%" 
            for hand, prob in probabilities.items()
        }
        
        return jsonify(formatted_probabilities)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on port 5001...")
    app.run(debug=True, port=5001) 