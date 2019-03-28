#!/usr/bin/python

"""SPOTBOX media playback backend"""

import os

from spotboxconfig import folder_configuration

class Playback:
    """A playback object, allows for audio files to be loaded, played back,
    and stopped whilst playing.
    """
    def __init__(self):
        pass

    def initialize_one_player(self, spotnumber):
        pass

    def load(self, spotnumber, filepath):
        pass

    def play(self, spotnumber):
        pass

    def stop(self):
        pass


class iTunesPlayback(Playback):
    # imperfect: itunes volume/ repeat mode is not currently handled directly.

    def __init__(self):
        import appscript
        import mactypes
        # TODO - number of playlists.
        self.itunes = self.appscript.app('iTunes')
        # make sure iTunes is opened???? TODO
        # USEFUL: applescript directory:
        # http://www.mugginsoft.com/html/kosmictask/ASDictionaryDocs/Apple/
        #iTunes/OS-X-10.7/iTunes-10.6.1/html/

    def initialize_one_player(self, spotnumber):
        # iTunes doesn't need to, assuming the playlists
        # have been created (TODO - check?)
        #try:
        #    tab.visible()
        #except:
        #   throw a toplevel warning to create such a playlist...
        pass

    def stop(self):
        self.itunes.stop()

    def load(self, spotnumber, filepath):
        playlisttoload = self.itunes.playlists['SPOTBOX' + str(spotnumber + 1)]
        playlisttracks = playlisttoload.tracks()
        if len(playlisttracks) > 0:
            self.itunes.delete(playlisttoload.tracks)
        self.itunes.add(self.mactypes.Alias(filepath), to=playlisttoload)
        # Now check to make sure the file actually loaded:
        playlisttracks = playlisttoload.tracks()
        if len(playlisttracks) == 0:
            # if the playlist is now empty, it's an error. don't continue.
            # possible reasons: it's a non-music file, that iTunes won't accept
            #                   it's a corrupted mp3, etc
            # Don't list the name in the 'load' text.
            return False
        # Check (enable) the file, (index 0 because
        # there can be only one) to make sure it plays!
        playlisttracks[0].enabled.set(1)
        return True

    def play(self, spotnumber):
        self.itunes.play(self.itunes.playlists['SPOTBOX'+str(spotnumber+1)])


class PygletPlayback(Playback):
    """Provide playback support using the Pyglet library.

    See https://bitbucket.org/pyglet/pyglet/overview"""

    def __init__(self):
        self.players = {}
        self.media = {}

    def initialize_one_player(self, spotnumber):
        import pyglet
        pygplayer = pyglet.media.Player()

        if spotnumber in self.players:
            # Make sure to free up queues and player resources
            self.players[spotnumber].delete()

        self.players[spotnumber] = pygplayer

    def stop(self):
        for spot_number, player in self.players.iteritems():
            player.pause()

            # Need to check to avoid OpenGL access exception (ugh)
            if player.time > 0:
                player.seek(0.0)

    def load(self, spotnumber, filepath):
        import pyglet

        # To support non-WAV files, you may need to install AVBin (http://avbin.github.io/AVbin)
        self.media[spotnumber] = pyglet.media.load(os.path.join(folder_configuration['MEDIADIRECTORY'], filepath))

        return True

    def play(self, spotnumber):
        player = self.players[spotnumber]

        if player.source is None:
            # re-enqueue media
            player.queue(self.media[spotnumber])

        if player.time > 0:
            # play from beginning
            player.seek(0)

        player.play()


if __name__ == '__main__':
    pass
