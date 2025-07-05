class flight:
    def __init__(self,carrier,flight_code,arrival,departure,duration,source,destination):
        self.carrier = carrier
        self.flight_code = flight_code
        self.arrival = arrival
        self.departure = departure
        self.duration = duration
        self.source  = source
        self.destination = destination
    

    def show_flight_info(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(f"flight_code : {self.flight_code}")
        print(f"carrier : {self.carrier}")
        print(f"arrival : {self.arrival} || departure : {self.departure}")
        print(f"source : {self.source} || destination : {self.destination}")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    
