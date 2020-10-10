from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
import xlsxwriter
import xlrd

frm = Tk()

# Variables

fnt   = 'Impact 30 bold'
bg    = 'yellow'
bgtxt = 'yellow'
fg    = 'red'
fw    = 900
fh    = 750
x     = ( frm.winfo_screenwidth() - fw ) / 2
y     = ( frm.winfo_screenheight() - fh ) / 2 - 50
pad   = 10


frm.geometry('%dx%d+%d+%d' % (fw,fh,x,y))
frm.title('Employee File Data')
frm.config(bg = bg)
frm.resizable(False,False)



Label(frm, text='Employee Data', bg='lightgrey', fg='black', font=fnt).pack(pady=pad)
frame = Frame(frm, bg=bg)
frame.pack(pady=pad)

Label(frame, text='Code:',bg=bg, fg=fg, font=fnt).grid(row=0, column=0)
Label(frame,text='Name:', bg=bg, fg=fg, font=fnt).grid(row=1, column=0)
Label(frame,text='Address:', bg=bg, fg=fg, font=fnt).grid(row=2, column=0)
Label(frame,text='Salary:', bg=bg, fg=fg, font=fnt).grid(row=3, column=0)


# Salary digits Validation

def num_only(text):
	if str.isdigit(text):
		return True
	elif text is'':
		return True
	else: 
		return False

reg_digits = frm.register(num_only)


# Vars.

svcode = StringVar()
svname = StringVar()
svaddress = StringVar()
svSalary = StringVar()
textcode = ttk.Entry(frame, font=fnt, textvariable=svcode)
textcode.focus()
textname = ttk.Entry(frame,font=fnt, textvariable=svname)
textaddress = ttk.Entry(frame, font=fnt, textvariable=svaddress)
textSalary = ttk.Entry(frame, font=fnt, textvariable=svSalary,validate='key', validatecommand=(reg_digits,'%P'))

textcode.grid(row=0, column=1, pady=pad)
textname.grid(row=1, column=1, pady=pad)
textaddress.grid(row=2,column=1, pady=pad)
textSalary.grid(row=3, column=1, pady=pad)


btn_style = ttk.Style()
btn_style.configure('TButton',font=fnt, pady=pad, padding=pad)


def txtmaker():
	file_name = svcode.get() + '_' + svname.get() + '.txt'
	f = open('data/'+file_name, 'a')
	f.write('Code   : ' + svcode.get() + '\n')
	f.write('Name   : ' + svname.get() + '\n')
	f.write('Address: ' + svaddress.get() + '\n')
	f.write('Salary : ' + svSalary.get() + '\n')
	f.close()

def xlsxmaker():
	file_name = svcode.get() + '_' + svname.get() + '.xlsx'
	f = xlsxwriter.Workbook('data/'+file_name)
	out = f.add_worksheet()
	out.write('A1','Code   : ')
	out.write('A2','Name   : ')
	out.write('A3','Address: ')
	out.write('A4','Salary : ')

	out.write('B1',svcode.get())
	out.write('B2',svname.get())
	out.write('B3',svaddress.get())
	out.write('B4',svSalary.get())
	f.close()

	#fr = xlrd.open_workbook('Search_db/db.xlsx')
	#sheet = fr.sheet_by_index(0)
	#r = str(sheet.nrows+1)

	#with open('Search_db/db.xlsx', 'a') as db:
		#f = xlsxwriter.Workbook(db)
		#add = f.add_worksheet()
		##add.write("A"+r,'test')
		#f.close()




c1 = BooleanVar()
c2 = BooleanVar()
cb1 = Checkbutton(frm,text='text file',bg=bg, font='Arial 15 bold', variable=c1)
cb2 = Checkbutton(frm,text='Excel file',bg=bg, font='Arial 15 bold', variable=c2)
ext = Label(frm, text='Export to:',bg=bg, fg='darkblue', font='Arial 15 bold')
ext.pack(pady=5)
cb1.pack(pady=5)
cb2.pack()

def check():
	if svcode.get().strip() == '':
		messagebox.showinfo('Code is Empty !','Enter code')
		textcode.focus()
	elif svname.get().strip() == '':
		messagebox.showinfo('name field is Empty !','Enter name')
		textname.focus()
	elif svaddress.get().strip() == '':
		messagebox.showinfo('Address field is Empty !','Enter Address')
		textaddress.focus()
	elif svSalary.get().strip() == '':
		messagebox.showinfo('Salary field is Empty !','Enter Salary')
		textSalary.focus()
	else:	
		checkbox1 = c1.get()
		checkbox2 = c2.get()


		if checkbox1 & checkbox2 == True:
			xlsxmaker()
			txtmaker()
			messagebox.showinfo('Done !','Employee Files Created Successfully !')
			svcode.set('')
			svname.set('')
			svaddress.set('')
			svSalary.set('')
			textcode.focus()

		elif checkbox1 == True:
			txtmaker()
			svcode.set('')
			svname.set('')
			svaddress.set('')
			svSalary.set('')
			messagebox.showinfo('Done !','Employee Text File Created Successfully !')
			textcode.focus()

		elif checkbox2 == True:
			xlsxmaker()
			svcode.set('')
			svname.set('')
			svaddress.set('')
			svSalary.set('')
			messagebox.showinfo('Done !','Employee Excel File Created Successfully !')
			textcode.focus()

		else:
			messagebox.showinfo('Choose the Export file type','i.e you can choose them together')
			textSalary.focus()



ttk.Button(frm, text='Create Employee File', command=check).pack(pady=pad)
ttk.Button(frm, text='Exit Now', command=frm.destroy).pack(pady=pad)

frm.mainloop()
