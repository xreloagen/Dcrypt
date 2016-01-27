# -*- coding: utf-8 -*-
import os
import platform
import sys
import random
from string import printable, digits, ascii_letters
from getpass import getuser
if sys.version_info[0] == 3:
	print("Oops, Python 3 isn't supported yet")
	exit()
try:
	import Tkinter as tk
	import tkFileDialog
except:
	try:
		import tkinter as tk
	except:
		if platform.system() == "Linux":
			print("Tkinter isn't installed")
			choice = raw_input("Would you like to install Tkinter [Y/N]?").lower()
			if choice == "y":
				list = []
				file = open("/etc/os-release", "r")
				a = file.read().replace("\n", "=")
				list = a.split("=")
				if list[1].replace('"', "").lower()[0:4] == "arch":
					os.system("sudo pacman -S tk")
				else:
					os.system("sudo apt-get install python-tk")
				os.system("python " + sys.argv[0])
		
			if choice == "n":
				print("Oops, Tkinter is a major module, we're forced to close the program")
				exit()
		else:
			print("Please install Tkinter.")

if platform.system() == "Linux":
	path = "/home/" + getuser() + "/dcrypt"

if platform.system() == "Windows":
	path = os.environ["appdata"] + "\\dcrypt"

if os.path.isdir(path) == False:
	algo = []
	name = ""
	filename = ""
	for i in digits:
		algo.append(i)

	for i in ascii_letters:
		algo.append(i)
	
	os.system("mkdir " + path)
	for i in range(4):
		name += random.choice(ascii_letters)

	for i in range(4):
		name += random.choice(digits)

	name += ".dcrt"
	if platform.system() == "Linux":
		filename = path + "/" + name
	if platform.system() == "Windows":
		filename = path + "\\" + name

	file = open(filename, "w")
	for i in range(len(printable)):
		file.write(random.choice(algo) + random.choice(algo))
		if i != len(printable) - 1:
			file.write("_")
	file.close()


class main(tk.Tk):

	def crypt(self):
		cryptt = ""
		try:
			file = open(self.filename.get(), "r")
		except:
			print("You don't select a dcrypt file")
			return False

		crypt = file.read().split("_")
		inputt = self.decrypt.get()
		for i in inputt:
			c = printable.index(i)
			cryptt += crypt[c]

		self.encrypt.set(cryptt)
		self.decrypt.set("")

	def encrypts(self):
		encryptt = ""
		try:
			file = open(self.filename.get(), "r")
		except:
			print("You don't select a dcrypt file")
			return False

		crypt = file.read().split("_")
		inputt = self.encrypt.get()
		a = 0
		c = 0
		for i in range(len(inputt) / 2):
			c = a
			a += 2
			v = crypt.index(inputt[c:a])
			encryptt += printable[v]
		self.decrypt.set(encryptt)
		self.encrypt.set("")

	def listname(self):
		self.filepath = tkFileDialog.askopenfilename(title="Ouvrir un fichier", filetypes = [("Dcrypt File", ".dcrt")])
		self.filename.set(self.filepath)

	def create(self):
		self.algo = []
		self.name = ""
		self.filename = ""
		for i in digits:
			self.algo.append(i)

		for i in ascii_letters:
			self.algo.append(i)
		if platform.system() == "Linux":
			self.path = "/home/" + getuser() + "/dcrypt"

		if platform.system() == "Windows":
			self.path = os.environ["appdata"] + "\\dcrypt"
		for i in range(4):
			self.name += random.choice(ascii_letters)
			
		for i in range(4):
			self.name += random.choice(digits)


		self.name += ".dcrt"
		if platform.system() == "Linux":
			self.filename = path + "/" + self.name
		if platform.system() == "Windows":
			self.filename = path + "\\" + self.name
		print(self.filename)
		self.file = open(self.filename, "w")
		for i in range(len(printable)):
			self.file.write(random.choice(self.algo) + random.choice(self.algo))
			if i != len(printable) - 1:
				self.file.write("_")
		self.file.close()


	def __init__(self):
		if platform.system() == "Linux":
			os.system("clear")
		if platform.system() == "Windows":
			os.system("cls")

		tk.Tk.__init__(self)
		self.title("XRELOAGEN Dcrypt")
		self.filename = tk.StringVar()
		self.decrypt = tk.StringVar()
		self.encrypt = tk.StringVar()
		tk.Button(self,text="Encrypt", padx=20, command=self.crypt).pack(padx=5,pady=5)
		tk.Button(self,text="Decrypt", padx=20, command=self.encrypts).pack(padx=5,pady=5)
		tk.Button(self, text="Browse File", command=self.listname).pack(padx=5,pady=5)
		tk.Button(self, text="Create List", command=self.create).pack(padx=5,pady=5)
		tk.Label(self, textvariable=self.filename).pack()
		tk.Entry(self,width=40, textvariable=self.encrypt).pack(side='bottom', pady=20)
		tk.Entry(self,width=40, textvariable=self.decrypt).pack(side='bottom')


app = main()
app.mainloop()
