
import tkinter as tk #this makes it so i can use tkinter
from tkinter import messagebox
#this is my list of all the questions with the question and the answer
te_reo_quiz = [
    {"question": "Kia ora means hello.", "answer": True},
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

def add_quescount():
    global quescount
    quescount += 1
quescount = 0 #WHAT question the user is up to
score = 0 #the users current score
def playquestion():
    if quescount < len(te_reo_quiz):
        queslabel.config(text=te_reo_quiz[quescount]["question"])
    else:
        messagebox.showinfo("Quiz done", f"Your score: {score} / {len(te_reo_quiz)}")
        root.destroy()



#belowq here is the actual parts of the quiz that arent functions
root = tk.Tk()
root.title("Te Reo quiz")
root.geometry("800x400")

def check(useranswer: bool):
    global quescount, score
    correct_answer = te_reo_quiz[quescount]["answer"]
    if useranswer == correct_answer:
        score += 1
    quescount += 1
    print(score)
    playquestion()


true = tk.Button(root, height=3, width=8,
    text='true',
    command=lambda: check(True),
    bg = 'lawn green'
)
true.place(relx=0.25, rely=0.5, anchor = "w")
false = tk.Button(root, height=3, width=8,
    text='false', 
    command=lambda: check(False),
    background ='red'
)
false.place(relx=0.75, rely=0.5, anchor = "e")



queslabel = tk.Label(root, text="", wraplength=380, font=("Arial", 14))
queslabel.pack(pady=20)



playquestion()
root.mainloop()