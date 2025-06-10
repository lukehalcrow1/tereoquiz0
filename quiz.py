#Luke Halcrow 22156@nayland.school.nz

import tkinter as tk #this makes it so i can use tkinter and as tk makes it easyer on line 57 and 75 and so on
from tkinter import messagebox #lets me use messege boxes in my code which make up alot of it
#this is my list of all the questions with the question and the answer
te_reo_quiz = [ # this is a list of dictionarys with the keys being question and answer
    {"question": "Welcome,\n click true to start. ", "answer": True},# this one is the stating screen so ity askes the player what they want to do this is user freedom
    {"question": "Kai is the Māori word for water.", "answer": False},
    {"question": "Whānau means family.", "answer": True},
    {"question": "Moana is the Māori word for river.", "answer": False},
    {"question": "New Zealand is the Māori name for New Zealand.", "answer": False},
    {"question": "Haka is a traditional Māori war dance.", "answer": True},
    {"question": "Waiata means food.", "answer": False},
    {"question": "Ngahere is the Māori word for forest.", "answer": True},
    {"question": "Maunga means mountain.", "answer": True},
    {"question": "Puku means ear.", "answer": False},
    {"question": "Tamariki means children.", "answer": True},
    {"question": "Waka is the Māori word for waves.", "answer": False},
    {"question": "Awa means house.", "answer": False},
    {"question": "Whare means house.", "answer": True},
    {"question": "Whetū means eight.", "answer": False},
    {"question": "Kura means school.", "answer": True},
    {"question": "Haere mai means go away.", "answer": False},
    {"question": "Kaiako means student.", "answer": False},
    {"question": "Ako means to teach and learn.", "answer": True},
    {"question": "Moana means mountain.", "answer": False},
    {"question": "Rangi means sky or heaven.", "answer": True},
    {"question": "Wai is the Māori word for water.", "answer": True},  
    {"question": "Hāngi is a traditional Māori cooking method.", "answer": True},
    {"question": "Rā means moon.", "answer": False},
    {"question": "Marama means moon.", "answer": True},
    {"question": "Moko refers to traditional tattoos.", "answer": True},
    {"question": "Ingoa means name.", "answer": True},
    {"question": "Wāhine means boy.", "answer": False},
    {"question": "Ika means fish.", "answer": True},
    {"question": "Aroha means Hate.", "answer": False},
    {"question": "Kōrero means to speak.", "answer": True},
]

question_count = 0 #WHAT question the user is up to at zero to start
score = 0 #the users current score as 0 to start
def play_question():
    """ this defines the playquestion function"""
    if question_count < len(te_reo_quiz):# this checks if the user is still in the quiz by comparing the length to the question_count
        question_label.config(text=te_reo_quiz[question_count]["question"], fg= "white") #this sets the question text as the question thats current
    else:
        if score >= 25:    # if the users score is above 25 they pass
            messagebox.showinfo("Quiz done", f"Your score: {score} / 30" "\n You passed!") #tells them they pass 
            root.destroy()# ends quiz when anthing is clicked
        else:
            messagebox.showinfo("Quiz done", f"Your score: {score} / 30" "\n You did not pass.")# tells them they fail in info box
            root.destroy()
            
def check(user_answer: bool):
    """this runs the function with the argument of the answer in boolean form (true or false)"""
    global question_count, score #lets function change and see these variables
    if question_count ==0 and user_answer == False: #when false is clicked on the first question
        root.destroy() # closes the quiz
        return #ends function as is
    if question_count >=1: #after the intro score can be taken
        correct_answer = te_reo_quiz[question_count]["answer"] #compares question answer to answer in dictionary
        if user_answer == correct_answer: 
            score += 1 #ads score
    question_count += 1
    play_question() #makes the next question play


#belowq here is the actual parts of the quiz that arent functions
root = tk.Tk() # Uses tkinter to make a box 
root.title("Te Reo quiz") #sets title of box
root.geometry("1200x600")# sets height and width of box
root.config(bg= "gray22") #sets colour of box at the right grey



true = tk.Button(root, # makes true button
    text='True',
    command=lambda: check(True), #the lamda allows function to be called from button with the argument of true of false
    font=("fixedsys", 16),
    bg = 'green', fg= "white" #green button white font
)
true.place(relx=0.25, rely=0.5, anchor = "w", relheight=0.2, relwidth=0.15,) #sets dimentions and positioning reletive to size of window with 'west' or w to set to the left
false = tk.Button(root, #all the code is the same exept the colours and posistions
    text='False', 
    command=lambda: check(False),
    font=("fixedsys", 16),
    background ='red', fg= "white"
)
false.place(relx=0.75, rely=0.5, anchor = "e", relheight=0.2, relwidth=0.15,)



question_label = tk.Label(root, text="", wraplength=380, font=("fixedsys", 20), bg= "gray22") #makes the label of the main window and sets font, size ,and colour
question_label.pack(pady=20) #adds padding so text stays away from top edge



play_question() #starts quiz by running first question
root.mainloop() #keeps window open