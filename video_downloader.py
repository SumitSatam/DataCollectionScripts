import csv
import youtube_dl


input_file = 'final_sheet.csv'

with open(input_file) as f:
    csv_reader = csv.reader(f)
    next(csv_reader) # skip header

    for row in csv_reader:
        videoLink = row[2]
        fileName = row[5]
        
        print(f"Downloading {videoLink}")
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{fileName}', 
            'noplaylist' : True
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([videoLink])
            
        print(f"Download completed for {videoLink}")
        
print("All Videos Downloaded Successfully.")
