import time
from tkinter import * 
import tkinter as tk
from tkinter import ttk
import time
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
counter = 540000
tiempo = 0
tiempoOut = 0
running = False
bitacora = pd.read_csv("PROYECTO/Bitacora_Tiempos.csv", encoding='latin-1')
task = []
project = []
graphics = ["Proyectos","Tarea"]
hide = 0
fig, ax = plt.subplots()
cmb_graphics = ttk.Combobox()


def SaveNewOption():
    global task
    global project
    global cmb_Project
    global cmb_Task

    if cmb_Project.get() not in project:
        project.append(cmb_Project.get())
    if cmb_Task.get() not in task:
        task.append(cmb_Task.get())

    cmb_Project['values'] = project
    cmb_Task['values'] = task

def cargar_csv(proyecto,tarea):
    
    proy=bitacora[bitacora['proyecto'] == proyecto]
    tarea= proy[proy['tarea'] == tarea]
    if tarea.empty:
        return(0)
    else:
        return(int(tarea['tiempo_total']))
    
def guarda_csv(proyecto,tarea):
    global tiempo
    global tiempoOut
    global checkVar
    index = bitacora[(bitacora['proyecto'] == proyecto) & (bitacora['tarea'] == tarea)].index

    if index.empty:
        row = [proyecto, tarea, tiempo - 1,tiempo - 1 - tiempoOut,tiempoOut]
        bitacora.loc[len(bitacora)] = row
    else:  
        bitacora.loc[index,'tiempo_total'] = tiempo - 1
        bitacora.loc[index,'tiempo_horario'] = tiempo - 1 - tiempoOut

    if checkVar.get() == 1:
        bitacora.loc[index,'tiempo_fuera_horario'] = tiempoOut - 1


    bitacora.to_csv("PROYECTO/Bitacora_Tiempos.csv",index=False)

def counter_label(label):
    def count():
        if running:
            global counter,tiempo,tiempoOut,checkVar
            tt = datetime.fromtimestamp(counter + tiempo)
            string = tt.strftime("%H:%M:%S")
            display=string            
            label['text']=display
            label.after(1000, count) 
            tiempo += 1
            if checkVar.get() == 1:
                tiempoOut +=1
            
    count()
         
def Start(label):
    global running,tiempo
    running=True
    tiempo = cargar_csv(cmb_Project.get(),cmb_Task.get())
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
 
def ShowHideReport():
    global hide, Report
    if hide:
        btnShow["text"]= "+"
        Report.pack_forget()
        hide = 0
    else:
        btnShow["text"]= "-"
        Report.pack_forget()
        createFrameReport()
        hide = 1

def SelectGraphic():
    global cmb_graphics,cmb_ProjectG
    selection = cmb_graphics.get()
    

    if selection == "Proyectos":
        ShowReportByProject()
    elif selection == "Tarea":
        selectedProject = cmb_ProjectG.get()
        ShowReportByTask(selectedProject)

def selection_changed(event):
    global cmb_graphics, Report,btnShowReport1,cmb_ProjectG
    selection = cmb_graphics.get()
    try:
        btnShowReport1.pack_forget()
    except:
        pass

    try:
        cmb_ProjectG.pack_forget()
    except:
        pass
    
    if selection == "Proyectos":
        btnShowReport1 = tk.Button(Report,text="Genera Grafica",command=SelectGraphic)
        btnShowReport1.pack(side=tk.TOP,padx=5)
    elif selection == "Tarea":
        cmb_ProjectG = ttk.Combobox(Report, values=project)
        btnShowReport1 = tk.Button(Report,text="Genera Grafica",command=SelectGraphic)
        cmb_ProjectG.pack(side=tk.TOP,padx=5)
        btnShowReport1.pack(side=tk.TOP,padx=5)

def createFrameReport():
    global Report,graphics,project,cmb_graphics

    Report = tk.Frame(window)
    Report.pack(anchor = 'w',pady=10,fill='x')
    cmb_graphics = ttk.Combobox(Report, values=graphics)
    cmb_graphics.bind("<<ComboboxSelected>>", selection_changed)
    cmb_graphics.pack(side=tk.TOP,padx=5) 

