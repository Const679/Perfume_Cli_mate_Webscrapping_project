import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from selenium.webdriver.edge.options import Options as EdgeOptions
import sys
sys.path.append('c:/users/fouzari/appdata/local/programs/python/python312/lib/site-packages')
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
        image_path = "C:/Users/fouzari/Desktop/web_scrapp/cert.png"
        image = Image.open(image_path).convert("RGBA")
        resized_image = image.resize((30, 30), Image.BILINEAR)
        self.photo = ImageTk.PhotoImage(resized_image)

        # Ajouter l'image à gauche du texte
        self.config(
            image=self.photo,
            compound="left",
            font=("Helvetica", 12),
            fg="white"
        )

class App:  

    def info(self):
        print("hello")

    def charger_donnees(self):
        # Charger les données depuis le fichier JSON
        with open('C:/Users/fouzari/Desktop/web_scrapp/JSONS/data.json', 'r') as fichier_json:
            self.donnees = json.load(fichier_json)
        return self.donnees

    def __init__(self, root):
        self.master = root  # Ajoutez cette ligne pour fixer l'erreur AttributeError
        root.title("Perfume_clim'mate")
        data = self.charger_donnees()
        # setting window size
        width = 1000
        height = 1000
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#444444")
        
        
        custom_button = CustomButton(root)
        custom_button.place(x=560, y=128)

        perfume_1=tk.Button(root)
        perfume_1["bg"] = "#0c5858"
        ft = tkFont.Font(family='Times',size=10)
        perfume_1["font"] = ft
        perfume_1["fg"] = "#f1eaea"
        perfume_1["justify"] = "center"
        perfume_1["text"] = str(data["perfumes"]["1"])
        perfume_1.place(x=190,y=240,width=500,height=50)
        perfume_1["command"] = self.info
        
        perfume_2 = tk.Button(root)
        perfume_2["bg"] = "#275e58"
        ft = tkFont.Font(family='Times', size=10)
        perfume_2["font"] = ft
        perfume_2["fg"] = "#f5f0f0"
        perfume_2["justify"] = "center"
        perfume_2["text"] = str(data["perfumes"]["2"])
        perfume_2.place(x=190, y=300, width=500, height=50)
        perfume_2["command"] = self.info
        
        perfume_3 = tk.Button(root)
        perfume_3["bg"] = "#196760"
        ft = tkFont.Font(family='Times', size=10)
        perfume_3["font"] = ft
        perfume_3["fg"] = "#f8fcfc"
        perfume_3["justify"] = "center"
        perfume_3["text"] = str(data["perfumes"]["3"])
        perfume_3.place(x=190, y=360, width=500, height=50)
        perfume_3["command"] = self.info
        
        perfume_4 = tk.Button(root)
        perfume_4["bg"] = "#2c7e76"
        perfume_4["disabledforeground"] = "#009688"
        ft = tkFont.Font(family='Times', size=10)
        perfume_4["font"] = ft
        perfume_4["fg"] = "#eef5f4"
        perfume_4["justify"] = "center"
        perfume_4["text"] = str(data["perfumes"]["4"])
        perfume_4.place(x=190, y=420, width=500, height=50)
        perfume_4["command"] = self.info

        perfume_5 = tk.Button(root)
        perfume_5["bg"] = "#338b83"
        ft = tkFont.Font(family='Times', size=10)
        perfume_5["font"] = ft
        perfume_5["fg"] = "#edf5f4"
        perfume_5["justify"] = "center"
        perfume_5["text"] = str(data["perfumes"]["5"])
        perfume_5.place(x=190, y=480, width=500, height=50)
        perfume_5["command"] = self.info

        perfume_6 = tk.Button(root)
        perfume_6["bg"] = "#309389"
        ft = tkFont.Font(family='Times', size=10)
        perfume_6["font"] = ft
        perfume_6["fg"] = "#f0f4f3"
        perfume_6["justify"] = "center"
        perfume_6["text"] = str(data["perfumes"]["6"])
        perfume_6.place(x=190, y=540, width=500, height=50)
        perfume_6["command"] = self.info

        perfume_7 = tk.Button(root)
        perfume_7["bg"] = "#37a398"
        ft = tkFont.Font(family='Times', size=10)
        perfume_7["font"] = ft
        perfume_7["fg"] = "#f2f7f6"
        perfume_7["justify"] = "center"
        perfume_7["text"] = str(data["perfumes"]["7"])
        perfume_7.place(x=190, y=600, width=500, height=50)
        perfume_7["command"] = self.info
        
        perfume_8 = tk.Button(root)
        perfume_8["bg"] = "#4da9a0"
        ft = tkFont.Font(family='Times', size=10)
        perfume_8["font"] = ft
        perfume_8["fg"] = "#eff5f5"
        perfume_8["justify"] = "center"
        perfume_8["text"] = str(data["perfumes"]["8"])
        perfume_8.place(x=190, y=660, width=500, height=50)
        perfume_8["command"] = self.info
        
        perfume_9 = tk.Button(root)
        perfume_9["bg"] = "#4db0a6"
        ft = tkFont.Font(family='Times', size=10)
        perfume_9["font"] = ft
        perfume_9["fg"] = "#f2f5f5"
        perfume_9["justify"] = "center"
        perfume_9["text"] = str(data["perfumes"]["9"])
        perfume_9.place(x=190, y=720, width=500, height=50)
        perfume_9["command"] = self.info
        
        perfume_10 = tk.Button(root)
        perfume_10["bg"] = "#52b8ae"
        ft = tkFont.Font(family='Times', size=10)
        perfume_10["font"] = ft
        perfume_10["fg"] = "#edf5f4"
        perfume_10["justify"] = "center"
        perfume_10["text"] = str(data["perfumes"]["10"])
        perfume_10.place(x=190, y=780, width=500, height=50)
        perfume_10["command"] = self.info
        
        GLabel_89 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=28)
        GLabel_89["font"] = ft
        GLabel_89["fg"] = "white"  # Couleur du texte en blanc
        GLabel_89["justify"] = "center"
        GLabel_89["text"] = "Perfume clim'mate"
        GLabel_89["relief"] = "flat"
        GLabel_89.place(x=210, y=40, width=500, height=30)
        GLabel_89["bg"] = "#444444"  # Couleur de fond Gris charbon

        GLabel_750 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_750["font"] = ft
        GLabel_750["fg"] = "white"  # Couleur du texte en blanc
        GLabel_750["justify"] = "center"
        GLabel_750["text"] = "Top 10 parfum"
        GLabel_750["relief"] = "flat"
        GLabel_750.place(x=340, y=180, width=180, height=40)
        GLabel_750["bg"] = "#444444"

        GLineEdit_954=tk.Entry(root)
        GLineEdit_954["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_954["font"] = ft
        GLineEdit_954["fg"] = "#333333"
        GLineEdit_954["justify"] = "center"
        GLineEdit_954["text"] = "Entry"
        GLineEdit_954["relief"] = "flat"
        GLineEdit_954.place(x=340,y=130,width=200,height=30)
        
        
    def demarrer(self):
        # Démarrer votre application
        self.master.mainloop()
        self.master.withdraw()


