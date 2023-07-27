class Banker:
    def __init__(self, available_resources, max_resources, allocated_resources):
        self.available_resources = available_resources
        self.max_resources = max_resources
        self.allocated_resources = allocated_resources
        self.num_processes = len(max_resources)
        self.num_resources = len(available_resources)
        self.need = self.calculate_need()

    def calculate_need(self):
        need = []
        for i in range(self.num_processes):
            process_need = []
            for j in range(self.num_resources):
                process_need.append(self.max_resources[i][j] - self.allocated_resources[i][j])
            need.append(process_need)
        return need

    def is_safe_state(self):
        work = self.available_resources.copy()
        finish = [False] * self.num_processes
        safe_sequence = []

        while True:
            found = False
            for i in range(self.num_processes):
                if not finish[i] and all(need <= work[j] for j, need in enumerate(self.need[i])):
                    work = [work[j] + self.allocated_resources[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True

            if not found:
                break

        return all(finish) and len(safe_sequence) == self.num_processes, safe_sequence

    def request_resources(self, process_id, request):
        if not all(0 <= request[j] <= self.need[process_id][j] for j in range(self.num_resources)):
            print("Invalid resource request.")
            return

        if not all(request[j] <= self.available_resources[j] for j in range(self.num_resources)):
            print("Insufficient resources available. Process must wait.")
            return

        self.available_resources = [self.available_resources[j] - request[j] for j in range(self.num_resources)]
        self.allocated_resources[process_id] = [self.allocated_resources[process_id][j] + request[j]
                                                for j in range(self.num_resources)]
        self.need[process_id] = [self.need[process_id][j] - request[j] for j in range(self.num_resources)]

        is_safe, safe_sequence = self.is_safe_state()
        if is_safe:
            print("Resource allocated. System is in a safe state.")
            print("Safe sequence:", safe_sequence)
        else:
            print("Resource allocation would lead to an unsafe state. Process must wait.")
            self.available_resources = [self.available_resources[j] + request[j] for j in range(self.num_resources)]
            self.allocated_resources[process_id] = [self.allocated_resources[process_id][j] - request[j]
                                                    for j in range(self.num_resources)]
            self.need[process_id] = [self.need[process_id][j] + request[j] for j in range(self.num_resources)]

    def display_state(self):
        print("Available resources:", self.available_resources)
        print("Max resources:")
        for i in range(self.num_processes):
            print(self.max_resources[i])
        print("Allocated resources:")
        for i in range(self.num_processes):
            print(self.allocated_resources[i])
        print("Need:")
        for i in range(self.num_processes):
            print(self.need[i])

# Example usage
if __name__ == "__main__":
    available_resources = [3, 3, 2]
    max_resources = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    allocated_resources = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    banker = Banker(available_resources, max_resources, allocated_resources)
    banker.display_state()

    # Request resources for process 1
    process_id = 1
    request = [1, 0, 2]
    banker.request_resources(process_id, request)

    # Request resources for process 4
    process_id = 4
    request = [3, 3, 0]
    banker.request_resources(process_id, request)

    banker.display_state()