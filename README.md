# DataCollectionScripts

> This repository contains codes that can be used to simplify the "Data Collection" process.

Code 1: convertsheet.py

> Modifying Sheet ('.csv' file) according to the requirement i.e.- add column, process & modify the data on the sheet.

Code 2: video_downloader.py

> Downloads all the videos mentioned in the '.csv' file.

Code 3: makeClip.py, makeClipV2.py

> Creates clip from the video.

Code 4: makeFrames.py

> Extract frames from clipped video.

Code 5: auto_annotate.py

> To make training data for fix positioned labels with creating bounding boxes around region of interest.
  This code will create .txt file for all the existing files in folder, except 'classes.txt'.
  Here one will need to decide ROI on the screen and edit the code according to number of labels involved.
