import math
import mido
from mido import Message


def freq_to_midi_pitch(frequency):
    # MIDI pitch values are defined such that A4 (A above middle C) has a pitch value of 69, 
    # with each semitone above or below A4 having a pitch value 1 higher or lower respectively.
    a4_pitch = 69
    a4_freq = 440 # A4 frequency (Hz)
    semitones_above_a4 = 12 * math.log2(frequency / a4_freq)
    pitch = a4_pitch + semitones_above_a4
    if pitch > 127:
        pitch = 127
    elif pitch < 0:
        pitch = 0    
    return int(pitch)



def midimap(primary_frequency_tuples, amino_frequency_tuples, protein_frequency_dict, filename):

    # Create a new MIDI file
    mid = mido.MidiFile()

    # Create three new tracks
    track_1 = mido.MidiTrack()
    track_name = mido.MetaMessage("track_name", name='Primary')
    track_1.append(track_name)
    track_2 = mido.MidiTrack()
    track_name = mido.MetaMessage("track_name", name='Amino acids')
    track_2.append(track_name)
    track_3 = mido.MidiTrack()
    track_name = mido.MetaMessage("track_name", name='Proteins')
    track_3.append(track_name)
    mid.tracks.append(track_1)
    mid.tracks.append(track_2)
    mid.tracks.append(track_3)

    # Set the tempo for all three tracks
    track_1.append(Message('control_change', control=0x51, value=0x07))
    track_1.append(Message('program_change', program=0))
    track_1.append(Message('control_change', control=0x01, value=0x00))
    track_1.append(Message('control_change', control=0x07, value=0x7F))
    track_1.append(Message('control_change', control=0x0A, value=0x00))
    track_1.append(Message('control_change', control=0x5B, value=0x00))
    track_1.append(Message('control_change', control=0x5D, value=0x00))
    track_1.append(Message('control_change', control=0x40, value=0x00))
    track_1.append(Message('control_change', control=0x43, value=0x00))
    track_1.append(Message('control_change', control=0x78, value=0x00))
    track_1.append(Message('control_change', control=0x7B, value=0x00))
    track_1.append(Message('control_change', control=0x7E, value=0x00))
    track_1.append(Message('control_change', control=0x7F, value=0x00))

    # Set the tempo for all three tracks
    track_2.append(Message('control_change', control=0x51, value=0x07))
    track_2.append(Message('program_change', program=0))
    track_2.append(Message('control_change', control=0x01, value=0x00))
    track_2.append(Message('control_change', control=0x07, value=0x7F))
    track_2.append(Message('control_change', control=0x0A, value=0x00))
    track_2.append(Message('control_change', control=0x5B, value=0x00))
    track_2.append(Message('control_change', control=0x5D, value=0x00))
    track_2.append(Message('control_change', control=0x40, value=0x00))
    track_2.append(Message('control_change', control=0x43, value=0x00))
    track_2.append(Message('control_change', control=0x78, value=0x00))
    track_2.append(Message('control_change', control=0x7B, value=0x00))
    track_2.append(Message('control_change', control=0x7F, value=0x00))
    track_2.append(Message('control_change', control=0x7E, value=0x00))

    # Set the tempo for all three tracks
    track_3.append(Message('control_change', control=0x51, value=0x07))
    track_3.append(Message('program_change', program=0))
    track_3.append(Message('control_change', control=0x01, value=0x00))
    track_3.append(Message('control_change', control=0x07, value=0x7F))
    track_3.append(Message('control_change', control=0x0A, value=0x00))
    track_3.append(Message('control_change', control=0x5B, value=0x00))
    track_3.append(Message('control_change', control=0x5D, value=0x00))
    track_3.append(Message('control_change', control=0x40, value=0x00))
    track_3.append(Message('control_change', control=0x43, value=0x00))
    track_3.append(Message('control_change', control=0x78, value=0x00))
    track_3.append(Message('control_change', control=0x7B, value=0x00))
    track_3.append(Message('control_change', control=0x7F, value=0x00))
    track_3.append(Message('control_change', control=0x7E, value=0x00))

    # Iterate through each dictionary and add each frequency as a note the corresponding track
    
    # Primary sequence notes
    for freq, duration in primary_frequency_tuples:
        pitch = freq_to_midi_pitch(freq)  # convert frequency to MIDI pitch
        on = Message('note_on', note=pitch)
        track_1.append(on)
        #print(duration)
        off = Message('note_off', note=pitch, time=duration)
        track_1.append(off)

    # Amino acid notes
    for freq, duration in amino_frequency_tuples:
        pitch = freq_to_midi_pitch(freq)  # convert frequency to MIDI pitch
        on = Message('note_on', note=pitch)
        track_2.append(on)
        #print(duration)
        off = Message('note_off', note=pitch, time=duration)
        track_2.append(off)
    
    
    # Protein notes
    for freq, duration in protein_frequency_dict.items():
        pitch = freq_to_midi_pitch(freq)  # convert frequency to MIDI pitch
        on = Message('note_on', note=pitch)
        track_3.append(on)
        #print(duration)
        off = Message('note_off', note=pitch, time=duration)
        track_3.append(off)

    # Save the MIDI file
    new_string = str(filename).replace(", complete genome", "")
    mid.save(f"Final_MIDI_Scores/{new_string}.mid")

    return print("Done")
