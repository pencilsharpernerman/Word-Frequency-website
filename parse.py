# import csv

# def parse(filename):
#     '''
#     takes a filename and returns attribute information and all the data in array of dictionaries
#     '''
#     # initialize variables

#     out = []    
#     csvfile = open(filename,'rb')
#     fileToRead = csv.reader(csvfile)

#     headers = fileToRead.next()

#     # iterate through rows of actual data
#     for row in fileToRead:
#         out.append(dict(zip(headers, row)))

#     return out

def parse(filename) :
        open_file = open(filename,'r')
        words_list = []
        contents = open_file.readlines()
        for i in range(len(contents)):
            words_list.extend(contents[i].split())
            return words_list
            #open_file.close()

if __name__ == "__main__":
	print parse("sample.txt")