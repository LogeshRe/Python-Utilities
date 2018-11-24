
from tkinter.filedialog import askdirectory
from tkinter.filedialog import asksaveasfile
from os import listdir


def openfile():
	folder = askdirectory()
	return(folder)

def filesave(files = [] , *args):
	filetypes = [("All Files","*"),("Text",".txt")]
	f = asksaveasfile(mode = 'w', defaultextension=".txt",filetypes = filetypes)
	if f is None:
		return
	else:
		for name in files:
			f.write(name + '\n')
	f.close

def main():
	filepath = openfile()
	filelist = listdir(filepath)
	filesave(filelist)

if __name__ == "__main__" :
	main()


