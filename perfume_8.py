import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import sys
from ficheInfos import *
from ParfumPerso import *
#sys.path.append('c:/users/fouzari/appdata/local/programs/python/python312/lib/site-packages')
import json

class CustomButton(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.configure(
            bg="#444444",  
            borderwidth=0,
            relief="flat"
        )

        # Charger l'image avec un fond transparent
        image_path = "./cert.png"
        image = Image.open(image_path).convert("RGBA")
        resized_image = image.resize((30, 30), Image.BILINEAR)
        #self.photo = ImageTk.PhotoImage(resized_image,master=None)

        # Ajouter l'image à gauche du texte
        '''self.config(
            image=self.photo,
            compound="left",
            font=("Helvetica", 12),
            fg="white"
        )'''

class App:  

    def info(self,informations):
        rootInfos = tk.Tk()
        app = FicheInfos(rootInfos,informations)
        app.DemarreInfos()

    def charger_donnees(self):
        # Charger les données depuis le fichier JSON
        with open('./output_data.json', 'r') as fichier_json:
            self.donnees = json.load(fichier_json)
        return self.donnees['Top']
    
    def Personalise(self,entry):
        rootPerso = tk.Tk()
        app = Perso(rootPerso,entry)
        app.DemarreInfos()

    def __init__(self, root):
        self.master = root  # Ajoutez cette ligne pour fixer l'erreur AttributeError
        root.title("Perfume_clim'mate")
        data = self.charger_donnees()
        # setting window size
        width = 900
        height = 850
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#444444")
        
        Title = tk.Label(root)
        ft = tkFont.Font(family='Times', size=28)
        Title["font"] = ft
        Title["fg"] = "white"  # Couleur du texte en blanc
        Title["justify"] = "center"
        Title["text"] = "Perfume clim'mate"
        Title["relief"] = "flat"
        Title.place(x=210, y=40, width=500, height=30)
        Title["bg"] = "#444444"  # Couleur de fond Gris charbonParfumPerso=tk.Entry(root)
        
        ParfumPerso=tk.Entry()
        ParfumPerso["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ParfumPerso["font"] = ft
        ParfumPerso["fg"] = "#333333"
        ParfumPerso["justify"] = "center"
        ParfumPerso["text"] = "Rentrer le nom de votre parfum"
        ParfumPerso["relief"] = "flat"
        ParfumPerso.place(x=340,y=90,width=200,height=30)  
        
        button = tk.Button(root, text="Search", command=lambda:self.Personalise(ParfumPerso.get())) 
        button.place(x=540,y=90,height=30) 
        
        TopParfum = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        TopParfum["font"] = ft
        TopParfum["fg"] = "white"  # Couleur du texte en blanc
        TopParfum["justify"] = "center"
        TopParfum["text"] = "Top 10 parfum"
        TopParfum["relief"] = "flat"
        TopParfum.place(x=340, y=140, width=180, height=40)
        TopParfum["bg"] = "#444444"
        
        #custom_button = CustomButton(root)
        #custom_button.place(x=560, y=128)

        perfume_1=tk.Button(root)
        perfume_1["bg"] = "#0c5858"
        ft = tkFont.Font(family='Times',size=10)
        perfume_1["font"] = ft
        perfume_1["fg"] = "#f1eaea"
        perfume_1["justify"] = "center"
        perfume_1["text"] = str(data[0]['name'])
        perfume_1.place(x=190,y=200,width=500,height=50)
        perfume_1["command"] = lambda:self.info(data[0])
        
        perfume_2 = tk.Button(root)
        perfume_2["bg"] = "#275e58"
        ft = tkFont.Font(family='Times', size=10)
        perfume_2["font"] = ft
        perfume_2["fg"] = "#f5f0f0"
        perfume_2["justify"] = "center"
        perfume_2["text"] = str(data[1]['name'])
        perfume_2.place(x=190, y=260, width=500, height=50)
        perfume_2["command"] = lambda:self.info(data[1])
        
        perfume_3 = tk.Button(root)
        perfume_3["bg"] = "#196760"
        ft = tkFont.Font(family='Times', size=10)
        perfume_3["font"] = ft
        perfume_3["fg"] = "#f8fcfc"
        perfume_3["justify"] = "center"
        perfume_3["text"] = str(data[2]['name'])
        perfume_3.place(x=190, y=320, width=500, height=50)
        perfume_3["command"] = lambda:self.info(data[2])
        
        perfume_4 = tk.Button(root)
        perfume_4["bg"] = "#2c7e76"
        perfume_4["disabledforeground"] = "#009688"
        ft = tkFont.Font(family='Times', size=10)
        perfume_4["font"] = ft
        perfume_4["fg"] = "#eef5f4"
        perfume_4["justify"] = "center"
        perfume_4["text"] = str(data[3]['name'])
        perfume_4.place(x=190, y=380, width=500, height=50)
        perfume_4["command"] = lambda:self.info(data[3])

        perfume_5 = tk.Button(root)
        perfume_5["bg"] = "#338b83"
        ft = tkFont.Font(family='Times', size=10)
        perfume_5["font"] = ft
        perfume_5["fg"] = "#edf5f4"
        perfume_5["justify"] = "center"
        perfume_5["text"] = str(data[4]['name'])
        perfume_5.place(x=190, y=440, width=500, height=50)
        perfume_5["command"] = lambda:self.info(data[4])

        perfume_6 = tk.Button(root)
        perfume_6["bg"] = "#309389"
        ft = tkFont.Font(family='Times', size=10)
        perfume_6["font"] = ft
        perfume_6["fg"] = "#f0f4f3"
        perfume_6["justify"] = "center"
        perfume_6["text"] = str(data[5]['name'])
        perfume_6.place(x=190, y=500, width=500, height=50)
        perfume_6["command"] = lambda:self.info(data[5])

        perfume_7 = tk.Button(root)
        perfume_7["bg"] = "#37a398"
        ft = tkFont.Font(family='Times', size=10)
        perfume_7["font"] = ft
        perfume_7["fg"] = "#f2f7f6"
        perfume_7["justify"] = "center"
        perfume_7["text"] = str(data[6]['name'])
        perfume_7.place(x=190, y=560, width=500, height=50)
        perfume_7["command"] = lambda:self.info(data[6])
        
        perfume_8 = tk.Button(root)
        perfume_8["bg"] = "#4da9a0"
        ft = tkFont.Font(family='Times', size=10)
        perfume_8["font"] = ft
        perfume_8["fg"] = "#eff5f5"
        perfume_8["justify"] = "center"
        perfume_8["text"] = str(data[7]['name'])
        perfume_8.place(x=190, y=620, width=500, height=50)
        perfume_8["command"] = lambda:self.info(data[7])
        
        perfume_9 = tk.Button(root)
        perfume_9["bg"] = "#4db0a6"
        ft = tkFont.Font(family='Times', size=10)
        perfume_9["font"] = ft
        perfume_9["fg"] = "#f2f5f5"
        perfume_9["justify"] = "center"
        perfume_9["text"] = str(data[8]['name'])
        perfume_9.place(x=190, y=680, width=500, height=50)
        perfume_9["command"] = lambda:self.info(data[8])
        
        perfume_10 = tk.Button(root)
        perfume_10["bg"] = "#52b8ae"
        ft = tkFont.Font(family='Times', size=10)
        perfume_10["font"] = ft
        perfume_10["fg"] = "#edf5f4"
        perfume_10["justify"] = "center"
        perfume_10["text"] = str(data[9]['name'])
        perfume_10.place(x=190, y=740, width=500, height=50)
        perfume_10["command"] = lambda:self.info(data[9])
        

        
        
    def demarrer(self):
        # Démarrer votre application
        self.master.mainloop()
        self.master.withdraw()


