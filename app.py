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

# Function to assign favorites, hobbies, and traits based on zodiac sign
def get_favorites_hobbies_and_traits(zodiac_sign):
    favorites_hobbies_and_traits = {
        "Capricorn": ("Black", "Reading", "Ambitious, Disciplined, Practical"),
        "Aquarius": ("Blue", "Experimenting with technology", "Independent, Innovative, Idealistic"),
        "Pisces": ("Sea Green", "Art & Painting", "Empathetic, Artistic, Compassionate"),
        "Aries": ("Red", "Adventure Sports", "Confident, Enthusiastic, Courageous"),
        "Taurus": ("Green", "Gardening", "Patient, Reliable, Determined"),
        "Gemini": ("Yellow", "Traveling", "Adaptable, Curious, Witty"),
        "Cancer": ("White", "Cooking", "Emotional, Intuitive, Protective"),
        "Leo": ("Gold", "Performing Arts", "Generous, Confident, Charismatic"),
        "Virgo": ("Brown", "Organizing", "Analytical, Meticulous, Practical"),
        "Libra": ("Pink", "Socializing", "Diplomatic, Fair-minded, Social"),
        "Scorpio": ("Maroon", "Exploring Mysteries", "Passionate, Resourceful, Determined"),
        "Sagittarius": ("Purple", "Outdoor Adventures", "Optimistic, Adventurous, Honest")
    }
    return favorites_hobbies_and_traits.get(zodiac_sign, ("Unknown", "Unknown", "Unknown"))

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

# Streamlit app
def main():
    # Display themed images at the top of the dashboard
    st.image("https://path_to_star_image.jpg", use_column_width=True)
    st.image("https://path_to_moon_image.jpg", use_column_width=True)
    st.image("https://path_to_mars_image.jpg", use_column_width=True)

    st.title("✨ Astrology & Age Calculator Dashboard ✨")

    # User inputs
    name = st.text_input("Enter your name:")
    birth_date_input = st.date_input("Enter your birthdate:")
    
    # Check if inputs are provided
    if name and birth_date_input:
        today = datetime.today()
        birth_date = birth_date_input
        years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        months = today.month - birth_date.month - (today.day < birth_date.day)
        days = today.day - birth_date.day if today.day >= birth_date.day else (today - datetime(today.year, today.month, birth_date.day)).days
        next_birthday = datetime(today.year + (today.month > birth_date.month or (today.month == birth_date.month and today.day >= birth_date.day)), birth_date.month, birth_date.day)
        next_birthday_day_of_week = next_birthday.strftime("%A")

        # Get horoscope details
        zodiac_sign = get_horoscope(birth_date.month, birth_date.day)
        lucky_day = get_lucky_day(zodiac_sign)
        lucky_number = random.randint(1, 100)
        favorite_color, hobby, personality_traits = get_favorites_hobbies_and_traits(zodiac_sign)
        challenge = health_challenge(zodiac_sign)

        # Display the zodiac sign image
        st.image(f"https://path_to_{zodiac_sign.lower()}_image.jpg", caption=f"{zodiac_sign}", use_column_width=True)

        # Display results with appealing sections
        st.markdown(f"### Hello, {name}!")
        st.write(f"- **You were born on:** {birth_date.strftime('%A')}")
        st.write(f"- **Age:** {years} years, {months} months, and {days} days")
        st.write(f"- **Next Birthday:** {next_birthday_day_of_week}")
        st.write(f"- **Zodiac Sign:** {zodiac_sign}")
        st.write(f"- **Lucky Day:** {lucky_day}")
        st.write(f"- **Lucky Number:** {lucky_number}")
        st.write(f"- **Favorite Color:** {favorite_color}")
        st.write(f"- **Hobby:** {hobby}")
        st.write(f"- **Personality Traits:** {personality_traits}")
        st.write(f"- **Health Challenge:** {challenge}")

        st.write("Developed by NIMIR")

if __name__ == "__main__":
    main()
