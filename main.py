import re
import long_responses as long
import discord
import json

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
    response('hahaha!',['haha','hahaha', 'funny'], single_response=True)

    # Bot profile responses
    response('My name is Johnny. Nice to meet you!', ['name', 'what', 'your'], required_words=['name'])
    response('Not to brag about it but I am ageless.', ['what', 'age', 'your'], required_words=['age'])
    response("I like viruses. So I guess I'm vi-sexual.", ['gender', 'what'], required_words=['gender'])
    response('hmm I live in your computer.', ['live', 'where', 'from'], required_words=['where'])
    response('I think I am more of a purple guy.', ['color', 'favorite'], required_words=['color'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.trivia(), ['give', 'me', 'trivia', "computer"], required_words=['trivia'])
    response(long.joke(), ['tell', 'joke', "funny"], required_words=['joke'])
    response(long.quote(), ['tell', 'say', 'quote',], required_words=['quote'])
    response(long.pickupLines(), ['tell', 'pickup', 'line', 'say'], required_words=['pickup', 'line'])
    response(long.weather(message), ['check', 'what', 'weather', 'tell'], required_words=['weather'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] < 1: 
        return long.unknown() 
    else:
        return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower()) # removes punctuations to get bare words
    response = check_all_messages(split_message)
    return response

def main():
    print("Johnny: Hello there! I'm Johnny, I am a very cool chat bot. I can tell trivias, quotes and I can even humor you with my jokes and pickup lines!.")

    while True:
        print('Johnny: ' + get_response(input('You: ')))

async def send_message(message, user_message, is_private):
    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    with open("config.json", "r") as f:
        config = json.load(f)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(config['token'])

if __name__ == '__main__':
    try:
        run_discord_bot() 
    except:
        main() # in case discord token is closed user can talk to johnny in terminal