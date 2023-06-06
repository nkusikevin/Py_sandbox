horoscopes = {
    "aquarius": "Today is a great day for new beginnings. Embrace change and take risks.",
    "pisces": "You may feel more emotional than usual today. Take some time for self-care.",
    "aries": "You're full of energy and enthusiasm. Channel it into a new project or goal.",
    "taurus": "Focus on your finances today. It's a good time to save and invest wisely.",
    "gemini": "Your communication skills are at their peak today. Express yourself freely.",
    "cancer": "Take care of your emotional well-being today. Surround yourself with loved ones.",
    "leo": "You're the star of the show today. Let your natural charisma shine through.",
    "virgo": "Attention to detail will serve you well today. Stay organized and focused.",
    "libra": "Balance is key today. Seek harmony in your relationships and decision-making.",
    "scorpio": "Your intuition is heightened today. Trust your gut instincts.",
    "sagittarius": "Embrace adventure and new experiences today. Step out of your comfort zone.",
    "capricorn": "Hard work pays off today. Stay disciplined and focused on your goals."
}

# Function to get the user's star sign and provide the horoscope
def get_horoscope():
    sign = input("Enter your star sign: ").lower()

    if sign in horoscopes:
        print(f"\n{sign.capitalize()} Horoscope: {horoscopes[sign]}")
    else:
        print("Invalid star sign. Please enter a valid sign.")

# Run the program
get_horoscope()

