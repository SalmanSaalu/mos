import math

# Function to calculate the number of pages required for a given memory size and page size
def calculate_num_pages(memory_size, page_size):
    return math.ceil(memory_size / page_size)

# Main function
def main():
    # Input memory size and page size
    memory_size = int(input("Enter memory size (in bytes): "))
    page_size = int(input("Enter page size (in bytes): "))

    num_pages = calculate_num_pages(memory_size, page_size)

    # Input logical address
    logical_address = int(input("Enter logical address: "))

    # Calculate page offset and physical address
    page_offset = logical_address % page_size
    page_number = logical_address // page_size
    physical_address = (page_number * page_size) + page_offset

    # Display results
    print("Number of pages:", num_pages)
    print("Page offset:", page_offset)
    print("Physical address:", physical_address)

# Run the main function
if __name__ == "__main__":
    main()