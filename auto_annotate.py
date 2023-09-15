import os

file_path = '/home/sumit/Videos/path_of _frames_folder'

for file in os.listdir(file_path):
    if file != 'classes.txt':
        root, ext = os.path.splitext(file)
        text_file = f"{root}.txt"

        print(text_file)

        with open(os.path.join(file_path, text_file), 'w') as f:
            f.write('0 0.135417 0.128704 0.172917 0.081481\n')
            f.write('1 0.143750 0.924074 0.136458 0.064815\n')
            f.write('2 0.856510 0.924074 0.139063 0.068519\n')
            f.write('3 0.500000 0.875926 0.153125 0.166667\n')