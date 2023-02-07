import random
import requests

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

# trivia reference: https://computercpr.com/computer-facts/
def trivia():
    trivias =  ["The First Computer Weighed More Than 27 Tons. Her name was ENIAC, and she took up a modest 1800 square feet of space", "About 90 percent of the World’s Currency Only Exists on Computers. This means only about 10 percent of the global currency is actually cash.", "The First Computer Mouse was Made of Wood Doug Engelbart invented it in 1964.", "About 70% of Virus Engineers Work for Organized Crime Syndicates. This gives new weight to the importance of anti-virus and anti-malware software, and excellent virus removal services.", "The First Known Computer Programmer was a Woman. Her name was Ada Lovelace, and she lived in England, where she worked as a mathematician and writer. She is famous for working on the “Analytical Engine.", "Some of the Biggest Computer Brands Started in Garages.","People Blink Less When They Use Computers. While the average person blinks about 20 times a minute under normal circumstances, people on computers only blink about seven times a minute.", "Hackers Write About 6,000 New Viruses Each Month. These viruses are designed to target a wide selection of operating systems, so learning to avoid viruses and malware is essential!", "More Than 80% of Daily Emails in the U.S. are Spam.To keep your data safe, delete these emails immediately and don’t click any links or attachments they might contain.", "MyDoom is the Most Expensive Computer Virus in History. The virus cost an estimated $38.5 billion in damage and came about in January of 2006. Shortly after that, it earned a name for itself as the fastest-spreading virus ever.","The Parts for the Modern Computer Were First Invented in 1833. A man named Charles Babbage put them together, but the first modern computer came about 120 years later.","The First Gigabyte Drive Cost $40,000. It was released in 1980 and weighed 550 lbs. How’s that for a portable drive?","The Case of the First Macintosh Computer Includes 47 Signatures. On the inside of the device, Macintosh’s entire 1982 division signed the case.","The Worst U.S. Security Breach of All Time Happened Because of a USB Stick. Someone found the stick (which a foreign intelligence agency infected) in a parking lot and plugged it into their computer. The computer had links to the U.S. Central Command. The attack happened in 2008 and resulted in the theft of thousands of classified and unclassified documents. The Pentagon spent about 14 months cleaning up the damage from the worm.","A Single Computer Catches 50% of all Wikipedia Vandalism"]
    response = trivias[random.randrange(len(trivias))]
    return response

# joke reference: https://parade.com/1287449/marynliles/short-jokes/
def joke():
    jokes = ['What did the lava say to his girlfriend? “I lava you!”', "What’s Thanos’ favorite app on his phone? Snapchat.", "What does a storm cloud wear under his raincoat? Thunderwear.", "What do you call an ant who fights crime? A vigilANTe!", "What kind of math do birds love? Owl-gebra!", 'Why was 6 afraid of 7? Because 7,8,9.', 'Why can’t you ever trust atoms? Because they make up everything.', 'What do you call a fish without an eye? A fsh', "What did the ghost call his Mum and Dad? His transparents.", "What kind of nut doesn’t like money? Cash ew", "What do you call a dog magician? A labracadabrador.", "What do you call a fake noodle? An impasta", "Can February March? No, but April May!"]
    response = jokes[random.randrange(len(jokes))]
    return response

def quote():
    try:
        response = requests.get("http://api.quotable.io/random").json()
        return f'"{response["content"]}" - {response["author"]}'
    except:
        return "I'm sorry i have no quotes for you today"
    
def pickupLines():
    pUpLines = ["Are you an exception? Let me catch you.", "You are my increment operator. You make my value increase.", "I think you're my compiler. My life wouldn't start without you.", "I am a BufferedReader. You input meaning into my life.", "You are my semicolon; always present in everything I do.", "If I were a method, you must be my parameter, because I will always need you.", "Can you be my private variable? I want to be the only one with access to you.", "We are an aggregation of classes: one cannot exist without the other.", "public class YourWorld extends MyWorld", "My love is a for loop without the increment operator-- infinitive, non-terminating, and difficult to stop once it starts running.", "Let me be the 'throws Exception' to your 'public static void main (String[] args)'. I will accept whatever you give me.","You are my superclass: you define what I can do.", "You are the IDE of my life: I find it easier because of you.", "My main method is 'public love iLoveYou().' ","I am the field attribute in your class: I can't exist unless you do.", "My love for you is a constant variable: unupdatable and unchangeable.", "Are you an applet? You make me feel all GUI (gooey) inside.", "You are my loop condition. I keep coming back to you.", "Can you be my EventListener? That way you notice everything that I do.", "I am a boolean method whose love will always return true."]
    response = pUpLines[random.randrange(len(pUpLines))]
    return response

def unknown():
    response = ["Could you please re-phrase that? ", "uhmm...", "I didn't quite get that...", "What does that mean?"][random.randrange(4)]
    return response
