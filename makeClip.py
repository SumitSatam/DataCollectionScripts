import os
import pandas as pd  
from pathlib import Path

videos_folder = '/home/sumit/Videos/'

df = pd.read_csv('final_sheet.csv', usecols=['fileName', 'clipStart', 'durationInSec'])

# Add new column with clipped video name
df['clip'] = 'c' + df['fileName'].apply(lambda x: Path(x).stem) + '.mp4' 

for index, row in df.iterrows():

    video_file = os.path.join(videos_folder, row['fileName'])
    
    start_time = row['clipStart']  
    duration = row['durationInSec']
    
    # Save clipped video with name from 'clip' column
    output_file = os.path.join(videos_folder, row['clip']) 
    
    ffmpeg_cmd = f'ffmpeg -ss {start_time} -t {duration} -i {video_file} -codec copy {output_file}'
    
    os.system(ffmpeg_cmd)

# Save updated CSV with new column  
df.to_csv('data_with_clips.csv', index=False)
