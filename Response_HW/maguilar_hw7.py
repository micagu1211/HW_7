global responses, responses2

class Speaker:

	def __init__(self,n,v):
		self.name = n
		self.vocab = v

	def getname(self):
		return self.name

	def getvocab(self,text):
		l = (hash(text) % len(self.vocab))
		return self.vocab[l]


def main():
	responses = ['I want to build the wall', 'We have some bad hombres here','We need the wall to be built', 'I am not a puppet, Hillary is the puppet','One of my first acts will be to get all the drug lords.','They are coming in illegally','We are a country of laws','They are rapists and criminals coming into our country illegally.','CHINA!','I will defeat Mexico and China single handedly.',' Excuse me. Putin has outsmarted her in Syria.']
	responses2 = ['I find that just astonishing', 'We will not have open borders', 'Donald calls me a puppet but I am not, I assure you', 'Well I have been the Secretary of State for years, that should mean something.', 'Well, first of all, I support the Second Amendment. I lived in Arkansas for 18 wonderful years. I represented upstate New York. I understand and respect the tradition of gun ownership. It goes back to the founding of our country.', 'And we have come too far to have that turned back now. And, indeed, he said women should be punished, that there should be some form of punishment for women who obtain abortions. And I could just not be more opposed to that kind of thinking.','Well, as he was talking, I was thinking about a young girl I met here in Las Vegas, Carla, who is very worried that her parents might be deported, because she was born in this country but they were not. They work hard, they do everything they can to give her a good life.','Cutting taxes on the wealthy, we have tried that. It has not worked the way that it has been promised.','There is only one of us on this stage who has actually shipped jobs to Mexico, because that is Donald. He has shipped jobs to 12 countries, including Mexico.']

	while 1:
		text = raw_input("Please ask Hillary and Donald a question: ")
		donald = Speaker('Donald Trump',responses)
		hillary = Speaker('Hillary Clinton', responses2)
		print("\n")
		print donald.getname(), " responds, ", donald.getvocab(text)
		print("\n")
		print hillary.getname(), " responds, ", hillary.getvocab(text)
		print("\n")

		ask = raw_input("Would you like to ask another question? Please type yes or no : ")
		yes = hash('yes')
		no = hash('no')

		if hash(ask) == yes:
			print "Ask another question: "

		elif hash(ask) == no : 
			print "Thank you for your time. Good luck! "
			break
		else:
			print "This was not a correct response. Please try again.\n"
			break

if __name__ == '__main__':
	main()


