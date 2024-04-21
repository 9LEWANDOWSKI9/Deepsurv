import os

def get_h5_file_paths(folder_path):
    h5_file_paths = []

    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for subfolder in subfolders:

        h5_files = [f for f in os.listdir(subfolder) if f.endswith('.h5')]

        for h5_file in h5_files:

            file_path = os.path.join(subfolder, h5_file)
            h5_file_paths.append(file_path)

    return h5_file_paths


data_folder_path = 'data'


h5_paths = get_h5_file_paths(data_folder_path)


for path in h5_paths:
    print(path)
