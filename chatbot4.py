# QUESTION BANK
# 1. Hotel Check-in
# When can I access my room?
# When can I check-in?
# When will my room be ready?

# 2. Hotel Check-out
# When should I check-out?
# When should I leave the room?
# When do I need to vacate the room?

# 3. Cab Availability
# Are cabs available at the hotel?
# Is a taxi available?
# Can I get a car from the hotel?

# 4. Flight Booking Status
# How can I check my flight status?
# Where can I find real-time flight updates?
# Has my flight arrived?

# 5. Airport Pickup/Drop
# Can I get a pickup from the airport?
# Do you offer airport pickup services?
# Is airport drop available?

# 6. WiFi Availability
# Is WiFi available at the airport?
# Can I access the WiFi?
# Does the airport provide WiFi?

# 7. Breakfast
# Is breakfast available in the hotel?
# Can I get breakfast at the hotel?
# Will breakfast be arranged by the hotel?

# 8. Cancellation
# What is the cancellation policy?
# Can I cancel my booking?
# How do I get a refund for my booking cancellation?

# 9. Pool and Gym
# Is there a pool and gym in the hotel?
# Can I use the pool and gym facilities?
# What are the timings for the pool and gym?

# 10. Room Service
# Does the hotel offer room service?
# Can I get an extra towel?
# Is housekeeping available in the hotel?


# CODE
import random
import pyttsx3
import nltk

knowledge_base = {
    "check-in": {
        "keywords": [
            "check-in",
            "checkin",
            "check in",
            "room ready",
            "access my room",
            "room be ready",
            "access the room",
        ],
        "responses": [
            "Most hotels allow check-in from 3:00 PM. Early check-in is available on request.",
            "You can check in from 3:00 PM onwards, please have your ID ready.",
            "Standard check-in begins at 3:00 PM.",
            "You can access your room by 3:00 PM.",
        ],
    },
    "checkout": {
        "keywords": [
            "check-out",
            "checkout",
            "vacate",
            "check out",
            "leave the room",
            "leave the hotel",
        ],
        "responses": [
            "Standard check-out time is 11:00 AM. Late check-out may cost extra.",
            "You can check out by 11:00 AM. Please drop your keys at the front desk.",
            "Checkout is at 11:00 AM. Hope you enjoyed your stay.",
        ],
    },
    "cab": {
        "keywords": ["cab", "taxi", "driver"],
        "responses": [
            "Cabs are available 24/7 at the hotel. Pre-booking is recommended.",
            "Cab services are located just outside the hotel.",
            "Affordable and spacious cabs are available 24/7 at the hotel.",
        ],
    },
    "flight": {
        "keywords": ["flight", "plane"],
        "responses": [
            "Please check your airline's website or app for real-time flight updates.",
            "It is highly advised to check the airline's website for the latest information regarding your flight.",
            "Please check the airline's website or approach the help desk of your airlines for the latest flight updates.",
            "Please approach the help desk of your airline's for this query.",
        ],
    },
    "airport": {
        "keywords": [
            "airport pickup",
            "airport drop",
            "shuttle",
            "airport commute",
            "pickup from the airport",
        ],
        "responses": [
            "Airport shuttle is available every hour. Share your arrival time to book.",
            "Please share your arrival time to book an airport shuttle.",
            "Airport shuttles are available 24/7. Please book in advance.",
        ],
    },
    "cancellation": {
        "keywords": [
            "cancel",
            "refund",
            "money back",
            "undo my booking",
        ],
        "responses": [
            "Free cancellation is available 48 hours before check-in. After that, a fee applies.",
            "You can cancel your booking up to 48 hours before check-in for a full refund.",
            "Cancellation fees apply if you cancel within 48 hours of your check-in date.",
        ],
    },
    "wifi": {
        "keywords": [
            "wifi",
            "wi-fi",
            "internet",
            "network",
        ],
        "responses": [
            "Free WiFi is available throughout the hotel. Ask the front desk for the password.",
            "WiFi is available in all guest rooms and common areas. The password is displayed on the TV in your room.",
            "We are happy to provide you with our WiFi services. Please ask at the front desk for the password.",
        ],
    },
    "breakfast": {
        "keywords": ["breakfast", "cereal", "morning meal", "morning food"],
        "responses": [
            "Breakfast is served from 7:00 AM to 10:30 AM in the main restaurant.",
            "You can enjoy a delicious breakfast in our main restaurant from 7:00 AM to 10:30 AM.",
            "Please visit our main restaurant for a delightful breakfast experience between 7:00 AM and 10:30 AM.",
            "For a luxurious experience, please visit our main restaurant between 7:00 AM and 10:30 AM.",
        ],
    },
    "roomservice": {
        "keywords": [
            "housekeeping",
            "house keeping",
            "room cleaning",
            "maid",
            "cleaner",
            "extra pillow",
            "extra blanket",
            "extra towel",
            "room service",
        ],
        "responses": [
            "Room service is available 24/7. Call extension 101 from your room.",
            "You can order room service at any time by calling extension 101.",
            "You can enjoy our premium room services 24/7 by calling extension 101.",
            "To ensure a hassle-free stay we provide premium room services. Call extension 101.",
        ],
    },
    "pool": {
        "keywords": ["pool", "swim", "gym", "fitness", "jacuzzi"],
        "responses": [
            "The pool and gym are open 24/7.",
            "The pool and gym are accessible to all guests.",
            "To ensure our customers have a great experience, we provide 24/7 access to our pool and gym facilities.",
            "To ensure our customers do not compromise their fitness goals, we provide 24/7 access to our pool and gym facilities.",
            "Call our front desk to get free access to our pool and gym.",
        ],
    },
}

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download("punkt_tab")

