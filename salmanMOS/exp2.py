class FileAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.file_allocation_table = [-1] * total_blocks
        self.file_list = {}

    def allocate_files(self, strategy):
        file_name = input("Enter file name: ")
        file_size = int(input("Enter file size: "))

        if strategy == "Sequential":
            self.allocate_sequential(file_name, file_size)
        elif strategy == "Indexed":
            self.allocate_indexed(file_name, file_size)
        elif strategy == "Linked":
            self.allocate_linked(file_name, file_size)
        else:
            print("Invalid allocation strategy.")

    def allocate_sequential(self, file_name, file_size):
        start_block = 0
        while start_block < self.total_blocks and self.file_allocation_table[start_block] != -1:
            start_block += 1

        if start_block + file_size > self.total_blocks:
            print("Not enough consecutive free blocks available.")
            return

        for i in range(start_block, start_block + file_size):
            self.file_allocation_table[i] = file_name

        self.file_list[file_name] = list(range(start_block, start_block + file_size))
        print(f"File '{file_name}' allocated using Sequential strategy.")

    def allocate_indexed(self, file_name, file_size):
        if file_size + 1 > self.total_blocks:
            print("Not enough free blocks available.")
            return

        index_block = []
        data_blocks = []
        for i in range(file_size):
            while True:
                block = input(f"Enter block for data {i+1}: ")
                if block.isdigit() and 0 <= int(block) < self.total_blocks and self.file_allocation_table[int(block)] == -1:
                    break
                else:
                    print("Invalid block number or already allocated. Try again.")

            block = int(block)
            self.file_allocation_table[block] = file_name
            data_blocks.append(block)

        index_block.append(data_blocks)
        self.file_allocation_table[file_size] = index_block
        self.file_list[file_name] = [file_size]
        print(f"File '{file_name}' allocated using Indexed strategy.")

    def allocate_linked(self, file_name, file_size):
        data_blocks = []
        for i in range(file_size):
            while True:
                block = input(f"Enter block for data {i+1}: ")
                if block.isdigit() and 0 <= int(block) < self.total_blocks and self.file_allocation_table[int(block)] == -1:
                    break
                else:
                    print("Invalid block number or already allocated. Try again.")

            block = int(block)
            self.file_allocation_table[block] = file_name
            data_blocks.append(block)

        self.file_list[file_name] = data_blocks
        print(f"File '{file_name}' allocated using Linked strategy.")

    def display_file_allocation_table(self):
        print("File Allocation Table:")
        print(f"Block\tFile Name")
        for i, file_name in enumerate(self.file_allocation_table):
            print(f"{i}\t{file_name}")

    def display_files(self):
        print("Files:")
        for file_name, blocks in self.file_list.items():
            print(f"File: {file_name} - Blocks: {blocks}")

    def menu(self):
        while True:
            print("\nFile Allocation Strategies:")
            print("1. Allocate using Sequential strategy")
            print("2. Allocate using Indexed strategy")
            print("3. Allocate using Linked strategy")
            print("4. Display File Allocation Table")
            print("5. Display Files")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.allocate_files("Sequential")
            elif choice == "2":
                self.allocate_files("Indexed")
            elif choice == "3":
                self.allocate_files("Linked")
            elif choice == "4":
                self.display_file_allocation_table()
            elif choice == "5":
                self.display_files()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    total_blocks = int(input("Enter the total number of blocks: "))
    file_allocation = FileAllocation(total_blocks)
    file_allocation.menu()