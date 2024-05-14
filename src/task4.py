import os
import time


def handle_files(folder_path: str, n: int):
    current_time = time.time()

    max_age = n * 24 * 60 * 60

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)

            if file_age > max_age:
                os.remove(file_path)
                print(f'file {file_name} deleted')
