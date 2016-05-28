#!/usr/bin/env python3
import re
import json
from urllib.parse import urlencode
from urllib.request import urlopen
import codecs

from backends.backend import Backend


class Metallum(Backend):

    def __init__(self, artist, title):
        self.site_url = 'http://www.metal-archives.com/'
        self.lyrics_not_available = '(lyrics not available)'
        self.lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
        self.band_name_re = re.compile(r'title="(?P<name>.*)\"')
        self.tags_re = re.compile(r'<[^>]+>')
        self.trash_re = re.compile(r'^\[[\d]+m', re.MULTILINE)
        self.artist = artist
        self.title = title

    def _get_songs_data(self, band, song):
        """Search on metal-archives for song coincidences"""
        params = dict(
            bandName=band,
            songTitle=song
        )

        url = "".join([self.site_url,
                       "search/ajax-advanced/searching/songs?",
                       urlencode(params)])

        reader = codecs.getreader('utf-8')

        return json.load(reader(urlopen(url)))['aaData']

    def _get_lyrics_by_song_id(self, song_id):
        """Search on metal-archives for lyrics based on song_id"""
        url = "".join([self.site_url, "release/ajax-view-lyrics/id/", song_id])
        reader = codecs.getreader('utf-8')
        html = reader(urlopen(url))

        return self.tags_re.sub('', html.read().strip())

    def _iterate_songs_and_print(self, songs):
        '''Iterate over returned song matches. If the lyrics are different \
        than "(lyrics not available)" then break the loop and print them out.\
        Otherwise the last song of the list will be printed.'''
        for song in songs:
            band_name = self.band_name_re.search(song[0]).group("name")
            song_title = song[3]
            song_id = self.lyric_id_re.search(song[4]).group("id")
            lyrics = self._get_lyrics_by_song_id(song_id)
            if lyrics != self.lyrics_not_available:
                break

        title = "".join([band_name, " - ", song_title, "\n"])
        lyrics = ("".join(["\033[4m", title, "\n\033[0m", lyrics, "\n"]))

        lyrics = self.trash_re.sub(r'', lyrics)
        return lyrics

    def get_lyrics(self):
        """Runs the program and handles command line options"""

        songs_data = self._get_songs_data(self.artist, self.title)

        if len(songs_data):
            return self._iterate_songs_and_print(songs_data)

        return None

        # sys.exit("\n\033[031m Lyrics not found\n")
