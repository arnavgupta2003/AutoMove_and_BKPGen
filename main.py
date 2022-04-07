import os
import shutil

# path
path = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder'

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
print("Before moving file:")
print(os.listdir(path))

for filename in os.listdir(path):
	# Source path
	source = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder/'+str(filename)

	# Destination path
	destination = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/dest_folder'

	# Move the content of
	# source to destination
	dest = shutil.move(source, destination)
	print("File:"+filename+"moved")