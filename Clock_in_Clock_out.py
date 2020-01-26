from tkinter import * #the tkinter module to use tkinter 

t = Tk() # how we store and use the callback to tkinter 
t.geometry('500x500') #how we manipulate the size of the GUI window where the button appears

#how we generate a button using tikinter
#inside the button are settings very simple to css but worded out and obviously used in python and not css
#alot of the settings im playing around with control text color,background color, the color of the button when you press it
#changing the height and width, having the button close the window once it is clicked, adding a border to my button, changing 
#the text when the button is being pressed.
btn1 = Button(t, text = 'Clock In', bd = '2', bg='#00B6FF',activebackground='red',
              activeforeground="white",fg="white",height=2, width=15, command = t.destroy)
btn2 = Button(t, text = 'Clock Out', bd='2', height=2, width=15, command=t.destroy)
#this is one easy method to use to place your buttons at the top of the gui of window. while there is and x and y coordinate you 
#can use to place buttons where ever on your window in this example i dont have it. it will be added later today. 
btn1.pack(side = 'top')
btn2.pack(side='top')

#the mainloop which is an infinite loop used to run you program. 
t.mainloop()
