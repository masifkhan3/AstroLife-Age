# Streamlit app
def main():
    st.title("Astrology and Age Calculator")
    
    # User inputs
    name = st.text_input("Enter your name:")
    birth_date_input = st.date_input("Enter your birthdate:", max_value=datetime.today())  # Prevent future dates
    
    # Check if inputs are provided
    if name and birth_date_input:
        today = datetime.today()

        # Calculate age
        birth_date = birth_date_input
        years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Calculate months and days
        months = (today.month - birth_date.month - (today.day < birth_date.day)) % 12
        days = (today - datetime(today.year, today.month, birth_date.day)).days if today.day >= birth_date.day else (today - datetime(today.year, today.month - 1, birth_date.day)).days
        
        # Determine the next birthday date
        next_birthday = datetime(today.year + (today.month > birth_date.month or (today.month == birth_date.month and today.day >= birth_date.day)), birth_date.month, birth_date.day)
        next_birthday_day_of_week = next_birthday.strftime("%A")
        
        # Categorize age
        age_category = categorize_age(years)

        # Remaining logic...
        # Get horoscope and lucky day
        zodiac_sign = get_horoscope(birth_date.month, birth_date.day)
        lucky_day = get_lucky_day(zodiac_sign)
        
        # Generate a random lucky number
        lucky_number = random.randint(1, 100)
        
        # User inputs for health calculations
        weight = st.number_input("Enter your weight in kilograms:", min_value=0.0)
        height_feet = st.number_input("Enter your height in feet:", min_value=0.0)

        if weight > 0 and height_feet > 0:  # Ensure weight and height are greater than 0
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
