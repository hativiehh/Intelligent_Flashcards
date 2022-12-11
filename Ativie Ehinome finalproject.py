"""

    Intelligent Flashcard App

        A program for people who need help with assignments

        as well as people who want to learn new languages

"""



""" Importing the GUI package """

from tkinter import *

from tkinter import ttk

import webview



win = Tk()



""" Updating the neccessary windows info """

win.title(string = "Intelligent Flashcard App")



# Adjusting the size of the window

win.geometry("400x600")

#set minimum window size value

win.minsize(width = 400, height = 600)



# function for closing windows

def Close():

    """

        Function to close the window

    """

    win.destroy()


# function for french language 


def FrenchCommand():

    webview.create_window('Language to French', 'https://translate.google.com/?sl=auto&tl=fr&op=translate')

    webview.start()

#function for Yoruba language 

def YorubaCommand():

    webview.create_window('Language to Yoruba', 'https://translate.google.com/?sl=auto&tl=yo&op=translate')

    webview.start()

  # function for Igbo Language  

def IgboCommand():

    webview.create_window('Language to Igbo', 'https://translate.google.com/?sl=auto&tl=ig&op=translate')

    webview.start()



    



# function to open a new window

def OpenLanWindow():



    #create a top level object that will be treated as a new window

    newWindow = Toplevel(win)



    #set the new title of the new window

    newWindow.title('Languages')



    # Adjusting the size of the window

    newWindow.geometry("400x600")

    #set minimum window size value

    newWindow.minsize(width = 400, height = 600)

    # window label

    label1=Label(newWindow,text='Languages Available',font=('Arial',18), justify = CENTER)

    label1.pack(pady = 100)

    # french button

    button1=Button(newWindow,text='French',font=('Arial',16),

               justify = CENTER, command=FrenchCommand)

    button1.pack()

    # Yoruba button

    button2=Button(newWindow,text='Yoruba',font=('Arial',16),

               justify = CENTER, command=YorubaCommand)

    button2.pack(pady = 10)

     # igbo Button

    button3 = Button(newWindow,text='Igbo',font=('Arial',16),

                     justify = CENTER, command = IgboCommand)

    button3.pack(pady = 10)



   # function for the search command

def SearchCommand():

    string = entry.get()

    webview.create_window('Solution', 'https://www.google.com/search?q={}'.format(string))

    webview.start()


   # function for the assignment window


def OpenAssWindow():



    #create a top level object that will be treated as a new window

    newWindow = Toplevel(win)



    #set the new title of the new window

    newWindow.title('Check for Assignment')



    # Adjusting the size of the window

    newWindow.geometry("400x600")

    #set minimum window size value

    newWindow.minsize(width = 400, height = 600)

    # label for get assignment done

    label1=Label(newWindow,text='Get Assignment Done!',font=('Arial',18), justify = CENTER)

    label1.pack(pady = 100)

    # label for new window

    Label2=Label(newWindow,text='Type Question',font=('Arial',16),

               justify = CENTER)

    Label2.pack()

    

    #Create an Entry widget to accept User Input

    global entry

    entry= Entry(newWindow, width= 40)

    entry.focus_set()

    entry.pack(pady = 10)

    # button for new window

    button1=Button(newWindow,text='Search',font=('Arial',16),

               justify = CENTER, command=SearchCommand)

    button1.pack()

    

    # Title text

label=Label(win,text='INTELLIGENT FLASHCARD',font=('Arial',22))

label.pack(side=TOP, pady = 20)

  # How can we help you

label1=Label(win,text='How can we help ?',font=('Arial',18), justify = CENTER)

label1.pack(padx = 100, pady = 100)

  # button for learn a new language

button1=Button(win,text='Learn a new language',font=('Arial',16),

               justify = CENTER, command=OpenLanWindow)

button1.pack()

  # button for check assignment

button2=Button(win,text='Check for assignment',font=('Arial',16),

               justify = CENTER, command=OpenAssWindow)

button2.pack(pady = 10)

 # quit button

button3 = Button(win,text='Quit',font=('Arial',16), justify = CENTER, command = Close)

button3.pack(pady = 10)









win.mainloop()