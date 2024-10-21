import streamlit as st
from datetime import datetime
import random

# Function to determine horoscope based on birthdate
def get_horoscope(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

# Function to set lucky day based on zodiac sign
def get_lucky_day(zodiac_sign):
    lucky_days = {
        "Capricorn": "Saturday",
        "Aquarius": "Tuesday",
        "Pisces": "Thursday",
        "Aries": "Tuesday",
        "Taurus": "Friday",
        "Gemini": "Wednesday",
        "Cancer": "Monday",
        "Leo": "Sunday",
        "Virgo": "Wednesday",
        "Libra": "Friday",
        "Scorpio": "Tuesday",
        "Sagittarius": "Thursday"
    }
    return lucky_days.get(zodiac_sign, "Unknown")

# Function to assign favorite color, bird, food, animal, place, and traits based on zodiac sign
def get_favorites_and_traits(zodiac_sign):
    favorites_and_traits = {
        "Capricorn": ("Black", "Eagle", "Pasta", "Goat", "Mountains", "Ambitious, Disciplined, Practical"),
        "Aquarius": ("Blue", "Owl", "Sushi", "Dolphin", "Rivers", "Independent, Innovative, Idealistic"),
        "Pisces": ("Sea Green", "Swan", "Seafood", "Fish", "Sea", "Empathetic, Artistic, Compassionate"),
        "Aries": ("Red", "Hawk", "Steak", "Ram", "Desert", "Confident, Enthusiastic, Courageous"),
        "Taurus": ("Green", "Robin", "Pizza", "Bull", "Lakes", "Patient, Reliable, Determined"),
        "Gemini": ("Yellow", "Parrot", "Tacos", "Monkey", "Historical Places", "Adaptable, Curious, Witty"),
        "Cancer": ("White", "Crane", "Ice Cream", "Crab", "Sea", "Emotional, Intuitive, Protective"),
        "Leo": ("Gold", "Peacock", "Burgers", "Lion", "Desert", "Generous, Confident, Charismatic"),
        "Virgo": ("Brown", "Sparrow", "Salad", "Cat", "Mountains", "Analytical, Meticulous, Practical"),
        "Libra": ("Pink", "Dove", "Pasta", "Deer", "Rivers", "Diplomatic, Fair-minded, Social"),
        "Scorpio": ("Maroon", "Phoenix", "Spicy Food", "Scorpion", "Lakes", "Passionate, Resourceful, Determined"),
        "Sagittarius": ("Purple", "Falcon", "Barbecue", "Horse", "Historical Places", "Optimistic, Adventurous, Honest")
    }
    return favorites_and_traits.get(zodiac_sign, ("Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown"))

# Function to provide health challenges based on zodiac sign
def health_challenge(zodiac_sign):
    challenges = {
        "Capricorn": "Challenge: Add 10 minutes of stretching exercises to your daily routine for a week.",
        "Aquarius": "Challenge: Try a new outdoor activity, like hiking or cycling, for 30 minutes each day.",
        "Pisces": "Challenge: Dedicate 10 minutes a day to mindfulness or meditation for better mental clarity.",
        "Aries": "Challenge: Incorporate 20 minutes of high-intensity interval training (HIIT) into your routine.",
        "Taurus": "Challenge: Focus on eating more plant-based meals throughout the week.",
        "Gemini": "Challenge: Try a new fitness class or workout routine to keep things interesting.",
        "Cancer": "Challenge: Prioritize self-care by getting at least 7-8 hours of sleep each night.",
        "Leo": "Challenge: Take a 20-minute walk outside every day to refresh your mind and body.",
        "Virgo": "Challenge: Plan your meals for the week and focus on balanced nutrition.",
        "Libra": "Challenge: Add yoga or Pilates to your weekly routine for better balance and flexibility.",
        "Scorpio": "Challenge: Drink at least 8 glasses of water daily to stay hydrated.",
        "Sagittarius": "Challenge: Dedicate time each day for an adventurous activity, like jogging or exploring nature."
    }
    return challenges.get(zodiac_sign, "No specific challenge available.")

# Function to categorize age based on the new age ranges
def categorize_age(years):
    if 30 <= years <= 39:
        return "Young Adult"
    elif 40 <= years <= 49:
        return "Midlife Adult"
    elif 50 <= years <= 59:
        return "Pre-Retirement"
    elif years >= 60:
        return "Retirement Age"
    else:
        return "Young"

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return round(bmi, 2)

# Function to provide BMI suggestions
def bmi_suggestions(bmi):
    if bmi < 18.5:
        return (
            "Suggestions for Underweight (BMI < 18.5):\n"
            "- Nutritional Assessment: Consult a healthcare professional.\n"
            "- Increase Caloric Intake: Focus on nutrient-dense foods.\n"
            "- Strength Training: Build muscle mass.\n"
            "- Monitor Health: Regular check-ups."
        )
    elif 18.5 <= bmi < 25:
        return (
            "Suggestions for Normal Weight (BMI 18.5–24.9):\n"
            "- Maintain Healthy Habits: Balanced nutrition and regular activity.\n"
            "- Monitor Changes: Watch for significant weight changes.\n"
            "- Stay Active: Aim for 150 minutes of exercise per week."
        )
    elif 25 <= bmi < 30:
        return (
            "Suggestions for Overweight (BMI 25.0–29.9):\n"
            "- Dietary Changes: Focus on portion control and reduce sugar.\n"
            "- Increase Physical Activity: 150 minutes of exercise per week.\n"
            "- Set Realistic Goals: Aim for gradual weight loss.\n"
            "- Professional Guidance: Work with a nutritionist."
        )
    else:
        return (
            "Suggestions for Obesity:\n"
            "- Seek Medical Advice.\n"
            "- Develop a structured weight loss plan.\n"
            "- Consider Support Groups.\n"
            "- Focus on long-term lifestyle changes."
        )

# Streamlit app
def main():
    st.title("Astrology and Age Calculator")
    
    # User inputs
    name = st.text_input("Enter your name:")
    birth_date_input = st.date_input("Enter your birthdate:")
    
    # Check if inputs are provided
    if name and birth_date_input:
        today = datetime.today()

        # Calculate age
        birth_date = birth_date_input
        years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        months = today.month - birth_date.month - (today.day < birth_date.day)
        days = today.day - birth_date.day if today.day >= birth_date.day else (today - datetime(today.year, today.month, birth_date.day)).days
        
        # Determine the next birthday date
        next_birthday = datetime(today.year + (today.month > birth_date.month or (today.month == birth_date.month and today.day >= birth_date.day)), birth_date.month, birth_date.day)
        next_birthday_day_of_week = next_birthday.strftime("%A")
        
        # Categorize age
        age_category = categorize_age(years)
        
        # Get horoscope and lucky day
        zodiac_sign = get_horoscope(birth_date.month, birth_date.day)
        lucky_day = get_lucky_day(zodiac_sign)
        
        # Generate a random lucky number
        lucky_number = random.randint(1, 100)
        
        # User inputs for health calculations
        weight = st.number_input("Enter your weight in kilograms:", min_value=0.0)
        height_feet = st.number_input("Enter your height in feet:", min_value=0.0)

        if weight and height_feet:
            height_meters = height_feet * 0.3048  # Convert feet to meters
            bmi = calculate_bmi(weight, height_meters)
            suggestions = bmi_suggestions(bmi)
        
            # Get favorites and health challenge
            favorite_color, favorite_bird, favorite_food, favorite_animal, favorite_place, personality_traits = get_favorites_and_traits(zodiac_sign)
            challenge = health_challenge(zodiac_sign)

            # Display results
            st.subheader(f"Hello, {name}!")
            st.write(f"You were born on a {birth_date.strftime('%A')}.")
            st.write(f"Your current age is: {years} years, {months} months, and {days} days.")
            st.write(f"Your next birthday will be on a {next_birthday_day_of_week}.")
            st.write(f"You are considered '{age_category}'.")
            st.write(f"Your zodiac sign is: {zodiac_sign}.")
            st.write(f"Your lucky number is: {lucky_number}.")
            st.write(f"Your lucky day is: {lucky_day}.")
            st.write(f"Your favorite color is: {favorite_color}.")
            st.write(f"Your favorite bird is: {favorite_bird}.")
            st.write(f"Your favorite food is: {favorite_food}.")
            st.write(f"Your favorite animal is: {favorite_animal}.")
            st.write(f"Your favorite place is: {favorite_place}.")
            st.write(f"Your personality traits are: {personality_traits}.")
            st.write(f"Your BMI is: {bmi}.")
            st.write(suggestions)
            st.write(challenge)
            st.write("Developed by: mak3.4")
    
if __name__ == "__main__":
    main()
