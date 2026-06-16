# check_notes.py

import pickle

notes = pickle.load(
    open("notes.pkl", "rb")
)

print("Total Notes:", len(notes))

print(notes[:20])