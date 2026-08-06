import json
import pandas as pd

df = pd.read_csv('data/processed/batch_features.csv')
params = ['Granulation_Time', 'Binder_Amount', 'Drying_Temp', 'Drying_Time',
          'Compression_Force', 'Machine_Speed', 'Lubricant_Conc', 'Moisture_Content']

t009 = df[df['Batch_ID'] == 'T009'][params].iloc[0].to_dict()
t005 = df[df['Batch_ID'] == 'T005'][params].iloc[0].to_dict()

f = open('data/processed/golden_signatures.json')
gs = json.load(f); f.close()

for key, batch, score in [
    ('GS1_MaxQuality_MinEnergy', t009, 0.72),
    ('GS2_MaxYield_MinCarbon',   t005, 0.70),
    ('GS3_Balanced',             t005, 0.68),
]:
    gs[key]['composite_score'] = score
    gs[key]['version']         = 1
    gs[key]['update_history']  = []
    gs[key]['process_params']  = {k: round(float(v), 3) for k, v in batch.items()}

f = open('data/processed/golden_signatures.json', 'w')
json.dump(gs, f, indent=2); f.close()
print('Demo ready. GS reset with correct baselines.')