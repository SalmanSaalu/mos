import threading
import time

class PhilosopherThread(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            print(f"{self.name} is contemplating.")
            time.sleep(2)  # Simulate contemplation

            print(f"{self.name} is hungry and attempting to pick up forks.")
            self.dine()

    def dine(self):
        while True:
            self.left_fork.acquire()  # Acquire left fork
            locked = self.right_fork.acquire(False)  # Acquire right fork without blocking

            if locked:
                break

            self.left_fork.release()  # Release left fork
            print(f"{self.name} is waiting to pick up the right fork.")

        self.eat()
        self.left_fork.release()  # Release left fork
        self.right_fork.release()  # Release right fork

    def eat(self):
        print(f"{self.name} is eating.")
        time.sleep(2)  # Simulate eating

if __name__ == "__main__":
    num_philosophers = 5
    philosophers = []

    forks = [threading.Lock() for _ in range(num_philosophers)]

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher = PhilosopherThread(f"Philosopher {i+1}", left_fork, right_fork)
        philosophers.append(philosopher)
        philosopher.start()
    # Wait for all philosophers to finish
    for philosopher in philosophers:
        philosopher.join()