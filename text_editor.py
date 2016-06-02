#coding=utf-8 
import sys,os,tkFileDialog
from Tkinter import *
import re
#by xtstc
class Editor(object):
	"""docstring for Editor"""
	def __init__(self):
		self.tk = Tk()
		# 设置窗口初始化大小
		self.tk.geometry('960x540')
		#建立主UI界面
		self.createUI()
		# 绑定快捷键
		self.bind_key()
		# 进入主循环
		self.tk.mainloop()
	
	def createUI(self):
		#设置程序的标题
		self.tk.title("XtStC Text Enditor")
		
		#主菜单栏
		menubar = Menu(self.tk)

		#主菜单栏的选项卡
		fmenu = Menu (menubar,tearoff = 0)
		Emenu = Menu(menubar ,tearoff = 0)
		
		# File选项
		# fmenu.add_command()函数，lable代表选项卡的名字，accelerator代表提示快捷键(但是要具体绑定键盘),command 代表点击该选项卡调用的函数
		fmenu.add_command(label = 'Open',accelerator='Command+O',command = self.open)
		fmenu.add_command(label = 'Save',accelerator = 'Command+S',command = self.save)
		fmenu.add_command(label = 'Exit',accelerator ='Command+Q',command = self.exit)
		menubar.add_cascade(label = "File",menu = fmenu)
		
		# Edit选项
		# 同上述fmenu
		Emenu.add_command(label = 'Select All',accelerator = 'Command+A',command = self.select_all)
		Emenu.add_command(label = 'Format',accelerator = 'Command+F',command = self.format)
		Emenu.add_command(label = 'Statics',command = self.Statics)
		Emenu.add_command(label = 'Find & Replace')
		Emenu.add_command(label = 'Sort')
		menubar.add_cascade(label = "Edit",menu = Emenu)
		
		#加入文本框，并让其与滚动条绑定
		self.tk.config(menu = menubar)
		#设置文本框背景颜色是‘black’,字的颜色是'white',光标的颜色是'white'
		self.text = Text(bg = 'black' , fg = 'white',insertbackground = 'white')
		#self.text.grid(sticky = N+E+S+W)
		
		#设置滚动条让其可以随文本框滚动，也可以控制文本框滚动
		self.scorollbar = Scrollbar(self.text)
		self.scorollbar.pack(side = RIGHT,fill = Y)
		self.text["yscrollcommand"] = self.scorollbar.set
		self.scorollbar.config(command = self.text.yview)
		
		#(expand = YES,fill = BOTH),pack的这个参数，让文本框可以随窗口大小变化
		self.text.pack(expand = YES,fill = BOTH)
	
	#类的成员函数
	#
	#绑定键盘到tk，实现快捷键功能
	def bind_key(self):
		self.tk.bind('<Command-o>',self.open)
		self.tk.bind('<Command-s>',self.save)
		self.tk.bind('<Command-f>',self.format)
		self.tk.bind('<Command-a>',self.select_all)
	#File菜单的函数
	def save(self,event = None):
		txtContent = self.text.get(1.0,END)
		self.SaveFile(content = txtContent)
	def open(self,event = None):
		self.filename = tkFileDialog.askopenfilename(initialdir  = os.getcwd())
		fileContent = self.OpenFile(fname = self.filename)
		if fileContent is not -1:
			self.text.delete(1.0,END)
			self.text.insert(1.0,fileContent)
	
	#Edit菜单的函数
	def format(self,event = None):
		FormatContent = self.text.get(1.0,END)
		result = ' '.join(FormatContent.split())
		self.text.delete(1.0,END)
		self.text.insert(1.0,result)
	def select_all(self ,event = None):
		self.text.tag_add(SEL,'1.0',END+'-1c')
		#下面这两句我也不知道要什么。。。注释掉，这个函数暂时没发现问题
		#self.text.mark_set(INSERT,'1.0')
		#self.text.see(INSERT)
		
	#open函数的细节函数
	def OpenFile(self,fname = None):
		if fname is None:
			return -1
		self.fname = fname
		file = open(fname,'r+')
		content = file.read()
		file.close()
		return content
	#save函数的细节函数
	def SaveFile(self,content = None):
		if content is None:
			return -1
		file = open(self.fname,'w')
		file.write(content)
		file.flush()
		file.close()
		return 0
	def Statics(self):
		StaticsContent = self.text.get(1.0,END)
		StaticsContent = StaticsContent.lower()
		StaticsContent = re.sub("\"|,|\.","",StaticsContent)
		result = {}
		for word in StaticsContent.split():
			if word not in result:
				result[word] = 0
			result[word] += 1
		#print result 
		return result


	def exit(self):
		os._exit(0)
if  __name__ == '__main__':
	Editor()
