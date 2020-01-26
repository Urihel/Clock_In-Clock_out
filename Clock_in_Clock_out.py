from tkinter import * 

t = Tk()
t.geometry('500x500') 
btn1 = Button(t, text = 'Clock In', bd = '2', bg='#00B6FF',activebackground='red',
              activeforeground="white",fg="white",height=2, width=15, command = t.destroy)
btn2 = Button(t, text = 'Clock Out', bd='2', height=2, width=15, command=t.destroy)
btn1.pack(side = 'top')
btn2.pack(side='top')

if btn1:
    print("the code is working")
t.mainloop()
