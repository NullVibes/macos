# GUI for MacOS commands
# Written by NullVibes

#import tkinter.simpledialog
#tk.Tk().withdraw()
#tkinter.simpledialog.askstring("Password", "Enter password:", show='*')

from tkinter import *
from tkinter import ttk
import os, subprocess

def hide(widget):
    widget.pack_forget()

def show(widget):
    widget.pack()

def check_brew():
    brewv = subprocess.run(["brew --version"], shell=True, text=True, capture_output=True)
    brewo = str(brewv.stdout)
    f = open("/tmp/appseloptions.txt", "a")
    if brewo.count("Homebrew") > 0:
        f.write("brew=yes")
        pytk = str(subprocess.run(["brew list | grep python-tk"], shell=True, text=True, capture_output=True).stdout)
        if pytk.count("python-tk") < 1:
            pyinsttk = str(subprocess.run(["brew install python-tk"], shell=True, text=True, capture_output=True).stdout)
            #print(pyinsttk.stdout)
    else:
        f.write("brew=no")
        pytk = str(subprocess.run(['/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'], shell=True, text=True, capture_output=True).stdout)
    f.close()

def check_xperm():
    cmdpwd = subprocess.run(["pwd"], shell=True, text=True, capture_output=True)
    checkx1 = subprocess.run(["ls -l mac_lockdown.sh | cut -d ' ' -f1"], shell=True, text=True, capture_output=True)
    checkx1 = str(checkx1.stdout)
    #print(cmdpwd)
    if checkx1.count("x") < 1:
        fixx1 = str(subprocess.run(["chmod +x mac_lockdown.sh"], shell=True, text=True, capture_output=True))

def absolute_x(widget):
    if widget == widget.winfo_toplevel():
        # top of the widget hierarchy for this window
        return 0
    print(widget.winfo_x() + absolute_x(widget.nametowidget(widget.winfo_parent())))
    return widget.winfo_x() + absolute_x(widget.nametowidget(widget.winfo_parent()))

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

    # Separator object for asthetics
        #items = cMenu.find("all")
        #print(items)
    s = ttk.Style()
    ttk.Separator(master=self, orient='horizontal', style='TSeparator').grid(row=2, column=0, columnspan=(i+1), sticky=E+W, pady=0, padx=5, ipadx=0, ipady=0)
    s.configure('TSeparator', background='#5daed7')
    print(TSeparator)
    #separator.place(relx=self(cMenu.button[i]), rely=0, relwidth=1, relheight=0.02)
    #separator.place(relx=absolute_x(cMenu.button[i]), rely=0, relwidth=1, relheight=0.02)
    
    # Add the actual Help button
    self.button.append(Button(self, text='Help ?', width=10, height=1, bd='0', command=window.destroy))
    self.button[i+1].config(bg="#22303C", fg="#888888", highlightthickness=2, highlightbackground="orange", highlightcolor="orange")
    self.button[i+1].grid(row=3, column=0, columnspan=(i+1), sticky=E+W, pady=2, padx=10, ipadx=2, ipady=2)
    

def open_app(appNum):
    cMenu.pack_forget()
    #Can we just app[appNum]() ?
    
    if appNum == 0:
        cApp1.pack()
        cApp2.pack_forget()
        #result = subprocess.run(["sudo ./mac_lockdown.sh"], shell=True, capture_output=True, text=True)
        crashreporter = subprocess.run(["defaults read com.apple.CrashReporter DialogType"], shell=True, capture_output=True, text=True)
        lstBox1.insert(END, "CrashReporter: " + str(crashreporter.stdout))
        sirianalytics = subprocess.run(["ls -l ~/Library/Assistant/SiriAnalytics.db | cut -d ' ' -f1"], shell=True, capture_output=True, text=True)
        lstBox1.insert(END, "CrashReporter: " + str(sirianalytics.stdout))
        sirianalytics = subprocess.run(["ls -l ~/Library/Application\ Support/Quick\ Look | cut -d ' ' -f1"], shell=True, capture_output=True, text=True)
        lstBox1.insert(END, "CrashReporter: " + str(sirianalytics.stdout))
    elif appNum == 1:
        cApp2.pack()
        cApp1.pack_forget()
        result = subprocess.run(["sudo ./rev_ssh.sh"], shell=True, text=True, capture_output=True)
        #lstBox1.insert(END, str(result.stdout))
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

lstBox1 = Listbox(cApp1, height=3, width=50, bd='0')
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

#If-exists stuff here...
f = open("/tmp/appseloptions.txt", "w")
f.write("")
f.close()
check_brew()
check_xperm()
window.mainloop()
