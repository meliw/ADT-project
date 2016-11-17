#!/usr/bin/python3.5
#coding: utf-8

import re, glob


def extract_entities_cat(dirname):
	"""
		Extracts the entities and according categories from the .ent files in a training directory
		and returns a dictionnary of all the entities as keys and their categories as values.

		:param dirname: name of the directory where the files are located
		:type dirname: str
		:return: entities and categories of the .ent files in the training directory
		:rtype: dict of str

	"""
	d_entities={}
	p=re.compile(r'\d+\t([A-Za-z]+)\s\d+-\d+\s([A-Za-z ]+)(\s\d+-\d+\s([A-Za-z ]+))?')

	files=glob.glob(dirname+'*.ent')
	for file in files:
    		with open(file, 'r') as fichier:
        		for line in fichier:
            			m=p.match(line)
            			if not m: break
            			cat = m.group(1)
            			nom = m.group(2)
				if cat == 'Bacteria': continue
            			if nom not in d_entities:
                			d_entities[nom]=cat
            			if m.group(4) is not None and m.group(4) not in d_entities:
                			d_entities[m.group(4)]=cat
                
	return d_entities



dirname='/media/DATA/Master/Analyse_donnees_text/data_suj1/train/'

dico_entities_cat=extract_entities_cat(dirname)
print(dico_entities_cat)
