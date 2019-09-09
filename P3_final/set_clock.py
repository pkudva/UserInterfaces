__author__ = 'kudva'

# From http://www.ferg.org/thinking_in_tkinter/tt070_py.txt
# Adapted by A. Hornof 2017

#Edited by Priya Kudva 11/1/17

from tkinter import *
import sound

class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		#create fullscreen window
		self.myContainer1 = root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
															   root.winfo_screenheight()))

		self.myParent.bind("j", self.button1Click)  # ajh
		self.myParent.bind("k", self.button2Click)  # ajh
		self.myParent.bind("<space>", self.button3Click)

		#Clickable button to move pointer left
		self.button1 = Button(self.myContainer1)
		# The background colors appear in Windows but not on a Macintosh.
		self.button1.configure(text="Left (j)", font=('Helvetica', 36) ,  background= "red", justify=LEFT)
		self.button1.place(rely=1.0, relx=0.0, x=0, y=0, anchor=SW)
		self.button1.bind("<Button-1>", self.button1Click) #allow button to be clicked
		self.button1.bind("j", self.button1Click)  #allow <j> to have same function

		#Clickable button to move pointer right
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right (k)", font=('Helvetica', 36), background="red", justify=RIGHT)
		self.button2.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
		self.button2.bind("<Button-1>", self.button2Click)
		self.button2.bind("k", self.button2Click)  #allow <k> to have same function

		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Select (space)", font=('Helvetica', 36), background="green", justify=CENTER)
		self.button3.place(rely=1.0, relx=0.5, x=0, y=0, anchor=S)
		self.button3.bind("<Button-1>", self.button3Click)
		self.button3.bind("<space>", self.button3Click) #allow <space> to have same function

		#function for arrow initialization to allow for startup delay through .after function
		def arrow_init():
			self.arrow = PhotoImage(file="arrow.pgm")
			self.arrowImage = Label(root, image=self.arrow)
			self.arrowXPosition = 0
			self.arrowYPosition = 20
			self.arrowImage.place(x=self.arrowXPosition, y=self.arrowYPosition)
			sound.Play("wav_files_provided/miscellaneous_f/Set_day_f.wav") #initial selection

		self.menu = ['Set Day', 'Set Hour', 'Set Minute', 'Exit Program']
		self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		self.hours = ['00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
					  '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
		self.minutes = ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45',  '50', '55']

		#creation of labels

		self.menuLabels = []
		self.menuX = 0
		for i in range(4):
			label4 = Label(root, text=self.menu[i])
			label4.place(x=100 * i, y=0) #.place() needed for horizontal alignment
			self.menuLabels.append(label4)

		self.dayLabels = []
		self.day = 0
		for i in range(7):
			label = Label(root, text=self.days[i])
			label.place(x=80 * i, y=60)
			self.dayLabels.append(label)

		self.hourLabels = []
		self.hour = 0
		for i in range(24):
			label1 = Label(root, text=self.hours[i])
			label1.place(x = 23*i, y = 120)
			self.hourLabels.append(label1)

		self.minuteLabels = []
		self.minute = 0
		for i in range(12):
			label2 = Label(root, text=self.minutes[i])
			label2.place(x=23 * i, y=180)
			self.minuteLabels.append(label2)

		#Starting program, play intro and wait to initialize arrow capabilities
		sound.Play("wav_files_provided/miscellaneous_f/Set_date_and_time_f.wav")
		self.myParent.after(3000, lambda: arrow_init())

	#Left button/key press
	def button1Click(self, event=None):
		print("j")
		if self.arrowYPosition == 80: #day list
			self.arrowXPosition = self.arrowXPosition - 80
			self.day = self.day - 1
			if self.arrowXPosition < 0: #off the window, correct position
				self.arrowXPosition = 480
				self.day = 6

		elif self.arrowYPosition == 140: #hour list
			self.arrowXPosition = self.arrowXPosition - 23
			self.hour = self.hour - 1
			if self.arrowXPosition < 0: #off the window, correct position
				self.arrowXPosition = 529
				self.hour = 23

		elif self.arrowYPosition == 200: #minute list
			self.arrowXPosition = self.arrowXPosition - 23
			self.minute = self.minute - 1
			if self.arrowXPosition < 0: #off the window, correct position
				self.arrowXPosition = 253
				self.minute = 11

		else: #menu list
			self.arrowXPosition = self.arrowXPosition - 100
			self.menuX -= 1
			if self.arrowXPosition < 0: #off the window, correct position
				self.arrowXPosition = 300
				self.menuX = 3

		self.arrowImage.place(x=self.arrowXPosition, y=self.arrowYPosition)
		report_event(self, event)        ### (3)

	#Right button/key press
	def button2Click(self, event=None):
		print("k")
		if self.arrowYPosition == 80: #day list
			self.arrowXPosition = self.arrowXPosition + 80
			self.day = self.day + 1
			if self.arrowXPosition > 480: #off the list, correct position
				self.arrowXPosition = 0
				self.day = 0

		elif self.arrowYPosition == 140:
			self.arrowXPosition = self.arrowXPosition + 23
			self.hour = self.hour + 1
			if self.arrowXPosition > 529: #off the list, correct position
				self.arrowXPosition = 0
				self.hour = 0

		elif self.arrowYPosition == 200:
			self.arrowXPosition = self.arrowXPosition + 23
			self.minute = self.minute + 1
			if self.arrowXPosition > 253: #off the list, correct position
				self.arrowXPosition = 0
				self.minute = 0

		else:
			self.arrowXPosition = self.arrowXPosition + 100
			self.menuX += 1
			if self.arrowXPosition > 300: #off the list, correct position
				self.arrowXPosition = self.arrowXPosition - 100
				self.menuX -= 1

		self.arrowImage.place(x=self.arrowXPosition, y=self.arrowYPosition)
		report_event(self, event)   ### (4)

	#Select button/key press
	def button3Click(self, event=None):
		print("space")
		if self.arrowYPosition == 20: #menu list
			if self.arrowXPosition == 0: #days
				self.arrowXPosition = 0
				self.arrowYPosition = self.arrowYPosition + 60 #move to day list
			elif self.arrowXPosition == 100: #hours
				self.arrowXPosition = 0
				self.arrowYPosition = self.arrowYPosition + 120 #move to hour list

			elif self.arrowXPosition == 200: #minutes
				self.arrowXPosition = 0
				self.arrowYPosition = self.arrowYPosition + 180 #move to minute list

			elif self.arrowXPosition == 300: #exit
				#close program
				sound.Play("wav_files_provided/miscellaneous_f/Exiting_program_f.wav")
				#delay before closing window
				self.myParent.after(1090, lambda: self.myParent.destroy())

			self.menuLabels[self.menuX].config(bg="red") #menu selection is red while chosing from other lists

		else: #selecting from one of the lists

			if self.arrowYPosition == 80: #days
				for i in range(7):
					self.dayLabels[i].config(bg="white") #if a selection was previously made, change it
				self.dayLabels[self.day].config(bg="blue") #highlight selection
				self.day = 0 #reinitialize counter
			elif self.arrowYPosition == 140:
				for i in range(24):
					self.hourLabels[i].config(bg="white")
				self.hourLabels[self.hour].config(bg="blue")
				self.hour = 0
			else:
				for i in range(12):
					self.minuteLabels[i].config(bg="white")
				self.minuteLabels[self.minute].config(bg="blue")
				self.minute = 0

			#move back to menu list after selection
			self.arrowXPosition = 0
			self.arrowYPosition = 20
			self.menuX = 0
			for i in range(4):
				self.menuLabels[i].config(bg="white") #clear highlight

		self.arrowImage.place(x=self.arrowXPosition, y=self.arrowYPosition)
		report_event(self, event)  ### (4)

def report_event(self, event):     ### (5)
	if self.arrowYPosition == 20: #menu list sounds
		if self.arrowXPosition == 0:
			sound.Play("wav_files_provided/miscellaneous_f/Set_day_f.wav")
		elif self.arrowXPosition == 100:
			sound.Play("wav_files_provided/miscellaneous_f/Set_hour_f.wav")
		elif self.arrowXPosition == 200:
			sound.Play("wav_files_provided/miscellaneous_f/Set_minute_f.wav")
		else:
			sound.Play("wav_files_provided/miscellaneous_f/Exit_program_f.wav")
	elif self.arrowYPosition == 80: #day audio
		sound.Play("wav_files_provided/days_of_week_f/" + self.days[self.day] + "_f.wav")
	elif self.arrowYPosition == 140: #hour audio
		sound.Play("wav_files_provided/numbers_f/" + self.hours[self.hour] + "_f.wav")
	else: #minute audio
		sound.Play("wav_files_provided/numbers_f/" + self.minutes[self.minute] + "_f.wav")


root = Tk()
myapp = MyApp(root)
root.mainloop()