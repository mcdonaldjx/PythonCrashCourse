#Created 10/25/2022 by Jared
#Exercise 8-10- Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
def send_messages(text_messages):
  sent_messages = []
  for text in text_messages:
    sent_messages.append(text)
  return sent_messages
text_messages = ["good morning", "hello", "good night", "see you soon"]
sent_messages = send_messages(text_messages)
for text in text_messages:
  print(f"Sending {text}...")
print()
for sent_text in sent_messages:
  print(f"Sent {sent_text}!")