stemmer = PorterStemmer()
memory = {}
question_count = 0


def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def tokenize(text):
    tokens = word_tokenize(text)
    return [stemmer.stem(token) for token in tokens]


def response(user_input):
    global question_count
    question_count += 1
    if question_count > 5:
        memory.clear()
        question_count = 0
    user_input = user_input.lower()
    last = memory.get("last_request")

    tokens = tokenize(user_input)
    for intent, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in tokens or keyword in user_input:
                memory["last_request"] = intent
                memory["last_" + intent + "_query"] = intent
                return random.choice(data["responses"])

    if "cost" in user_input or "price" in user_input or "how much" in user_input:
        if last == "cab":
            return "Cab fares start at $5 within the hotel area. Long distance rides are metered."
        elif last == "breakfast":
            return "Breakfast is complimentary for premium guests. Others pay $12 per person."
        elif last == "wifi":
            return "WiFi is completely free for all hotel guests!"
        elif last == "roomservice":
            return "Room service charges depend on your order. A small delivery fee of $2 applies."

    elif "how long" in user_input or "how far" in user_input:
        if last == "airport":
            return "The airport is about 25 minutes from the hotel by shuttle."
        elif last == "cab":
            return "Cabs usually arrive within 5 minutes of your request at the front desk."

    elif "still" in user_input or "available" in user_input:
        if last == "cab":
            return "Yes, cabs are available 24/7 right outside the hotel entrance."
        elif last == "breakfast":
            return "Breakfast is served until 10:30 AM. Head to the main restaurant!"
        elif last == "wifi":
            return "Yes, WiFi is available throughout the hotel at all times."

    elif "where" in user_input or "location" in user_input:
        if last == "cab":
            return "Cabs are stationed right at the hotel main entrance."
        elif last == "breakfast":
            return "Breakfast is served in the main restaurant on the ground floor."
        elif last == "roomservice":
            return "Just call extension 101 from your room and we'll come to you!"
        elif last == "airport":
            return "The shuttle pickup point is at the hotel main gate."
    return "I'm sorry, I don't have information on that topic. Please rephrase or ask about check-in, check-out, cabs, flights, airport pickup, cancellation, wifi, breakfast, room service, or pool and gym."


print(
    "'The world is a book and those who do not travel read only a page' - St. Augustine."
)
print(
    "Welcome to the Flyzy Travel Chatbot! My name is Hugo, how may I help you today? Type 'quit' to exit."
)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Hugo: Thank you. Have a nice trip.")
        speak("Thank you. Have a nice trip.")
        break
    response_text = response(user_input)
    print("Hugo: " + response_text)
    speak(response_text)
    print(memory)
