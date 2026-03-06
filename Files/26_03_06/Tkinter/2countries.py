import tkinter as tk
import random

# Setup data

countries = [
"Afghanistan","Albania","Algeria","Argentina","Armenia","Australia","Austria","Azerbaijan","Bangladesh","Belarus",
"Belgium","Bolivia","Bosnia and Herzegovina","Brazil","Bulgaria","Cambodia","Canada","Chile","China","Colombia",
"Croatia","Cuba","Cyprus","Czechia","Denmark","Dominican Republic","Ecuador","Egypt","Estonia","Finland",
"France","Georgia","Germany","Greece","Hungary","Iceland","India","Indonesia","Iran","Iraq",
"Ireland","Israel","Italy","Japan","Jordan","Kazakhstan","Kenya","Kuwait","Latvia","Lebanon",
"Lithuania","Luxembourg","Malaysia","Mexico","Moldova","Mongolia","Montenegro","Morocco","Nepal","Netherlands",
"New Zealand","North Korea","North Macedonia","Norway","Pakistan","Peru","Philippines","Poland","Portugal","Qatar",
"Romania","Russia","Saudi Arabia","Serbia","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain",
"Sri Lanka","Sweden","Switzerland","Syria","Taiwan","Thailand","Tunisia","Turkey","Ukraine","United Arab Emirates",
"United Kingdom","United States","Uruguay","Uzbekistan","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe","Ethiopia"
]

cities = [
"Kabul","Tirana","Algiers","Buenos Aires","Yerevan","Canberra","Vienna","Baku","Dhaka","Minsk",
"Brussels","Sucre","Sarajevo","Brasilia","Sofia","Phnom Penh","Ottawa","Santiago","Beijing","Bogotá",
"Zagreb","Havana","Nicosia","Prague","Copenhagen","Santo Domingo","Quito","Cairo","Tallinn","Helsinki",
"Paris","Tbilisi","Berlin","Athens","Budapest","Reykjavik","New Delhi","Jakarta","Tehran","Baghdad",
"Dublin","Jerusalem","Rome","Tokyo","Amman","Astana","Nairobi","Kuwait City","Riga","Beirut",
"Vilnius","Luxembourg","Kuala Lumpur","Mexico City","Chișinău","Ulaanbaatar","Podgorica","Rabat","Kathmandu","Amsterdam",
"Wellington","Pyongyang","Skopje","Oslo","Islamabad","Lima","Manila","Warsaw","Lisbon","Doha",
"Bucharest","Moscow","Riyadh","Belgrade","Singapore","Bratislava","Ljubljana","Pretoria","Seoul","Madrid",
"Sri Jayawardenepura Kotte","Stockholm","Bern","Damascus","Taipei","Bangkok","Tunis","Ankara","Kyiv","Abu Dhabi",
"London","Washington","Montevideo","Tashkent","Caracas","Hanoi","Sana'a","Lusaka","Harare","Addis Ababa"
]

total_questions = 5

count = 0
correct = 0 
i = 0
answer = ""

# Setup widgets        

def submit_text(data):
    global answer
    answer = answer_entry.get().strip()
    answer_entry.delete(0,tk.END)
    show_result()

def show_question(data=None):
    global i

    i = random.randint(0,len(countries)-1)

    result_label.pack_forget()
    continue_button.pack_forget()

    question_label.configure(text=f"What is the capital city of {countries[i]}?")

    question_label.pack()
    answer_entry.bind(sequence="<Return>",func=submit_text)
    answer_entry.pack()
    answer_entry.focus_set()

    answer_entry.focus_set()

    root.update_idletasks()


def show_result():
    global answer,i,count,correct

    count += 1

    question_label.pack_forget()
    answer_entry.unbind("<Return>")
    answer_entry.pack_forget()

    if answer.lower() == cities[i].lower():
        result_label.configure(text="Correct")
        correct += 1
    else:
        result_label.configure(text=f"Wrong. The correct answer is {cities[i]}")

    result_label.pack()

    if count < total_questions:
        continue_button.config(text="Continue")
    else:
        continue_button.config(text="End game")
        continue_button.config(command=exit)

        end_text = tk.Label(text=f"Congratulations. Your score is {correct}/{count}")
        end_text.pack()
    

    continue_button.pack()
    continue_button.focus_set()
    

    root.update_idletasks()


root = tk.Tk()
root.title("Country quiz")

## Guess window setup

question_label = tk.Label()

answer_entry = tk.Entry()


## Result window setup

result_label = tk.Label()

continue_button = tk.Button(text="Next question",command=show_question)

width = 400
height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")

show_question()

root.mainloop()