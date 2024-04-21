import os
def remove_prefix(files_folder_path):
    for filename in os.listdir(files_folder_path):
        if '-' in filename:
            new_filename = filename.split('-', 1)[1]
            old_filepath = os.path.join(files_folder_path, filename)
            new_filepath = os.path.join(files_folder_path, new_filename)

            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {filename} to {new_filename}')


files_folder_path = 'K_fold5_data'


remove_prefix(files_folder_path)

import os
import shutil

def rename_h5_files(folder_path):
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for subfolder in subfolders:
        h5_files = [f for f in os.listdir(subfolder) if f.endswith('.h5')]

        for h5_file in h5_files:

            folder_name = os.path.basename(subfolder)
            new_filename = f'{folder_name}.h5'

            old_filepath = os.path.join(subfolder, h5_file)
            new_filepath = os.path.join(subfolder, new_filename)

            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {h5_file} to {new_filename}')


folder_path = 'K_fold5_data'


rename_h5_files(folder_path)
