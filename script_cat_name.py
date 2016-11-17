#!/usr/bin/python
#coding: utf-8


import re, nltk, glob, sys
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

def main(dirname):
	print "\tLancement de l'analyse "

	files=glob.glob(dirname+'*.txt')
	print "\tOuverture des fichiers "

	with open(dirname+'Results.txt', 'w') as f_out :
		for file in files : 
			with open(file, 'r') as f_in : 
				for n, line in enumerate(f_in) :
					list_taggs= []

					"""---- Analyse par tagg ---- """
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
						if name not in list_name:
							list_name.append(name)
							fichier=re.sub(r'(.+)/(.+).txt', r'\2', file)
							fin_name="Nom de bacterie dans le fichier "+fichier+"\t"+name+"\n"
							f_out.write(fin_name)
							#print "name "+name


					"""---- Si la première ligne ne contenait pas le nom de la bactérie----"""

					"""---- On récupère l'ensemble des termes qui ressemble à des noms----"""
					if re.match(r'(.+)?([A-Z][a-z]+(um|us|i|ii|a|as) (sp . )?([a-z]+)?) (.+)', line) :
						nom=re.findall(r'([A-Z][a-z]+(um|us|i|ii|a|as) (sp . )?([a-z]+)?)', line)
						for j in range(len(nom)) :
							if nom[j][0] not in list_name :
								if nom[j][0][0] not in stop_words and nom[j][0][1] not in stop_words :
									fichier=re.sub(r'(.+)/(.+).txt', r'\2', file)
									fin_nom="Nom de bacterie dans le fichier "+fichier+"\t"+nom[j][0]+"\n"
									f_out.write(fin_nom)
									list_name.append(nom[j][0])


					"""---- On récupère l'ensemble des abbréviations qui correspondent à des bactéries----"""
					if re.match(r'(.+)([A-Z]\. [a-z]+)(.+)', line) :
						abb=re.findall(r'[A-Z]\. [a-z]+', line )
						for k in range(len(abb)):
							if abb[k] not in list_name and abb[k].find(" et")== -1 :
								list_name.append(abb[k]) 
								fichier=re.sub(r'(.+)/(.+).txt', r'\2', file)
								fin_abb="Nom de bacterie dans le fichier "+fichier+"\t"+abb[k]+"\n"
								f_out.write(fin_abb)

	print "\tFin de l'analyse et fermeture des fichiers "
	


					
				




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
	if len(sys.argv)<2 :
		print "Precisez le dossier contenant vos fichiers"
	else:
		dirname = sys.argv[1]
		main(dirname)