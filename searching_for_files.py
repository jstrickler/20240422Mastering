import os
import shutil

start_folder = '.'

for folder, subfolders, filenames in os.walk(start_folder):
    if '.git' in subfolders:
        subfolders.remove('.git')
    for filename in filenames:
        if filename.endswith('.json'):
            file_path = os.path.join(folder, filename)
            new_name = "wombat_" + filename
            new_path = os.path.join(folder, new_name)
            # os.rename(file_path, new_path)
            shutil.copy(file_path, new_path)
            file_size = os.path.getsize(new_path)
            print(f"{file_size:10d} {new_path}")
