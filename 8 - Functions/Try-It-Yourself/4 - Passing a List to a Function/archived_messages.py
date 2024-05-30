def send_messages(messages, sent_messages):
	"""
	Send the message.
	Then, add it to the sent messages.
	"""

	messages_duplicate = messages[:]
	
	while messages_duplicate:
		current_message = messages_duplicate.pop()
		print(f"Sending Message: {current_message}")
		sent_messages.append(current_message)

def show_sent_messages(sent_messages):
	"""Show all the sent messages."""
	print("\n--- Sent Messages ---")
	for message in sent_messages:
		print(f"{message}")

def show_original_messages(original_messages):
	"""Show all the original messages."""
	print("\n--- Original Messages ---")
	for message in original_messages:
		print(f"{message}")

messages = [
	"Hi, Emmar!",
	"I love you!",
	"Thank you so much!"
]
sent_messages = []

send_messages(messages, sent_messages)
show_sent_messages(sent_messages)
show_original_messages(messages)