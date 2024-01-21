
import tkinter as tk
import tkinter.font as tkFont

class FicheInfos:
    def __init__(self, root,info):
        #setting title
        self.rootInfos=root
        root.title("Fiche Info : "+info['name'])
        #setting window size
        width=900
        height=850
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#958BF9")
        

        Nom=tk.Label(root)
        Titleft = tkFont.Font(family='Times',size=20)
        Nom["font"] = Titleft
        Nom["bg"] = "#958BF9"
        Nom["text"] = info['name']
        Nom.grid(column=0, row = 0, columnspan=3)

        Marque=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Marque["font"] = ft
        Marque["fg"] = "black"
        Marque["bg"] = "#958BF9"
        Marque["text"] = "Marque : "+info['brand']['name']
        Marque.grid(column=0, row = 1,sticky="W")

        Engagement=tk.Label(root)
        Engagement["font"] = ft
        Engagement["fg"] = "black"
        Engagement["bg"] = "#958BF9"
        Engagement['wraplength']=875
        Engagement["text"] = "Engagement climatique de la marque : "+info['brand']['engagement']
        Engagement.grid(column=0, row = 2,columnspan=2,sticky="W")

        Ingredients=tk.Label(root)
        Ingredients["font"] = ft
        Ingredients["fg"] = "black"
        Ingredients["bg"] = "#958BF9"
        Ingredients["text"] = "Ingredients : "
        Ingredients.grid(column=0, row = 3, sticky="W")

        ingredient=info['Ingredient']
        Ing1=tk.Label(root)
        Ingft = tkFont.Font(family='Times',size=9)
        Ing1["font"] = Ingft
        Ing1["fg"] = "black"
        Ing1["justify"] = "left"
        Ing1['wraplength']=875
        Ing1["bg"] = "#958BF9"
        Ing1["text"] = ingredient[0]['name']+" : "+ingredient[0]['description']+"\n"+ingredient[0]['endocrinien']+" et "+ingredient[0]['allergène']
        Ing1.grid(column=0, row = 4, columnspan=2,sticky="W")

        Ing2=tk.Label(root)
        Ing2["font"] = Ingft
        Ing2["fg"] = "black"
        Ing2["justify"] = "left"
        Ing2['wraplength']=875
        Ing2["bg"] = "#958BF9"
        Ing2["text"] = ingredient[1]['name']+" : "+ingredient[1]['description']+"\n"+ingredient[1]['endocrinien']+" et "+ingredient[1]['allergène']
        Ing2.grid(column=0, row = 5, columnspan=2,sticky="W")

        Ing3=tk.Label(root)
        Ing3["font"] = Ingft
        Ing3["fg"] = "black"
        Ing3["justify"] = "left"
        Ing3['wraplength']=875
        Ing3["bg"] = "#958BF9"
        Ing3["text"] = ingredient[2]['name']+" : "+ingredient[2]['description']+"\n"+ingredient[2]['endocrinien']+" et "+ingredient[2]['allergène']
        Ing3.grid(column=0, row = 6, columnspan=2,sticky="W")

        Ing4=tk.Label(root)
        Ing4["font"] = Ingft
        Ing4["fg"] = "black"
        Ing4["justify"] = "left"
        Ing4['wraplength']=875
        Ing4["bg"] = "#958BF9"
        Ing4["text"] = ingredient[3]['name']+" : "+ingredient[3]['description']+"\n"+ingredient[3]['endocrinien']+" et "+ingredient[3]['allergène']
        Ing4.grid(column=0, row = 7, columnspan=3,sticky="W")

        Ing5=tk.Label(root)
        Ing5["font"] = Ingft
        Ing5["fg"] = "black"
        Ing5["justify"] = "left"
        Ing5['wraplength']=875
        Ing5["bg"] = "#958BF9"
        Ing5["text"] = ingredient[4]['name']+" : "+ingredient[4]['description']+"\n"+ingredient[4]['endocrinien']+" et "+ingredient[4]['allergène']
        Ing5.grid(column=0, row = 8, columnspan=3,sticky="W")

        Ing6=tk.Label(root)
        Ing6["font"] = Ingft
        Ing6["fg"] = "black"
        Ing6["justify"] = "left"
        Ing6['wraplength']=875
        Ing6["bg"] = "#958BF9"
        Ing6["text"] = ingredient[5]['name']+" : "+ingredient[5]['description']+"\n"+ingredient[5]['endocrinien']+" et "+ingredient[5]['allergène']
        Ing6.grid(column=0, row = 9, columnspan=3,sticky="W")

        Ing7=tk.Label(root)
        Ing7["font"] = Ingft
        Ing7["fg"] = "black"
        Ing7["justify"] = "left"
        Ing7['wraplength']=875
        Ing7["bg"] = "#958BF9"
        Ing7["text"] = ingredient[6]['name']+" : "+ingredient[6]['description']+"\n"+ingredient[6]['endocrinien']+" et "+ingredient[6]['allergène']
        Ing7.grid(column=0, row = 10, columnspan=3,sticky="W")

        Ing8=tk.Label(root)
        Ing8["font"] = Ingft
        Ing8["fg"] = "black"
        Ing8["justify"] = "left"
        Ing8['wraplength']=875
        Ing8["bg"] = "#958BF9"
        Ing8["text"] = ingredient[7]['name']+" : "+ingredient[7]['description']+"\n"+ingredient[7]['endocrinien']+" et "+ingredient[7]['allergène']
        Ing8.grid(column=0, row = 11, columnspan=3,sticky="W")

        Ing9=tk.Label(root)
        Ing9["font"] = Ingft
        Ing9["fg"] = "black"
        Ing9["justify"] = "left"
        Ing9['wraplength']=875
        Ing9["bg"] = "#958BF9"
        Ing9["text"] = ingredient[8]['name']+" : "+ingredient[8]['description']+"\n"+ingredient[8]['endocrinien']+" et "+ingredient[8]['allergène']
        Ing9.grid(column=0, row = 12, columnspan=3,sticky="W")

        Ing10=tk.Label(root)
        Ing10["font"] = Ingft
        Ing10["fg"] = "black"
        Ing10["justify"] = "left"
        Ing10['wraplength']=875
        Ing10["bg"] = "#958BF9"
        Ing10["text"] = ingredient[9]['name']+" : "+ingredient[9]['description']+"\n"+ingredient[9]['endocrinien']+" et "+ingredient[9]['allergène']
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
            
       
if __name__ == "__main__":
    infos1={'keys': 1, 'name': 'Gentleman Society - Eau De Parfum pour homme', 'brand': {'name': 'GIVENCHY', 'engagement': 'Sans engagement'}, 'Ingredient': [{'name': 'ALCOHOL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR L'alcool cétéarylique appartient à la famille des alcools gras. Il est utilisé en tant qu'émollient. Il permet d'épaissir les crèmes et de les stabiliser. Il adoucit et protège la peau sans effet gras. L'alcool cétéarylique contient principalement de l'alcool cetylique (Cetyl alcohol) et de l'alcool stearylique (Stearyl alcohol). Il est autorisé en bio.  Le CIR (Cosmetic Ingredient Review) dans un rapport annuel publié en 2008, a conclut à l'innocuité des alcools gras."}, {'name': 'PARFUM (FRAGRANCE)', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Derrière ce terme de parfum, se cachent malheureusement de nombreuses molécules odorantes potentiellement irritantes voire allergisantes. Difficile de s'y retrouver lorsque que l'on devient allergique à un produit et que l'information n'est pas plus détaillée que cela. Néanmoins, pour nous aider, l'Europe a réglementé 24 molécules qui, lorsqu'elles sont utilisées au delà d'une certaine concentration, doivent être mentionnées dans la liste INCI (en général à la fin), bien que faisant partie elles-mêmes du parfum d'un produit. C'est le cas par exemple du Limonène, du linalol..."}, {'name': 'AQUA (WATER)', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR L'eau est l'ingrédient le plus utilisé en cosmétique : 83% des produits en contiennent (pourcentage établi à partir de 50 000 produits de l'App Inci Beauty). L'eau étant d'origine minérale, elle ne pourra jamais être certifiée Bio. C'est la raison pour laquelle les labels Bio, pour certifier les produits, autorisent des minimums d'ingrédients biologiques assez bas (10% pour Ecocert) sur le total d'une formule, en prenant en compte que la présence d'eau non Bio est indispensable et souvent majoritaire dans de nombreux cas."}, {'name': 'LIMONENE', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Linalol est un composé aromatique classé parmi les 24 allergènes réglementés par l'Europe. Il est présent à l'état naturel dans les huiles essentielles de thym, de lavande, de lavandin, de pin sylvestre ou de menthe poivrée... On le retrouve aussi dans de nombreux extraits (citron, orange, verveine...)."}, {'name': 'LINALOOL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Linalol est un composé aromatique classé parmi les 24 allergènes réglementés par l'Europe. Il est présent à l'état naturel dans les huiles essentielles de thym, de lavande, de lavandin, de pin sylvestre ou de menthe poivrée... On le retrouve aussi dans de nombreux extraits (citron, orange, verveine...)."}, {'name': 'COUMARIN', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Tocophérol représente différentes composantes de la Vitamine E. Il est utilisé en cosmétique pour ses propriétés antioxydantes. Cet ingrédient liposoluble (qui se dissout dans l'huile) se trouve à l'état naturel dans des huiles végétales comme l'huile de palme, de tournesol ou encore de germe de blé ... En 2014, le Tocopherol a fait l'objet d'une nouvelle étude du CIR ainsi que 13 autres dérivés de la vitamine E. L'organisme a conclu a son innocuité. Notez que le Tocopherol peut être d'origine synthétique (fabriqué entièrement en laboratoire)."}, {'name': 'BUTYL METHOXYDIBENZOYLMETHANE', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le beurre de karité est obtenu à partir du fruit (les noix) du karité, un arbre présent majoritairement sur le continent Africain. Il est composé principalement de triglycérides, d'acides gras, des esters de cire et d'actifs : parmi ceux-ci, des vitamines (A, D, E), des esters résineux, des phytostérols, du latex. Il est utilisé dans de nombreux cosmétiques pour ses propriétés assoupissantes et adoucissantes pour l'épiderme. Il peut aussi protéger la peau et le cuir chevelu des nombreuses agressions extérieures."}, {'name': 'ALPHA-ISOMETHYL IONONE', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Cette molécule synthétique incolore utilisée en parfumerie, fait partie des 24 allergènes réglementés par l'Europe. Ses senteurs florales sont proches de celles de la violette ou de l'iris."}, {'name': 'CITRAL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Citral est un agent parfumant faisant partie des 24 allergènes réglementés par l'Europe. Il est présent en quantité importante dans l'huile de citronnelle, mais aussi dans les huiles essentielles de verveine, d'orange, de citron... Il est utilisé comme composant aromatique en cosmétique pour ses odeurs de citron. Il est constitué par un mélange des deux isomères géométriques le géranial et le néral."}, {'name': 'GERANIOL', 'endocrinien': 'Non endocrinien', 'allergène': 'Non Allergène', 'description': "À SAVOIR Le Géraniol aussi nommé rhodinol, est un alcool monoterpénique qui fait partie des 24 allergènes réglementés par l'Europe. On le retrouve présent dans les huiles essentielles de Géranium, de citronnelle mais aussi dans l'huile de rose et de Palmarosa. Il est utilisé en parfumerie pour son odeur de rose."}]}
    root = tk.Tk()
    app = FicheInfos(root,infos1)
    root.mainloop()


