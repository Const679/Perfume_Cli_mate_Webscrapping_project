from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
import time
import json

#Function pour scrapper les 10 meilleures vente de parfum sur Sephora
def Sephora(options,executablePath):
    dicParfum={}
    listeMarque=[]
    listeIngredient=[]
    #Ouverture de Edge et recherche de Sephora
    driver = Edge(executable_path =executablePath,options = options)
    driver.get("https://www.sephora.fr/")
    #Accepte les cookies
    cookies=driver.find_element(By.XPATH,'//*[@id="footer_tc_privacy_button_2"]')
    cookies.click()
    i=1 #placement sur la page web
    key=0 #classement
    #Tant qu'il n'y a pas 10 parfum dans le dictionnaire va en rajouter
    while key<10:
        #Se dirge sur la page des meilleures ventes de parfum
        driver.get("https://www.sephora.fr/parfum-meilleures-ventes/?srule=Sorting%20Rule%20-%20Best%20Sellers&start=0&sz=24")
        id=str(i)
        #Recherche les cases de parfums (2 mises en page possibles du site)
        try:
            pathparfum="/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/ul/li["+id+"]"
            Parfum=driver.find_element(By.XPATH, pathparfum)
        except :
            pathparfum="/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/ul/li["+id+"]"
            Parfum=driver.find_element(By.XPATH, pathparfum)
        #Si la case sélectionnnée n'est pas une pub
        if Parfum.get_attribute('class')=='grid-tile':
            key+=1
            #Enregistre la marque
            marque=driver.find_element(By.XPATH,pathparfum+"/div/div[3]/div/a/span").get_attribute('innerText')
            listeMarque.append(marque)
            #Va sur la page du parfum
            Parfum.click()
            #Enregistre le nom du parfum      
            nomParfum=driver.find_element(By.CLASS_NAME,'product-name.product-name-bold').get_attribute("innerText")
            dicParfum[key]=nomParfum
            #Enregistre la liste des ingredients
            driver.find_element(By.ID,'tab-ingredients').click()
            time.sleep(1) #Attend que la page des ingredients soit visible
            liste_I=driver.find_element(By.CLASS_NAME,"ingredients-content").get_attribute('innerText')
            listeIngredient.append(liste_I)
        i+=1
    #Fermeture de la page Sephora        
    driver.close()
    return dicParfum,listeMarque,listeIngredient

#Mise en forme des ingredients : Sépare les ingrédiente sous format string en liste selon leurs séparateurs
def miseEnForme(ingredients):
    phrase="Cette liste d'ingrédients peut faire l'objet de modifications, veuillez consulter l'emballage du produit acheté."
    Ingredient=[]
    ouisticram=ingredients.replace("\n",'')
    ouisticram=ouisticram.replace(phrase,'')
    if "INGREDIENTS" in ouisticram:
        champenfeu=ouisticram.split(':')
        champenfeu=champenfeu[-1]
    else:
        champenfeu=ouisticram
    if "●" in champenfeu :
        simiabraz=champenfeu.split("●")
    elif " | " in champenfeu:
        simiabraz=champenfeu.split(" | ")
    elif ' , ' in champenfeu:
        simiabraz=champenfeu.split(" , ")
    elif ' ,' in champenfeu:
        simiabraz=champenfeu.split(" ,")
    elif ', ' in champenfeu:
        simiabraz=champenfeu.split(", ")
    elif ', ' in champenfeu:
        simiabraz=champenfeu.split(",")
    elif " • " in champenfeu:
        simiabraz=champenfeu.split(" • ")
    elif " · " in champenfeu:
        simiabraz=champenfeu.split(" · ")
    elif "; " in champenfeu:
        simiabraz=champenfeu.split("; ")
    elif ". " in champenfeu:
        simiabraz=champenfeu.split(". ")
    elif " —" in champenfeu:
        simiabraz=champenfeu.split(" —")
    else :
        simiabraz=champenfeu
        print(simiabraz)
    Ingredient.extend(simiabraz)
    return(Ingredient)

