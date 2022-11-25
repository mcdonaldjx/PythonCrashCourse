#Created 10/25/2022 by Jared
#Exercise 8-9- Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
def show_messages(text_messages):
  for text in text_messages:
    print(f"Text Message: {text}")
text_messages = ["good morning", "hello", "good night", "see you soon"]
show_messages(text_messages)
