# Poker Probability Calculator

A web application that calculates the probabilities of different poker hands based on your current cards and the community cards.

## Features

- Select your two hole cards
- Select community cards (flop, turn, river)
- Real-time probability calculations
- Dark/Light mode support
- Responsive design

## Tech Stack

- Frontend: Next.js, TypeScript, Tailwind CSS, Shadcn UI
- Backend: Python, Flask
- Probability Calculations: Custom poker hand evaluation algorithms

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python 3.x
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/poker.git
cd poker
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
pip install flask flask-cors
```

### Running the Application

1. Start the Flask backend:
```bash
python app.py
```

2. In a new terminal, start the Next.js frontend:
```bash
cd frontend
npm run dev
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Select your two hole cards using the card selectors
2. Optionally select any revealed community cards
3. Click "Calculate Probabilities" to see your chances of making different poker hands

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created by Dhruv Charan 
