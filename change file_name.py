import os
import shutil

def process_h5_files(folder_path):

    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for subfolder in subfolders:

        h5_files = [f for f in os.listdir(subfolder) if f.endswith('.h5')]

        for h5_file in h5_files:

            new_filename = h5_file.split('-')[-1]


            new_filepath = os.path.join(subfolder, new_filename)


            shutil.move(os.path.join(subfolder, h5_file), new_filepath)
            print(f'Moved: {h5_file} to {new_filepath}')


data_folder_path = 'K_fold5_data'


process_h5_files(data_folder_path)
