import re
import dbus
import html

from backends.metallum import Metallum
from backends.lyricwikia import Lyricwikia


class Pyrics:

    _backends = [Metallum, Lyricwikia]

    @staticmethod
    def get_backends():
        return Pyrics._backends

    def __init__(self, backends=None):
        self.detect_player()

        if backends is None:
            self._backends = Pyrics._backends
        else:
            self._backends = backends

        self._current_order = 0

        self._lyrics = None
        self._not_found = False

    def load(self):
        if not self.metadata:
            return

        self.current_artist = self.metadata['xesam:artist']
        self.current_album = self.metadata['xesam:album']
        self.current_song = self.metadata['xesam:title']
        self._current_order = 0

        artist = self.metadata['xesam:artist']
        song = self.metadata['xesam:title']

        self._lyrics = None

        if isinstance(artist, dbus.Array):
            artist = artist[0]

        while (self._lyrics is None
               and self._current_order < len(self._backends)):
            m = self._backends[self._current_order](artist, song)
            self._lyrics = m.get_lyrics()
            self._current_order += 1

        if self._lyrics is None:
            self._not_found = True
            self._lyrics = '[not found]'
            return

        self._lyrics = html.unescape(self._lyrics)

    def print_all(self):
        for attr, value in self.metadata.items():
            print(attr, '\t', value)

    def show_lyrics(self):
        self.load()
        if self._lyrics:
            print(self._lyrics)

    def get_lyrics(self):
        return self._lyrics

    def detect_player(self):
        """Detect a running music player by checking the processes"""
        self.detected_players = []
        bus = dbus.SessionBus()
        for service in bus.list_names():
            if re.match('org.mpris.MediaPlayer2.', service):
                self.detected_players.append(service)

        if not self.detected_players:
            self.metadata = None
            return

        player = bus.get_object(self.detected_players[0],
                                '/org/mpris/MediaPlayer2')

        self.metadata = (player
                         .Get('org.mpris.MediaPlayer2.Player', 'Metadata',
                              dbus_interface='org.freedesktop.DBus.Properties'))


def main():
    p = Pyrics()
    p.show_lyrics()

if __name__ == '__main__':
    main()
