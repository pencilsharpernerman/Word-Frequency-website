# Word-Frequency-website

Goal: Build a webapp that performs simple frequency analysis on a user-supplied text document.

The application should accept a text document from the user, count how often each word is used in it, and report the top 25 most frequently used.

In order to make the results more useful, the analysis should extract the stems of the words so that different inflections of the same word are all counted in the same bucket. Use the following categories when stemming:

Regularly conjugated english verbs. For example, consider "talk", "talks", "talking", and "talked" to all be forms of "talk".
Regularly pluralized english nouns. For example, consider "cat" and "cats" to be forms of "cat".

Usage:

Click the "Choose File" button and upload a text file which you need to evaluate.
The webpage displays the Top 25 frequent words in the file present the English language dictionary excluding stop words.
The top25 words returned are in-order of the frequency from max to min.



FrameWork:
Flask 

Tools and Technologies:
HTML , CSS , Python

Libraries:
ntlk
enchant

To Run:

Install nltk : Follwoing the instructions from :

http://www.pitt.edu/~naraehan/python2/faq.html

Download the stop words dictionary :

Step 1 ) Open a python shell
Step 2) import nltk
        nltk.download('stopwords')

Install enchant using the cmdline :

pip install pyenchant

Run the server on the localhost using the cmdline:
python server.py



