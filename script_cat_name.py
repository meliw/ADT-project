#!/usr/bin/python
#coding: utf-8

dirname = "/Users/Meline/Documents/M2BIG/ADT/data_suj1/train/"


import re, nltk, glob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download()
stop_words = stopwords.words("english")
list_name= []


files=glob.glob(dirname+'*.txt')
for file in files : 
	with open(file, 'r') as f_in : 
		for i, line in enumerate(f_in) :
			if i==0 : 
				list_taggs = []
				tagg0, tagg1, tagg2, tagg3 = '','','',''
				tokens = word_tokenize(line)
				tokens = [i for i in tokens if i not in stop_words]
				taggs = nltk.pos_tag(tokens)
				for tagg in taggs :
					list_taggs.append(tagg[1])
					 

				print list_taggs