class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class SingleLevelDirectory:
    def __init__(self):
        self.files = {}

    def create_file(self, name, size):
        if name in self.files:
            print("File with the same name already exists.")
            return

        file = File(name, size)
        self.files[name] = file
        print(f"File '{name}' created in the single-level directory.")

    def delete_file(self, name):
        if name in self.files:
            del self.files[name]
            print(f"File '{name}' deleted from the single-level directory.")
        else:
            print("File not found in the single-level directory.")

    def display_files(self):
        if self.files:
            print("Files in the single-level directory:")
            for name, file in self.files.items():
                print(f"Name: {name} - Size: {file.size}")
        else:
            print("No files in the single-level directory.")

class TwoLevelDirectory:
    def __init__(self):
        self.directories = {}

    def create_file(self, directory, name, size):
        if directory not in self.directories:
            self.directories[directory] = {}

        if name in self.directories[directory]:
            print("File with the same name already exists in the directory.")
            return

        file = File(name, size)
        self.directories[directory][name] = file
        print(f"File '{name}' created in the directory '{directory}'.")

    def delete_file(self, directory, name):
        if directory in self.directories:
            if name in self.directories[directory]:
                del self.directories[directory][name]
                print(f"File '{name}' deleted from the directory '{directory}'.")
            else:
                print("File not found in the directory.")
        else:
            print("Directory not found.")

    def display_files(self):
        if self.directories:
            print("Files in the two-level directory:")
            for directory, files in self.directories.items():
                print(f"Directory: {directory}")
                if files:
                    for name, file in files.items():
                        print(f"\tName: {name} - Size: {file.size}")
                else:
                    print("\tNo files in the directory.")
        else:
            print("No directories in the two-level directory.")

class HierarchicalDirectory:
    def __init__(self):
        self.root = {}

    def create_file(self, path, name, size):
        directories = path.split("/")
        current_directory = self.root

        for directory in directories:
            if directory not in current_directory:
                current_directory[directory] = {}

            current_directory = current_directory[directory]

        if name in current_directory:
            print("File with the same name already exists in the directory.")
            return

        file = File(name, size)
        current_directory[name] = file
        print(f"File '{name}' created at path '{path}'.")

    def delete_file(self, path):
        directories = path.split("/")
        filename = directories[-1]
        current_directory = self.root

        for directory in directories[:-1]:
            if directory not in current_directory:
                print("Directory not found.")
                return

            current_directory = current_directory[directory]

        if filename in current_directory:
            del current_directory[filename]
            print(f"File '{filename}' deleted from path '{path}'.")
        else:
            print("File not found in the directory.")

    def display_files(self):
        if self.root:
            print("Files in the hierarchical directory:")
            self._display_files_recursive(self.root, "")
        else:
            print("No files in the hierarchical directory.")

    def _display_files_recursive(self, directory, path):
        for name, item in directory.items():
            if isinstance(item, File):
                print(f"Path: {path}/{name} - Size: {item.size}")
            elif isinstance(item, dict):
                self._display_files_recursive(item, f"{path}/{name}")


def simulate_single_level_directory():
    directory = SingleLevelDirectory()

    directory.create_file("file1.txt", 10)
    directory.create_file("file2.txt", 20)
    directory.display_files()

    directory.delete_file("file1.txt")
    directory.display_files()

def simulate_two_level_directory():
    directory = TwoLevelDirectory()

    directory.create_file("subdir1", "file1.txt", 10)
    directory.create_file("subdir1", "file2.txt", 20)
    directory.create_file("subdir2", "file3.txt", 15)
    directory.display_files()

    directory.delete_file("subdir1", "file1.txt")
    directory.display_files()

def simulate_hierarchical_directory():
    directory = HierarchicalDirectory()

    directory.create_file("dir1/subdir1", "file1.txt", 10)
    directory.create_file("dir1/subdir1", "file2.txt", 20)
    directory.create_file("dir1/subdir2", "file3.txt", 15)
    directory.display_files()

    directory.delete_file("dir1/subdir1/file1.txt")
    directory.display_files()

if __name__ == "__main__":
    print("Simulating Single Level Directory:")
    simulate_single_level_directory()

    print("\nSimulating Two Level Directory:")
    simulate_two_level_directory()

    print("\nSimulating Hierarchical Directory:")
    simulate_hierarchical_directory()