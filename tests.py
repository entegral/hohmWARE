import resident_controller

rlist = resident_controller.residentsAtHome()

if len(rlist) == 1:
	print(i.name)
elif len(rlist) == 0:
	print("there are no residents yet")
else:
	for i in rlist:
		print (i.name/n)


