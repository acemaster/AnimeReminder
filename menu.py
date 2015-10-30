import updatelist as u

while (1):
	print "1. Update List"
	print '2. Add Animes to checklist'
	print '3.Exit'
	i=raw_input("Enter the text: ")
	if i == '1':
		u.update_list()
	if i == '2':
		u.getAlist(1)
	if i == '3':
		exit()


