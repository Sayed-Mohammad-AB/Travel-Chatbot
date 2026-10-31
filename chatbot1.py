responses = {
    "check-in": "Most hotels allow check-in after 12 PM (local time). It is highly recommended to contact the specific hotel for a hassle-free stay.",
    "flight": "Please check the official website of your airline's for real-time flight updates.",
    "wifi": "Most hotels and airports provide complimentary WiFi access.",
    "currency": "Currency exchange services are available at major airports and banks.",
    "roaming": "Enable international roaming or buy a local SIM card.",
    "booking": "Booking services are available through our website or mobile app.",
    "cab": "Cabs are usually available 24/7 at major airports. Pre-booking is highly recommended.",
    "hotel": "There are various luxury and budget-friendly hotels available for your stay. Please contact the hotels beforehand to enjoy early-bird offers and a smooth stay.",
    "visa": "Visa requirements depend on your destination. Contact the respective embassy for details.",
    "passport": "Make sure your passport is valid for at least 6 months beyond your planned return date to avoid being denied boarding or entry to foreign countries.",
    "luggage": "Most airlines allow one carry-on and one checked bag. Please check your airline's luggage policy. Popular airlines such as Emirates, Qatar Airways and Singapore Airlines generally offer generous baggage allowances. Maximum check-in weight is usually 32 kg per piece.",
    "weather": "Please check the weather app for the latest forecast at your present or future destination.",
}

print(
    "'The world is a book and those who do not travel read only a page' - St. Augustine."
)
print(
    "Welcome to the Flyzy Travel Chatbot! My name is Hugo, how may I help you today? Type 'quit' to exit."
)
while True:
    user_input = input("You: ").lower()
    if user_input == "quit":
        print("Hugo: Thank you. Have a nice trip.")
        break
    matched = False
    for keyword, answer in responses.items():
        if keyword in user_input:
            print("Hugo: " + answer)
            matched = True
            break
    if not matched:
        print(
            "Hugo: I'm not sure about that. Try asking about check-in, flights, cabs, hotels, passport, visa, luggage or weather etc."
        )
