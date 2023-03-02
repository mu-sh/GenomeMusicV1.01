# Genome Music

Genome Music translates primary sequence genome data into MIDI files to be used within a DAW. The script utilizes the DNA Toolkit created by Juris Laivins AKA RebelCoder in his [YouTube series](https://www.youtube.com/watch?v=3joOQ3A3KBQ&list=PLpSOMAcxEB_hD18TAtBrTlRJDyu-PmRbj&index=1).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary packages from requirements.txt.

```bash
pip install -r requirements.txt
```

## Usage

Extract primary sequence FASTA file to working directory or import your own desired DNA sequence in FASTA format.

Run main.py

MIDI files are saved to Final_MIDI_Scores folder simply import into any DAW or sequencer to use.

## Translation
### Scaler.py
Scaler.py defines three functions: primaryscaler, aminoscaler, and proteinscaler. These functions take a sequence of characters, scale them, and return the scaled sequence, the length of the sequence, and a dictionary that maps each character in the sequence to a frequency.

The primaryscaler function scales the input sequence of characters using a linear scaling function. The characters are first converted to lowercase, then scaled using the np.interp function, which interpolates between the original range (0 to 1) and the desired range (20 to 20000). The function returns the scaled sequence, its length, and a dictionary of frequencies.

The aminoscaler function scales the input sequence of amino acids by first converting it to lowercase and then applying the same scaling function as the primaryscaler function. Additionally, it includes a condition to handle underscores in the sequence. It returns the scaled sequence, its length, and a dictionary of frequencies.

The proteinscaler function scales the input sequence of proteins by first converting each protein to lowercase and then calculating the average frequency for each protein using the same scaling function as the primaryscaler function. It then scales the length of each protein by multiplying the length of the protein by 240 ticks (480 ticks per quarter note) for faster playback. Finally, it returns the scaled sequence, its length, and a dictionary of frequencies that maps each protein to its corresponding frequency and length.
### Midimapper.py
Midimapper.py defines two functions for generating MIDI files based on protein sequences. freq_to_midi_pitch() converts a given frequency to its corresponding MIDI pitch, which is a numerical value used to represent a specific musical note. The midimap() function takes in several input arguments, including two sets of frequency tuples and a protein frequency dictionary, and creates a new MIDI file with three tracks: one for the primary frequencies, one for the amino acid frequencies, and one for the protein frequencies. Each track is assigned the same tempo settings, and the frequency tuples are used to generate notes in each track with frequencies corresponding to their MIDI pitches.
### ScoreGenerator.py
ScoreGenerator.py, takes a dictionary of DNA sequences, selects a subset of sequences based on user-defined start and end indices, and generates random RNA sequences for each selected DNA sequence. It then scales the primary, amino acid, and protein sequence frequencies and lengths using custom functions and passes the scaled data to the MIDI mapper function for export. 

## Contributing

Clone and have fun, message me if you have any issues running the scripts or just want to chat!

## Demo
[Click here](https://www.youtube.com/channel/UCixFM0m2huAfIyIkEZXLelA) see a demo of the results of this code in action utilizing Ableton Live 11 and Touchdesigner to create a generative AV performance driven by DNA.
