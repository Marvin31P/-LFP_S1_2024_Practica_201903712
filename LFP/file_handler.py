def read_pet_manager_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_pet_manager_file(file_path, content):
    with open(file_path, 'w') as file:
        file.writelines(content)