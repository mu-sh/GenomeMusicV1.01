# DNA Toolset/Code testing file
import numpy as np
from Bio import SeqIO
from bio_seq import bio_seq
from scaler import primaryscaler, aminoscaler, proteinscaler
from utilities import read_FASTA, readTextFile, writeTextFile
from midimapper import midimap


def scoreGen(seq_dict, start_index, end_index):
    
    keys = list(seq_dict.keys())
    selected_keys = keys[int(start_index):int(end_index)]
    print(selected_keys)

    for key in keys:
        selection = str(key)
        test_dna = bio_seq(seq_dict[selection], label=selection)
        test_dna.generate_rnd_seq(len(seq_dict[selection]), "RNA")

        # Store scaled primary seq frequencies and length as variables
        primary_freq_list = primaryscaler(seq_dict[selection])[2]
        primary_seq_len = primaryscaler(seq_dict[selection])[3]
        print(f"Primary seq length: {primary_seq_len}")

        # Store scaled amino acid frequencies and length as variables    
        amino_freq_list = aminoscaler(test_dna.translate_seq())[2]
        amino_seq_len = aminoscaler(test_dna.translate_seq())[3]  
        print(f"Amino seq length: {amino_seq_len}")

        # Store scaled protein frequencies and length as variables
        protein_frequency_dict = proteinscaler(test_dna.all_proteins_from_orfs())[2]
        protein_seq_len = proteinscaler(test_dna.all_proteins_from_orfs())[0]
        print(f"Protein seq length: {len(protein_seq_len)}")

        # Map scaled protein frequencies and their corresponding lengths to MIDI notes and export as a file
        midimap(primary_freq_list, amino_freq_list, protein_frequency_dict, selection)
        seq_name = str(selection).replace(", complete genome", "")

    done = "Done"
    return seq_name, primary_seq_len, amino_seq_len, protein_seq_len, done 



#print(sum(ticks))

##time = sum(ticks)/480
#dict_to_fft(frequency_dict, time)
