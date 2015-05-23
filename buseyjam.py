from json import loads
from sys import version_info
import time
import re

if version_info[0] != 2:
	exit("Python 2.7.9 or less than Py3k recommended.")

rounds = 1000
current_milli_time = lambda: int(round(time.time() * 1000))
fh = open('samples.json', 'r')
samples = loads(fh.read())
success_max = len(samples)*rounds

def regex_method(message):
	results = re_compiled.search(message)
	if results:
		return 1
	return 0
def default_method(message):
	message = message.lower()
	new_message = ''
	last_char = ''
	for i in message:
		if i != last_char:
			new_message += i
			last_char = i
	if new_message.find("busey") > -1:
		return 1
	return 0
def busey_bank_method(message):
	message = message.lower()
	words = message.split(' ')
	for word in words:
		new_word = ''
		last_char = ''
		for char in word:
			if char != last_char:
				new_word += char
				last_char = char
		if new_word.find('busey') > -1:
			return 1
	return 0

# Define a function here that takes an unfiltered message
# Call return 1 when your function finds busey
# Always return 0 for the fail condition

# Stage any variables you need below this line
re_compiled = re.compile('b+u+s+e+y+', re.I)

# Append your function's name to this list for it to be tested
# Times will be printed as each function finishes running
methods = ['regex_method', 'busey_bank_method', 'default_method']

for method in methods:
	results = 0
	start = current_milli_time()
	for i in range(rounds):
		for sample in samples:
			results += locals()[method](sample)
	end = current_milli_time()
	total = (end - start)
	print 'Time taken for %s: %d milliseconds. Success rate: %d%%' % (method, total, (results/success_max)*100)