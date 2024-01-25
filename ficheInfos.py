from tkscrolledframe import ScrolledFrame
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

#Second Window
class FicheInfos:
    #Create the format of the windows
    def Frames(self,root,info):
        frame = tk.Frame(root)
        frame.configure(bg="#958BF9",width=900,height=750)
        
        # Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        #Label du titre
        Nom=tk.Label(frame)
        Titleft = tkFont.Font(family='Times',size=22)
        Nom["font"] = Titleft#font
        Nom["bg"] = "#958BF9"# Couleur de fond Lila
        Nom["text"] = info['name']
        Nom.pack()
        
        text = Text(frame, yscrollcommand=scrollbar.set,height=45,width=110,wrap=tk.WORD)
        text["bg"] = "#958BF9" # Couleur de fond Lila
        text.pack(fill=BOTH, expand=True)
        
        text.insert(END,"Marque : "+info['brand']['name']+"\n\n")
        text.insert(END,"Engagement climatique de la marque : "+info['brand']['engagement']+"\n\n\n")
        text.insert(END,"Ingredients : "+"\n")
        for i in range (10):
            ingredient=info['Ingredient']
            text.insert(END,ingredient[i]['name']+" : "+ingredient[i]['description']+"\n"+ingredient[i]['endocrinien']+" et "+ingredient[i]['allergène']+"\n\n")

        for widget in frame.winfo_children():
            widget.pack()
            
        # Attach the scrollbar to the text widget
        scrollbar.config(command=text.yview)
        
        return frame
        
    def __init__(self, root,info):
        #setting title
        self.rootInfos=root
        root.title("Fiche Info : "+info['name'])
        #setting window size
        width=900
        height=750
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)        
        root.configure(bg="#958BF9")
        
        info_frame =self.Frames(root,info)
        info_frame.grid(column=0, row=0)

    #Lance la fenetre
    def DemarreInfos(self):
        self.rootInfos.mainloop()
        self.rootInfos.withdraw()
            
'''  
if __name__ == "__main__":
    infos1={'keys': 1, 'name': 'Gentleman Society - Eau De Parfum pour homme', 'brand': {'name': 'GIVENCHY', 'engagement': 'Sans engagement'}, 'Ingredient': [{'name': 'ALCOHOL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR L'alcool cétéarylique appartient à la famille des alcools gras. Il est utilisé en tant qu'émollient. Il permet d'épaissir les crèmes et de les stabiliser. Il adoucit et protège la peau sans effet gras. L'alcool cétéarylique contient principalement de l'alcool cetylique (Cetyl alcohol) et de l'alcool stearylique (Stearyl alcohol). Il est autorisé en bio.  Le CIR (Cosmetic Ingredient Review) dans un rapport annuel publié en 2008, a conclut à l'innocuité des alcools gras."}, {'name': 'PARFUM (FRAGRANCE)', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Derrière ce terme de parfum, se cachent malheureusement de nombreuses molécules odorantes potentiellement irritantes voire allergisantes. Difficile de s'y retrouver lorsque que l'on devient allergique à un produit et que l'information n'est pas plus détaillée que cela. Néanmoins, pour nous aider, l'Europe a réglementé 24 molécules qui, lorsqu'elles sont utilisées au delà d'une certaine concentration, doivent être mentionnées dans la liste INCI (en général à la fin), bien que faisant partie elles-mêmes du parfum d'un produit. C'est le cas par exemple du Limonène, du linalol..."}, {'name': 'AQUA (WATER)', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR L'eau est l'ingrédient le plus utilisé en cosmétique : 83% des produits en contiennent (pourcentage établi à partir de 50 000 produits de l'App Inci Beauty). L'eau étant d'origine minérale, elle ne pourra jamais être certifiée Bio. C'est la raison pour laquelle les labels Bio, pour certifier les produits, autorisent des minimums d'ingrédients biologiques assez bas (10% pour Ecocert) sur le total d'une formule, en prenant en compte que la présence d'eau non Bio est indispensable et souvent majoritaire dans de nombreux cas."}, {'name': 'LIMONENE', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Linalol est un composé aromatique classé parmi les 24 allergènes réglementés par l'Europe. Il est présent à l'état naturel dans les huiles essentielles de thym, de lavande, de lavandin, de pin sylvestre ou de menthe poivrée... On le retrouve aussi dans de nombreux extraits (citron, orange, verveine...)."}, {'name': 'LINALOOL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Linalol est un composé aromatique classé parmi les 24 allergènes réglementés par l'Europe. Il est présent à l'état naturel dans les huiles essentielles de thym, de lavande, de lavandin, de pin sylvestre ou de menthe poivrée... On le retrouve aussi dans de nombreux extraits (citron, orange, verveine...)."}, {'name': 'COUMARIN', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Tocophérol représente différentes composantes de la Vitamine E. Il est utilisé en cosmétique pour ses propriétés antioxydantes. Cet ingrédient liposoluble (qui se dissout dans l'huile) se trouve à l'état naturel dans des huiles végétales comme l'huile de palme, de tournesol ou encore de germe de blé ... En 2014, le Tocopherol a fait l'objet d'une nouvelle étude du CIR ainsi que 13 autres dérivés de la vitamine E. L'organisme a conclu a son innocuité. Notez que le Tocopherol peut être d'origine synthétique (fabriqué entièrement en laboratoire)."}, {'name': 'BUTYL METHOXYDIBENZOYLMETHANE', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le beurre de karité est obtenu à partir du fruit (les noix) du karité, un arbre présent majoritairement sur le continent Africain. Il est composé principalement de triglycérides, d'acides gras, des esters de cire et d'actifs : parmi ceux-ci, des vitamines (A, D, E), des esters résineux, des phytostérols, du latex. Il est utilisé dans de nombreux cosmétiques pour ses propriétés assoupissantes et adoucissantes pour l'épiderme. Il peut aussi protéger la peau et le cuir chevelu des nombreuses agressions extérieures."}, {'name': 'ALPHA-ISOMETHYL IONONE', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Cette molécule synthétique incolore utilisée en parfumerie, fait partie des 24 allergènes réglementés par l'Europe. Ses senteurs florales sont proches de celles de la violette ou de l'iris."}, {'name': 'CITRAL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Citral est un agent parfumant faisant partie des 24 allergènes réglementés par l'Europe. Il est présent en quantité importante dans l'huile de citronnelle, mais aussi dans les huiles essentielles de verveine, d'orange, de citron... Il est utilisé comme composant aromatique en cosmétique pour ses odeurs de citron. Il est constitué par un mélange des deux isomères géométriques le géranial et le néral."}, {'name': 'GERANIOL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Géraniol aussi nommé rhodinol, est un alcool monoterpénique qui fait partie des 24 allergènes réglementés par l'Europe. On le retrouve présent dans les huiles essentielles de Géranium, de citronnelle mais aussi dans l'huile de rose et de Palmarosa. Il est utilisé en parfumerie pour son odeur de rose."}]}
    root = tk.Tk()
    app = FicheInfos(root,infos1)
    root.mainloop()'''


