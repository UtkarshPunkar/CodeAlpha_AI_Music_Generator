import glob
from music21 import converter

files = glob.glob("dataset/midi_files/*.mid")

print("Files Found:", len(files))

print(files[:5])

midi = converter.parse(files[0])

print("MIDI Loaded Successfully")