import os

def list_subfolders_and_files(folder_path):
    entries = os.scandir(folder_path)
    with open('folders_and_files.txt', 'w') as file:
        for entry in entries:
            if entry.is_dir():
                file.write(f'{entry.name}\n')
            else:
                file.write(f'{entry.name}\n')

if __name__ == "__main__":
   path = "D:/Best Summer Research Project/van_allen_code/pnet_prostate_paper/utils/"
   list_subfolders_and_files(path)
