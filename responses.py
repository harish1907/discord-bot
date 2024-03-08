import random

def handle_response(message):
    p_message = message.lower()

    if p_message == "hello":
        return "Hye there!"
    
    if p_message == "roll":
        return str(random.randint(1,6))
    
    if p_message == "!help":
        return "I will help section after all the use cases."