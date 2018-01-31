import random
def question:
	ask = input("what is your question?")
	return ask
possible_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, Definitely", "You may rely on it",
"As I see it, Yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply Hazey, try again",
"Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't Count on it",
"My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

question()

print(random.choice(possible_answers))
