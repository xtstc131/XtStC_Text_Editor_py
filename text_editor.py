#coding=utf-8 
import sys,os,tkFileDialog
from Tkinter import *

#by xtstc
class Editor(object):
	"""docstring for Editor"""
	def __init__(self):
		self.tk = Tk()

		self.createUI()
		self.tk.mainloop()
	def createUI(self):
		self.tk.title("XtStC Text Enditor")
		menubar = Menu(self.tk)
		fmenu = Menu (menubar,tearoff = 0)
		Emenu = Menu(menubar ,tearoff = 0)
		#File选项
		fmenu.add_command(label = 'Open',command = self.open)
		fmenu.add_command(label = 'Save',command = self.save)
		fmenu.add_command(label = 'Exit',command = self.exit)
		menubar.add_cascade(label = "File",menu = fmenu)
		#Edit选项
		Emenu.add_command(label = 'Format')
		Emenu.add_command(label = 'Statics')
		Emenu.add_command(label = 'Find & Replace')
		Emenu.add_command(label = 'Sort')
		menubar.add_cascade(label = "Edit",menu = Emenu)
		
		self.tk.config(menu = menubar)
		self.text = Text(bg = 'black' , fg = 'white')
		#self.text.grid(sticky = N+E+S+W)
		#self.scorollbar = Scrollbar(self.text)
		#self.scorollbar.pack(side = RIGHT,fill = Y)
		#self.scorollbar.config(command = self.text.yview)
		#self.text.config(yscrollcommand=self.scorollbar.set)
		self.text.pack(expand = YES,fill = BOTH)
		
	def save(self):
		txtContent = self.text.get(1.0,END)
		self.SaveFile(content = txtContent)
	def open(self):
		self.filename = tkFileDialog.askopenfilename(initialdir  = os.getcwd())
		fileContent = self.OpenFile(fname = self.filename)
		if fileContent is not -1:
			self.text.delete(1.0,END)
			self.text.insert(1.0,fileContent)


	def OpenFile(self,fname = None):
		if fname is None:
			return -1
		self.fname = fname
		file = open(fname,'r+')
		content = file.read()
		file.close()
		return content
	def SaveFile(self,content = None):
		if content is None:
			return -1
		file = open(self.fname,'w')
		file.write(content)
		file.flush()
		file.close()
		return 0
	def exit():
		os._exit(0)
if  __name__ == '__main__':
	Editor()
