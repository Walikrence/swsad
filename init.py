import os


for i in range(1,12):
	command = "mkdir hw" + str(i)
	os.system(command)
	command = "mkdir hw" + str(i) + "/pic"
	os.system(command)
	command = "mkdir hw" + str(i) + "/css"
	os.system(command)
	command = "mkdir hw" + str(i) + "/js"
	os.system(command)
	command = "mkdir hw" + str(i) + "/pic"
	os.system(command)
	command = "touch hw" + str(i) + "/hw" + str(i) +".html"
	os.system(command)
	pass