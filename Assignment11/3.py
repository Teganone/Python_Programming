import os

def create_subdirectory(parent_dir, sub_dir):
    if os.path.exists(os.path.join(parent_dir, sub_dir)):
        remove_files(os.path.join(parent_dir, sub_dir))
        os.rmdir(os.path.join(parent_dir, sub_dir))
    os.makedirs(os.path.join(parent_dir, sub_dir))

def remove_files(directory):
    files = os.listdir(directory)
    for file in files:
        os.remove(os.path.join(directory,file))

def create_files(directory, num_files):
    for i in range(1, num_files + 1):
        with open(os.path.join(directory, f"{i}.txt"), 'w') as file:
            file.write(str(i))

def rename_files(directory):
    files = os.listdir(directory)
    for i, filename in enumerate(sorted(files)):
        if filename.endswith('.txt'):
            name, _ = filename.split('.txt')
            index = int(name)
            os.rename(os.path.join(directory, filename), os.path.join(directory, f"{str(index).zfill(3)}.txt"))

def main():
    parent_dir = '.'
    sub_dir = 'temp1'
    create_subdirectory(parent_dir, sub_dir)
    create_files(os.path.join(parent_dir, sub_dir), 10)
    rename_files(os.path.join(parent_dir, sub_dir))

if __name__ == "__main__":
    main()