import random
import math

class Simulation:
    def __init__(self, mean_interarrival: float, mean_service: float, num_delays_required: int, q_limit: int, store_name: str):
        # Input parameters
        self.mean_interarrival = mean_interarrival
        self.mean_service = mean_service
        self.num_delays_required = num_delays_required
        self.q_limit = q_limit
        self.store_name = store_name

        # State variables
        self.sim_time = 0.0
        self.server_status = 0  # 0 = idle, 1 = busy
        self.num_in_q = 0
        self.time_last_event = 0.0
        self.num_custs_delayed = 0
        self.total_of_delays = 0.0
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        self.time_next_event = [math.inf, math.inf, math.inf]  # index 1=arrival, 2=departure
        self.time_arrival = [0.0 for _ in range(self.q_limit + 1)]

        # File output (UTF-8 fix)
        self.outfile = open(f"{self.store_name}.out", "w", encoding="utf-8")

        # Initialize event list
        self.time_next_event[1] = self.sim_time + self.expon(self.mean_interarrival)
        self.time_next_event[2] = math.inf

        self.outfile.write(f"Simulation of Store: {self.store_name}\n")
        self.outfile.write("-------------------------------------------------\n\n")

    def expon(self, mean):
        """Generate an exponential random variate."""
        return -mean * math.log(random.random())

    def timing(self):
        """Determine the next event type and advance simulation clock."""
        min_time_next_event = math.inf
        next_event_type = 0

        for i in range(1, 3):
            if self.time_next_event[i] < min_time_next_event:
                min_time_next_event = self.time_next_event[i]
                next_event_type = i

        if next_event_type == 0:
            self.outfile.write("Event list empty at time {:.2f}\n".format(self.sim_time))
            return 0

        self.sim_time = min_time_next_event
        return next_event_type

    def arrive(self):
        """Handle an arrival event."""
        # Schedule next arrival
        self.time_next_event[1] = self.sim_time + self.expon(self.mean_interarrival)

        if self.server_status == 1:
            # Server busy → customer joins queue
            self.num_in_q += 1
            if self.num_in_q > self.q_limit:
                self.outfile.write(f"Queue overflow at time {self.sim_time:.2f}\n")
                return
            self.time_arrival[self.num_in_q] = self.sim_time
        else:
            # Server idle → customer begins service immediately
            self.server_status = 1
            delay = 0.0
            self.total_of_delays += delay
            self.num_custs_delayed += 1
            self.time_next_event[2] = self.sim_time + self.expon(self.mean_service)

    def depart(self):
        """Handle a departure event."""
        if self.num_in_q == 0:
            # Queue empty → make server idle
            self.server_status = 0
            self.time_next_event[2] = math.inf
        else:
            # Remove one customer from queue
            self.num_in_q -= 1
            delay = self.sim_time - self.time_arrival[1]
            self.total_of_delays += delay
            self.num_custs_delayed += 1
            self.time_next_event[2] = self.sim_time + self.expon(self.mean_service)

            # Shift the queue
            for i in range(1, self.num_in_q + 1):
                self.time_arrival[i] = self.time_arrival[i + 1]

    def close(self):
        """Write report and close output file."""
        avg_delay = self.total_of_delays / self.num_custs_delayed if self.num_custs_delayed else 0
        avg_num_in_q = self.area_num_in_q / self.sim_time if self.sim_time > 0 else 0
        server_util = self.area_server_status / self.sim_time if self.sim_time > 0 else 0

        self.outfile.write(f"\nSimulation Results for {self.store_name}\n")
        self.outfile.write("-------------------------------------------------\n")
        self.outfile.write(f"Total customers served: {self.num_custs_delayed}\n")
        self.outfile.write(f"Average delay in queue: {avg_delay:.3f} minutes\n")
        self.outfile.write(f"Average number in queue: {avg_num_in_q:.3f}\n")
        self.outfile.write(f"Server utilization: {server_util:.3f}\n")
        self.outfile.write(f"Simulation ended at time: {self.sim_time:.3f} minutes\n")

        self.outfile.close()


if __name__ == "__main__":
    sim = Simulation(
        mean_interarrival=11.3,
        mean_service=16.3,
        num_delays_required=14,
        q_limit=50,
        store_name="Sapphire-LuckyOne"
    )

    # Run simulation
    while sim.num_custs_delayed < sim.num_delays_required:
        next_event_type = sim.timing()
        if next_event_type == 1:
            sim.arrive()
        elif next_event_type == 2:
            sim.depart()
        else:
            break

    sim.close()
    print("✅ Simulation for Sapphire-LuckyOne completed. Check 'Sapphire-LuckyOne.out' file.")
