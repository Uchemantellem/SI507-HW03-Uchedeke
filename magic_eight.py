
import random


def get_answer(dict):
    rand_num = random.randint(0,20)
    return dict[rand_num]

response = ""
while response != "quit":
	response = input("What is your question?")
	print(response[-1])
	if response == "quit":
		break
	if response[-1] != "?":
		print("I'm sorry, I can only answer questions")

	possible_questions = {0: "It is certain", 1:"It is decidedly so", 2: "Without a doubt", 3: "Yes - definitely", 4: "You may rely on it", 
	                      5: "As I see it, yes", 6: "Most likely", 7: "Outlook good", 8: "Yes", 9: "Signs point to yes", 10: "Reply hazey, try again", 
	                      11: "Ask again later", 12: "Better not tell you now", 13: "Cannot predict now", 14: "Concentrate and ask again", 
	                      15: "Don\'t count on it", 16: "My reply is no", 17: "My sources say no", 18: "Outlook not good", 19: "Very doubtful"}
	answer = get_answer(possible_questions)
	print(answer)

