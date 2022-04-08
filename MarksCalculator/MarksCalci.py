from tkinter import*


def CIE():
   # global l1,l2,l3,l4,l5,ia1,ia2,ia3,ia4,ia5
   win2=Toplevel()
   win2.geometry('300x300')
   global t1,t2,t3,t4,t5
   CIE_ins=Label(win2,text='Calculation of CIE Marks').grid(row=0,column=5)
   # Code for all the required input fields
   l1=Label(win2,text='Marks in IA-1*:')
   l1.grid(row=1,column=4)
   t1=Text(win2,height=1,width=10)
   t1.grid(row=1,column=5)

   l2=Label(win2,text='Marks in IA-2*:')
   l2.grid(row=2,column=4)
   t2=Text(win2,height=1,width=10)
   t2.grid(row=2,column=5)

   l3=Label(win2,text='Marks in IA-3*:')
   l3.grid(row=3,column=4)
   t3=Text(win2,height=1,width=10)
   t3.grid(row=3,column=5)

   l4=Label(win2,text='Average Quiz score*:')
   l4.grid(row=4,column=4)
   t4=Text(win2,height=1,width=10)
   t4.grid(row=4,column=5)

   l5=Label(win2,text='ABA marks*:')
   l5.grid(row=5,column=4)
   t5=Text(win2,height=1,width=10)
   t5.grid(row=5,column=5)




   def cieLogic():
      
      ia1=int(t1.get('1.0',END))
      ia2=int(t2.get('1.0',END))
      ia3=int(t3.get('1.0',END))
      quiz=int(t4.get('1.0',END))
      aba=int(t5.get('1.0',END))
      total=((ia1+ia2+ia3)*0.4)+quiz+aba

      cieAns=Label(win2,text='Your average CIE score :')
      cieAns.grid(row=8,column=4)
      cieAnsDisp=Text(win2,height=1,width=10)
      cieAnsDisp.grid(row=8,column=5)
      # Inserting the result in textbox and disbling it
      cieAnsDisp.insert(END,str(total))

   
   button_cal=Button(win2,text='Calculate',padx=20,command=cieLogic)
   button_cal.grid(row=6,column=4,columnspan=2)

   
def Predict():
   win1=Toplevel()
   win1.geometry('550x400')
   Predict_ins=Label(win1,text='Marks PREDICTOR for the given CIE marks').grid(row=0,column=5)
   # continue.........
   pl0=Label(win1,text='Target CIE marks*:')
   pl0.grid(row=1,column=4)
   pt0=Text(win1,height=1,width=10)
   pt0.grid(row=1,column=5)

   pl1=Label(win1,text='Marks in IA-1*:')
   pl1.grid(row=2,column=4)
   pt1=Text(win1,height=1,width=10)
   pt1.grid(row=2,column=5)

   pl2=Label(win1,text='Marks in IA-2:')
   pl2.grid(row=3,column=4)
   pt2=Text(win1,height=1,width=10)
   pt2.grid(row=3,column=5)
   # pt2.insert(END,'Enter 0 if unknown')
   pl22=Label(win1,text='(Enter 0 if unknown)',font=('helvetica',6))
   pl22.grid(row=4,column=4)

   
   pl3=Label(win1,text='Quiz score*:')
   pl3.grid(row=5,column=4)
   pt3=Text(win1,height=1,width=10)
   pt3.grid(row=5,column=5)


   def preLogic():
      _cie=int(pt0.get('1.0',END))
      pia1=int(pt1.get('1.0',END))
      pia2=int(pt2.get('1.0',END))
      pquiz=int(pt3.get('1.0',END))
      pTotal=((_cie-10-pquiz)/0.4)-pia1-pia2

      #Display of answer 
      abaLabel=Label(win1,text='Assuming your average ABA score as 10 ').grid(row=8,column=4)
      preAns=Label(win1,text='To get the target CIE score your \ncombined score of IA2 & IA3 must be  :')
      preAns.grid(row=9,column=4)
      preAnsDisp=Text(win1,height=1,width=10)
      preAnsDisp.grid(row=9,column=5)
      preAnsDisp.insert(END,str(pTotal))

   pbutton_cal=Button(win1,text='Calculate',padx=20,command=preLogic)
   pbutton_cal.grid(row=6,column=4,columnspan=2)
   
   
   

# Main window
root=Tk()   
root.geometry('400x500')#Defines the measurement of the window
root.title("Marks Calculator")

inst1=Label(root,text='*****************Marks Calculator*****************').grid(row=0,column=2)
inst2=Label(root,text='What do you want to do?')
inst2.grid(row=2,column=2)

# inst3=Label(root,text='1.Calculate CIE Marks')
# inst3.grid(row=4,column=1)
inst3 =Button(root,text='1.Calculate CIE Marks',padx=35,pady=5,command=CIE)
inst3.grid(row=5,column=2)
inst3 =Button(root,text='2.Predict the marks to obtain\nfor the entered CIE marks',padx=15,pady=5,command=Predict)
inst3.grid(row=8,column=2)




botton_quit=Button(root,text='Exit',padx=82,pady=5,command=root.quit).grid(row=9,column=2)

root.mainloop()