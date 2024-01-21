
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
import os
import winreg
from zipfile import ZipFile
warnings.filterwarnings("ignore")
import json

options = EdgeOptions()
options.use_chromium = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.set_capability("acceptInsecureCerts", True)
options.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

#Try to connect if the edgeriver version is 108
try : 
    options.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
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
            downloads_path = winreg.QueryValueEx(reg_key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]  #Recupère le dossier téléchargement sans avoir à entrer le user de la session
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
            
            os.remove(downloads_path+"/edgedriver_win64.zip")
        executablePath=r'.\driverEdge\msedgedriver_v'+version.split('.')[0]+".exe"        
        options.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

def Sephora():
    dicParfum={}
    listeMarque=[]
    listeIngredient=[]
    driver = Edge(executable_path =executablePath)
    driver.get("https://www.sephora.fr/")
    cookies=driver.find_element(By.XPATH,'//*[@id="footer_tc_privacy_button_2"]')
    cookies.click()
    i=0 #placement sur la page web
    key=0 #classement
    while key<10:
        div=0
        driver.get("https://www.sephora.fr/parfum-meilleures-ventes/?srule=Sorting%20Rule%20-%20Best%20Sellers&start=0&sz=24")
        id=str(i+1)
        try:
            pathparfum="/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/ul/li["+id+"]"
            Parfum=driver.find_element(By.XPATH, pathparfum)
        except :
            pathparfum="/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/ul/li["+id+"]"
            Parfum=driver.find_element(By.XPATH, pathparfum)
        if Parfum.get_attribute('class')=='grid-tile':
            key+=1
            marque=driver.find_element(By.XPATH,pathparfum+"/div/div[3]/div/a/span").get_attribute('innerText')
            #print(marque)
            listeMarque.append(marque)
            Parfum.click()
            #nom du parfum      
            nomParfum=driver.find_element(By.CLASS_NAME,'product-name.product-name-bold').get_attribute("innerText")
            #print(nomParfum)
            dicParfum[key]=nomParfum
            #liste des ingredients
            ingredient=driver.find_element(By.ID,'tab-ingredients').click()
            time.sleep(1)
            liste_I=driver.find_element(By.CLASS_NAME,"ingredients-content").get_attribute('innerText')
            #print('Ingredient : '+ ingredient)
            listeIngredient.append(liste_I)
            #print("\n")
        i+=1
            
    driver.close()
    return dicParfum,listeMarque,listeIngredient
#dicParfum,listeMarque,listeIngredient=Sephora()

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
    Ingredient.append(simiabraz)
    return(Ingredient)

def IngredientForme(listeIngredient):
    for i in listeIngredient:
        Ingredient=miseEnForme(i)
    
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
    setIngredient=set(Ingredients)
    return (listeingredient,setIngredient)
#Ingredient,setIngredient=IngredientForme(listeIngredient)


 
def incibeauty(setIngredient):
    descIng={}
    Allergene=[]
    endo=[]
    driver = Edge(executable_path =executablePath)
    driver.get("https://incibeauty.com/ingredients")
    cookies=driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/button")
    cookies.click()
    for i in setIngredient:
        if 'ALCOHOL'==i:
            driver.get("https://incibeauty.com/ingredients/14307-alcohol")
            url=True
        else : 
            driver.get("https://incibeauty.com/ingredients")
            search=driver.find_element(By.ID,'searchInci')
            search.click()
            search.clear()
            search.send_keys(i)
            count=0
            url=False
            b=True
            while b:
                count+=1
                search.send_keys(Keys.ENTER)
                if driver.current_url!="https://incibeauty.com/ingredients":
                    b=False
                    url=True
                if count>=10:
                    b=False
        if url :
            listeInfo= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/section[1]/div/div/div/ul')))
            if 'Allergène' in listeInfo.get_attribute('innerText'):
                Allergene.append(i)
            if 'Perturbateur endocrinien' in listeInfo.get_attribute('innerText'):
                endo.append(i)
            try:
                aSavoir=driver.find_element(By.XPATH,'/html/body/section[1]/div/div/div/div[2]/div')
                desc=aSavoir.get_attribute('innerText')
                desc=desc.replace('"',"''")
                descIng[i]=desc.replace('\n',' ')
            except:
                descIng[i]="Pas d'information supplémentaire"

    driver.close()
    return descIng,Allergene,endo

 
def engagement(listeMarque):
    marqueEco={}
    driver = Edge(executable_path =executablePath)
    driver.get("https://sciencebasedtargets.org/companies-taking-action#dashboard")
    time.sleep(5)
    cookies=driver.find_element(By.CLASS_NAME,"font-bold.text-center.rounded-full.appearance-none.o-btn.border-3.border-currentColor.flex-shrink-0.is-current")
    cookies.click()
    #recherche la marque
    inputs=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input")
                                         #/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input
    for i in listeMarque:
        inputs.send_keys(i)
        time.sleep(5)
        try :
            #click sur view more pour avoir accès à la target
            driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/label/span/span").click()
            target=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]").get_attribute("innerText")
            marqueEco[i]=target
        except:
            marqueEco[i]="Sans engagement"
        inputs.clear()
    driver.close()
    return marqueEco

#descIng,Allergene,endo=incibeauty(setIngredient)
#marqueEco=engagement(listeMarque)

def jsonIngredient(setIngredient, descIng, Allergene, endo):
    json_Ingredients='{'
    i=1
    for k,v in descIng.items():
        ing=k
        endo='Endocrinien' if ing in endo else 'Non endocrinien'
        alle='Allergène' if ing in Allergene else 'Non Allergène'
        desc=v
        json_Ingredients+='"'+ing+'":{"endocrinien": "'+endo+'","allergène": "'+alle+'","description": "'+desc+'"}'
        if i<len(descIng):
            json_Ingredients += ',' 
            i+=1
    json_Ingredients+='}'
    print(json_Ingredients)
    json_object = json.loads(json_Ingredients)
    with open('Ingredients_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_object, json_file, ensure_ascii=False, indent=4)
        
#jsonIngredient(setIngredient, descIng, Allergene, endo)

def create_json(dicParfum, listeMarque, Ingredient, descIng, Allergene, endo, marqueEco):
    json_structure='{"Top": ['
    for k,v in dicParfum.items():
        marque=listeMarque[k-1]
        json_structure += ' {"keys":'+str(k) +',"name": "'+v+'","brand": {"name": "'+marque+'","engagement": "'+marqueEco[marque]+'"},'
        json_structure+='"Ingredient":['
        for i in range(len(Ingredient[k-1])):
            if i <10:
                ing=Ingredient[k-1][i]
                endo='Endocrinien' if ing in endo else 'Non endocrinien'
                alle='Allergène' if ing in Allergene else 'Non Allergène'
                desc=descIng[ing] if ing in descIng.keys() else "Pas d'information supplémentaire"
                json_structure+='{"name": "'+ing+'","endocrinien": "'+endo+'","allergène": "'+alle+'","description": "'+desc+'"}'
                if i<9:
                    json_structure += ','
        json_structure += ' ]}'
        if k<10:
            json_structure += ','
    json_structure+=']}'
    print(json_structure)
    json_object = json.loads(json_structure)
    with open('output_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_object, json_file, ensure_ascii=False, indent=4)
        
#create_json(dicParfum, listeMarque, Ingredient, descIng, Allergene, endo, marqueEco)