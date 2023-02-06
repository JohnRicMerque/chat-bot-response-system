import random
import long_responses as long

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower()) # removes punctuations
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))