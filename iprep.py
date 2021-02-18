#!/usr/bin/python
from __future__ import print_function
import sys,re
import xforceIBM
def webscraping():
	myXForcePrint4 = ''
	count = 0
	valid = 0
	invalid = 0
	header = 'IP, COUNTRY, RISK VALUE, CATEGORIES'
	if len(sys.argv) != 3:
		print('>>>>> Welcome to my iprep Tool <<<<<')
		print('     Usage: python iprep.py file-in file-out')
	else:
		filepath = sys.argv[1]
		writepath = sys.argv[2]
		print('>>>>> Welcome to iprep Tool <<<<<')
		print('>>>>> Shamefull made by copypasting fron stackexchange <<<<<')
		#if not os.path.isfile(filepath):
		#	print("Invalid or non existent file. Exiting...".format(filepath))
		#	sys.exit()
		with open(filepath) as fp:
			with open(writepath, "a") as fw:
				fw.writelines(header + '\n')
				for line in fp:
					count = count +1
				# regular expression for IP
					re_ip = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
					#print("Now checking " + line + " ...")
					#print("")
				# If the IP format is valid:
					if re_ip.match(line):
				# Call xforceIBM.py
						myXForcePrint4 = xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/ipr/" + line)
					#print ("")
						message = line.rstrip('\n') + ' , ' + ' , '.join(myXForcePrint4)
						print (message)
						fw.writelines(message + '\n')
						valid = valid + 1
					else:
						print('[!] IP invalid or malformed : ' + line)
						invalid = invalid + 1
		print('Processed ' + str(count) + '  address: \n valid: ' + str(valid) + '\n invalid: ' + str(invalid))
if __name__ == '__main__':
    webscraping()
