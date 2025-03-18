import random
from collections import Counter

# Helper function to create a deck
def create_deck():
    suits = 'HDSC'
    ranks = '23456789TJQKA'
    return [rank + suit for rank in ranks for suit in suits]

# Check functions for each hand type
def is_royal_flush(hand):
    # Check if the hand is a straight flush
    if is_straight_flush(hand):
        # Check if 'A' is in the hand and ensure it's not an Ace-low straight
        ranks = [card[0] for card in hand]
        if 'A' in ranks and not ('2' in ranks and '3' in ranks and '4' in ranks and '5' in ranks):
            return True
    return False

def is_straight_flush(hand):
    # String representing all possible ranks in order
    ranks_sequence = '23456789TJQKA'
    
    # Group cards by suits
    suits = {}
    for card in hand:
        rank = card[0]
        suit = card[1]
        if suit not in suits:
            suits[suit] = []
        suits[suit].append(rank)
    
    # Check for straight flush in each suit
    for suit, ranks in suits.items():
        # Sort ranks in the suit according to the ranks sequence
        ranks = sorted(set(ranks), key=ranks_sequence.index)
        
        # For the A-2-3-4-5 special case
        if 'A' in ranks and '2' in ranks and '3' in ranks and '4' in ranks and '5' in ranks:
            return True
        
        # Check for 5 consecutive ranks
        for i in range(len(ranks) - 4):  # Loop from the 1st item to the 5th last item
            straight_flush = True
            
            # Check for the next 4 consecutive superior ranks
            for j in range(1, 5):
                if ranks_sequence.index(ranks[i + j]) != ranks_sequence.index(ranks[i]) + j:
                    straight_flush = False
                    break
            
            if straight_flush:
                return True
    
    return False

def is_four_of_a_kind(hand):
    ranks = [card[0] for card in hand]
    return any(ranks.count(rank) == 4 for rank in ranks)

def is_full_house(hand):
    # Extract the ranks from the hand
    ranks = [card[0] for card in hand]
    # Count the occurrences of each rank
    rank_counts = list(Counter(ranks).values())
    # Find the highest frequency
    highest_frequency = max(rank_counts)
    # Check if the highest frequency is less than 3
    if highest_frequency < 3:
        return False
    # Remove the value of the highest frequency (Three of a Kind or Four of a Kind)
    rank_counts.remove(highest_frequency)
    # Check for a value of 2 or more in the remaining list
    has_pair = any(count >= 2 for count in rank_counts)
    return has_pair

def is_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

def is_straight(hand):
    # String representing all possible ranks in order
    ranks_sequence = '23456789TJQKA'
    
    # Extract the ranks from the hand and sort them
    ranks = sorted(set(card[0] for card in hand), key=ranks_sequence.index)
    
    # For the A,2,3,4,5 special case
    if 'A' in ranks and '2' in ranks and '3' in ranks and '4' in ranks and '5' in ranks:
        return True
    
    # Check for 5 consecutive ranks
    for i in range(len(ranks) - 4):  # Loop from the 1st item to the 5th last item
        straight = True
        
        # Check for the next 4 consecutive superior ranks
        for j in range(1, 5):
            if ranks_sequence.index(ranks[i + j]) != ranks_sequence.index(ranks[i]) + j:
                straight = False
                break
        
        if straight:
            return True
    
    return False

def is_three_of_a_kind(hand):
    ranks = [card[0] for card in hand]
    return any(ranks.count(rank) == 3 for rank in ranks)

def is_two_pair(hand):
    ranks = [card[0] for card in hand]
    pairs = [rank for rank in set(ranks) if ranks.count(rank) == 2]
    #print(pairs)
    return len(pairs) >= 2

def is_one_pair(hand):
    ranks = [card[0] for card in hand]
    pairs = [rank for rank in set(ranks) if ranks.count(rank) == 2]
    return len(pairs) >= 1
    #ranks = [card[0] for card in hand]
    #return len(set(ranks)) == 4

def is_high_card(hand):
    return True

# Function to evaluate a hand and return its rank
def evaluate_hand(hand):
    if is_royal_flush(hand):
        return "Royal Flush"
    if is_straight_flush(hand):
        return "Straight Flush"
    if is_four_of_a_kind(hand):
        return "Four of a Kind"
    if is_full_house(hand):
        return "Full House"
    if is_flush(hand):
        return "Flush"
    if is_straight(hand):
        return "Straight"
    if is_three_of_a_kind(hand):
        return "Three of a Kind"
    if is_two_pair(hand):
        return "Two Pair"
    if is_one_pair(hand):
        return "One Pair"
    return "High Card"

# Simulate drawing remaining cards from the deck
def simulate_draws(initial_hand, drawn_cards, deck, num_simulations):
    hand_counts = Counter()
    used_cards = initial_hand + drawn_cards

    for x in range(num_simulations):
        remaining_deck = [card for card in deck if card not in used_cards]
        num_needed = 7 - len(used_cards)
        drawn_cards = random.sample(remaining_deck, num_needed)
        full_hand = used_cards + drawn_cards
        best_hand = evaluate_hand(full_hand)
        hand_counts[best_hand] += 1

    total_simulations = sum(hand_counts.values())
    probabilities = {hand: count / total_simulations for hand, count in hand_counts.items()}
    return probabilities

# Display the results
def display_probabilities(probabilities):
    for hand, probability in probabilities.items():
        print(f"{hand}: {probability:.2%}")

# Example usage
initial_hand = ['7S', 'QS']  # Initial hand
drawn_cards = ['2D', '3H', '3D']  # Drawn cards
deck = create_deck()

# Number of simulations
num_simulations = 500000

probabilities = simulate_draws(initial_hand, drawn_cards, deck, num_simulations)
display_probabilities(probabilities)
