import difflib
import sys
def readRockYouData(size=None, filename='rockyou-withcount.txt'):
    word_lst = []
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            word = line.split(' ')[1]
            word_lst.append(word)
            count += 1
            if size and count == size:
                break
    return word_lst

def findMostSimilarStringFromPool(inputFile):
    cut_off_val = 0.9
    string_pool = readRockYouData(100)
    output_string_pool =[]
    result=[]
    for word in inputFile :
    	output_string_pool.append( difflib.get_close_matches(word, string_pool,
                                                   cutoff=cut_off_val))
    if len(output_string_pool) and inputFile != output_string_pool[0]:
        for x in output_string_pool:
        	for y in x:
        		if y in inputFile:
        			inputFile.remove(y)
    	return inputFile
    else:
        return None

if __name__ == '__main__':
	inputFile = open(sys.argv[1])
	inputList = []
	for line in inputFile:
		inputList.append(line)
	print findMostSimilarStringFromPool(inputList[0].split(','))