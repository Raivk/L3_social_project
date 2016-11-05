Installation process : (for windows, should be similar for linux/mac)

- install python 2.7 (don't forget to set path)
- install pygame corresponding to your python (carefull, choose your python installation folder when installing pygame)
    -> http://www.pygame.org/download.shtml
- install kivy deps :
    -> python -m pip install --upgrade pip wheel setuptools
    -> python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
    -> for gstreamer :
        -> https://kivy.org/downloads/appveyor/deps/gstreamer/    #contains all links
        -> https://kivy.org/downloads/appveyor/deps/gstreamer/kivy.deps.gstreamer-0.1.7-cp27-cp27m-win_amd64.whl
        #above is link for python 2.7 and x64 version
        #exemple command : python -m pip install https://kivy.org/downloads/appveyor/deps/gstreamer/kivy.deps.gstreamer-0.1.7-cp27-cp27m-win_amd64.whl
    -> python -m pip install kivy

And that's it. It should now run properly.
