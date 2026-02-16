import pandas as pd
from Bio.Align import PairwiseAligner


REF_SEQ = "PQFSLWKRPVVTAYIEGQPVEVLLDTGADDSIVAGIELGNNYSPKIVGGIGGFINTLEYKNVEIEVLNKKVRATIMTGDTTPINIFGRNILTKGLGCTLNF"


aligner = PairwiseAligner()

input_file = "C:/Users/nunna/OneDrive/Desktop/4th semester/IBS_2/LAB 1/HIV2_NCBI_Sequences.xlsx"
df = pd.read_excel(input_file)
print(f"Total sequences loaded: {len(df)}")

proper_sequences = []

for index, row in df.iterrows():
    seq = str(row['Sequence']).upper().strip()
    
    if not (90 <= len(seq) <= 110):
        continue

    if "DTG" not in seq:
        continue

    score = aligner.score(seq, REF_SEQ)
    identity_percent = (score / len(REF_SEQ)) * 100
    
    if identity_percent >= 80.0:
        row_dict = row.to_dict()
        row_dict['Identity_vs_1IVP'] = round(identity_percent, 2)
        proper_sequences.append(row_dict)

df_refined = pd.DataFrame(proper_sequences)
df_refined.to_excel("HIV2_PROPER_DATASET.xlsx", index=False)

print(f"Refinement complete. Final Count: {len(df_refined)}")
