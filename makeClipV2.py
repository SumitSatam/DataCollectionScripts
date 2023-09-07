import pandas as pd
from pathlib import Path
import os

VID_DIR = '/home/sumit/Videos/'

df = pd.read_csv('final_sheet.csv', usecols=['fileName','clipStart','durationInSec'])

df['clip'] = 'c' + df['fileName'].apply(lambda x: Path(x).stem) + '.mp4'

for i,r in df.iterrows():
    vin = os.path.join(VID_DIR, r['fileName'])
    vout = os.path.join(VID_DIR, r['clip'])
    
    os.system(f"ffmpeg -ss {r['clipStart']} -t {r['durationInSec']} -i {vin} -c copy {vout}")

df.to_csv('data_with_clips.csv', index=False)
