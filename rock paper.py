from tkinter import*
from random import randint
from tkinter import ttk

root=Tk()
root.title('🎮          ROCK-PAPER-SCISSOR️ GAME          🎮')
root.geometry("500x600")
root.config(bg="white")
rock=PhotoImage(file='C:\\Users\hp\\PycharmProjects\\pythonProject10\\rock.jpeg')
paper= PhotoImage(file='C:\\Users\\hp\\PycharmProjects\\pythonProject10\\paper.jpeg')
scissor=PhotoImage(file='C:\\Users\\hp\\PycharmProjects\\pythonProject10\\scissor.jpeg')
image_set= [rock,paper,scissor]
select_number = randint(0,2)
image_tag = Label(root, image=image_set[select_number],bd=0)
image_tag.pack(pady=20)


def computer():
    select_number= randint(0,3)
    image_tag.config(image=image_set[select_number],bd=0)
    if user_choice.get()=="ROCK":
        user_choice_value = 0
    elif user_choice.get()=="PAPER":
        user_choice_value = 1
    elif user_choice.get()=="SCISSOR":
        user_choice_value = 2
    if user_choice_value==0:
        if select_number==0:
            result_label.config(text="It's a Tie play again")
        elif select_number==1:
            result_label.config(text="You Lose... Better Luck Next Time")
        elif select_number==2:
            result_label.config(text="You Win!!!!")

    if user_choice_value==2:
        if select_number==2:
            result_label.config(text="It's a Tie play again")
        elif select_number==0:
            result_label.config(text="You Lose... Better Luck Next Time")
        elif select_number==1:
            result_label.config(text="You Win!!!!")

    if user_choice_value==1:
        if select_number==1:
            result_label.config(text="It's a Tie play again")
        elif select_number==0:
            result_label.config(text="You Win hurray!!!")
        elif select_number==2:
            result_label.config(text="You Lose.. Better luck next time")




spin_button = Button(root, text= "Play🎮",command=computer)
spin_button.pack(pady=10)
user_choice = ttk.Combobox(root, value=("ROCK","PAPER","SCISSOR"))
user_choice.current(0)
user_choice.pack(pady=20)

result_label=Label(root,text="",font=("Helvetica",18))
result_label.pack(pady=50)




root.mainloop()