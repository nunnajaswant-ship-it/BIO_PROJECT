from Bio import Entrez, SeqIO
import pandas as pd


Entrez.email = "your_email@example.com" 


search_term = '("Human immunodeficiency virus 2"[Organism] AND "protease"[All Fields])'
search_handle = Entrez.esearch(db="protein", term=search_term, retmax=1745)
search_results = Entrez.read(search_handle)
id_list = search_results["IdList"]

print(f"Found {len(id_list)} sequences. Starting download...")


fetch_handle = Entrez.efetch(db="protein", id=id_list, rettype="fasta", retmode="text")
records = list(SeqIO.parse(fetch_handle, "fasta"))


sequence_data = []
for record in records:
    sequence_data.append({
        "Sequence ID": record.id,
        "Description": record.description,
        "Sequence": str(record.seq),
        "Length": len(record.seq)
    })


df = pd.DataFrame(sequence_data)
df.to_excel("HIV2_NCBI_Sequences.xlsx", index=False)

print("Success! File saved as HIV2_NCBI_Sequences.xlsx")
