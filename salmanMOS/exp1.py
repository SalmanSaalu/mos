def calculate_waiting_turnaround_time(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0
    turnaround_time[0] = processes[0]["burst_time"]

    for i in range(1, n):
        waiting_time[i] = processes[i - 1]["burst_time"] + waiting_time[i - 1]
        turnaround_time[i] = processes[i]["burst_time"] + waiting_time[i]

    for i in range(n):
        processes[i]["waiting_time"] = waiting_time[i]
        processes[i]["turnaround_time"] = turnaround_time[i]


def compare_arrival_time(p1, p2):
    return p1["arrival_time"] < p2["arrival_time"]


def compare_burst_time(p1, p2):
    return p1["burst_time"] < p2["burst_time"]


def compare_priority(p1, p2):
    return p1["priority"] < p2["priority"]


def fcfs(processes):
    processes.sort(key=lambda x: x["arrival_time"])

    calculate_waiting_turnaround_time(processes)

    print("FCFS Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(
            f"{process['process_id']}\t\t{process['burst_time']}\t\t{process['arrival_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}"
        )
    print()


def sjf(processes):
    processes.sort(key=lambda x: x["burst_time"])

    calculate_waiting_turnaround_time(processes)

    print("SJF Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(
            f"{process['process_id']}\t\t{process['burst_time']}\t\t{process['arrival_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}"
        )
    print()


def round_robin(processes, quantum):
    n = len(processes)
    remaining_time = [process["burst_time"] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    completed = 0

    while completed != n:
        for i in range(n):
            if remaining_time[i] <= quantum and remaining_time[i] > 0:
                current_time += remaining_time[i]
                remaining_time[i] = 0
                waiting_time[i] = current_time - processes[i]["burst_time"]
                turnaround_time[i] = current_time
                completed += 1
            elif remaining_time[i] > 0:
                current_time += quantum
                remaining_time[i] -= quantum

    print("Round Robin Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(
            f"{processes[i]['process_id']}\t\t{processes[i]['burst_time']}\t\t{processes[i]['arrival_time']}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}"
        )
    print()


def priority(processes):
    processes.sort(key=lambda x: x["priority"])

    calculate_waiting_turnaround_time(processes)

    print("Priority Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(
            f"{process['process_id']}\t\t{process['burst_time']}\t\t{process['arrival_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}"
        )
    print()


if __name__ == "__main__":
    processes = [
        {"process_id": 1, "burst_time": 10, "arrival_time": 0, "priority": 3},
        {"process_id": 2, "burst_time": 5, "arrival_time": 1, "priority": 2},
        {"process_id": 3, "burst_time": 8, "arrival_time": 2, "priority": 1},
        {"process_id": 4, "burst_time": 4, "arrival_time": 3, "priority": 4},
        {"process_id": 5, "burst_time": 6, "arrival_time": 4, "priority": 5},
    ]
    fcfs(processes.copy())
    sjf(processes.copy())
    round_robin(processes.copy(), 2)
    priority(processes.copy())
    
def calculate_waiting_turnaround_time(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0
    turnaround_time[0] = processes[0]["burst_time"]

    for i in range(1, n):
        waiting_time[i] = processes[i - 1]["burst_time"] + waiting_time[i - 1]
        turnaround_time[i] = processes[i]["burst_time"] + waiting_time[i]

    for i in range(n):
        processes[i]["waiting_time"] = waiting_time[i]
        processes[i]["turnaround_time"] = turnaround_time[i]


def compare_arrival_time(p1, p2):
    return p1["arrival_time"] < p2["arrival_time"]


def compare_burst_time(p1, p2):
    return p1["burst_time"] < p2["burst_time"]


def compare_priority(p1, p2):
    return p1["priority"] < p2["priority"]


def fcfs(processes):
    processes.sort(key=lambda x: x["arrival_time"])

    calculate_waiting_turnaround_time(processes)

    print("FCFS Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(
            f"{process['process_id']}\t\t{process['burst_time']}\t\t{process['arrival_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}"
        )
    print()


def sjf(processes):
    processes.sort(key=lambda x: x["burst_time"])

    calculate_waiting_turnaround_time(processes)

    print("SJF Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(
            f"{process['process_id']}\t\t{process['burst_time']}\t\t{process['arrival_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}"
        )
    print()


def round_robin(processes, quantum):
    n = len(processes)
    remaining_time = [process["burst_time"] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    completed = 0

    while completed != n:
        for i in range(n):
            if remaining_time[i] <= quantum and remaining_time[i] > 0:
                current_time += remaining_time[i]
                remaining_time[i] = 0
                waiting_time[i] = current_time - processes[i]["burst_time"]
                turnaround_time[i] = current_time
                completed += 1
            elif remaining_time[i] > 0:
                current_time += quantum
                remaining_time[i] -= quantum

    print("Round Robin Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(
            f"{processes[i]['process_id']}\t\t{processes[i]['burst_time']}\t\t{processes[i]['arrival_time']}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}"
        )
    print()


def priority(processes):
    processes.sort(key=lambda x: x["priority"])

    calculate_waiting_turnaround_time(processes)

    print("Priority Scheduling:")
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(
            f"{process['process_id']}\t\t{process['burst_time']}\t\t{process['arrival_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}"
        )
    print()


if __name__ == "__main__":
    processes = [
        {"process_id": 1, "burst_time": 10, "arrival_time": 0, "priority": 3},
        {"process_id": 2, "burst_time": 5, "arrival_time": 1, "priority": 2},
        {"process_id": 3, "burst_time": 8, "arrival_time": 2, "priority": 1},
        {"process_id": 4, "burst_time": 4, "arrival_time": 3, "priority": 4},
        {"process_id": 5, "burst_time": 6, "arrival_time": 4, "priority": 5},
    ]
    fcfs(processes.copy())
    sjf(processes.copy())
    round_robin(processes.copy(), 2)
    priority(processes.copy())