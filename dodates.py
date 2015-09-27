from PIL import Image
import  sys, pyscr
import time, re
import subprocess
from pytesseract import image_to_string

shell = pyscr.terminal()

# read in a png type image and convert to text
def to_text(img_path=''):
	try:
		img = Image.open("./images/" + img_path)
		img.load()
	except:
		return

	parser(image_to_string(img))

# convert a pdf file to text
def to_pdf(pdf):
	proc = subprocess.Popen('echo "to stdout"', shell=True, stdout=subprocess.PIPE, )
	output = proc.communicate()[0]
	parser(output)

def parser(subject):

	for match in re.finditer(
	    r"""(?ix)             # case-insensitive, verbose regex
	    \b                    # match a word boundary
	    (?:                   # match the following three times:
	     (?:                  # either
	      \d+                 # a number,
	      (?:\.|st|nd|rd|th)* # followed by a dot, st, nd, rd, or th (optional)
	      |                   # or a month name
	      (?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)
	      |					  # or full month name
	      (?:(?:January|Febuary|March|April|May|June|July|August|September|October|November|December)[a-z]*)
	     )
	     [\s./-]*             # followed by a date separator or whitespace (optional)
	    ){3}                  # do this three times
	    \b""",                # and end at a word boundary. 
	    subject):
		match.start()
		match.end()
		print match.group()

if __name__ == "__main__":
	if sys.argv[1] == "-u":
		to_pdf(sys.argv[2])
	else:
		to_text(sys.argv[1])