def Stop():
    global running
    global checkVar
    state = check.state()
    start['state']='normal'
    stop['state']='disabled'
    running = False
    guarda_csv(cmb_Project.get(),cmb_Task.get())
    label['text']="Welcome!"
    SaveNewOption()
    checkVar.set(0)

def autolabel(rects):
    global fig, ax
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
def ShowReportByProject():
    global fig, ax
    activity_t = bitacora ['tiempo_total'] /60
    proyectos = bitacora['proyecto'].unique()
    proyect_labels=[]
    proyect_task=[]
    proyect_time=[]
    for proyecto in proyectos:
        proy= bitacora[bitacora['proyecto'] == proyecto]
        time_sum = proy['tiempo_total'].sum()
        time_sum= time_sum/60
        formato_proy = proyecto.replace(' ', '\n')
        proyect_labels.append(formato_proy)
        proyect_task.append(time_sum)

    x = np.arange(len(proyect_labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, proyect_task, width, label='proyect_task')
    #rects2 = ax.bar(x + width/2, school_wom, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time x Project')
    ax.set_title('Projects')
    ax.set_xticks(x)
    ax.set_xticklabels(proyect_labels)
    ax.legend()
    ax.figsize = [30,8]

    autolabel(rects1)
    fig.tight_layout()
    plt.show()

def ShowReportByTask(selectedProject):
    global fig, ax
    tareas = bitacora['tarea'].unique()
    proyect_labels=[]
    proyect_task=[]
    for tarea in tareas:
        proy= bitacora[bitacora['tarea'] == tarea]
        time_sum = proy['tiempo_total'].sum()
        time_sum= time_sum/60
        formato_proy = tarea.replace(' ', '\n')
        proyect_labels.append(formato_proy)
        proyect_task.append(time_sum)

    x = np.arange(len(proyect_labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, proyect_task, width, label='proyect_task')
    #rects2 = ax.bar(x + width/2, school_wom, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time x Project')
    ax.set_title(selectedProject)
    ax.set_xticks(x)
    ax.set_xticklabels(proyect_labels)
    ax.legend()
    ax.figsize = [30,8]

    autolabel(rects1)
    fig.tight_layout()
    plt.show()

pvez = False
if pvez == False:
    proyectos = bitacora['proyecto'].unique()
    tarea = bitacora['tarea'].unique()
    task=list(tarea)
    project=list(proyectos)
    pvez = True 

window = Tk()
window.title("Personal Time Manager")
window.configure(width=500, height=300)
window.configure(bg='lightgray')
window.minsize(width=250, height=70)

# move window center
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() - winWidth - 60)
posDown = int(window.winfo_screenwidth() / 20)
window.geometry("+{}+{}".format(posRight, posDown))
window.resizable(False, False)

frm = tk.Frame(window)
frm.pack(anchor = 'center',pady=0,fill='x')
frm2 = tk.Frame(window)
frm2.pack(anchor = 'w',pady=0,fill='x')
Report = tk.Frame(window)


lbl_Project = ttk.Label(frm, text="Project ")
cmb_Project = ttk.Combobox(frm, values=project)
start = tk.Button(frm, text='Start', width=6, command=lambda:Start(label))
stop = tk.Button(frm, text='Stop',width=6,state='disabled', command=Stop)
label = tk.Label(frm, text="Welcome!", fg="black", font="Verdana 15")

lbl_Task = ttk.Label(frm2, text="Task     ")
cmb_Task = ttk.Combobox(frm2, values=task)
checkVar = tk.IntVar()
check = ttk.Checkbutton(frm2,text='Out of hour', padding=10, variable=checkVar)
btnShow = tk.Button(frm2,text="+",command=ShowHideReport)


lbl_Project.pack(side=tk.LEFT,padx=5)
cmb_Project.pack(side=tk.LEFT,padx=5)
start.pack(side=tk.LEFT,padx=5)
stop.pack(side=tk.LEFT,padx=5)
label.pack(side=tk.LEFT,padx=5)

lbl_Task.pack(side=tk.LEFT,padx=5)
cmb_Task.pack(side=tk.LEFT,padx=5)
check.pack(side=tk.LEFT,padx=5)
btnShow.pack(side=tk.RIGHT,padx=5)

window.mainloop()
