from PIL import Image
import  sys, pyscr
from pytesseract import image_to_string

shell = pyscr.terminal()

# read in a png type image and convert to text
def to_text(img_path=''):
	try:
		img = Image.open("./images/" + img_path)
		img.load()
	except:
		return

	save_to_file(img, img_path)

# convert a pdf file to text
def to_pdf(pdf):
	open("output.txt", "r+")
	shell.execute("pdf2txt.py -O ./ -o ./output.txt -t text ./PDFs/" + pdf)

# save text output to text file
def save_to_file(img, file_name):
	f = open("output.txt", "r+")
	f.write(image_to_string(img))
	f.close()

if __name__ == "__main__":
	if sys.argv[1] == "-u":
		to_pdf(sys.argv[2])
	else:
		to_text(sys.argv[1])