#Seconde mise en forme sur chaque ingrédient dans les listes 
def IngredientForme(listeIngredient):
    Ingredient= []
    for i in listeIngredient:
        Ingredient.append(miseEnForme(i))
    Ingredients=[]
    listeingredient=[]
    for i in Ingredient:
        for j in i :
            b=False
            if ':' in j:
                j=j.split(':')[-1]
            if '#1' in j :
                ij=j.split(' ')
                j=ij[1]
            if j.startswith(' '):
                j=j[1:]
            if j.endswith(' '):
                j=j[:-1]
            if '/' in j:
                j=j.split('/')[0]
            if ',' in j:
                j=j.split(',')
                b=True
            if b:
                Ingredients.extend(j)
            else:
                Ingredients.append(j)
        listeingredient.append(Ingredients)
    setIngredient=set(Ingredients) #Sert à recenser les informations sur chaque ingrédient
    return (listeingredient,setIngredient)

#Function pour scrapper les informations de chaque ingrédient trouvé dans les parfums
def incibeauty(setIngredient,options,executablePath):
    descIng={} #description des ingrédients
    Allergene=[] #s'ils sont allergènes
    endo=[]#s'ils sont pertubateurs endocriniens
    #Ouverture de Edge et recherche des ingrédients de Inci Beauty
    driver = Edge(executable_path =executablePath,options = options)
    driver.get("https://incibeauty.com/ingredients")
    #Possibilité de Host not found
    try:
        #Continue sans accepter les cookies
        cookies=driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/button[1]")
        cookies.click()
        #Pour tous les ingredients
        for i in setIngredient:
            #Si c'est de l'acool, ce n'est pas dans les premiere propositino il faut faire une requete "manuelle"
            if 'ALCOHOL'==i:
                driver.get("https://incibeauty.com/ingredients/14307-alcohol")
                url=True
            #sinon recherche ingrédient un par un 
            else : 
                driver.get("https://incibeauty.com/ingredients")
                # rentre le nom de l'ingredient dans la bar de recherche
                search=driver.find_element(By.ID,'searchInci')
                search.click()
                search.clear() #vide la case avant d'envoyer un nouvel ingredient
                search.send_keys(i)
                count=0 #Compte le nombre de tour
                url=False #Changement d'url
                b=True #envoie de l'ingredient
                #Essaye de rechercher le nom de l'ingredient pendant 10 tours max en cherchant à ce que l'URL change 
                while b: 
                    count+=1
                    search.send_keys(Keys.ENTER) #click sur rechercher
                    if driver.current_url!="https://incibeauty.com/ingredients": #si on a changer d'URL
                        b=False
                        url=True
                    if count>=10:
                        b=False
            # si l'URL n'est plus la page de recherche
            if url :
                #Attend que la page se charge totalement
                listeInfo= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/section[1]/div/div/div/ul')))
                # remplit Allergene si l'information est trouvée
                if 'Allergène' in listeInfo.get_attribute('innerText'):
                    Allergene.append(i)
                # remplit endo si l'information est trouvée
                if 'Perturbateur endocrinien' in listeInfo.get_attribute('innerText'):
                    endo.append(i)
                #Essaye de trouver la description de l'ingrédient si elle est présente sur la page
                try:
                    aSavoir=driver.find_element(By.XPATH,'/html/body/section[1]/div/div/div/div[2]/div')
                    desc=aSavoir.get_attribute('innerText')
                    #mise en forme rapide de la description
                    desc=desc.replace('"',"''")
                    descIng[i]=desc.replace('\n',' ')
                except:
                    descIng[i]="Pas d'information supplémentaire"
    except : 
        titre=driver.find_element(By.XPATH,'/html/head/title').get_attribute('innerText')
        if titre=='incibeauty.com | 520: Web server is returning an unknown error':
            print(titre)
        "Exception"
    #Ferme la fenêtre de Inci Beauty
    driver.close()
    return (descIng,Allergene,endo)



