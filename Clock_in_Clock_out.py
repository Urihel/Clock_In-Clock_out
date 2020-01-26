from tkinter import * #the tkinter module to use tkinter 

t = Tk() # how we store and use the callback to tkinter 
t.geometry('500x500') #how we manipulate the size of the GUI window where the button appears

#how we generate a button using tikinter
#inside the button are settings very similar to css but worded out and obviously used in python and not css
#alot of the settings im playing around with control text color,background color, the color of the button when you press it
#changing the height and width, having the button close the window once it is clicked, adding a border to my button, changing 
#the text when the button is being pressed. if you also notice the way i created btn1. Im sure you are wondering why i pressed enter and 
#ran some code on another line rather than on just one single line. Well since im play around with python im not trying to see how flexible 
#python really is and how it behaves when i do things like press enter and run sytle settings on a different line that is all. basically 
#my code runs the same as one line but now you can edit easier rather look across one long line and it works the same way.
btn1 = Button(t, text = 'Clock In', bd = '2', bg='#00B6FF',activebackground='red',
              activeforeground="white",fg="white",height=2, width=15, command = t.destroy)
btn2 = Button(t, text = 'Clock Out', bd='2', height=2, width=15, command=t.destroy)
#this is one easy method to use to place your buttons at the top of the gui of window. while there is and x and y coordinate you 
#can use to place buttons where ever on your window in this example i dont have it. it will be added later today. 
btn1.pack(side = 'top')
btn2.pack(side='top')

#the mainloop which is an infinite loop used to run you program. 
t.mainloop()
