# Airbnb Chatbot

This project is a local Python chatbot inspired by Airbnb, designed to assist users in finding properties based on their preferences. The chatbot utilizes natural language processing to understand user queries and provides relevant property listings.

## Project Structure

```
airbnb-chatbot
├── data
│   └── properties.csv
├── src
│   ├── chatbot.py
│   ├── __init__.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Features

- **Property Search**: Users can search for properties based on location and price.
- **Natural Language Processing**: The chatbot processes user input to extract relevant information.
- **Mock Dataset**: A sample dataset of properties is included for demonstration purposes.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd airbnb-chatbot
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the chatbot**:
   Execute the following command to start the chatbot:
   ```
   python src/chatbot.py
   ```

## Usage

- Start the chatbot and interact with it by typing your queries.
- You can ask for properties by specifying a location and a maximum price, e.g., "Find properties in Miami under $200".

## License

This project is licensed under the MIT License.