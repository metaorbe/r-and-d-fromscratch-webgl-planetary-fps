import http.server
import socketserver
import os

# Configuration
PORT = 8000  # Port sur lequel le serveur sera accessible (par exemple, http://localhost:8000)
DIRECTORY = "."  # Dossier contenant index019.html et NormMatrix.gltf (chemin relatif au script)

# Changer le répertoire de travail pour pointer vers le dossier contenant les fichiers
os.chdir(DIRECTORY)

# Définir le gestionnaire pour servir les fichiers
Handler = http.server.SimpleHTTPRequestHandler

# Configurer le serveur TCP
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serveur démarré sur http://localhost:{PORT}")
    print(f"Serveur les fichiers depuis : {os.getcwd()}")
    
    # Démarrer le serveur et le garder actif
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
        httpd.server_close()