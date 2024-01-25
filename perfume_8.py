import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from msedge.selenium_tools import Edge, EdgeOptions
import warnings
import os
import winreg
from zipfile import ZipFile
warnings.filterwarnings("ignore")
from ficheInfos import *
from ParfumPerso import *
from web_const_mod import * 
import json

#Main window
class App:  
    #Function that open all the infos of a clicked parfume
    def info(self,informations):
        rootInfos = tk.Tk() #create a new window
        app = FicheInfos(rootInfos,informations) #complete with the information and format from Fiche infos
        app.DemarreInfos() #open second window

    #Function that charged the perfume's infos into the program
    def charger_donnees(self):
        # Charger les données depuis le fichier JSON
        with open('./output_data.json', 'r') as fichier_json:
            self.donnees = json.load(fichier_json)
        return self.donnees['Top']
    
    #Function that search the info and open windows to show infos of a written perfume
    def Personalise(self,entry):
        messagebox.showinfo('Recherche!', "Nous recherchons des informations sur votre parfum.\nCela peut prendre jusqu'à 1 minute.")
        rootPerso = tk.Tk()#create a new window
        app = Perso(rootPerso,entry)#complete with the information and format from Perso
        app.DemarreInfos()#open second window
    
    #Function that update the source json
    def MiseAJour(self):
        #Check if sure 
        Box=messagebox.askquestion('Attention', "La mise à jour prendra autour de 5 minutes.\nEtes vous sur.e?")
        if Box=='yes': #begin the process of updating
        
            #add all the options necessary to begin webscrapping
            messagebox.showinfo('Lancement', "Lancement du programme.\nUn nouveau message s'affichera à la fin de la mise à jour")
            options = EdgeOptions()
            options.use_chromium = True
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.set_capability("acceptInsecureCerts", True)
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
              
            #Begin webscrapping with all the functions from web_wonst_mod.py
            dicParfum,listeMarque,listeIngredient=Sephora(options,executablePath)
            Ingredient,setIngredient=IngredientForme(listeIngredient)
            descIng,Allergene,endo=incibeauty(setIngredient,options,executablePath)
            marqueEco=engagement(listeMarque,options,executablePath)
            jsonIngredient(setIngredient, descIng, Allergene, endo)
            create_json(dicParfum, listeMarque, Ingredient, descIng, Allergene, endo, marqueEco)
            #Update the windows with the new infos
            messagebox.showinfo('Fini!', "La mise à jour est finie.\nLa fenêtre va se relancer.")
            self.master.update()
            self.master.update_idletasks()

    #Create the format of the windows
    def __init__(self, root):
        self.master = root  # Ajoutez cette ligne pour fixer l'erreur AttributeError
        root.title("Perfume_clim'mate")
        data = self.charger_donnees()
        # setting window size
        width = 900
        height = 800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#444444")
        
        #Label du titre 
        Title = tk.Label(root)
        Titleft = tkFont.Font(family='Times', size=28)
        Title["font"] = Titleft #font
        Title["fg"] = "white"  # Couleur du texte en blanc
        Title["justify"] = "center" #alignement du texte
        Title["text"] = "Perfume clim'mate"
        Title.place(x=210, y=40, width=500, height=30) #Placement dans la fenetre
        Title["bg"] = "#444444"  # Couleur de fond Gris charbonParfumPerso=tk.Entry(root)
        
        #Bouton de mise à jour
        MaJ = tk.Button(root)
        MaJ["bg"] = "#0c5858" #Couleur bouton
        ft = tkFont.Font(family='Times', size=9)
        MaJ["font"] = ft #font
        MaJ["fg"] = "#f5f0f0" #Couleur font
        MaJ["justify"] = "center"#alignement du texte
        MaJ["text"] = "Mise à jour des données"
        MaJ.place(x=650, y=70, width=150, height=40)#Placement dans la fenetre
        MaJ["command"] = lambda:self.MiseAJour() #Applique la fonction de mise à jour
        
        #Bouton quitter
        Quit = Button(root, text ="Quitter", command = root.destroy) 
        Quit["bg"] = "#0c5858" #Couleur bouton
        ft = tkFont.Font(family='Times', size=9)
        Quit["font"] = ft #font
        Quit["fg"] = "#f5f0f0" #Couleur font
        Quit["justify"] = "center"#alignement du texte
        Quit.place(x=120, y=70, width=150, height=40)
        
        #Input du parfum personalisé
        ParfumPerso=tk.Entry()
        ParfumPerso["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ParfumPerso["font"] = ft #font
        ParfumPerso["fg"] = "#333333" #Couleur font
        ParfumPerso["justify"] = "center" #alignement du texte
        ParfumPerso["text"] = "Rentrer le nom de votre parfum"
        ParfumPerso.place(x=340,y=90,width=200,height=30)  #Placement dans la fenetre
        
        #Bouton de recherche de parfum personalisé
        button = tk.Button(root, text="Search", command=lambda:self.Personalise(ParfumPerso.get()))  #Applique la fonction de personalisation
        button.place(x=540,y=90,height=30) #Placement dans la fenetre
        
        #Label du Top parfum
        TopParfum = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        TopParfum["font"] = ft #font
        TopParfum["fg"] = "white"  # Couleur du texte en blanc
        TopParfum["justify"] = "center"#alignement du texte
        TopParfum["text"] = "Top 10 parfum"
        TopParfum.place(x=340, y=140, width=180, height=40) #Placement dans la fenetre
        TopParfum["bg"] = "#444444" #Couleur du fond

        #Set the font for the button
        ft = tkFont.Font(family='Times',size=10)
        
        #Bouton du parfum 1
        perfume_1=tk.Button(root)
        perfume_1["bg"] = "#0c5858" #Couleur du fond
        perfume_1["font"] = ft #font
        perfume_1["fg"] = "#f1eaea" #Couleur font
        perfume_1["justify"] = "center" #alignement du texte
        perfume_1["text"] = str(data[0]['name']) #Texte du parfum n°1
        perfume_1.place(x=190,y=200,width=500,height=50)#Placement dans la fenetre
        perfume_1["command"] = lambda:self.info(data[0]) #Applique la fonction de info pour le parfum 1
        
        #Bouton du parfum 2
        perfume_2 = tk.Button(root)
        perfume_2["bg"] = "#275e58" #Couleur du fond
        perfume_2["font"] = ft #font
        perfume_2["fg"] = "#f5f0f0"  #Couleur font
        perfume_2["justify"] = "center"#alignement du texte
        perfume_2["text"] = str(data[1]['name']) #Texte du parfum n°2
        perfume_2.place(x=190, y=260, width=500, height=50)#Placement dans la fenetre
        perfume_2["command"] = lambda:self.info(data[1]) #Applique la fonction de info pour le parfum 2
        
        #Bouton du parfum 3
        perfume_3 = tk.Button(root)
        perfume_3["bg"] = "#196760" #Couleur du fond
        perfume_3["font"] = ft #font
        perfume_3["fg"] = "#f8fcfc"  #Couleur font
        perfume_3["justify"] = "center" #alignement du texte
        perfume_3["text"] = str(data[2]['name']) #Texte du parfum n°3
        perfume_3.place(x=190, y=320, width=500, height=50)#Placement dans la fenetre
        perfume_3["command"] = lambda:self.info(data[2]) #Applique la fonction de info pour le parfum 3
        
        #Bouton du parfum 4
        perfume_4 = tk.Button(root)
        perfume_4["bg"] = "#2c7e76" #Couleur du fond
        perfume_4["disabledforeground"] = "#009688"
        perfume_4["font"] = ft #font 
        perfume_4["fg"] = "#eef5f4"  #Couleur font
        perfume_4["justify"] = "center" #alignement du texte
        perfume_4["text"] = str(data[3]['name']) #Texte du parfum n°4
        perfume_4.place(x=190, y=380, width=500, height=50)#Placement dans la fenetre
        perfume_4["command"] = lambda:self.info(data[3]) #Applique la fonction de info pour le parfum 4

        #Bouton du parfum 5
        perfume_5 = tk.Button(root)
        perfume_5["bg"] = "#338b83" #Couleur du fond
        perfume_5["font"] = ft #font 
        perfume_5["fg"] = "#edf5f4" #Couleur font
        perfume_5["justify"] = "center" #alignement du texte
        perfume_5["text"] = str(data[4]['name']) #Texte du parfum n°5
        perfume_5.place(x=190, y=440, width=500, height=50) #Placement dans la fenetre
        perfume_5["command"] = lambda:self.info(data[4])#Applique la fonction de info pour le parfum 5

        #Bouton du parfum 6
        perfume_6 = tk.Button(root)
        perfume_6["bg"] = "#309389" #Couleur du fond
        perfume_6["font"] = ft #font 
        perfume_6["fg"] = "#f0f4f3" #Couleur font
        perfume_6["justify"] = "center" #alignement du texte
        perfume_6["text"] = str(data[5]['name']) #Texte du parfum n°6
        perfume_6.place(x=190, y=500, width=500, height=50) #Placement dans la fenetre
        perfume_6["command"] = lambda:self.info(data[5])#Applique la fonction de info pour le parfum 6

        #Bouton du parfum 7
        perfume_7 = tk.Button(root)
        perfume_7["bg"] = "#37a398" #Couleur du fond
        perfume_7["font"] = ft #font 
        perfume_7["fg"] = "#f2f7f6" #Couleur font
        perfume_7["justify"] = "center" #alignement du texte
        perfume_7["text"] = str(data[6]['name']) #Texte du parfum n°7
        perfume_7.place(x=190, y=560, width=500, height=50) #Placement dans la fenetre
        perfume_7["command"] = lambda:self.info(data[6])#Applique la fonction de info pour le parfum 7
        
        #Bouton du parfum 8
        perfume_8 = tk.Button(root)
        perfume_8["bg"] = "#4da9a0" #Couleur du fond
        perfume_8["font"] = ft #font 
        perfume_8["fg"] = "#eff5f5"#Couleur font
        perfume_8["justify"] = "center"  #alignement du texte
        perfume_8["text"] = str(data[7]['name']) #Texte du parfum n°8
        perfume_8.place(x=190, y=620, width=500, height=50) #Placement dans la fenetre
        perfume_8["command"] = lambda:self.info(data[7])#Applique la fonction de info pour le parfum 8
        
        #Bouton du parfum 9
        perfume_9 = tk.Button(root)
        perfume_9["bg"] = "#4db0a6" #Couleur du fond
        perfume_9["font"] = ft #font 
        perfume_9["fg"] = "#f2f5f5" #Couleur font
        perfume_9["justify"] = "center"  #alignement du texte
        perfume_9["text"] = str(data[8]['name']) #Texte du parfum n°9
        perfume_9.place(x=190, y=680, width=500, height=50) #Placement dans la fenetre
        perfume_9["command"] = lambda:self.info(data[8])#Applique la fonction de info pour le parfum 9
    
        #Bouton du parfum 10
        perfume_10 = tk.Button(root)
        perfume_10["bg"] = "#52b8ae" #Couleur du fond
        perfume_10["font"] = ft #font 
        perfume_10["fg"] = "#edf5f4" #Couleur font
        perfume_10["justify"] = "center"  #alignement du texte
        perfume_10["text"] = str(data[9]['name']) #Texte du parfum n°10
        perfume_10.place(x=190, y=740, width=500, height=50) #Placement dans la fenetre
        perfume_10["command"] = lambda:self.info(data[9])#Applique la fonction de info pour le parfum 10
        

    #Demarre et redemarre la fenetre principale
    def demarrer(self):
        # Démarrer l'application
        self.master.mainloop()
        self.master.withdraw()


