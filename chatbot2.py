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
        "response": "You can check in from 3:00 PM onwards. Please keep your ID and booking confirmation ready for a smooth check-in process.",
    },
    "checkout": {
        "keywords": ["check-out", "checkout", "vacate", "check out", "leave the room", "leave the hotel"],
        "response": "Standard check-out time is 11:00 AM. Late checkout may cost extra.",
    },
    "cab": {
        "keywords": ["cab", "taxi", "driver"],
        "response": "Cabs/Taxis are available 24/7 at the hotel. Pre-booking is recommended.",
    },
    "flight": {
        "keywords": [
            "flight",
            "plane",
        ],
        "response": "Please check your airline's website or app for real-time flight updates.",
    },
    "airport": {
        "keywords": [
            "airport pickup",
            "airport drop",
            "shuttle",
            "airport commute",
            "pickup from the airport"
        ],
        "response": "Airport shuttle is available every hour. Share your arrival time to book.",
    },
    "cancellation": {
        "keywords": [
            "cancel",
            "refund",
            "money back",
            "undo my booking",
        ],
        "response": "Free cancellation is available 48 hours before check-in. After that a fee applies.",
    },
    "wifi": {
        "keywords": [
            "wifi",
            "wi-fi",
            "internet",
            "network",
        
        ],
        "response": "Free WiFi is available throughout the hotel. Ask the front desk for the password.",
    },
    "breakfast": {
        "keywords": [
            "breakfast",
            "cereal",
            "morning meal",
            "morning food",
        ],
        "response": "You can enjoy a delicious breakfast in our main restaurant from 7:00 AM to 10:30 AM.",
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
        "response": "Room service is available 24/7. Call extension 101 from your room.",
    },
    "pool": {
        "keywords": ["pool", "swim", "gym", "fitness", "jacuzzi"],
        "response": "The pool and gym are open 24/7.",
    },
}



def tokenize(text):
    return text.split()


def get_response(user_input):
    user_input = user_input.lower()
    for data in knowledge_base.values():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return data["response"]
    return "I'm sorry, I don't have information on that topic. Please ask about check-in, checkout, cabs, flights, airport pickup, cancellation, wifi, breakfast, room service, or pool and gym."


print(
    "'The world is a book and those who do not travel read only a page' - St. Augustine."
)
print(
    "Welcome to the Flyzy Travel Chatbot! My name is Hugo, how may I help you today? Type 'quit'  to exit."
)
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Hugo: Thank you. Have a nice trip.")
        break
    response_text = get_response(user_input)
    print("Hugo: " + response_text)
