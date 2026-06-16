import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

# ---------------------------
# Load Notes
# ---------------------------

notes = pickle.load(
    open("notes.pkl", "rb")
)

sequence_length = 50

pitchnames = sorted(set(notes))

n_vocab = len(pitchnames)

print("Unique Notes:", n_vocab)

# ---------------------------
# Note Mapping
# ---------------------------

note_to_int = dict(
    (note, number)
    for number, note
    in enumerate(pitchnames)
)

# ---------------------------
# Create Training Sequences
# ---------------------------

network_input = []
network_output = []

for i in range(
    len(notes) - sequence_length
):

    sequence_in = notes[
        i:i + sequence_length
    ]

    sequence_out = notes[
        i + sequence_length
    ]

    network_input.append(
        [
            note_to_int[note]
            for note in sequence_in
        ]
    )

    network_output.append(
        note_to_int[
            sequence_out
        ]
    )

n_patterns = len(network_input)

print(
    "Training Patterns:",
    n_patterns
)

# ---------------------------
# Reshape Input
# ---------------------------

network_input = np.reshape(
    network_input,
    (
        n_patterns,
        sequence_length,
        1
    )
)

network_input = (
    network_input /
    float(n_vocab)
)

network_output = np.array(
    network_output
)

# ---------------------------
# Build LSTM Model
# ---------------------------

model = Sequential()

model.add(
    LSTM(
        128,
        input_shape=(
            network_input.shape[1],
            network_input.shape[2]
        )
    )
)

model.add(
    Dropout(0.2)
)

model.add(
    Dense(
        n_vocab,
        activation="softmax"
    )
)

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam"
)

# ---------------------------
# Model Summary
# ---------------------------

model.summary()

# ---------------------------
# Train Model
# ---------------------------

print("\nTraining Started...\n")

model.fit(
    network_input,
    network_output,
    epochs=3,
    batch_size=64
)

# ---------------------------
# Save Model
# ---------------------------

model.save(
    "music_model.h5"
)

print(
    "\nModel Saved Successfully!"
)