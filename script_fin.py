from script_name_fin import cat_name
import sys, glob, os, re

def main(dirname):

	print ("\tLancement de l'analyse")

	files=glob.glob(dirname+'*.txt')
	print ("\tOuverture des fichiers ")

	
	for file in files :
		path=os.path.dirname(file)
		ent_file= re.sub(r'.txt', r'.ent2', os.path.basename(file))
		end_file=path+'/'+ent_file
		print(end_file)
		with open(end_file, 'w') as f_out :
			list_name=cat_name(file)
			for elem in list_name: 
				fin_name='ID\tBacteria\telem'
				f_out.write(fin_name)
			#print (list_name)


	print ("\tFin de l'analyse et fermeture des fichiers ")






if __name__ == '__main__':
	if len(sys.argv)<2 :
		print ("Precisez le dossier contenant vos fichiers")
	else:
		dirname = sys.argv[1]
		main(dirname)