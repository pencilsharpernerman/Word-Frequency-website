import re
from nltk.corpus import stopwords
import enchant

suffix = ['able','ac','acity','ocity','ade','age','aholic','oholic','al','algia','an','ian','ance','ant','ar','ard',
'arian','arium','ary','ate','ation','ative','cide','cracy','crat','cule','cy','cycle','dom','dox','ectomy','ed','ee',
'eer','emia','en','ence','ency','ent','er','ern','escence','ese','esque','ess','est','etic','ette','ful','fy','gam',
'gon','hood','ial','ian','iasis','iatric','ible','ic','ile','ily','ine','ing','ion','ious','ish','ism','ist','ite',
'itis','ity','ive','ization','ize','less','let','like','ling','loger','log','ly','ment','ness','oid','ology','oma',
'onym','opia','opsy','or','ory','osis','ostomy','ous','path','pathy','phile','phobia','phone','phyte','plegia','plegic',
'pnea','s','scopy','scribe','sect','ship','sion','some','sophy','th','tion','tome','trophy','tude','ty','ular','uous',
'ure','ward','ware','wise','y']


def root_mode(word):
	for s in suffix:
		pattern = re.compile(s + "$")
		if re.search(pattern,word):
			word = re.split(pattern,word)[0]
	return word

#parses the text file and returns a list of words
def parse(file):
              with open(file, 'rb') as f:
              	return  re.findall(re.compile('\w+'), f.read().lower())

#checks for an stop words present in the  text file
def stop_words_remove(word_list):
	filtered_words = [word for word in word_list if word not in stopwords.words('english')]
	return filtered_words

#checks if a word is present in the US English dictionary
def check_valid_word(word):
	d = enchant.Dict("en_US")
	
	if word != "" and d.check(word) and len(word) > 1 and  not is_number(word):
		return word
	return ""

#checks if a string is a number 
def is_number(s):
    try:
        float(s)
        int(s)
        return True
    except ValueError:
        return False

#parses the dictionary to return the key with the max value
def getMax(dictionary):
	v=list(dictionary.values())
	k=list(dictionary.keys())
	return k[v.index(max(v))]

#returns the final dictionary of root words from the text file with the word count 
def final_word(filename):
	word_list = stop_words_remove(parse(filename))
	output = {}

	for word in word_list:
		if check_valid_word(word):
			
			if check_valid_word(root_mode(word)):
				
				insert_word = root_mode(word)
				
				if insert_word in output:
					output[insert_word] +=1
				else:
					output[insert_word] = 1
			else:
				if word in output:
					output[word] += 1
				else:
					output[word] = 1
	
	return output

#returns the top25frequently words in the dictionary
def top25FrequentWords(filename):
	i = 25
	output = {}
	result = []
	output = final_word(filename)
	while i != 0 and len(output.keys()) != 0:
		result.append(getMax(output))
		output.pop(getMax(output), None)
		i -= 1
	return result
# if __name__ == "__main__":
# 	result = top25FrequentWords('./dbms_2.txt')
# 	print result
	