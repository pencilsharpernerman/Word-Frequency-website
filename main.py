import Queue as queue
import re
import parse
suffix = ['able','ac','acity','ocity','ade','age','aholic','oholic','al','algia','an','ian','ance','ant','ar','ard',
'arian','arium','ary','ate','ation','ative','cide','cracy','crat','cule','cy','cycle','dom','dox','ectomy','ed','ee',
'eer','emia','en','ence','ency','ent','er','ern','escence','ese','esque','ess','est','etic','ette','ful','fy','gam',
'gon','hood','ial','ian','iasis','iatric','ible','ic','ile','ily','ine','ing','ion','ious','ish','ism','ist','ite',
'itis','ity','ive','ization','ize','less','let','like','ling','loger','log','ly','ment','ness','oid','ology','oma',
'onym','opia','opsy','or','ory','osis','ostomy','ous','path','pathy','phile','phobia','phone','phyte','plegia','plegic',
'pnea','scopy','scribe','sect','ship','sion','some','sophy','th','tion','tome','trophy','tude','ty','ular','uous',
'ure','ward','ware','wise','y']


def index():
	word_list = queue.PriorityQueue()
	text = parse.parse("sample.txt")
	for word in text:
		for s in suffix:
			pattern = re.compile("([A-Z]|[a-z])" + s + "$")
			print pattern
		# if pattern.match(word):
		# 	word_list.put()

		#Check if the above pattern pattern matches with word
		#Remove the pattern part from the word and store it in a global list

#Once the loop is out, count the frequently occurring words in the list



if __name__ == "main":
	index()
