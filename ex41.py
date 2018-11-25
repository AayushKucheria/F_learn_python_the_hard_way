# Importing the random function
import random
# Importing the url library to open the url
from urllib.request import urlopen
# Importing the basic library
import sys

# The url through which we've to download the words
WORD_URL = "http://learncodethehardway.org/words.txt"

# The word list from WORD_URL is stored here.
WORDS = []

# A basic dictionary of syntax of the different sentences
PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function *** that takes self and @@@",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, call it with parameters.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
	}
	
# Do they want to drill phrases first
# If argv has english, do PHRASE_FIRST true else false
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# Load up the words from the website
# A for loop to run through each word in the lines of the .txt file opened by urlopen()
for word in urlopen(WORD_URL).readlines():
	
	# Appending all the words to WORDS[] by stripping their sides, then converting them to string by telling the encoding.
	WORDS.append(str(word.strip(), encoding="utf-8"))
	
# TODO a pretty big function, I'll get back to it later
def convert(snippet, phrase):

	# Capitalizing the first letters of classes
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	# Setting random numbers of parameters, and then random parameters.
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', ' .join(
			random.sample(WORDS, param_count)))
			
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# Fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# Fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# Fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
	
	return results
	

# Keep going until they hit CTRL-D
try:
	while True: 
		# Snippet is a list of the keys of the Phrases dict
		snippets = list(PHRASES.keys())
		# Shuffle the snippets!
		random.shuffle(snippets)
		
		# Iterating through each snippet
		for snippet in snippets:
		
			# Get the answer to the key and store in phrase
			phrase = PHRASES[snippet]
			
			# Change the snippet and phrase to actual question and answer
			question, answer = convert(snippet, phrase)
			
			# If mentioned "English" in argv, interchange
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print(question)
			
			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError: # EOFError = CTRL-D
	print("\nBye")
