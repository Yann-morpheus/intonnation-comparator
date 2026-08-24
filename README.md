
# Intonnation comparaison
Api permettant de comparer deux fichier audio et de donner letaux de ressemblance comme le pitch et l'énergie 
## Deployment  

créer l'environnement virtuel (windows) 

```bash
  python -m venv .venv
```  
Démarer l'environnement virtuel (windows) 

```bash
  source .venv/bin/activate
```  

installer les dépendances 

```bash
  pip install -r requirement-dev.txt
```  
Lancer le serveur flask

```bash
  flask run
```  

## API Reference

#### Create and Get comparaison
format fichier autorisé (mp3, flac, wav)

taille maximale des fichier 10 mo

durée du fichier maximale du fichier 3 minutes


~~~http
  POST /api/compare
~~~

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `audio_cand`  | `file` | **Obligatoire**. fichier audio |
| `audio_ref` | `file` | **Obligatoire**. fichier audio |  

## Tech Stack  
**Client:** html, tailwindcss, javascript 

**Server:** Flask , parselmouth, numpy, praat-dtw-python

## Author 
- [@Happi yann](https://www.github.com/Yann-morpheus)  



