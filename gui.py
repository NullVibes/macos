# GUI for MacOS commands
# Written by NullVibes

from tkinter import *
import os, subprocess

def hide(widget):
    widget.pack_forget()

def show(widget):
    widget.pack()

def check_brew():
    brewv = subprocess.run(["brew --version"], shell=True, text=True, capture_output=True)
    brewo = str(brewv.stdout)
    f = open("/tmp/appseloptions.txt", "a")
    if brewo.find("Homebrew") > 0:
        f.write("brew=yes")
    else:
        f.write(str(brewo))
    f.close()

def app_layout(self):
    cApp1.pack_forget()
    #cApp2.pack_forget()
    self.button = []
    self.label = []
    appList = ["Lockdown\nMacOS","SSH\nProxy"]
    x = 0

    # Dynamically add button objects to the canvas, based on the items in appList[]
    for i in range(len(appList)):
        self.button.append(Button(self, text=appList[i], width=5, height=3, bd='0', command=lambda i=i: open_app(i)))
        self.button[i].config(bg="#22303C", fg="#888888", highlightthickness=2, highlightbackground="orange", highlightcolor="orange")
        self.button[i].grid(row=0, column=i, sticky=N+E+S+W, pady=2, padx=10, ipadx=2, ipady=2)

    # Add an empty Label object for Help spacing
    self.label.append(Label(self, text='', width=10, height=1, bd='0'))
    self.label[0].config(bg="#22303C", highlightthickness=0, borderwidth=0)
    self.label[0].grid(row=1, column=0, columnspan=(i+1), sticky=E+W, pady=2, padx=10, ipadx=2, ipady=2)
    
    # Add the actual Help button
    self.button.append(Button(self, text='Help ?', width=10, height=1, bd='0', command=window.destroy))
    self.button[i+1].config(bg="#22303C", fg="#888888", highlightthickness=2, highlightbackground="orange", highlightcolor="orange")
    self.button[i+1].grid(row=2, column=0, columnspan=(i+1), sticky=E+W, pady=2, padx=10, ipadx=2, ipady=2)
    

def open_app(appNum):
    cMenu.pack_forget()
    #Can we just app[appNum]() ?
    
    if appNum == 0:
        cApp1.pack()
        cApp2.pack_forget()
        result = subprocess.run(["ls","-l", "/dev/null"], capture_output=True, text=True)
        lstBox1.insert(END, str(result.stdout))
    elif appNum == 1:
        cApp2.pack()
        cApp1.pack_forget()
        result = subprocess.run(["sudo systemctl status kismet"], shell=True, text=True, capture_output=True)
        lstBox1.insert(END, str(result.stdout))
    else:
        lstBox1.insert(END, str(appNum))

    lstBox1.pack(side = LEFT, fill = BOTH)
    scrollbar1.pack(side = RIGHT, fill = BOTH)

def btnB():
    #label.value = "Hunting for ALL XYZs"
    pass

#def btnC():
    #label.value = "Help"
#    pass

window = Tk()
window.title('App Selector')
window.geometry('800x400')
window.resizable(False, False)

# --- Canvas: App #2 (Name ?) ---
cApp2 = Canvas(window, height=400, width=800, bg="#22303C", bd='0', borderwidth=0, highlightthickness=0)
cApp2.place(x=0, y=0)
cApp2.pack_forget()


# --- Canvas: App #1 (Name ?) ---
cApp1 = Canvas(window, height=400, width=800, bg="#22303C", bd='0', borderwidth=0, highlightthickness=0)
cApp1.place(x=0, y=0)

lstBox1 = Listbox(cApp1, height=3, width=10, bd='0')
#lstBox1.pack(side = LEFT, fill = BOTH)
scrollbar1 = Scrollbar(cApp1)
#scrollbar1.pack(side = RIGHT, fill = BOTH)
lstBox1.config(yscrollcommand = scrollbar1.set)
scrollbar1.config(command = lstBox1.yview)

cApp1.pack_forget()

# --- Canvas: Main Menu ---
cMenu = Canvas(window, height=400, width=800, bg="#22303C", bd='0', borderwidth=0, highlightthickness=0)
cMenu.place(x=0, y=0)
cMenu.pack()

app_layout(cMenu)
f = open("/tmp/appseloptions.txt", "w")
f.write("")
f.close()
check_brew()
window.mainloop()
