import string
import random
from tkinter import *
from tkinter import messagebox
import re

class GUI():
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        #self.checkpassword = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_checkpassword = StringVar()
        self.n_passwordlen = IntVar()
        
        root.title('Password Generator')
        root.geometry('700x800')
        #root.resizable(False, False)

        self.label = Label(text="Password Generator", anchor=N, fg='darkblue', font='arial 20 bold underline')
        self.label.grid(row=0, column=1)

        self.blank_label1 = Label(text="")
        self.blank_label1.grid(row=1, column=0, columnspan=2)
        
        self.blank_label2 = Label(text="")
        self.blank_label2.grid(row=2, column=0, columnspan=2)    

        self.blank_label2 = Label(text="")
        self.blank_label2.grid(row=3, column=0, columnspan=2)    

        self.blank_label3 = Label(text="")
        self.blank_label3.grid(row=5, column=0)

        self.length = Label(text="Enter password length: ", font='times 15')
        self.length.grid(row=6, column=0)

        self.length_textfield = Entry(textvariable=self.n_passwordlen, font='times 15', bd=6, relief='ridge')
        self.length_textfield.grid(row=6, column=1)

        
        self.blank_label4 = Label(text="")
        self.blank_label4.grid(row=9, column=0)
 
        self.generated_password = Label(text="Generated password: ", font='times 15')
        self.generated_password.grid(row=10, column=0)

        self.generated_password_textfield = Entry(textvariable=self.n_generatedpassword, font='times 15', bd=6, relief='ridge', fg='darkgreen')
        self.generated_password_textfield.grid(row=10, column=1)
   
        self.blank_label5 = Label(text="")
        self.blank_label5.grid(row=11, column=0)

        self.blank_label6 = Label(text="")
        self.blank_label6.grid(row=12, column=0)

        self.generate = Button(text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1, font='forte 15 bold', fg='white', bg='darkblue', command=self.generate_pass)
        self.generate.grid(row=13, column=1)

        self.blank_label5 = Label(text="")
        self.blank_label5.grid(row=14, column=0)

        self.blank_label1 = Label(text="")
        self.blank_label1.grid(row=16, column=1)

        self.length1 = Label(text="Enter password to check: ", font='times 15')
        self.length1.grid(row=17, column=0)

        self.length1_textfield = Entry(textvariable=self.n_checkpassword, font='times 15', bd=6, relief='ridge')
        self.length1_textfield.grid(row=17, column=1)

        self.blank_label1 = Label(text="")
        self.blank_label1.grid(row=22, column=1)
        
        self.blank_label6 = Label(text="")
        self.blank_label6.grid(row=23, column=0)
        
        self.generate = Button(text="CHECK", bd=3, relief='solid', padx=1, pady=1, font='forte 15 bold', fg='white', bg='darkblue', command=self.checkpassword)
        self.generate.grid(row=24, column=1)

        
        self.blank_label6 = Label(text="")
        self.blank_label6.grid(row=25, column=0)

        self.reset = Button(text="RESET", bd=3, relief='solid', padx=1, pady=1, font='forte 15', fg='darkblue', bg='white', command=self.reset_fields)
        self.reset.grid(row=26, column=1)


    def generate_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        numbers = "1234567890"
        upper = list(upper)
        lower = list(lower)
        chars = list(chars)
        numbers = list(numbers)
        leng = self.length_textfield.get()
        length = int(leng) 
        if length<6:
            messagebox.showerror("Error", "Password must be atleast 6 characters long")
            self.textfield.configure(text="")
            return
        else:
            self.blank_label1.configure(text="")

        self.generated_password_textfield.delete(0, length)

        u = random.randint(1, length-3)
        l = random.randint(1, length-2-u)
        c = random.randint(1, length-1-u-l)
        n = length-u-l-c

        password = random.sample(upper, u)+random.sample(lower, l)+random.sample(chars, c)+random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        n_generatedpassword = self.generated_password_textfield.insert(0, gen_passwd)

    
    def accept_fields(self):
        messagebox.showinfo("Success!", "Password generated successfully")

    def checkpassword(self):
        l, u, p, d = 0, 0, 0, 0
        s=self.length1_textfield.get()
        if(len(s)==0):
            messagebox.showerror("Error","Name cannot be empty")
            
        else:
            if (len(s) >= 8):
                for i in s:
     
            # counting lowercase alphabets
                    if (i.islower()):
                        l+=1           
     
            # counting uppercase alphabets
                    if (i.isupper()):
                        u+=1           
     
            # counting digits
                    if (i.isdigit()):
                        d+=1           
     
            # counting the mentioned special characters
                    if(i=='@'or i=='$' or i=='_'):
                        p+=1          
        
            if (l>=1 and u>=1 and p>=1 and d>=1):
                r='GOOD'
            elif(l>=1 and u>=1):
                r='MODERATE'
            else:
                r='POOR'
            messagebox.showinfo("Strength of password!", f'Password entered is {r}')

    def reset_fields(self):
        self.length_textfield.delete(0, 25)
        self.length1_textfield.delete(0, 25)
        self.generated_password_textfield.delete(0, 25)


if __name__=='__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
