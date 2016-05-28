# About
pyrics is a lyrics fetcher written in python. It should detect automatically your current running player and display the lyrics. It should work with any player that uses mpris. pyrics was written as an API. There's the `qpyrics.py` that displays that lyrics in a QT GUI, or you can just run `pyrics.py` and show the lyrics on the terminal.

It was written using the Linux's dbus, but it should be easy to port to another platform.

I wrote it because some music players I use lack the ability to display the song's lyrics, or when they do, they don't have good lyrics sources. So now I can have lyrics for any player I might be using.

# Dependencies
Pyrics depends on:
- psutil
- beautiful soup 4
- pyqt5 (for QT GUI)
You can install all of them running `pip3 install -r requirements.txt`

# Backends
Currently the following sources of lyrics are available:
- Metallum (forked from https://github.com/noeldelgado/metallum)
- Lyricwikia
