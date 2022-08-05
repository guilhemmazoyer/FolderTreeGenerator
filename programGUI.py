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
root.resizable(width=False, height=False)

    ## Actions des bouttons de l'interface ##
def askUserDirectoryToParse():
    parseFolder = askdirectory()
    resetGUIOutput()

    # recupere les variables pour l'execution
    depth = int(rangeEdit.get())
    doDefault = valueCheckDefaultIgnoreList.get()
    doCustom = valueCheckCustomIgnoreList.get()
    generator = TG(parseFolder, depth, doDefault, doCustom)

    customIgnoreList = ignoreEdit.get()
    outputDisplay = generator.launch(customIgnoreList)

    if(outputDisplay == 1):
        #erreur
        statusLabel.config(text=ERROR_1_STATUS[lang.LANG])

    else:
        statusLabel.config(text=SUCCESS_STATUS[lang.LANG])
        outputArea.delete('1.0', END)
        outputArea.insert(tk.INSERT, outputDisplay)

def resetGUIPresets():
    # Parse preset
    checkDefaultIgnoreList.select()
    checkCustomIgnoreList.deselect()
    rangeEdit.delete(0, END)
    rangeEdit.insert(0, "0")

def resetGUIOutput():
    # reset status & output
    statusLabel.config(text=LABEL_STATUS[lang.LANG])
    outputArea.delete('1.0', END)

def updateLanguageDisplay():
    ## Title
    root.title(APP_TITLE[lang.LANG])

    ## Menus
    menubar.entryconfig(index=1, label=MENU_FILES_TITLE[lang.LANG])
    filemenu.entryconfig(index=0, label=MENU_FILES_OPEN_FOLDER[lang.LANG])
    filemenu.entryconfig(index=1, label=MENU_FILES_RESET_PRESETS[lang.LANG])
    filemenu.entryconfig(index=2, label=MENU_FILES_RESET_OUTPUT[lang.LANG])
    filemenu.entryconfig(index=4, label=MENU_FILES_EXIT[lang.LANG])
    menubar.entryconfig(index=2, label=MENU_LANGUAGE_TITLE[lang.LANG])

    ## Status
    statusFrame.config(text=LABELFRAME_STATUS[lang.LANG])
    statusLabel.config(text=LABEL_STATUS[lang.LANG])

    ## IgnoreList
    ignoreFrame.config(text=LABELFRAME_IGNORE_LIST[lang.LANG])

    ## Presets
    presetFrame.config(text=LABELFRAME_PRESETS_SELECTION[lang.LANG])
    checkDefaultIgnoreList.config(text=CHECK_DEFAULT_IGNORE_LIST[lang.LANG])
    checkCustomIgnoreList.config(text=CHECK_CUSTOM_IGNORE_LIST[lang.LANG])
    rangeLabel.config(text=LABEL_RANGE_TO_SCAN[lang.LANG])

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
filemenu.add_command(accelerator='Ctrl+R', command=resetGUIPresets)
filemenu.add_command(accelerator='Ctrl+T', command=resetGUIOutput)
filemenu.add_separator()
filemenu.add_command(command=root.quit)

menubar.add_cascade(menu=filemenu)

langmenu = Menu(menubar, tearoff=0)

langmenu.add_radiobutton(accelerator='Alt+E', variable=langOption, value=0, label="English", command=changeGUILangToEnglish)
langmenu.add_radiobutton(accelerator='Alt+F', variable=langOption, value=1, label="Français", command=changeGUILangToFrench)

menubar.add_cascade(menu=langmenu)


    ## Frame affichant le statut du programme ##
statusFrame = LabelFrame(root, padx=5, pady=5)
statusFrame.grid(row=0, column=0, padx=10, pady=10, sticky=NW)

statusLabel = Label(statusFrame)
statusLabel.grid(row=0, column=0)


    ## Frame affichant la liste à ignorer personnalisable du programme ##
ignoreFrame = LabelFrame(root, padx=5, pady=5)
ignoreFrame.grid(row=0, column=0, padx=10, pady=10, sticky=NE)

ignoreEdit = Entry(ignoreFrame, width=50)
ignoreEdit.grid(row=0, column=0)


    ## Frame constituee des presets pour le programme ##
presetFrame = LabelFrame(root, padx=5, pady=5)
presetFrame.grid(row=0, column=2, padx=10, pady=10, sticky=NE)

valueCheckDefaultIgnoreList = IntVar()
checkDefaultIgnoreList = Checkbutton(presetFrame, variable=valueCheckDefaultIgnoreList)
checkDefaultIgnoreList.select()
checkDefaultIgnoreList.grid(row=0, sticky=W)

valueCheckCustomIgnoreList = IntVar()
checkCustomIgnoreList = Checkbutton(presetFrame, variable=valueCheckCustomIgnoreList)
checkCustomIgnoreList.deselect()
checkCustomIgnoreList.grid(row=1, sticky=W)

rangeLabel = Label(presetFrame)
rangeLabel.grid(row=2, sticky=W)

rangeEdit = Entry(presetFrame, width=5)
rangeEdit.grid(row=2, sticky=W, padx=50)
rangeEdit.insert(0,"0")


    ## Frame affichant le resultat du programe ##
outputFrame = LabelFrame(root, padx=5, pady=5)
outputFrame.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

outputArea = scrolledtext.ScrolledText(outputFrame, wrap=tk.WORD, width=75, height=20)
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
root.bind_all("<Control-r>", lambda event: resetGUIPresets())
root.bind_all("<Control-R>", lambda event: resetGUIPresets())
root.bind_all("<Control-t>", lambda event: resetGUIOutput())
root.bind_all("<Control-T>", lambda event: resetGUIOutput())

def debugTest ():
    print("## debug ##")

    print("## debug ##")

root.bind_all("<Control-d>", lambda event: debugTest())
root.bind_all("<Control-D>", lambda event: debugTest())

root.mainloop()