import tkinter as tk
import tkinter.font as tkFont
from Projet_Webcrapping_2 import * 
from web_const_mod import * 
import json

class Perso:
    def RecherchePerso(self,entry):
        options = EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.set_capability("acceptInsecureCerts", True)
        #options.add_argument('headless') #hide the browser
        #Try to connect if the edgeriver version is 108
        options.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        lamarque,lesingredients,lengagement=parfumPerso(entry,options)
        ingredient=miseEnForme(lesingredients)
        # Charger les données depuis le fichier JSON
        with open('./Ingredients_data.json', 'r') as fichier_json:
            donnees = json.load(fichier_json)
        return (lamarque,ingredient,lengagement,donnees)
    
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
        
        lamarque,ingredient,lengagement,donnees=self.RecherchePerso(entry)

        Nom=tk.Label(root)
        Titleft = tkFont.Font(family='Times',size=20)
        Nom["font"] = Titleft
        Nom["bg"] = "#958BF9"
        Nom["text"] = entry
        Nom.grid(column=0, row = 0, columnspan=3)

        Marque=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Marque["font"] = ft
        Marque["fg"] = "black"
        Marque["bg"] = "#958BF9"
        Marque["text"] = "Marque : "+lamarque
        Marque.grid(column=0, row = 1,sticky="W")

        Engagement=tk.Label(root)
        Engagement["font"] = ft
        Engagement["fg"] = "black"
        Engagement["bg"] = "#958BF9"
        Engagement['wraplength']=875
        Engagement["text"] = "Engagement climatique de la marque : "+lengagement
        Engagement.grid(column=0, row = 2,columnspan=2,sticky="W")

        Ingredients=tk.Label(root)
        Ingredients["font"] = ft
        Ingredients["fg"] = "black"
        Ingredients["bg"] = "#958BF9"
        Ingredients["text"] = "Ingredients : "
        Ingredients.grid(column=0, row = 3, sticky="W")
        
        ing=ingredient[0][0].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" : Pas d'information trouvée"
        Ing1=tk.Label(root)
        Ingft = tkFont.Font(family='Times',size=9)
        Ing1["font"] = Ingft
        Ing1["fg"] = "black"
        Ing1["justify"] = "left"
        Ing1['wraplength']=875
        Ing1["bg"] = "#958BF9"
        Ing1["text"] = phrase
        Ing1.grid(column=0, row = 4, columnspan=2,sticky="W")

        ing=ingredient[0][1].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing2=tk.Label(root)
        Ing2["font"] = Ingft
        Ing2["fg"] = "black"
        Ing2["justify"] = "left"
        Ing2['wraplength']=875
        Ing2["bg"] = "#958BF9"
        Ing2["text"] = phrase
        Ing2.grid(column=0, row = 5, columnspan=2,sticky="W")

        ing=ingredient[0][2].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing3=tk.Label(root)
        Ing3["font"] = Ingft
        Ing3["fg"] = "black"
        Ing3["justify"] = "left"
        Ing3['wraplength']=875
        Ing3["bg"] = "#958BF9"
        Ing3["text"] = phrase
        Ing3.grid(column=0, row = 6, columnspan=2,sticky="W")

        ing=ingredient[0][3].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing4=tk.Label(root)
        Ing4["font"] = Ingft
        Ing4["fg"] = "black"
        Ing4["justify"] = "left"
        Ing4['wraplength']=875
        Ing4["bg"] = "#958BF9"
        Ing4["text"] = phrase
        Ing4.grid(column=0, row = 7, columnspan=3,sticky="W")

        ing=ingredient[0][4].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing5=tk.Label(root)
        Ing5["font"] = Ingft
        Ing5["fg"] = "black"
        Ing5["justify"] = "left"
        Ing5['wraplength']=875
        Ing5["bg"] = "#958BF9"
        Ing5["text"] = phrase
        Ing5.grid(column=0, row = 8, columnspan=3,sticky="W")

        ing=ingredient[0][5].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing6=tk.Label(root)
        Ing6["font"] = Ingft
        Ing6["fg"] = "black"
        Ing6["justify"] = "left"
        Ing6['wraplength']=875
        Ing6["bg"] = "#958BF9"
        Ing6["text"] = phrase
        Ing6.grid(column=0, row = 9, columnspan=3,sticky="W")
  
        ing=ingredient[0][6].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing7=tk.Label(root)
        Ing7["font"] = Ingft
        Ing7["fg"] = "black"
        Ing7["justify"] = "left"
        Ing7['wraplength']=875
        Ing7["bg"] = "#958BF9"
        Ing7["text"] = phrase
        Ing7.grid(column=0, row = 10, columnspan=3,sticky="W")

        ing=ingredient[0][7].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing8=tk.Label(root)
        Ing8["font"] = Ingft
        Ing8["fg"] = "black"
        Ing8["justify"] = "left"
        Ing8['wraplength']=875
        Ing8["bg"] = "#958BF9"
        Ing8["text"] = phrase
        Ing8.grid(column=0, row = 11, columnspan=3,sticky="W")

        ing=ingredient[0][8].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing9=tk.Label(root)
        Ing9["font"] = Ingft
        Ing9["fg"] = "black"
        Ing9["justify"] = "left"
        Ing9['wraplength']=875
        Ing9["bg"] = "#958BF9"
        Ing9["text"] = phrase
        Ing9.grid(column=0, row = 12, columnspan=3,sticky="W")

        ing=ingredient[0][9].upper()
        phrase=ing+" : "+donnees[ing]['description']+"\n"+donnees[ing]['endocrinien']+" et "+donnees[ing]['allergène'] if ing in donnees.keys() else ing+" :Pas d'information trouvée"
        Ing10=tk.Label(root)
        Ing10["font"] = Ingft
        Ing10["fg"] = "black"
        Ing10["justify"] = "left"
        Ing10['wraplength']=875
        Ing10["bg"] = "#958BF9"
        Ing10["text"] = phrase
        Ing10.grid(column=0, row = 13, columnspan=3,sticky="W")

        '''GLabel_852=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_852["font"] = ft
        GLabel_852["fg"] = "#333333"
        GLabel_852["justify"] = "left"
        GLabel_852["text"] = "label"
        GLabel_852.place(x=50,y=500,width=262,height=40)'''
        
    def DemarreInfos(self):
        self.rootInfos.mainloop()
        self.rootInfos.withdraw()
            
'''       
if __name__ == "__main__":
    root = tk.Tk()
    app = Perso(root,'Azzaro homme')
    root.mainloop()'''