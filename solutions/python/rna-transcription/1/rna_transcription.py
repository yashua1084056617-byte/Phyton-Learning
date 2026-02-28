def to_rna(dna_strand):
    complement = ""
    for rna in dna_strand:
        if "G" in rna :
            complement += "C"
        elif "C" in rna:
            complement += "G"
        elif "T" in rna:
            complement += "A"
        elif "A" in rna:
            complement += "U"
    return complement
            
    
