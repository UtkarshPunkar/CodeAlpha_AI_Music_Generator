# 🎵 AI Music Generator using LSTM

An AI-powered music generation system developed using Python, TensorFlow, and Music21 that learns musical patterns from MIDI files and generates new music compositions.

## 📌 Project Overview

This project uses Deep Learning and Recurrent Neural Networks (RNNs), specifically Long Short-Term Memory (LSTM) networks, to generate original music.

The model is trained on a collection of classical MIDI files, learns note sequences and musical structures, and then generates new note patterns that are converted back into a playable MIDI file.

This project was developed as part of the **CodeAlpha Internship Program**.

---

## 🚀 Features

* MIDI music data preprocessing
* Note and chord extraction using Music21
* Sequence generation for model training
* LSTM-based deep learning model
* AI-generated music creation
* Automatic MIDI file generation
* Support for classical music datasets

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* Music21
* NumPy
* Pickle

---

## 📂 Project Structure

```text
music-generator-ai/
│
├── dataset/
│   └── midi_files/
│
├── preprocess.py
├── train.py
├── generate.py
│
├── notes.pkl
├── music_model.h5
├── generated_music.mid
│
├── requirements.txt
└── README.md
```

---

## Dataset

The MIDI dataset is not included in this repository due to size limitations.

Users can download any public MIDI dataset and place the files inside:

dataset/midi_files/

---

## ⚙️ Workflow

### 1. Data Collection

* Download classical MIDI files.
* Store them inside the dataset folder.

### 2. Data Preprocessing

* Extract notes and chords from MIDI files.
* Convert musical data into note sequences.
* Save processed notes for training.

### 3. Model Training

* Build an LSTM Neural Network.
* Train the model on extracted note sequences.
* Learn musical patterns and note transitions.

### 4. Music Generation

* Load the trained model.
* Predict new note sequences.
* Convert predictions into MIDI format.

### 5. Output

* Generate a new MIDI music file.
* Save it as:

```text
generated_music.mid
```

---

## ▶️ Run Project

### Step 1: Preprocess MIDI Files

```bash
python preprocess.py
```

### Step 2: Train Model

```bash
python train.py
```

### Step 3: Generate Music

```bash
python generate.py
```

---

## 🎹 Output

After generation, a new MIDI file is created:

```text
generated_music.mid
```

Open it using:

* MuseScore
* VLC Media Player
* Windows Media Player
* Any MIDI-compatible software

---

## 📚 Learning Outcomes

Through this project, I learned:

* Music Data Processing
* MIDI File Handling
* Sequence Modeling
* Deep Learning with LSTM Networks
* Music Generation using AI
* TensorFlow Model Training

---

## 👨‍💻 Author

**Utkarsh Punkar** 
