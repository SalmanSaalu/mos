# fifo ,lru ,lfu
from collections import deque
def fifo(page_references, page_frames):
    page_table = deque(maxlen=page_frames)
    page_faults = 0
    page_replacements = 0

    for page in page_references:
        if page not in page_table:
            page_faults += 1
            if len(page_table) == page_frames:
                page_table.popleft()
                page_replacements += 1
            page_table.append(page)

    print("FIFO:")
    print("Page Faults:", page_faults)
    print("Page Replacements:", page_replacements)

def lru(page_references, page_frames):
    page_table = []
    page_faults = 0
    page_replacements = 0

    for page in page_references:
        if page not in page_table:
            page_faults += 1
            if len(page_table) == page_frames:
                page_table.pop(0)
                page_replacements += 1
            page_table.append(page)
        else:
            page_table.remove(page)
            page_table.append(page)

    print("LRU:")
    print("Page Faults:", page_faults)
    print("Page Replacements:", page_replacements)

def lfu(page_references, page_frames):
    page_table = []
    page_faults = 0
    page_replacements = 0
    frequency_table = {}

    for page in page_references:
        if page not in page_table:
            page_faults += 1
            if len(page_table) == page_frames:
                least_frequent_pages = [p for p in page_table if frequency_table[p] == min(frequency_table.values())]
                page_to_replace = least_frequent_pages[0]
                page_table.remove(page_to_replace)
                page_replacements += 1
            page_table.append(page)
            frequency_table[page] = 1
        else:
            frequency_table[page] += 1

    print("LFU:")
    print("Page Faults:", page_faults)
    print("Page Replacements:", page_replacements)

# Example usage
if __name__ == "__main__":
    page_frames = 3
    page_references = [2, 3, 4, 2, 1, 3, 7, 5, 4, 3, 6, 7, 3, 1, 5, 3, 6, 4, 2, 3]

    fifo(page_references, page_frames)
    lru(page_references, page_frames)
    lfu(page_references, page_frames)