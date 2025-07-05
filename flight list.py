from flights import flight
class flight_list:
    def __init__(self,name):
        self.list_of_flights =[]


    def add_flight(self):
        carrier = input("Enter carrier: ")
        flight_code = input("Enter flight code: ")
        arrival = input("Enter arrival time: ")
        departure = input("Enter departure time: ")
        duration = input("Enter duration: ")
        source = input("Enter source: ")
        destination = input("Enter destination: ")
        new_flight = flight(carrier, flight_code, arrival, departure, duration, source, destination)
        self.list_of_flights.append(new_flight)
        print("flight added successfully")

    
    def delete_flight(self,given_code):
         found = False
         for i,flight in enumerate(self.list_of_flights):
              if flight.flight_code == given_code:
                   found = True
                   del self.list_of_flights[i]
                   break
         if not found:
              print("no such flight found")


    def display_all(self):
         print("-----------------all teh flights are---------------------")
         for flight in self.list_of_flights:
              flight.show_flight_info()
    
              
         
    def  search_flight(self,given_code):
        flag = False
        for flight in self.list_of_flights:
            if flight.flight_code == given_code:
                    flight.show_flight_info()
                    flag = True
                    break
            
        if flag == False:
             print("flight not found")
    
    def finding_flights(self,given_source,given_destination):
         found = False
         print("---------flights are given below-------------")
         for flight in self.list_of_flights:
              
              if (flight.source.lower() == given_source.lower() and flight.destination.lower() == given_destination.lower()):
                   found = True
                   flight.show_flight_info()
         if not found:
                   print("no flight found")

            

flight1 = flight(
    carrier="IndiGo",
    flight_code="6E203",
    arrival="09:45 AM",
    departure="07:15 AM",
    duration="2h 30m",
    source="Delhi",
    destination="Mumbai"
)

# Example 2
flight2 = flight(
    carrier="SpiceJet",
    flight_code="SG421",
    arrival="01:30 PM",
    departure="11:00 AM",
    duration="2h 30m",
    source="Delhi",
    destination="Mumbai"
)

# Example 3
flight3 = flight(
    carrier="Air India",
    flight_code="AI502",
    arrival="05:00 PM",
    departure="02:45 PM",
    duration="2h 15m",
    source="Kolkata",
    destination="Chennai"
)

# Example 4
flight4 = flight(
    carrier="Vistara",
    flight_code="UK811",
    arrival="10:10 AM",
    departure="08:00 AM",
    duration="2h 10m",
    source="Ahmedabad",
    destination="Delhi"
)

# Example 5
flight5 = flight(
    carrier="GoAir",
    flight_code="G8147", 
    arrival="08:30 PM",
    departure="06:00 PM",
    duration="2h 30m",
    source="Pune",
    destination="Goa"
)

flight_list1 = flight_list("local flights")
flight_list1.list_of_flights = [flight1,flight2,flight3,flight4,flight5]
flight_list1.display_all()


