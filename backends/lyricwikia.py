from backends.backend import Backend


class Lyricwikia(Backend):

    def __init__(self, artist=None, song=None):
        super(Lyricwikia, self).__init__("http://lyrics.wikia.com/wiki/"
                                         + "%s:%s")

        self._artist = artist
        self._song = song
        self.class_ = 'lyricbox'
        self._url_separator = '_'

    def _after_fetch(self, content):
        # remove span html from instrumental results
        span = content.find('span')
        if span:
            span.replaceWith('')

        return content

    def print_lyrics(self):
        print(self.get_lyrics(self._artist, self._song))
