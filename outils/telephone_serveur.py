"""SERVEUR LOCAL DU TÉLÉPHONE DE WILLIAM (créé le 27/10/2026 : le téléphone doit marcher SANS Claude).

La page « téléphone » (sorties/telephone/index.html) est publiée sur claude.ai par Claude (outil Artifact) ; un autre agent (Gemini dans
Antigravity, Codex…) n'a pas cet outil : le joueur ne voyait plus le téléphone. Ce serveur sert la même page depuis le PC, à l'adresse
http://localhost:8765, et, sur le même Wi-Fi, depuis le vrai téléphone du joueur (l'adresse du réseau est affichée au démarrage).

    python outils/telephone_serveur.py            # sert la page ; ouvrir.bat / ouvrir-telephone.bat l'ouvre dans le navigateur
    python outils/telephone_serveur.py --ouvrir   # + ouvre le navigateur du PC
    python outils/telephone_serveur.py --local    # seulement ce PC (pas le réseau)
    python outils/telephone_serveur.py --essai    # essai automatique (page, PDF, chemins interdits), sans rester ouvert

La page est régénérée au démarrage et chaque fois que l'horloge de la simulation est plus récente que la page (`tour.py fin` la régénère
déjà) : recharger l'onglet suffit. Les PDF de `documents_william/` et de `courriels/` sont servis en lecture seule (l'application Fichiers
les ouvre alors aussi depuis le téléphone). Rien d'autre du dépôt n'est servi.
"""
import argparse
import http.server
import re
import socket
import subprocess
import sys
import threading
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PAGE = RACINE / "sorties" / "telephone" / "index.html"
HORLOGE = RACINE / "etat" / "horloge.txt"
PORT = 8765


def regenerer():
    subprocess.run([sys.executable, str(RACINE / "outils" / "telephone.py")], capture_output=True, cwd=str(RACINE))


def page_a_jour():
    return PAGE.is_file() and (not HORLOGE.is_file() or PAGE.stat().st_mtime >= HORLOGE.stat().st_mtime)


class Gestionnaire(http.server.BaseHTTPRequestHandler):
    server_version = "TelephoneWilliam"

    def log_message(self, *args):  # silencieux
        pass

    def _repondre(self, code, corps=b"", type_="text/plain; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", type_)
        self.send_header("Content-Length", str(len(corps)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corps)

    def do_GET(self):
        chemin = urllib.parse.unquote(urllib.parse.urlparse(self.path).path)
        if chemin in ("/", "/index.html", "/telephone"):
            if not page_a_jour():
                regenerer()
            if not PAGE.is_file():
                return self._repondre(503, "Page du téléphone absente : lancer python outils/telephone.py".encode("utf-8"))
            return self._repondre(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        m = re.fullmatch(r"/(documents_william|courriels)/([^/\\]+\.pdf)", chemin)
        if m:
            fichier = RACINE / m.group(1) / m.group(2)
            if fichier.is_file():
                return self._repondre(200, fichier.read_bytes(), "application/pdf")
        return self._repondre(404, "Introuvable".encode("utf-8"))


def adresse_reseau():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return None


def essai():
    if not PAGE.is_file():
        regenerer()
    serveur = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Gestionnaire)
    port = serveur.server_address[1]
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"

    def lire(chemin):
        try:
            with urllib.request.urlopen(base + chemin, timeout=20) as r:
                return r.status, r.headers.get("Content-Type", ""), r.read(64)
        except urllib.error.HTTPError as e:
            return e.code, "", b""
    erreurs = []
    code, type_, debut = lire("/")
    if code != 200 or "html" not in type_:
        erreurs.append(f"page : {code} {type_}")
    pdfs = sorted((RACINE / "documents_william").glob("*.pdf")) or sorted((RACINE / "courriels").glob("*.pdf"))
    if pdfs:
        dossier = pdfs[0].parent.name
        code, type_, debut = lire(f"/{dossier}/{urllib.parse.quote(pdfs[0].name)}")
        if code != 200 or "pdf" not in type_ or not debut.startswith(b"%PDF"):
            erreurs.append(f"PDF : {code} {type_}")
    for interdit in ("/etat/horloge.txt", "/documents_william/../etat/horloge.txt", "/documents_william/%2e%2e%2fetat%2fhorloge.txt", "/CLAUDE.md", "/outils/relais.py"):
        code, _, _ = lire(interdit)
        if code == 200:
            erreurs.append(f"chemin interdit servi : {interdit}")
    serveur.shutdown()
    print("essai : conforme" if not erreurs else "essai : ÉCHEC : " + " ; ".join(erreurs))
    return 0 if not erreurs else 1


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=PORT)
    ap.add_argument("--local", action="store_true", help="seulement ce PC")
    ap.add_argument("--ouvrir", action="store_true", help="ouvre le navigateur du PC")
    ap.add_argument("--essai", action="store_true")
    a = ap.parse_args()
    if a.essai:
        sys.exit(essai())
    regenerer()
    hote = "127.0.0.1" if a.local else "0.0.0.0"
    try:
        serveur = http.server.ThreadingHTTPServer((hote, a.port), Gestionnaire)
    except OSError:
        print(f"Le port {a.port} est déjà utilisé : le serveur tourne sans doute déjà (ouvrir http://localhost:{a.port}).")
        if a.ouvrir:
            webbrowser.open(f"http://localhost:{a.port}")
        return
    print("TÉLÉPHONE DE WILLIAM — serveur local (laisser cette fenêtre ouverte ; Ctrl+C pour arrêter)")
    print(f"  Sur ce PC          : http://localhost:{a.port}")
    ip = None if a.local else adresse_reseau()
    if ip:
        print(f"  Sur ton téléphone  : http://{ip}:{a.port}  (même Wi-Fi ; autoriser le réseau privé si Windows le demande)")
    print("  La page se met à jour à chaque tour : recharger l'onglet.")
    if a.ouvrir:
        webbrowser.open(f"http://localhost:{a.port}")
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("Serveur arrêté.")


if __name__ == "__main__":
    main()
