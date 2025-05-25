
import tkinter as tk #this makes it so i can use tkinter
from tkinter import messagebox
#this is my list of all the questions with the question and the answer
te_reo_quiz = [
    {"question": "Kia ora means hello.", "answer": True},
    {"question": "Kai is the Māori word for water.", "answer": False},
    {"question": "Whānau means family.", "answer": True},
    {"question": "Moana is the Māori word for river.", "answer": False},
    {"question": "Aotearoa is the Māori name for New Zealand.", "answer": True},
    {"question": "Haka is a traditional Māori war dance.", "answer": True},
    {"question": "Waiata means food.", "answer": False},
    {"question": "Ngahere is the Māori word for forest.", "answer": True},
    {"question": "Maunga means mountain.", "answer": True},
    {"question": "Puku means ear.", "answer": False},
    {"question": "Tamariki means children.", "answer": True},
    {"question": "Waka is the Māori word for kayak.", "answer": True},
    {"question": "Awa means lake.", "answer": False},
    {"question": "Whare means house.", "answer": True},
    {"question": "Whetū means star.", "answer": True},
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
    {"question": "Aroha means love.", "answer": True},
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
root.title("Te Reo Māori quiz")
root.geometry("800x400")


true = tk.Button(root, height=3, width=8,
    text='true', 
    command=add_quescount,
    bg = 'lawn green'
)
true.place(x=250, y=200)
false = tk.Button(root, height=3, width=8,
    text='false', 
    command=add_quescount,
    background ='red'
)
false.place(x=500, y=200)



queslabel = tk.Label(root, text="", wraplength=380, font=("Arial", 14))
queslabel.pack(pady=20)



playquestion()
root.mainloop()