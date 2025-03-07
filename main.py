import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets
import re  # Import regular expression module for checking password patterns


# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += (
            string.punctuation
        )  # Adds special characters (!@#$%^&* etc.) if selected

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))


# Function to evaluate the strength of a password
def evaluate_password_strength(password):
    length_score = len(password) >= 12  # Score for length (strong if at least 12 characters)
    digit_score = bool(re.search(r"\d", password))  # Contains at least one digit
    lower_case_score = bool(re.search(r"[a-z]", password))  # Contains at least one lowercase letter
    upper_case_score = bool(re.search(r"[A-Z]", password))  # Contains at least one uppercase letter
    special_char_score = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))  # Contains at least one special character

    # Summing up the score
    score = sum([length_score, digit_score, lower_case_score, upper_case_score, special_char_score])

    # Assign strength based on the score
    if score == 5:
        return "Strong"
    elif score == 4:
        return "Medium"
    else:
        return "Weak"


# Streamlit UI setup
st.title("Simple Password Generator & Strength Meter")  # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
use_special = st.checkbox(
    "Include special characters"
)  # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(
        length, use_digits, use_special
    )  # Call the password generation function
    st.write(f"Generated Password: `{password}`")  # Display the generated password

    # Evaluate and display the password strength
    strength = evaluate_password_strength(password)
    st.write(f"Password Strength: {strength}")  # Display password strength

    st.write("---------------------------------")
   
