import numpy as np
import math

def primaryscaler(seq):
    primary_seq_length = len(seq)
    seq = seq.lower()
    scaled_seq  = []
    scaled_seq_len = []
    for i in seq:
        x = (ord(i)-96)/26

        # original range
        original_range = [0, 1]

        # desired range
        frequency_range = [20, 20000]

        # input value (between 0 and 1)
        input_value = x

        # scale the value
        primary_scaled_frequency = np.interp(input_value, original_range, frequency_range)

        scaled_seq.append(round(primary_scaled_frequency))

    value = 480
    note_lengths = [480] * primary_seq_length

    # Convert lists to list of tuples
    primary_freq_dict = [(key, value) for key, value in zip(scaled_seq, note_lengths)]
        
    
    #print(scaled_seq)
    return scaled_seq, scaled_seq_len, primary_freq_dict, primary_seq_length

def aminoscaler(seq):
    amino_seq_length = len(seq)
    seq = "".join(seq)
    seq = seq.lower()
    scaled_seq  = []
    scaled_seq_len = []
    for i in seq:
        if i == "_":
            scaled_seq.append(0.5)
        else:
            x = (ord(i)-96)/26

            # original range
            original_range = [0, 1]

            # desired range
            frequency_range = [20, 20000]

            # input value (between 0 and 1)
            input_value = x

            # scale the value
            amino_scaled_frequency = np.interp(input_value, original_range, frequency_range)

            scaled_seq.append(round(amino_scaled_frequency))

            value = 480
            note_lengths = [480] * amino_seq_length

            # Convert lists to list of tuples
            amino_freq_dict = [(key, value) for key, value in zip(scaled_seq, note_lengths)]
        
    
    
    return scaled_seq, scaled_seq_len, amino_freq_dict , amino_seq_length

def proteinscaler(seq):
    scaled_seq_ascii  = []
    scaled_seq_len = []
    for i in seq:

            # Converting to MIDI ticks (480 ticks per quarter note)

            # Mulitplying protein length by 240 ticks or eigth notes for faster playback 
            protein_ticks = len(seq[seq.index(i)])*240

            scaled_seq_len.append(protein_ticks)

            x = 0
            for char in i:
                char =  char.lower()
                x += (ord(char)-96)/26
            x = x/len(seq[seq.index(i)])

            # original range
            original_range = [0, 1]

            # desired range
            frequency_range = [20, 20000]

            # input value (between 0 and 1)
            input_value = x

            # scale the value
            scaled_frequency = np.interp(input_value, original_range, frequency_range)

            scaled_seq_ascii.append(round(scaled_frequency))

    # Convert lists to dictionary
    protein_frequency_dict = dict(map(lambda i,j : (i,j) , scaled_seq_ascii,scaled_seq_len))
    
    return scaled_seq_ascii, scaled_seq_len, protein_frequency_dict
