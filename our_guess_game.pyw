from tkinter import*
import random
from tkinter.messagebox import *
from PIL import ImageTk, Image

# Create a new window
window = Tk()
#backgroud
image_bg = Image.open('guess_pic.png')
bck_end = ImageTk.PhotoImage(image_bg)
label1 = Label(window,image = bck_end)
label1.place(x = 0 , y = 0)

# Set the dimensions of the created window
window.geometry("700x500")

# Set the background color of the window
window.config(bg="#EB96EB")

window.resizable(width=False, height=False)

# Set Window Title
window.title('Number Guessing Game')




# The code for the buttons and text and other
# interactive UI elements go here

TARGET = random.randint(0, 10)
RETRIES = 0

#FUNCTIONS

def wrong():
    error =showerror(title = 'RESULTS' , message = 'Wrong Guess!! Try Again')



def correct():
    right = showinfo(title = 'RESULTS' , message = 'You had the guess correct!')


def confirm():
    answer = askyesno(title = 'CONFIRMATION' , message = 'ARE YOU SURE THAT YOU WANT TO QUIT ?')
    if answer:
        window.destroy()



def update_result(text):
    result.configure(text=text)


# Create a new game
def new_game():

    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 10)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 10")


# Continue the ongoing game or end it
def play_game():
    global RETRIES

    choice = int(number_form.get())

    if choice != TARGET:
        RETRIES += 1
        wrong()

        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and {}".format(choice)
        else:
            hint = "The required number lies between {} and 10".format(choice)
        result += "\n\nHINT :\n" + hint

    else:
        correct()
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"

    update_result(result)


# Heading of our game
title = Label(window, text="GUESS THE NUMBER", font=("Arial", 24 ,'bold'))

# Result and hints of our game
result = Label(window, text="Click on Play to start a new game", font=("Arial", 12, "bold", "italic")
                , justify=LEFT)

# Play Button
play_button = Button(window, text="Play Game", font=("Arial", 14, "bold"), fg="Black", bg="#FAD000", command=new_game)

                        

# Guess Button
guess_button = Button(window, text="Guess", font=("Arial", 13), state='disabled', fg="#13d675", bg="Black",
                         command=play_game)

# Exit Button
exit_button = Button(window, text="Exit Game", font=("Arial", 14), fg="White", bg="#b82741", command=confirm)

# Entry Fields
guessed_number = StringVar()
number_form = Entry(window, font=("Arial", 11), textvariable=guessed_number)

# Place the labels

title.place(x=170, y=50)
result.place(x=180, y=210)

# Place the buttons
exit_button.place(x=300, y=320)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

# Place the entry field
number_form.place(x=180, y=150)

# Start the window
window.mainloop()
