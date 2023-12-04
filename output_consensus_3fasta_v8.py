import sys
import gzip
from collections import Counter

def calculate_consensus(sequences):
    nucleotide_counts = Counter(sequences)
    
    for nucleotide, count in nucleotide_counts.items():
        if count >= 2:
            consensus = nucleotide
            consensus_support = count
            return consensus, consensus_support
    
    return '', 0

def fasta_to_tabular(input_file, output_file):
    sequences = []
    
    with gzip.open(input_file, 'rt') as fasta_file:
        current_sequence = ""
        
        for line in fasta_file:
            line = line.strip()
            
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ""
            else:
                current_sequence += line
        
        if current_sequence:
            sequences.append(current_sequence)

    with gzip.open(output_file, 'wt') as tabular_file:
        for position in range(len(sequences[0])):
            position_nucleotides = [seq[position] for seq in sequences]
            
            # If there are two or more 'N's, treat it as missing data
            if position_nucleotides.count('N') >= 2:
                tabular_file.write(f"{position + 1}\t0\t.\n")
            else:
                consensus, support = calculate_consensus([n for n in position_nucleotides if n != 'N'])
                if consensus:
                    tabular_file.write(f"{position + 1}\t{consensus}\t{support}\n")
                else:
                    tabular_file.write(f"{position + 1}\t0\t.\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py inputfile outputfile")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    fasta_to_tabular(input_file, output_file)
