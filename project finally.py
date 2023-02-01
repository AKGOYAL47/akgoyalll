#use virtual studio code 
from tkinter import*
from datetime import date

root = Tk()
root.geometry("3000x3000")
entry = Entry(root)
entry.pack()

def age():
   pass


my_label= Label(root,text="Please Enter Your Date Of Birth in above box", font=("Lucida",20))
my_label.pack(pady=20)
X_label= Label(root,text="input your date in format- DD/MM/YYYY ", font=("Lucida",15))
X_label.pack(pady=5)


def calculator():
   global result
   result = str(entry.get())
   today = date.today()
   dob_data = result.split("/")
   date1 = int(dob_data[0])
   month = int(dob_data[1])
   year = int(dob_data[2])
   dob = date(year,month,date1)
   numberOfDays = (today - dob).days
   age = numberOfDays // 365
   
   label=Label(root, text="Your age is " +str(age))
   label.pack()
   
   if age>18:
      a_label=Label(root, text="You have a  vote and can contest elections too")
      b_label=Label(root, text="You are already eligible  for voter  card, driving license, and  open a bank acoount too." )
      c_label=Label(root, text="You have all of above as your identity proof" )
      a_label.pack()
      b_label.pack()
      c_label.pack()
   elif age==18 :
      d_label=Label(root, text="You are now eligible to vote" )
      e_label=Label(root, text="You can apply for voter  card, driving license, and can open a bank acoount too." )
      f_label=Label(root, text="You can have all of above as your identity proof" ) 
      d_label.pack()
      e_label.pack()
      f_label.pack()
   elif  age==0 :
      j_label=Label(root, text="You are born today " )
      k_label=Label(root, text="You have to wait untill u reach age 18" )
      l_label=Label(root, text="You can have birth certificate as your identity proof" ) 
      j_label.pack()
      k_label.pack()
      l_label.pack()
   elif  age<=18 and age>=0 :
      g_label=Label(root, text="You are not eligible for voting " )
      h_label=Label(root, text="You have to wait untill u reach age 18" )
      i_label=Label(root, text="You can have birth certificate and adhaar card as your identity proof" ) 
      g_label.pack()
      h_label.pack()
      i_label.pack()
   
   elif  age<=0 :
      j_label=Label(root, text="You have input wrong date " )
      j_label.pack()
     
  




button = Button(root, text="Click here ", command=calculator)                                                        
button.pack(pady=10)
root.mainloop()