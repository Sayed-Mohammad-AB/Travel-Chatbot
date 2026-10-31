# FLYZY Travel Chatbot ("Hugo")

A rule-based, voice-enabled customer-support chatbot developed in Python. The project was built iteratively across four versions, each one introducing new programming concepts and fixing limitations of the previous one.



Author: Sayed Mohammad Ataullaha Bellary

## Table of Contents

1. [Overview](#1-overview)
2. [Objectives](#2-objectives)
3. [Features of the Final Version](#3-features-of-the-final-version)
4. [Technologies Used](#4-technologies-used)
5. [Repository Structure](#5-repository-structure)
6. [Installation and Usage](#6-installation-and-usage)
7. [Supported Topics](#7-supported-topics)
8. [Development Progression](#8-development-progression)
9. [Summary of Versions](#9-summary-of-versions)
10. [Limitations](#10-limitations)
11. [Future Work](#11-future-work)
12. [Acknowledgements](#12-acknowledgements)

\---

## 1\. Overview

The FLYZY Travel Chatbot is a command-line assistant named **Hugo**. It answers common questions that a hotel guest or traveller might ask, such as check-in times, airport transfers, Wi-Fi access and cancellation policy. Hugo reads the user's message, identifies the topic using keyword matching, and replies in text and in speech.

The project is intentionally rule-based rather than machine-learning based. Its purpose is to demonstrate the fundamentals of programming and basic Natural Language Processing (NLP): data structures, functions, control flow, modular design, text processing and state management.

## 2\. Objectives

* To build a working conversational program using core Python concepts.
* To show how a program evolves from a simple script into a structured, extensible design.
* To introduce basic NLP techniques (tokenisation and stemming).
* To add usability features: varied responses, spoken output and conversational memory.
* To document the learning process and the reasoning behind each design change.

## 3\. Features of the Final Version

* **Ten supported topics** covering hotel and airport services.
* **Keyword-based intent detection** with several keywords per topic.
* **Varied responses:** a random reply is chosen from several alternatives for each topic.
* **Text-to-speech output:** every reply, including the goodbye message, is spoken aloud.
* **Conversational memory:** Hugo remembers the last topic discussed and can answer short follow-up questions such as "How much does it cost?" or "Where is it?".
* **Graceful fallback:** if a message is not understood, Hugo lists the topics he can help with.
* **Clean exit:** typing `quit` ends the conversation.

## 4\. Technologies Used

|Technology|Purpose|
|-|-|
|Python 3|Core programming language|
|`random` (standard library)|Selecting varied responses|
|[NLTK](https://www.nltk.org/)|Tokenisation (`word\_tokenize`) and stemming (`PorterStemmer`)|
|[pyttsx3](https://pypi.org/project/pyttsx3/)|Offline text-to-speech|

5\. Repository Structure
 chatbot1.py    ( Version 1: simple keyword-to-answer dictionary )
 chatbot2.py    ( Version 2: structured knowledge base and functions )
 chatbot3.py    ( Version 3: varied responses, NLP preprocessing, speech )
 chatbot4.py    ( Version 4: conversational memory (final version))

&#x20;README.md



Each file is a complete, runnable program. `chatbot4.py` is the final version.

## 6\. Installation and Usage

### Requirements

* Python 3.9 or later
* A recent version of NLTK (3.9 or later is recommended, as it uses the `punkt\_tab` resource)
* pyttsx3
* A speakers or headphones output for the spoken replies

Setup
pip install nltk pyttsx3

The first time versions 3 or 4 are run, the program downloads the NLTK `punkt\_tab` tokeniser data automatically, so an internet connection is needed on the first run only.

Running
python chatbot4.py

(Versions 1 and 2 need no extra libraries and can be run the same way with `chatbot1.py` and `chatbot2.py`.)

### Platform note

The text-to-speech engine is initialised with `"sapi5"`, the Windows speech driver. On macOS or Linux, replace `pyttsx3.init("sapi5")` with `pyttsx3.init()` so that the platform's default driver is used.

### Example session (version 4)

```
'The world is a book and those who do not travel read only a page' - St. Augustine.
Welcome to the Flyzy Travel Chatbot! My name is Hugo, how may I help you today? Type 'quit' to exit.
You: Are cabs available?
Hugo: Cabs are available 24/7 at the hotel. Pre-booking is recommended.
You: How much does it cost?
Hugo: Cab fares start at $5 within the hotel area. Long distance rides are metered.
You: quit
Hugo: Thank you. Have a nice trip.
```

Because responses are chosen at random, the wording of the first reply may differ between runs. The follow-up answer is fixed.

## 7\. Supported Topics

|#|Topic|Example questions|
|-|-|-|
|1|Hotel check-in|"When can I check-in?", "When will my room be ready?"|
|2|Hotel check-out|"When should I check-out?", "When do I need to vacate the room?"|
|3|Cab availability|"Is a taxi available?", "Are cabs available at the hotel?"|
|4|Flight status|"How can I check my flight status?"|
|5|Airport pickup / drop|"Do you offer airport pickup services?"|
|6|Wi-Fi|"Can I access the WiFi?"|
|7|Breakfast|"Is breakfast available in the hotel?"|
|8|Cancellation and refunds|"Can I cancel my booking?"|
|9|Pool and gym|"What are the timings for the pool and gym?"|
|10|Room service and housekeeping|"Can I get an extra towel?"|

These ten topics, with three sample questions each, form the **question bank** documented at the top of versions 2, 3 and 4.

## 8\. Development Progression

### Version 1: `chatbot1.py` (Foundation)

**Purpose:** To build the simplest working chatbot and understand the basic input, process, output cycle.

**What it contains**

* A single flat dictionary, `responses`, that maps one keyword to one answer.
* Twelve general travel topics: check-in, flight, Wi-Fi, currency, roaming, booking, cab, hotel, visa, passport, luggage and weather.
* A `while True` loop that reads input, converts it to lowercase and checks each keyword using the `in` operator.
* A `matched` flag to detect when no keyword was found, triggering a fallback message listing example topics.
* A welcome banner with a travel quotation and a `quit` command to exit.

**Key concepts practised:** dictionaries, `while` loops, `for` loops over `.items()`, string methods, conditional statements, the `break` statement and Boolean flags.

**Limitations that motivated the next version**

* Each topic had exactly one keyword and one answer, so many phrasings were missed. For example, "check in" (without a hyphen) did not match the `"check-in"` key.
* All logic was written directly in the main loop, making it hard to reuse or extend.
* The topics were broad and general, with no defined scope for the chatbot's role.

\---

### Version 2: `chatbot2.py` (Restructuring and Scope)

**Purpose:** To give the chatbot a clear purpose and a more scalable structure.

**What changed**

1. **Defined scope.** The chatbot was refocused from general travel advice to hotel and airport guest services. Four topics were kept (check-in, flight, Wi-Fi, cab) and the rest (currency, roaming, booking, hotel, visa, passport, luggage, weather) were removed. Six new topics were added: check-out, airport transfers, cancellation, breakfast, room service, and pool and gym.
2. **Question bank.** A commented list of ten categories, each with three example questions, was added at the top of the file. This documents the expected user queries and acts as a specification for the chatbot.
3. **Nested data structure.** The flat dictionary was replaced with an intent-based structure, where each topic holds a list of `keywords` and a `response`. Several keywords can now trigger one answer (for example `"check in"`, `"checkin"` and `"check-in"`).
4. **Separation of logic and interface.** The matching logic moved from the main loop into a function, `get\_response()`, which returns the answer as a string. The main loop is now only responsible for input and output. The `matched` flag was no longer needed because the function returns directly.
5. **Improved fallback.** The "not understood" message now lists the specific topics the chatbot supports.
6. **Quality refinements.** Punctuation, spacing, time formats (for example `3:00 PM`) and hyphenation (`check-in`, `check-out`) were made consistent, and redundant keywords were removed.

**Key concepts practised:** nested dictionaries, functions with return values, separation of concerns, planning with a question bank.

**Problems solved:** limited phrasing coverage, tightly coupled code, unclear scope.

**Limitations that motivated the next version**

* Each topic still gave one fixed answer, so repeated questions felt mechanical.
* The chatbot could only be used through reading text.
* A `tokenize()` function that split text into words was defined but not yet used in the matching.

\---

### Version 3: `chatbot3.py` (Natural Interaction and NLP)

**Purpose:** To make Hugo feel more natural and to introduce basic language processing.

**What was added**

1. **Varied responses.** The `response` entry was changed to a `responses` list containing three to five alternatives per topic (36 in total). `random.choice()` selects one each time, so repeated questions do not always receive identical replies.
2. **Tokenisation and stemming.** The NLTK library was introduced. `word\_tokenize()` splits the user's message into tokens, and `PorterStemmer` reduces each token to its stem (for example "cancelling" becomes "cancel"). The `tokenize()` function now performs this processing.
3. **Text-to-speech.** A `speak()` function using `pyttsx3` was added, so Hugo reads each reply aloud. The goodbye message is also spoken.
4. **Improved fallback.** The fallback now asks the user to rephrase before listing the supported topics.

**Key concepts practised:** importing and using third-party libraries, list-based data, randomisation, introductory NLP, using external APIs.

**Problems solved:** repetitive answers, text-only output.

**Notes from testing and review**

* Calling `speak()` before `break` was necessary so that the goodbye message is spoken; otherwise the program exited before reaching the speech call.
* Creating a fresh speech engine inside `speak()` on every call was found to be the reliable approach with `pyttsx3` on Windows. Reusing a single engine caused the voice to stop after the first reply.
* A small wrapper function that only called `.lower()` was removed as unnecessary; the conversion is done directly inside `response()`.

**Limitations that motivated the next version**

* Every message was treated independently. A user could not ask a short follow-up such as "How much is it?" because Hugo had no memory of the previous topic.
* Stemming was applied to the user's words only, while keyword matching still relied mainly on substring search, so the stemmer added little practical benefit yet. It was kept as groundwork for future improvements (see [Future Work](#11-future-work)).

\---

### Version 4: `chatbot4.py` (Conversational Memory, Final Version)

**Purpose:** To let Hugo handle context, so that follow-up questions can be understood.

**What was added**

1. **Memory.** A `memory` dictionary stores the last topic that matched (`last\_request`), and a `question\_count` counter tracks how many questions have been asked.
2. **Memory reset.** After more than five questions, the memory is cleared and the counter reset, so that old context does not persist indefinitely.
3. **Context-aware follow-ups.** If no keyword matches, the chatbot checks for follow-up phrases and answers according to the remembered topic:

|Follow-up phrase|Example topics answered|
|-|-|
|"cost", "price", "how much"|cab, breakfast, Wi-Fi, room service|
|"how long", "how far"|airport, cab|
|"still", "available"|cab, breakfast, Wi-Fi|
|"where", "location"|cab, breakfast, room service, airport|

4. **State visibility.** The contents of `memory` are printed after each reply, which makes the chatbot's internal state easy to observe while testing.

**Key concepts practised:** global state, the `global` keyword, dictionaries as memory, nested conditionals, context handling in dialogue systems.

**Problems solved:** inability to understand short or incomplete follow-up questions.

**Note:** The follow-up figures (fares, prices, durations and locations) are illustrative placeholder data for demonstration purposes and do not represent a real business.

\---

## 9\. Summary of Versions

|Feature|V1|V2|V3|V4|
|-|:-:|:-:|:-:|:-:|
|Number of topics|12|10|10|10|
|Multiple keywords per topic|No|Yes|Yes|Yes|
|Question bank documentation|No|Yes|Yes|Yes|
|Logic in a separate function|No|Yes|Yes|Yes|
|Multiple responses per topic|No|No|Yes|Yes|
|Tokenisation and stemming (NLTK)|No|No|Yes|Yes|
|Text-to-speech|No|No|Yes|Yes|
|Conversational memory|No|No|No|Yes|
|Follow-up question handling|No|No|No|Yes|
|External libraries|None|None|NLTK, pyttsx3|NLTK, pyttsx3|

## 10\. Limitations

* **Keyword matching.** Topics are identified by searching for keywords inside the message. This does not understand meaning, so unusual phrasing, spelling mistakes or questions covering several topics at once may not be handled correctly.
* **Single-topic memory.** Hugo remembers only the most recent matched topic and forgets it after more than five questions.
* **Static information.** All answers are predefined. The chatbot does not access live data such as real flight status or actual room availability.
* **Placeholder data.** Prices, times and facilities are fictional.
* **Platform dependency.** The speech driver is set to `sapi5`, which is available on Windows only (see the platform note above).
* **No automated tests.** The chatbot was tested manually with the question bank.

## 11\. Future Work

* Stem the keywords as well as the user's words, and compare whole words rather than substrings. This would make full use of the stemmer, handle word variations such as "arrive", "arrived" and "arrival", and prevent accidental matches inside longer words.
* Add tolerance for spelling mistakes (for example fuzzy string matching).
* Replace keyword rules with a trained intent classifier.
* Add speech recognition so that users can talk to Hugo instead of typing.
* Make text-to-speech cross-platform.
* Provide a graphical or web interface.
* Connect to real data sources or APIs for live information.
* Add automated unit tests, using the question bank as test cases.

## 12\. Acknowledgements

* [NLTK](https://www.nltk.org/) for natural language processing tools.
* [pyttsx3](https://pypi.org/project/pyttsx3/) for offline text-to-speech.
* The quotation displayed at startup is commonly attributed to St. Augustine.

