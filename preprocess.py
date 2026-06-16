from music21 import converter
from music21 import note
from music21 import chord
import glob
import pickle

notes = []

files = glob.glob(
    "dataset/midi_files/*.mid"
)

print("Files Found:", len(files))

for file in files:

    print("Reading:", file)

    midi = converter.parse(file)

    for element in midi.flatten().notes:

        if isinstance(element, note.Note):

            notes.append(
                str(element.pitch)
            )

        elif isinstance(
            element,
            chord.Chord
        ):

            notes.append(
                ".".join(
                    str(n)
                    for n in element.normalOrder
                )
            )

print("\nTotal Notes Found:", len(notes))

print("\nFirst 20 Notes:")

print(notes[:20])

with open(
    "notes.pkl",
    "wb"
) as f:

    pickle.dump(notes, f)

print("\nNotes Saved Successfully")