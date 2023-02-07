import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {} #DICTIONARY OF RESPONSES

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'],  single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Bot profile responses
    response('My name is Johnny. Nice to meet you!', ['name', 'what', 'your'], required_words=['name'])
    response('Not to brag about it but I am ageless.', ['how', 'old', 'you'], single_response=True)
    response("I like viruses. So I guess I'm vi-sexual.", ['gender', 'what'], required_words=['gender'])
    response('hmm I live in your computer.', ['live', 'where', 'from'], required_words=['where'])
    response('I think I am more of a purple guy.', ['color', 'favorite'], required_words=['color'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.trivia(), ['give', 'me', 'trivia', "computer"], required_words=['trivia'])
    response(long.joke(), ['tell', 'joke', "funny"], required_words=['joke'])
    response(long.quote(), ['tell', 'quote',], required_words=['quote'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] < 1: 
        return long.unknown() 
    else:
        return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower()) # removes punctuations to get bare words
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Johnny: ' + get_response(input('You: ')))