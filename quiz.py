#Luke Halcrow 22156@nayland.school.nz

import tkinter as tk #this makes it so i can use tkinter
from tkinter import messagebox #lets me use messege boxes in my code which make up alot of it
#this is my list of all the questions with the question and the answer
te_reo_quiz = [
    {"question": "Welcome, read the statement and click your answer,like this:\n 'You want to start the Quiz' ", "answer": True},# this one is the stating screen so ity askes the player what they want to do this is user freedom
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

quescount = 0 #WHAT question the user is up to at zero to start
score = 0 #the users current score as 0 to start
def playquestion():# this defines the playquestion function
    if quescount < len(te_reo_quiz):# this checks if the user is still in the quiz by comparing the length to the quescount
        queslabel.config(text=te_reo_quiz[quescount]["question"], fg= "white") #this sets the question text as the question thats current
    else:
        if score >= 25:    # if the users score is above 25 they pass
            messagebox.showinfo("Quiz done", f"Your score: {score} / '30" "\n You passed!") #tells them they pass 
            root.destroy()
        else:
            messagebox.showinfo("Quiz done", f"Your score: {score} / 30" "\n You did not pass.")
            root.destroy()
            



#belowq here is the actual parts of the quiz that arent functions
root = tk.Tk()
root.title("Te Reo quiz")
root.geometry("1200x600")
root.config(bg= "gray22")

def check(useranswer: bool):
    global quescount, score
    if quescount ==0 and useranswer == False:
        root.destroy()
        return
    if quescount > 1:
        correct_answer = te_reo_quiz[quescount]["answer"]
        if useranswer == correct_answer:
            score += 1
    quescount += 1
    playquestion()


true = tk.Button(root, 
    text='True',
    command=lambda: check(True),
    font=("fixedsys", 16),
    bg = 'green', fg= "white"
)
true.place(relx=0.25, rely=0.5, anchor = "w", relheight=0.2, relwidth=0.15,)
false = tk.Button(root, 
    text='False', 
    command=lambda: check(False),
    font=("fixedsys", 16),
    background ='red', fg= "white"
)
false.place(relx=0.75, rely=0.5, anchor = "e", relheight=0.2, relwidth=0.15,)



queslabel = tk.Label(root, text="", wraplength=380, font=("fixedsys", 20), bg= "gray22")
queslabel.pack(pady=20)



playquestion()
root.mainloop()