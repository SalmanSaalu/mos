# fcfs,scan , csan
class DiskScheduling():
    
    def fcfs(self,initial_head, requests):
        total_head_movement = 0
        current_head = initial_head

        for request in requests:
            head_movement = abs(request - current_head)
            total_head_movement += head_movement
            current_head = request

        return total_head_movement

    def scan(self,initial_head, requests, max_cylinder):
        total_head_movement = 0
        current_head = initial_head
        direction = 1  # 1 for moving towards higher cylinders, -1 for moving towards lower cylinders

        while True:
            if current_head in requests:
                requests.remove(current_head)

            if not requests:
                break

            if current_head == max_cylinder:
                direction = -1
            elif current_head == 0:
                direction = 1

            current_head += direction
            total_head_movement += 1

        return total_head_movement

    def cscan(self,initial_head, requests, max_cylinder):
        total_head_movement = 0
        current_head = initial_head

        while True:
            if current_head in requests:
                requests.remove(current_head)

            if not requests:
                break

            if current_head == max_cylinder:
                current_head = 0
                total_head_movement += max_cylinder
            else:
                current_head += 1
                total_head_movement += 1

        return total_head_movement


if __name__ == "__main__":
    initial_head = 50
    requests = [82, 170, 43, 140, 24, 16, 190]
    max_cylinder = 199
    
    scheduler = DiskScheduling()
    fcfs_head_movement = scheduler.fcfs(initial_head, requests.copy())
    scan_head_movement = scheduler.scan(initial_head, requests.copy(), max_cylinder)
    cscan_head_movement = scheduler.cscan(initial_head, requests.copy(), max_cylinder)

    print("FCFS Head Movement:", fcfs_head_movement)
    print("SCAN Head Movement:", scan_head_movement)
    print("C-SCAN Head Movement:", cscan_head_movement)