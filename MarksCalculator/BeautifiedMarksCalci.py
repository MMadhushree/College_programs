'''IA  Score Predictor with a simple UI'''

from tkinter import*


def CIE():
   # global l1,l2,l3,l4,l5,ia1,ia2,ia3,ia4,ia5
   win2=Toplevel()
   win2.geometry('400x450')
   win2.configure(bg='#CEF4DE')

   global t1,t2,t3,t4,t5
   CIE_ins=Label(win2,text='Calculation of CIE Marks',fg='#1D8348').place(x=120,y=25)
   l1=Label(win2,text='Marks in IA-1*:',bg='#CEF4DE')
   l1.place(x=80,y=80)
   t1=Text(win2,height=1,width=10)
   t1.place(x=200,y=80)

   l2=Label(win2,text='Marks in IA-2*:',bg='#CEF4DE')
   l2.place(x=80,y=120)
   t2=Text(win2,height=1,width=10)
   t2.place(x=200,y=120)

   l3=Label(win2,text='Marks in IA-3*:',bg='#CEF4DE')
   l3.place(x=80,y=160)
   t3=Text(win2,height=1,width=10)
   t3.place(x=200,y=160)

   l4=Label(win2,text='Average Quiz score*:',bg='#CEF4DE')
   l4.place(y=200,x=80)
   t4=Text(win2,height=1,width=10)
   t4.place(x=200,y=200)

   l5=Label(win2,text='ABA marks*:',bg='#CEF4DE')
   l5.place(x=80,y=240)
   t5=Text(win2,height=1,width=10)
   t5.place(x=200,y=240)


   def cieLogic():
      
      ia1=int(t1.get('1.0',END))
      ia2=int(t2.get('1.0',END))
      ia3=int(t3.get('1.0',END))
      quiz=int(t4.get('1.0',END))
      aba=int(t5.get('1.0',END))
      total=((ia1+ia2+ia3)*0.4)+quiz+aba

      cieAns=Label(win2,text='Your average CIE score :',bg='#CEF4DE')
      cieAns.place(x=80,y=310)
      cieAnsDisp=Text(win2,height=1,width=10)
      cieAnsDisp.place(x=230,y=310)
      # Inserting the result in textbox and disbling it
      cieAnsDisp.insert(END,str(total))

   
   button_cal=Button(win2,text='Calculate',bg='white',padx=20,command=cieLogic)
   button_cal.place(x=150,y=280)

   
def Predict():
   win1=Toplevel()
   win1.configure(bg='#CEF4DE')
   win1.geometry('420x450')
   Predict_ins=Label(win1,text='Marks PREDICTOR for the given CIE marks',fg='#1D8348').place(x=70,y=25)
   # continue.........
   pl0=Label(win1,text='Target CIE marks*:',bg='#CEF4DE')
   pl0.place(x=80,y=80)
   pt0=Text(win1,height=1,width=10)
   pt0.place(x=200,y=80)

   pl1=Label(win1,text='Marks in IA-1*:',bg='#CEF4DE')
   pl1.place(x=80,y=130)
   pt1=Text(win1,height=1,width=10)
   pt1.place(x=200,y=130)

   pl2=Label(win1,text='Marks in IA-2:',bg='#CEF4DE')
   pl2.place(x=80,y=180)
   pt2=Text(win1,height=1,width=10)
   pt2.place(x=200,y=180)
   # pt2.insert(END,'Enter 0 if unknown')
   pl22=Label(win1,text='(Enter 0 if unknown)',bg='#CEF4DE',font=('helvetica',8))
   pl22.place(x=80,y=200)

   
   pl3=Label(win1,text='Quiz score*:',bg='#CEF4DE')
   pl3.place(x=80,y=230)
   pt3=Text(win1,height=1,width=10)
   pt3.place(x=200,y=230)


   def preLogic():
      _cie=int(pt0.get('1.0',END))
      pia1=int(pt1.get('1.0',END))
      pia2=int(pt2.get('1.0',END))
      pquiz=int(pt3.get('1.0',END))
      pTotal=((_cie-10-pquiz)/0.4)-pia1-pia2

      #Display of answer 
      abaLabel=Label(win1,text='Assuming your average ABA score as 10 ',bg='#CEF4DE').place(x=80,y=320)
      preAns=Label(win1,text='To get the target CIE score your \ncombined score of IA2 & IA3 must be  :',bg='#CEF4DE')
      preAns.place(x=80,y=350)
      preAnsDisp=Text(win1,height=1,width=10)
      preAnsDisp.place(x=300,y=365)
      preAnsDisp.insert(END,str(pTotal))

   pbutton_cal=Button(win1,text='Calculate',bg='white',padx=20,command=preLogic)
   pbutton_cal.place(x=150,y=280)
   
   
# Main window
root=Tk()   
root.configure(bg='#CEF4DE')
root.geometry('400x350')#Defines the measurement of the window
root.title("Marks Calculator")

frHeading=Frame(root,bg='sky blue')
frHeading.place(relx=0.5, relwidth=0.75, relheight=0.1, anchor='n')

inst1=Label(root,text='\t\tMarks Calculator \t\t\t',font=('helvetica',12,'bold'))
inst1.grid(row =1,column=2)
# inst1.place(x=95,y=44) IT DOES'NT WORK PROPERLY

inst2=Label(root,text='What do you want to do?',fg='#1D8348')
inst2.place(x=120,y=50)
# inst3=Label(root,text='1.Calculate CIE Marks')
# inst3.grid(row=4,column=1)
inst3 =Button(root,text='1.Calculate CIE Marks',padx=35,pady=5,bg='white',command=CIE)
inst3.place(height=50, x=95, y=80)
inst3 =Button(root,text='2.Predict the marks to obtain\nfor the entered CIE marks',padx=15,pady=5,bg='white',command=Predict)
inst3.place(height=50,x=95,y=140)

botton_quit=Button(root,bg='white',text='Exit',padx=82,pady=5,command=root.quit).place(height=50,x=95,y=200)

root.mainloop()