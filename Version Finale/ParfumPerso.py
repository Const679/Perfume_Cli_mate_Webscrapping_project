import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
from Projet_Webcrapping_2 import * 
from web_const_mod import * 
from msedge.selenium_tools import Edge, EdgeOptions
import warnings
import os
import time
import winreg
import json
from zipfile import ZipFile
warnings.filterwarnings("ignore")
#Troisieme fenetre 
class Perso:
    #Fonction de webscrapping pour le parfum personalisé
    def RecherchePerso(self,entry):
        #add all the options necessary to begin webscrapping
        options = EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.set_capability("acceptInsecureCerts", True)
        #options.add_argument('headless') #hide the browser
        options.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        #Try to connect if the edgeriver version is 122
        try : 
            executablePath=r".\driverEdge\msedgedriver_v122.exe"
            driver = Edge(executable_path =executablePath, options = options)
            driver.close()
        #If it is another version try to find or download it 
        except Exception as error:
            #Go search for the suitable version of edge driver
            if 'This version of Microsoft Edge WebDriver only supports Microsoft Edge version 122' in str(error):
                error_version =str(error).split('\n')[1]
                version=error_version.split(' ')[4]
                #Check if the Edge driver isn't already completed
                if not os.path.isfile(r'.\driverEdge\msedgedriver_v'+version.split('.')[0]+".exe"):
                    try : 
                        #Go download the edge driver
                        os.system('start '+'https://msedgedriver.azureedge.net/'+version+'/edgedriver_win64.zip')
                    except:
                        #Ask the user to click on the download link
                        print('Please, with Edge, go to : ' + 'https://msedgedriver.azureedge.net/'+version+'/edgedriver_win64.zip')
                        
                    # spécifiant le nom du fichier zip
                    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
                    #Recupère le dossier téléchargement sans avoir à entrer le user de la session
                    downloads_path = winreg.QueryValueEx(reg_key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]  
                    winreg.CloseKey(reg_key)
                    file = downloads_path+"/edgedriver_win64.zip"
                    
                    #Wait until the file has been downloaded
                    while not os.path.exists(file):
                        time.sleep(1)
                    
                    # ouvrir le fichier zip en mode lecture
                    with ZipFile(file, 'r') as zip: 
                        # extraire tous les fichiers vers un autre répertoire
                        zip.extractall(r'.\driverEdge')
                        os.rename(r'.\driverEdge\msedgedriver.exe', r'.\driverEdge\msedgedriver_v'+version.split('.')[0]+".exe")
                    #delete the zip folder
                    os.remove(downloads_path+"/edgedriver_win64.zip")
                executablePath=r'.\driverEdge\msedgedriver_v'+version.split('.')[0]+".exe"
                
        #Lance la recherche des informations personalisées
        lamarque,lesingredients,lengagement=parfumPerso(entry,options,executablePath)
        #Met les ingredients en forme pour pouvoir les retrouver avec le json Ingredients
        ingredient=miseEnForme(lesingredients)
        # Charger les données Ingredient depuis le fichier JSON
        with open('./Ingredients_data.json', 'r') as fichier_json:
            donnees = json.load(fichier_json)
        return (lamarque,ingredient,lengagement,donnees)
    
    #Fenetre affichage des infromations personalisé
    def Frames(self,root,lamarque,ingredient,lengagement,donnees,entry):
        frame = tk.Frame(root)
        frame.configure(bg="#958BF9",width=900,height=750)
        
        # Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        #Label du Parfum
        Nom=tk.Label(frame)
        Titleft = tkFont.Font(family='Times',size=20)
        Nom["font"] = Titleft#font
        Nom["bg"] = "#958BF9" # Couleur de fond Lila
        Nom["text"] = entry
        Nom.pack()#Placement dans la fenetre
        
        text = Text(frame, yscrollcommand=scrollbar.set,height=45,width=110,wrap=tk.WORD)
        text["bg"] = "#958BF9" # Couleur de fond Lila
        text.pack(fill=BOTH, expand=True)
        
        text.insert(END,"Marque : "+lamarque+"\n\n")
        text.insert(END,"Engagement climatique de la marque : "+lengagement+"\n\n\n")
        text.insert(END,"Ingredients : "+"\n")
        for i in range (10):
            if '/' in ingredient[i]:
                ing=ingredient[i].split('/')[0]
            else:
                ing=ingredient[i].upper()#Enregistre l'ingredient
            #Créer une pharse avec ingredient: description et s'il est pertubateur et/ou allergene
            phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
            text.insert(END,phrase+"\n\n")

        for widget in frame.winfo_children():
            widget.pack()
            
        # Attach the scrollbar to the text widget
        scrollbar.config(command=text.yview)
        
        return frame
    def __init__(self, root,entry):
        #setting title
        self.rootInfos=root
        root.title("Fiche Info : "+entry)
        #setting window size
        width=900
        height=850
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#958BF9")
        
        #Recupère les infromation de la fontion Recherche Perso
        lamarque,ingredient,lengagement,donnees=self.RecherchePerso(entry)
        
        info_frame =self.Frames(root,lamarque,ingredient,lengagement,donnees,entry)
        info_frame.grid(column=0, row=0)
 

    #Lance la fenetre
    def DemarreInfos(self):
        self.rootInfos.mainloop()
        self.rootInfos.withdraw()
            
'''       
if __name__ == "__main__":
    root = tk.Tk()
    app = Perso(root,'Azzaro homme')
    root.mainloop()'''