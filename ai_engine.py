def get_ai_response(user_message, personality):
    if personality == "friendly":
        return f"I'm your friendly AI! You said: {user_message}"
    elif personality == "sarcastic":
        return f"Oh wow... {user_message}? How original. 🙄"
    else:
        return f"You said: {user_message}. Let's keep talking!"
