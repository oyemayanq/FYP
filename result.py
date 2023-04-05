from os import system

def fun(inp):
	#data = [(  'actions','produce',   'sequences of environment states'  ),(  'Humans',   'have',   'desires and preferences of their own'  ),(  'environment states',   'are' ,   'desirable from their point of view'  ),(  'the notion of rationality as applied to humans',   'to do' ,   'with their success in choosing actions'  )]
	#print(data)
	model_path = '../acl/tanl-06w_'
	system('cd ' + model_path)
	#write inp to input.txt
	system('echo ' + inp + ' > input.txt')
	model_addr = 'deploy.py'
	conv_addr = 'tanl_to_carb.py'
	system('conda activate t5')
	system('python ' + model_addr)
	system('python ' + conv_addr + '--input=temp_deploy.tsv --output=output.tsv')
	#read output.tsv
	opfile = open('output.tsv', 'r')
	data = opfile.readline()
	#return data

fun()