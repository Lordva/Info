from bs4 import BeautifulSoup
from os import path, makedirs
import requests

destination=''
url='http://ptsi-chaptal.fr/SI/cours.html'
banlist=['https:','#','index.php', 'cours.html','edt.html','#navPanel','programme.pdf','www.lycee-chaptal-paris.fr']
user, pwd = "ptsi",""
soup = BeautifulSoup(requests.get(url).text, 'html.parser')


def isbanned(liste):
    for i in liste:
        if i in banlist:
            return True
    return False


def download(_url, dest, name, docs):
    file = requests.get(_url, auth=(user,pwd), stream=True)
    file_size = int(file.headers['content-length'])

    #Met les elements de docs dans un string
    st=""
    for i in docs: st += str(i) + "/"
    _path=dest+"/"+st+name

    #Crée le/les dossiers 
    if not path.exists(dest + "/" + st):
        makedirs(dest + "/" + st)
        print("Le dossier " + st + " à été créé")

    #Télécharge le fichier
    if not path.exists(_path):
        with open(_path, "wb") as pdf:
            print("Downloading: " + name + " Taille: " + str(round(file_size*10**-6,2)) + "Mb")
            for chunk in file.iter_content(chunk_size=8192):
                pdf.write(chunk)
            pdf.close()

def main():
    #check toute les balises <a> de la page, recup le href et split dans une liste
    for link in soup.find_all('a'):
        u = link.get('href')
        liste = u.split("/") 
        if not isbanned(liste):
            
            #Prend le nom du fichier et la liste des dossiers le contenant
            filename=liste[-1]
            doc = liste[:-1]
            
            # Formate l'url pour virer le /cours.html
            format_url_liste = url.split("/")[:-1]
            format_url = ""
            for i in format_url_liste: format_url += i + "/"
            
            download(format_url + "/" + u, destination, filename, doc)


if __name__ == "__main__":
    main()
