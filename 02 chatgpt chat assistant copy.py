import openai
from trial import detect_adult_content

openai.api_key = "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"

# Function to check for adult-related content
def check_for_adult_content(message):
    adult_keywords = ["adult content ", "explicit", "dirty", "inappropriate"]  # Add more keywords as needed
    for keyword in adult_keywords:
        if keyword in message.lower():
            return True
    return False

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:  # Infinite loop until user types "quit()"
    message = input()
    messages.append({"role": "user", "content": message})
    
    # Check for adult-related content
    if check_for_adult_content(message):
        print("Flagged message adult content")
        messages.append({"role": "assistant", "content": "adult content"})
        continue  # Skip processing and sending the flagged message
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

    if message.lower() == "quit()":  # Check if user wants to quit
        break  # Exit the loop if user types "quit()"
