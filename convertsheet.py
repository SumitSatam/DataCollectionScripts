import csv
import os
from datetime import datetime

input_file = '/home/sumit/Documents/test_sheet.csv'
output_file = 'final_sheet.csv'

with open(input_file, 'r') as read_obj, open(output_file, 'w', newline='') as write_obj:
    csv_reader = csv.DictReader(read_obj)
    fieldnames = csv_reader.fieldnames
    fieldnames.extend(['videoId', 'durationInSec', 'fileName'])
    csv_writer = csv.DictWriter(write_obj, fieldnames=fieldnames)
    csv_writer.writeheader()

    for row in csv_reader:
        video_link = row['videoLink']
        video_id = video_link.split('/')[-1][-10:]
        row['videoId'] = video_id
        
        start = datetime.strptime(row['clipStart'], '%H:%M:%S')
        end = datetime.strptime(row['clipEnd'], '%H:%M:%S')
        duration = (end - start).seconds
        row['durationInSec'] = duration

        row['fileName'] = video_id + '.mp4'
        csv_writer.writerow(row)

print('CSV file edited successfully!')
