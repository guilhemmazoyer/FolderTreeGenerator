# -*- coding : utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
from program import TreeGenerator as TG

root = tk.Tk()

from language.lang import lang
from language.lang import *

root.title(APP_TITLE[lang.LANG])
root.resizable(width=True, height=True)
root.geometry('700x275')

    ## Actions des bouttons de l'interface ##
def askUserDirectoryToParse():
    parseFolder = askdirectory()
    generator = TG(parseFolder)
    outputDisplay = generator.launch()

    if(outputDisplay == 1):
        #erreur
        statusLabel.config(text=ERROR_1_STATUS[lang.LANG])

    else :
        if (outputDisplay == 2) :
            #erreur
            statusLabel.config(text=ERROR_2_STATUS[lang.LANG])

        else:
            statusLabel.config(text=SUCCESS_STATUS[lang.LANG])
            outputArea.delete('1.0', END)
            outputArea.insert(tk.INSERT, outputDisplay)

def resetGUIPreset():
    # reset status
    statusLabel.config(text=LABEL_STATUS[lang.LANG])

    # reset output
    outputArea.delete('1.0', END)

def updateLanguageDisplay():
    ## Title
    root.title(APP_TITLE[lang.LANG])

    ## Menus
    menubar.entryconfig(index=1, label=MENU_FILES_TITLE[lang.LANG])
    filemenu.entryconfig(index=0, label=MENU_FILES_OPEN_FOLDER[lang.LANG])
    filemenu.entryconfig(index=1, label=MENU_FILES_RESET[lang.LANG])
    filemenu.entryconfig(index=3, label=MENU_FILES_EXIT[lang.LANG])
    menubar.entryconfig(index=2, label=MENU_LANGUAGE_TITLE[lang.LANG])

    ## Status
    statusFrame.config(text=LABELFRAME_STATUS[lang.LANG])
    statusLabel.config(text=LABEL_STATUS[lang.LANG])

    ## Output
    outputFrame.config(text=LABELFRAME_OUTPUT[lang.LANG])

def changeGUILangToEnglish():
    lang.LANG = 0
    langOption.set(0)
    updateLanguageDisplay()

def changeGUILangToFrench():
    lang.LANG = 1
    langOption.set(1)
    updateLanguageDisplay()

    ## Menu avec choix de langue et de dossier ##
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(accelerator='Ctrl+O', command=askUserDirectoryToParse)
filemenu.add_command(accelerator='Ctrl+R', command=resetGUIPreset)
filemenu.add_separator()
filemenu.add_command(command=root.quit)

menubar.add_cascade(menu=filemenu)

langmenu = Menu(menubar, tearoff=0)

langmenu.add_radiobutton(accelerator='Alt+E', variable=langOption, value=0, label="English", command=changeGUILangToEnglish)
langmenu.add_radiobutton(accelerator='Alt+F', variable=langOption, value=1, label="Français", command=changeGUILangToFrench)

menubar.add_cascade(menu=langmenu)

    ## Frame affichant le statut du programe ##
statusFrame = LabelFrame(root, padx=5, pady=5)
statusFrame.grid(row=0, column=0, padx=10, pady=10, sticky=NW)

statusLabel = Label(statusFrame)
statusLabel.grid(row=0, column=0)

    ## Frame affichant le resultat du programe ##
outputFrame = LabelFrame(root, padx=5, pady=5)
outputFrame.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

outputArea = scrolledtext.ScrolledText(outputFrame, wrap=tk.WORD, width=75, height=8)
outputArea.grid(column=0, row=0)

    ## Lancement du programme ##
launchFrame = Frame(root, padx=2, pady=2)
launchFrame.grid(row=1, column=0, sticky=SW)

root.config(menu=menubar)

updateLanguageDisplay();

    ## Accelerators ##
root.bind_all('<Alt-f>', lambda event: changeGUILangToFrench())
root.bind_all('<Alt-F>', lambda event: changeGUILangToFrench())
root.bind_all("<Alt-e>", lambda event: changeGUILangToEnglish())
root.bind_all("<Alt-E>", lambda event: changeGUILangToEnglish())
root.bind_all("<Control-o>", lambda event: askUserDirectoryToParse())
root.bind_all("<Control-O>", lambda event: askUserDirectoryToParse())
root.bind_all("<Control-r>", lambda event: resetGUIPreset())
root.bind_all("<Control-R>", lambda event: resetGUIPreset())

root.mainloop()