from tkinter import *

# Ce fichier contient tous les noms et les traductions des éléments du GUI
# Les noms sont écris sous la forme :
# varname = ["english", "français"]

    ## Title
APP_TITLE = ["Tree Generator", "Générateur d'arborescence"]

    ## Menus
MENU_FILES_OPEN_FOLDER = ["Open Folder...", "Ouvrir un Dossier..."]
MENU_FILES_RESET_PRESETS = ["Presets reset", "Réinitilisation des réglages"]
MENU_FILES_RESET_OUTPUT = ["Output reset", "Réinitilisation du résultat"]
MENU_FILES_EXIT = ["Exit", "Quitter"]
MENU_FILES_TITLE = ["File", "Fichier"]
MENU_LANGUAGE_TITLE = ["Language", "Langue"]

    ## File Selection
LABELFRAME_FILE_SELECTION = ["Files selection", "Sélection des fichiers", "ファイル選択"]

    ## Status
LABELFRAME_STATUS = ["Status", "Statut"]
LABEL_STATUS = ["Waiting to scan a folder", "Attente de la récupération d'un dossier"]
SUCCESS_STATUS = ["The folder was successfully scanned", "Le dossier a été récupéré avec succès"]
ERROR_1_STATUS = ["This folder is nowhere to be found", "Ce fichier est introuvable"]
ERROR_2_STATUS = ["This folder is nowhere to be found", "Ce fichier est introuvable"]

    ## Ignore List
LABELFRAME_IGNORE_LIST = ["Ignore List", "Liste à ignorer"]

    ## Presets
LABELFRAME_PRESETS_SELECTION = ["Scan presets", "Réglages"]
CHECK_DEFAULT_IGNORE_LIST = ["Use the default ignore list", "Utiliser la liste à ignorer par défaut"]
CHECK_CUSTOM_IGNORE_LIST = ["Use the custom ignore list", "Utiliser la liste à ignorer personnelle"]
LABEL_RANGE_TO_SCAN = ["Range :", "Portée :"]

    ## Output
LABELFRAME_OUTPUT = ["Output", "Résultat"]

class lang:

    global langOption
    langOption = IntVar()
    langOption.set(0)
    LANG = 0    

    def __init__(self) -> None:
        pass