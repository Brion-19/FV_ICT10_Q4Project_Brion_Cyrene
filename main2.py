from pyscript import document, display
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import numpy as np
import matplotlib.pyplot as plt


#prevents an emppty plot from appearing
plt.figure()
plt.plot([0,1], [0,1])
plt.close()


#empty lists to store the days and absences
days = []
absences = []

def submit_button(e):
    output = document.getElementById("output")
    day = document.getElementById('day_absences').value
    absence = int(document.getElementById('number_absences').value) #made it intger so it can be graphed up and down
   
    days.append(day) #shows text (day of week)
    absences.append(absence)
    days_absences = np.array(absences) #shows number

    plt.clf() #Clears previous graph
    plt.plot(days, days_absences, marker='o')
    plt.show() #shows the graph when user clicks submit

    plt.title("Weekly Attendance") #Title of the graph
    plt.xlabel("Days of the Week") #Label of the x axis (the one at the bottom of the graph)
    plt.ylabel("Number of Absences")#Label for the y axis (left of the graph)
