# DNA Toolset/Code testing file
from Bio import SeqIO
from utilities import read_FASTA, readTextFile, writeTextFile
from scoreGenerator import scoreGen

filein = "mitochondrion.1.1.genomic.fna"

seq_dict = {rec.description : rec.seq for rec in SeqIO.parse(filein, "fasta")}

start_index = 1
end_index = -1

scoreGen(seq_dict, start_index, end_index)
#print(scoreGen(seq_dict, start_index, end_index)[1])
'''
#print(scaler(seq_dict['NC_012975.1']))
selection = 'NC_012975.1'
test_dna = bio_seq(seq_dict[selection])
test_dna.generate_rnd_seq(len(seq_dict[selection]), "RNA")

#print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
#print(test_dna.transcription())
#print(test_dna.reverse_complement())
print(test_dna.gc_content())
#print(test_dna.gc_content_subsec())
#print(aminoscaler(test_dna.translate_seq()))

res = np.array(test_dna.translate_seq()) 
unique_res = np.unique(res) 
print(f"Unique elements of the list using numpy.unique(): {unique_res}")

for i in unique_res:
    print(test_dna.codon_usage(i))


#for rf in test_dna.gen_reading_frames():

# Store scaled primary seq frequencies and length as variables
primary_freq_list = primaryscaler(seq_dict[selection])[2]

# Store scaled amino acid frequencies and length as variables    
amino_freq_list = aminoscaler(test_dna.translate_seq())[2]

# Store scaled protein frequencies and length as variables
protein_frequency_dict = proteinscaler(test_dna.all_proteins_from_orfs())[2]

# Displays scaled protein frequencies and their corresponding lengths
#print(proteinscaler(test_dna.all_proteins_from_orfs()))

# Map scaled protein frequencies and their corresponding lengths to MIDI notes and export as a file
midimap(primary_freq_list, amino_freq_list, protein_frequency_dict, selection)



#print(sum(ticks))

##time = sum(ticks)/480
#dict_to_fft(frequency_dict, time)
'''