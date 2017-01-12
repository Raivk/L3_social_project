Installation : (pour windows et linux (linux est plus simple))

- installer python 2.7 (n'oubliez pas de configurer le path)
- installer pygame par rapport a votre version de python (ici 2.7) (ATTENTION : choisir le dossier d'installation de votre python pour pygame)
    -> http://www.pygame.org/download.shtml

- installer les dependences de kivy puis kivy:
    WINDOWS :
        -> python -m pip install --upgrade pip wheel setuptools
        -> python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
        -> pour gstreamer :
        -> https://kivy.org/downloads/appveyor/deps/gstreamer/    #contient tous les lien
        -> https://kivy.org/downloads/appveyor/deps/gstreamer/kivy.deps.gstreamer-0.1.7-cp27-cp27m-win_amd64.whl #lien correspondant a notre windows, ne pas prendre en compte
        #exemple de commande : python -m pip install https://kivy.org/downloads/appveyor/deps/gstreamer/kivy.deps.gstreamer-0.1.7-cp27-cp27m-win_amd64.whl

        INSTALLER KIVY :
            -> python -m pip install kivy

    LINUX (UBUNTU ET SIMILAIRES) (SINON, aller voir ici : https://kivy.org/docs/installation/installation-linux.html):
        -> "sudo add-apt-repository ppa:kivy-team/kivy"
        -> "sudo apt-get update"
        -> "sudo apt-get install python-kivy"

- installer matplotlib
    -> python -m pip install -U pip setuptools
    -> python -m pip install matplotlib
    - Si installation non standard de python, se réferer à : http://matplotlib.org/users/installing.html

POUR FINIR :
    -> Lancer l'application avec "python sample.py" dans le répertoire principal
