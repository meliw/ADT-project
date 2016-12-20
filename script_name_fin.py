#!/usr/bin/python
#coding: utf-8


import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download()



stop_words = stopwords.words("english")

list_stop_words = ["et","also","far","thus","sea","whereas","any","other"]

list_tag7 = [['NNP', 'NN', 'NN', '.', 'NN', 'NNP', 'CD']]
list_tag6 = [['NNP', 'NNP', 'NN', 'NN', '.', 'NNP']]
list_tag5 = [['NNP', 'NN', 'NNP', 'NN', 'NNP']]
list_tag4 = [['NN', 'NN', 'NNP', 'PRP'], ['NNP', 'NN', 'NNP', 'CD'], ['NNP', 'NN', '.', 'NNP'], ['NNP', 'NN', '.', 'CC'], ['NNP', 'NNS', 'VBP', 'CD'], ['NNP', 'NNP', 'VBZ', 'CD'],['NNP', 'VBZ', 'NNP', 'CD']]
list_tag3 = [['NNP', 'VBZ', 'NNP'], ['NNP', 'NN', 'CD'], ['NNP', 'NN', 'NNP'], ['NNP', 'VBD', 'CD'], ['NNP', 'NNS', 'NNP']]
list_tag2 = [['NNP', 'NN'],['NNP', 'NNP'], ['NNP', 'NNS'], ['NNS', 'NNS'], ['NN', 'NN'], ['NNS', 'VBP']]
list_tag1 = [['NNP'], ['NNS'], ['NN']]

list_tagg_v2 = ['NNP', 'NNS', 'NN']


def cat_name(file):
			with open(file, 'r') as f_in : 
				list_name=[]
				for n,line in enumerate(f_in) :
					list_taggs= []
					

					"""---- Generation des tagg ---- """

					tokens = word_tokenize(line)
					tokens = [i for i in tokens if i not in stop_words]
					taggs = nltk.pos_tag(tokens)
					

					"""---- Traitement de la première ligne de chaque texte ----"""
					
					if n==0 : 
						name=''
						for tagg1 in taggs :
							list_taggs.append(tagg1[1])
						if check_tagg(list_taggs) : 
							for tag in taggs :
								name+=tag[0]+' '
						if name not in list_name and name!='':
							list_name.append(name)
							


					"""---- Si la première ligne ne contenait pas le nom de la bactérie----"""

					"""---- On récupère l'ensemble des termes qui ressemble à des noms de bactérie----"""
					if re.match(r'(.+)?([A-Z][a-z]+(um|us|i|ii|a|as) (sp . )?([a-z]+)?) (.+)', line) :
						nom=re.findall(r'([A-Z][a-z]+(um|us|i|ii|a|as) (sp . )?([a-z]+)?)', line)
						for j in range(len(nom)) :
							if nom[j][0] not in list_name :
								next_word=nom[j][0].split(" ")[1]								
								if next_word not in stop_words and next_word not in list_stop_words:
									fichier=re.sub(r'(.+)/(.+).txt', r'\2', file)
									if nom[j][0] not in list_name :
										list_name.append(nom[j][0])

					"""---- On récupère les noms ou phrases avec bacteria ou bacterial----"""
					debut=re.match(r'(.+)bacteria', line )
					if debut :
						bacteria=re.findall(r'((([A-Za-z]+ ){2})([A-Za-z]+)?bacteria(l)?)', line)
						for m in range(len(bacteria)):
							if bacteria[m][3]!='':
								name1 = bacteria[m][3]+'bacteria'
								#print (name1)
								if name1 not in list_name :
									list_name.append(name1)
							elif bacteria[m][2][:-1] not in stop_words and bacteria[m][2][:-1] not in list_stop_words:
								tagg_bacteria = nltk.pos_tag(word_tokenize(bacteria[m][0]))
								#print (tagg_bacteria)
								if tagg_bacteria[1][1] in ['JJ', 'NN', 'NNP']:
									if tagg_bacteria[0][1] in ['JJ', 'NN']:
										#print (bacteria[m][0])
										if bacteria[m][0] not in list_name :
											list_name.append(bacteria[m][0])
									else : 
										name2=tagg_bacteria[1][0]+' bacteria'
										#print(name2)
										if name2 not in list_name :
											list_name.append(name2)	
										
						
					

					"""---- On récupère l'ensemble des abbréviations qui correspondent à des bactéries----"""
					if re.match(r'(.+)([A-Z]\. [a-z]+)(.+)', line) :
						abb=re.findall(r'[A-Z]\. [a-z]+', line )
						for k in range(len(abb)):
							if abb[k] not in list_name :
								next_abb=abb[k].split(" ")[1]
								if next_abb not in stop_words and next_abb not in list_stop_words :
									if abb[k] not in list_name :
										list_name.append(abb[k]) 
									

				return list_name	
	


					
				




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

