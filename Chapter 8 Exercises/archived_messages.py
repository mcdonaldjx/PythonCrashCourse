#Created 10/25/2022 by Jared
#Exercise 8-11- Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list hasa retained its messages.
def send_messages(text_messages):
  sent_messages = []
  while text_messages:
    sent_messages.append(text_messages.pop())
  return sent_messages
text_messages = ["good morning", "hello", "good night", "see you soon"]
sent_messages = send_messages(text_messages[:])
print("Messages to send:")
for text in text_messages:
  print(text)
print()
print("Messages sent:")
for sent_text in sent_messages:
  print(f"{sent_text}")
