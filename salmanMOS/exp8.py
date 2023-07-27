import threading
import time

BUFFER_SIZE = 5
buffer = []
mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
items_to_produce = 10
items_produced = 0
items_consumed = 0

class ProducerThreadNew(threading.Thread):
    def run(self):
        global buffer, mutex, empty, full, items_to_produce, items_produced
        while items_produced < items_to_produce:
            time.sleep(1)  # Simulating production time
            empty.acquire()  # Wait if the buffer is full
            mutex.acquire()  # Acquire mutex to access the buffer
            buffer.append(items_produced)
            print(f"ProducerNew {self.name} produced: Item {items_produced}")
            items_produced += 1
            mutex.release()  # Release mutex
            full.release()  # Notify the consumer that an item is available

class ConsumerThreadNew(threading.Thread):
    def run(self):
        global buffer, mutex, empty, full, items_to_produce, items_consumed
        while items_consumed < items_to_produce:
            time.sleep(2)  # Simulating consumption time
            full.acquire()  # Wait if the buffer is empty
            mutex.acquire()  # Acquire mutex to access the buffer
            item = buffer.pop(0)
            print(f"ConsumerNew {self.name} consumed: Item {item}")
            items_consumed += 1
            mutex.release()  # Release mutex
            empty.release()  # Notify the producer that space is available

# Create producer and consumer threads
producer1_new = ProducerThreadNew()
producer2_new = ProducerThreadNew()
consumer1_new = ConsumerThreadNew()
consumer2_new = ConsumerThreadNew()

# Start the threads
producer1_new.start()
producer2_new.start()
consumer1_new.start()
consumer2_new.start()

# Wait for all threads to finish
producer1_new.join()
producer2_new.join()
consumer1_new.join()
consumer2_new.join() 