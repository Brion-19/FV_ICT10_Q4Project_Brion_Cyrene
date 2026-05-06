from pyscript import display, document

class Classmate: #classmate is the class name
   def __init__(self, name, section, favorite_subject): #takes the name, section and fav subject and stores it in the classmate object
       self.name = name #attribute
       self.section = section #attribute
       self.favorite_subject = favorite_subject #attribute
 
   def introduce(self):
       # The introduction format for each person
       return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

classmates_list = [
   Classmate("Jabez", "10 - Emerald", "Math"),
   Classmate("Lucas", "10 - Emerald", "Science"),
   Classmate("Giana", "10 - Emerald", "English"),
   Classmate("Emillie", "10 - Emerald", "Math"),
   Classmate("Shia", "10 - Emerald", "History")
]

#Green Button or the show list
def show_all_classmates(event=None):
   container = document.querySelector("#list-container")
   container.innerHTML = ""

   #Loop through my list and print each introduction one by one
   for c in classmates_list:
       display(c.introduce(), target="list-container", append=True)

#Add new classmate
def add_new_classmate(event):
   name = document.querySelector("#name_in").value
   sect = document.querySelector("#sect_in").value
   subj = document.querySelector("#subj_in").value

   if name and sect and subj:
       new_person = Classmate(name, sect, subj)
       classmates_list.append(new_person)
     
       document.querySelector("#name_in").value = ""
       document.querySelector("#sect_in").value = ""
       document.querySelector("#subj_in").value = ""
     
       show_all_classmates()

show_all_classmates()





