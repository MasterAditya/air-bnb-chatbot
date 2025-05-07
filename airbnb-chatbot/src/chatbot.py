import pandas as pd
import os
import re

# Function to load the Airbnb property dataset
def load_dataset():
    """
    Loads the Airbnb property dataset and validates its structure.
    """
    data_path = os.path.join(os.path.dirname(__file__), '../data/properties.csv')
    try:
        # Load the dataset
        properties_df = pd.read_csv(data_path)
        print("Dataset loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Dataset not found at {data_path}. Please ensure the file exists.")
        exit()
    except pd.errors.EmptyDataError:
        print(f"Error: Dataset at {data_path} is empty. Please provide a valid dataset.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred while loading the dataset: {e}")
        exit()
     
    # Normalize column names to lowercase and strip spaces
    properties_df.columns = properties_df.columns.str.strip().str.lower()
    
    # Validate required columns
    required_columns = {'location', 'price', 'description'}
    missing_columns = required_columns - set(properties_df.columns)
    if missing_columns:
        print(f"Error: Dataset is missing the following required columns: {missing_columns}")
        print(f"Columns found in dataset: {list(properties_df.columns)}")
        exit()
    
    # Ensure the price column is numeric
    try:
        properties_df['price'] = pd.to_numeric(properties_df['price'], errors='coerce')
        if properties_df['price'].isnull().any():
            print("Error: Some entries in the 'price' column are not numeric.")
            exit()
    except Exception as e:
        print(f"Error while processing the 'price' column: {e}")
        exit()
    
    return properties_df

# Function to process user input
def process_input(input_text):
    """
    Tokenizes and filters user input by removing unnecessary characters.
    """
    tokens = re.findall(r'\b\w+\b', input_text.lower())
    return tokens

# Function to search properties based on user input
def search_properties(properties_df, location=None, max_price=None):
    """
    Filters properties based on location and maximum price.
    """
    filtered_properties = properties_df
    if location:
        filtered_properties = filtered_properties[
            filtered_properties['location'].str.lower().str.contains(location.lower(), na=False)
        ]
    if max_price is not None:
        filtered_properties = filtered_properties[
            filtered_properties['price'] <= max_price
        ]
    return filtered_properties

# Function to process queries and return property results
def process_and_search(properties_df, query):
    """
    Extracts location and price from user query and searches for matching properties.
    """
    tokens = process_input(query)
    location = None
    max_price = None

    # Extract location and price from tokens
    for token in tokens:
        if token.startswith('$') and token[1:].isdigit():
            max_price = int(token[1:])
        elif token.isdigit():
            max_price = int(token)
        elif token.lower() in properties_df['location'].str.lower().unique():
            location = token.lower()

    return search_properties(properties_df, location=location, max_price=max_price)

# Chatbot logic for handling queries
def chatbot_response(properties_df, user_input):
    """
    Generates a response based on user input.
    """
    if "property" in user_input.lower() or "find" in user_input.lower():
        results = process_and_search(properties_df, user_input)
        if not results.empty:
            response = "Here are some available properties:\n"
            for _, row in results.iterrows():
                response += f"- {row['description']} in {row['location']} for ${row['price']}\n"
            return response
        else:
            return "Sorry, no properties match your criteria."
    else:
        return "I can help you find properties! Try asking something like 'Find a property in Paris under $200'."

# Main chatbot loop
if __name__ == "__main__":
    print("Welcome to Airbnb Chatbot! Type 'exit' to quit.")
    properties_df = load_dataset()  # Load the dataset once at the start
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            response = chatbot_response(properties_df, user_input)
        except Exception as e:
            response = f"An error occurred: {e}"
        print(f"Bot: {response}")