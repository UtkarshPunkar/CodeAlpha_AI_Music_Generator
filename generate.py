import pickle
import numpy as np

from tensorflow.keras.models import load_model

from music21 import note
from music21 import stream
from music21 import chord

# ---------------------------
# Load Notes
# ---------------------------

notes = pickle.load(
    open("notes.pkl", "rb")
)

pitchnames = sorted(
    set(notes)
)

n_vocab = len(
    pitchnames
)

# ---------------------------
# Mappings
# ---------------------------

note_to_int = dict(
    (note, number)
    for number, note
    in enumerate(
        pitchnames
    )
)

int_to_note = dict(
    (number, note)
    for number, note
    in enumerate(
        pitchnames
    )
)

# ---------------------------
# Load Model
# ---------------------------

model = load_model(
    "music_model.h5"
)

# ---------------------------
# Random Starting Pattern
# ---------------------------

start = np.random.randint(
    0,
    len(notes)-50
)

pattern = [
    note_to_int[n]
    for n in notes[
        start:start+50
    ]
]

prediction_output = []

# ---------------------------
# Generate Notes
# ---------------------------

for note_index in range(
    200
):

    prediction_input = np.reshape(
        pattern,
        (
            1,
            len(pattern),
            1
        )
    )

    prediction_input = (
        prediction_input /
        float(n_vocab)
    )

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = np.argmax(
        prediction
    )

    result = int_to_note[
        index
    ]

    prediction_output.append(
        result
    )

    pattern.append(index)

    pattern = pattern[1:]

# ---------------------------
# Convert To MIDI
# ---------------------------

offset = 0

output_notes = []

for pattern in prediction_output:

    if (
        "." in pattern
        or pattern.isdigit()
    ):

        notes_in_chord = (
            pattern.split(".")
        )

        notes_list = []

        for current_note in notes_in_chord:

            new_note = note.Note(
                int(current_note)
            )

            new_note.offset = (
                offset
            )

            notes_list.append(
                new_note
            )

        new_chord = chord.Chord(
            notes_list
        )

        output_notes.append(
            new_chord
        )

    else:

        new_note = note.Note(
            pattern
        )

        new_note.offset = (
            offset
        )

        output_notes.append(
            new_note
        )

    offset += 0.5

# ---------------------------
# Save MIDI
# ---------------------------

midi_stream = stream.Stream(
    output_notes
)

midi_stream.write(
    "midi",
    fp="generated_music.mid"
)

print(
    "Music Generated Successfully!"
)