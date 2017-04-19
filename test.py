import enchant
def check_valid_word(word):
	d = enchant.Dict("en_US")
	output = []
	#for word in word_list:
	if d.check(word):
		output.append(word)
	return output
if __name__ == "__main__":
              print check_valid_word("hell")