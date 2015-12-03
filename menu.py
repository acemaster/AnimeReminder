import updatelist as u
import os

while (1):
	if(os.path.exists('AnimeList.txt') == False):
		print "List not found....Creating anime list: "
		u.update_list()

	print "1. Update List"
	print '2. Add Animes to checklist'
	print '3.Exit'
	i=raw_input("Enter the text: ")
	if i == '1':
		u.update_list()
	if i == '2':
		u.getAlist()
	if i == '3':
		exit()


