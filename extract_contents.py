import os 

# loop through all folders in the current directory
for folder in os.listdir('.'):
    # check if the folder is a directory
    if os.path.isdir(folder):
        # loop through all files in the current folder
        # replace underscores with spaces, latex doesn't like it
        print(f"[{folder.replace('_', ' ')}]")
        for file in os.listdir(folder):
            # get the filename with and without the extension
            filename, file_extension = os.path.splitext(file)
            filename = filename.replace('_', ' ') 
            if file_extension == '.cpp':  
                file_path = os.path.join(folder, file)
                print(f"{file_path}\t{filename}")
