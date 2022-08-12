import os
import shutil
import time


username = input('Enter your username: ')

def groupFiles():
	os.chdir('/home/'+ username +'/Downloads')

	names = os.listdir()

	try:
		os.chdir('other')
		os.chdir('..')
	except:
		os.mkdir('other')

	try:
		os.chdir('images')
		os.chdir('..')
	except:
		os.mkdir('images')

	for name in names:
		fname, lname = os.path.splitext(name)

		if(name == 'other') or (name == 'images'):
			continue
		else:

			if (lname == '.png') or (lname == '.jpeg') or (lname == '.jpg') or (lname == '.webp'):
				os.replace('/home/'+ username +'/Downloads/'+ name , '/home/'+ username +'/Downloads/images/'+name)
				print('(+) moving '+ name + ' to '+ ' /home/'+ username +'/Downloads/images/'+name)
			else:
				os.replace('/home/'+ username +'/Downloads/'+ name , '/home/'+ username +'/Downloads/other/'+name)
				print('(+) moving '+ name + ' to '+ ' /home/'+ username +'/Downloads/other/'+name)
				#more if else statements can be added for more types of files


while True:
	groupFiles()
	time.sleep(2)