#Function pour scrapper les engagement de chaque marque
def engagement(listeMarque,options,executablePath) :
    #Ouverture de Edge et recherche des engagement sur Science Based Targets
    driver = Edge(executable_path =executablePath,options = options)
    driver.get("https://sciencebasedtargets.org/companies-taking-action#dashboard")
    time.sleep(5)
    #Accepte les cookies
    try:
        cookies=driver.find_element(By.CLASS_NAME,"font-bold.text-center.rounded-full.appearance-none.o-btn.border-3.border-currentColor.flex-shrink-0.is-current")
        cookies.click()
    except:
        "pas de cookies"
    #Repérage de la barre dédiée à la recherche
    inputs=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input")
    #Pour chaque marque recherche si elle a des engagements
    marqueEco={}
    for i in listeMarque:
        inputs.send_keys(i)
        time.sleep(5)
        try :
            #click sur view more pour avoir accès à la target
            driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/label/span/span").click()
            #Enregistre la partie Target
            target=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]").get_attribute("innerText")
            marqueEco[i]=target
        except:
            #Si la marque n'a pas été trouvée alors pas d'engagement enregistré
            marqueEco[i]="Sans engagement"
        #Vide la barre de recherche
        inputs.clear()
    #Ferme la fenetre de Science based targets
    driver.close()
    return marqueEco


#Creer un json qui ressence toutes les inforamtions des ingredients pour pouvoir le réutiliser avec le parfum personalisé
def jsonIngredient(setIngredient, descIng, Allergene, endo):
    json_Ingredients='{' #Créer la structure du json en str
    i=1 #Sers à gérer les virgules en fin d'ingrédient
    for k,v in descIng.items():
        ing=k
        endo='Endocrinien' if ing in endo else 'Non endocrinien'
        alle='Allergène' if ing in Allergene else 'Non Allergène'
        desc=v
        json_Ingredients+='"'+ing+'":{"endocrinien": "'+endo+'","allergène": "'+alle+'","description": "'+desc+'"}'
        #Tant qu'on est pas au dernier ingrédient, ajoute une virgule à la fin de la ligne
        if i<len(descIng):
            json_Ingredients += ',' 
            i+=1
    json_Ingredients+='}' #Fini le json
    json_object = json.loads(json_Ingredients) #Transforme le string en format json
    #Enregistre le fichier
    with open('Ingredients_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_object, json_file, ensure_ascii=False, indent=4)

#Creer un json qui ressence toutes les inforamtions des parfum pour pouvoir le réutiliser avec l'application principale'
def create_json(dicParfum, listeMarque, Ingredient, descIng, Allergene, endo, marqueEco):
    json_structure='{"Top": [' #Créer la structure du json en str
    for k,v in dicParfum.items(): #Pour chaque parfum, creer un ligne dans le json
        marque=listeMarque[k-1]
        #Format json : Top, Nom, marque (nom, engagement), liste d'ingrédient (endocrinien, allergene, description)
        json_structure += ' {"keys":'+str(k) +',"name": "'+v+'","brand": {"name": "'+marque+'","engagement": "'+marqueEco[marque]+'"},'
        json_structure+='"Ingredient":['
        for i in range(len(Ingredient[k-1])):
            if i <10:
                ing=Ingredient[k-1][i]
                endo='Endocrinien' if ing in endo else 'Non endocrinien'
                alle='Allergène' if ing in Allergene else 'Non Allergène'
                desc=descIng[ing] if ing in descIng.keys() else "Pas d'information supplémentaire"
                json_structure+='{"name": "'+ing+'","endocrinien": "'+endo+'","allergène": "'+alle+'","description": "'+desc+'"}'
                #ajoute une virgule jusqu'à l'avant dernier ingredient
                if i<9:
                    json_structure += ','
        json_structure += ' ]}' #Fini les ingrédients
        if k<10:
            #ajoute une virgule jusqu'à l'avant dernier parfum
            json_structure += ','
    json_structure+=']}'#Fini le json
    json_object = json.loads(json_structure)#Transforme le string en format json
    #Enregistre le fichier
    with open('output_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_object, json_file, ensure_ascii=False, indent=4)