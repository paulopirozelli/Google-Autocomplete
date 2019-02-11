import requests

querry = input("digite uma busca: ")

# site da api
url = "http://suggestqueries.google.com/complete/search"

# client pode ser "chrome" ou "firefox"
client = "chrome"
language = "pt"

params = {
        "client": client,
        "q": querry,
        "hl": language
        }

r = requests.get(url, params = params)
answers = r.json()[1]
print(answers)
# o número de respostas varia bastante, então é possível limitar as alternativas:
#limit = 8
#answers = answers[:limit]

questions_en = [
		'Power Rangers are', 
		'Gremlins are', 
		'Is it OK to eat',
		'What is the highest',
		'Why are white people',
		'Is Africa in',
		'How long until',
		'Why is Batman so',
		'Why do people like', 
		'What is the biggest', 
		'When did women start', 
		'Can I eat my',
		'Kim Kardashian is',
		'I would never vote for a',
		'Why did Pikachu ',
		'When is the best time to',
		'Is it bad to like',
		'How do you pronounce',
		'How do you get rid of',
		'How to get an awesome',
		'I think my dog wants to',
		'What happens if you eat too much',
		'Is it safe to travel to',
		'What happens inside of a',
		'What does it mean when',
		'Why are Americans so',
		'Is it legal to marry',
		'Is it cool to wear',
		'Why is Mel Gibson so',
		'I am terrified of',
		'Chuck Norris is a',
		'How to fix a stupid',
		'I wish I had more',
		'I wish I had some goddamn',
		'My dog peed on my',
		'Release the',
		'When will McDonalds have',
		'Pirates are the',
		'Why is the world so',
		'Why does it smell when I',
		'When will Apple release the new',
		'Will the moon ever',
		'I am stuck in a'
	]