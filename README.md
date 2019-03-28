# KZSU Spotbox

AKA "jingle box" AKA "digicart." Software that allows DJs to cue and play
back short audio tracks.

## Authors

Written by Mark Mollineaux (2013) <bufordsharkley@gmail.com>

## Installation and running

### Prerequisites

You need the following:

- Python 2.7 and `pip`
- Recommended: AVBin for playing spotbox files (https://avbin.github.io/AVbin/Download.html)

Use `pip install` to install:

- `pip install pyglet`

### Steps to install

- Download the spotbox code from GitHub (clone or zip)
- Navigate to the repository
- Create a shortcut, script, or alias to run `python spotbox.py`.

## Contributing

Read the [contribution guidelines](./CONTRIBUTING.md) to help out.

## More info

Uses Tkinter front-end, simple python backend, and allows for audio playback
through iTunes, through appscript, a python wrapper for Applescript. A more
cross-platform playback method may be Pyglet (not fully implemented), which
doesn't have the reliability of iTunes, but is less of a hacky implementation.

Allows for menus for multiple types of audio files (PSAs, LIDs), with metadata
configured in the filename itself. The menu headers/etc are configured in a
dict in the spotbox.py file.

Files are loaded statically on startup from the MEDIA folder. Any files that
need to be queried for updates (for instance, a Dropbox folder containing
newscasts) are given the "polling" designation.
