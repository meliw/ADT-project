#!/usr/bin/python
#coding: utf-8

dirname = "/Users/Meline/Documents/M2BIG/ADT/data_suj1/train/"


import re, nltk, glob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download()



stop_words = stopwords.words("english")

list_tag7 = [['NNP', 'NN', 'NN', '.', 'NN', 'NNP', 'CD']]
list_tag6 = [['NNP', 'NNP', 'NN', 'NN', '.', 'NNP']]
list_tag5 = [['NNP', 'NN', 'NNP', 'NN', 'NNP']]
list_tag4 = [['NN', 'NN', 'NNP', 'PRP'], ['NNP', 'NN', 'NNP', 'CD'], ['NNP', 'NN', '.', 'NNP'], ['NNP', 'NN', '.', 'CC'], ['NNP', 'NNS', 'VBP', 'CD'], ['NNP', 'NNP', 'VBZ', 'CD'],['NNP', 'VBZ', 'NNP', 'CD']]
list_tag3 = [['NNP', 'VBZ', 'NNP'], ['NNP', 'NN', 'CD'], ['NNP', 'NN', 'NNP'], ['NNP', 'VBD', 'CD'], ['NNP', 'NNS', 'NNP']]
list_tag2 = [['NNP', 'NN'],['NNP', 'NNP'], ['NNP', 'NNS'], ['NNS', 'NNS'], ['NN', 'NN'], ['NNS', 'VBP']]
list_tag1 = [['NNP'], ['NNS'], ['NN']]

list_tagg_v2 = ['NNP', 'NNS', 'NN']
list_name=[]

def main():
	files=glob.glob(dirname+'*.txt')
	for file in files : 
		with open(file, 'r') as f_in : 

			for n, line in enumerate(f_in) :
				list_taggs= []
				list_taggs2 = []
				tokens = word_tokenize(line)
				tokens = [i for i in tokens if i not in stop_words]
				taggs = nltk.pos_tag(tokens)
				if n==0 : 
					name=''
					for tagg1 in taggs :
						list_taggs.append(tagg1[1])
					if check_tagg(list_taggs) : 
						for tag in taggs :
							name+=tag[0]+' '
					if name not in list_name:
						list_name.append(name)
					if name!='' :
						#print "name "+name
				 		break
				if re.match(r'(.+)?([A-Z][a-z]+(um|us|i|ii|a|as) ([a-z]+)?) (.+)', line) :
					nom=re.findall(r'([A-Z][a-z]+(um|us|i|ii|a|as) ([a-z]+)?)', line)
					for j in range(len(nom)) :
						if nom[j][0] not in list_name :
							list_name.append(nom[j][0])
				if re.match(r'(.+)([A-Z]\. [a-z]+)(.+)', line) :
					abb=re.findall(r'[A-Z]\. [a-z]+', line )
					for k in range(len(abb)):
						if abb[k] not in list_name :
							list_name.append(abb[k]) 
	print list_name
				#for tagg2 in taggs :
				#	list_taggs2.append(tagg2[1])
				#for x in list_tag2 : 
				#	try :
				#		print x
				#		print list_taggs2
				#		index= list_taggs2.index(','.join(x))
				#		print index	
				#	except : 
				#		print "pas trouver"			
					#list_name.append(tagg2[0])
					
				#print text_taggs2
				#if list_taggs2 in list_tag2 : print list_tagg2
					
				




def check_tagg(list):
	if len(list)==1 : 
		if list in list_tag1 : return True
	if len(list)==2 :
		if list in list_tag2 : return True
	if len(list)==3 : 
		if list in list_tag3 : return True
	if len(list)==4 : 
		if list in list_tag4 : return True
	if len(list)==5 : 
		if list in list_tag5 : return True
	if len(list)==6 : 
		if list in list_tag6 : return True
	if len(list)==7 : 
		if list in list_tag7 : return True

if __name__ == '__main__':
	main()