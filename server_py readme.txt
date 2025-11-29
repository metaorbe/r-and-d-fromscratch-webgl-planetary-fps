server.py pas à pas

Imports :

http.server : Fournit un gestionnaire de requêtes HTTP de base pour servir des fichiers statiques comme index019.html et NormMatrix.gltf.
socketserver : Permet de créer un serveur TCP pour gérer les connexions réseau.
os : Utilisé pour changer le répertoire de travail vers le dossier contenant les fichiers du site.


Configuration :

PORT = 8000 : Le serveur sera accessible sur http://localhost:8000. Tu peux changer ce port (par exemple, 8080) si 8000 est déjà utilisé, mais choisis un port supérieur à 1024 pour éviter les conflits.
DIRECTORY = "." : Indique le dossier où se trouvent index019.html et NormMatrix.gltf. Si ces fichiers sont dans un sous-dossier (par exemple, website/), remplace "." par "website".


Changement de répertoire :

os.chdir(DIRECTORY) : Change le répertoire de travail pour que le serveur serve les fichiers depuis le bon dossier. Par exemple, si index019.html est dans C:\mon_projet\, le serveur servira les fichiers de ce dossier.


Gestionnaire HTTP :

Handler = http.server.SimpleHTTPRequestHandler : Utilise le gestionnaire par défaut de http.server pour servir les fichiers statiques (HTML, GLTF, JavaScript, etc.). Ce gestionnaire répond aux requêtes GET en renvoyant les fichiers demandés (par exemple, index019.html).


Serveur TCP :

socketserver.TCPServer(("", PORT), Handler) : Crée un serveur TCP qui écoute sur toutes les interfaces réseau ("") au port spécifié (8000). Cela permet d’accéder au serveur via localhost ou l’adresse IP de la machine.
httpd.serve_forever() : Lance le serveur en continu jusqu’à ce qu’il soit arrêté manuellement (avec Ctrl+C).


Gestion de l’arrêt :

Le bloc try/except KeyboardInterrupt permet d’arrêter proprement le serveur avec Ctrl+C, en affichant un message de confirmation.