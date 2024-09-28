import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Passenger:
    def __init__(self, name, age, phone, source_airport, destination_airport):
        self.name = name
        self.age = age
        self.phone = phone
        self.source_airport = source_airport
        self.destination_airport = destination_airport  

class ListNode:
    def __init__(self, passenger):
        self.passenger = passenger
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_passenger(self, passenger):
        new_node = ListNode(passenger)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_passenger(self, passenger_name):
        current = self.head
        while current:
            if current.passenger.name == passenger_name:
                return current.passenger
            current = current.next
        return None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = {}

    def add_edge(self, src, dest, weight):
        self.vertices[src][dest] = weight
        self.vertices[dest][src] = weight

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.vertices[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def list_all_airports(graph):
    airports = list(graph.vertices.keys())
    formatted_airports = "\n".join(f"{i + 1}. {airport}" for i, airport in enumerate(airports))
    return formatted_airports

def show_flight_map(graph):
    lines = ["*" * 60, "        Flight Map", "       ------------------", "-" * 50]

    for airport, connections in graph.vertices.items():
        line = f"\n{airport} =>"

        for neighbor, weight in connections.items():
            line += f"\n\t{neighbor:<25} {weight}"

        lines.append(line)

    lines.extend(["-" * 50, "-" * 50])
    return "\n".join(lines)

def get_shortest_distance(graph, source, destination):
    source_name = get_airport_name(source.upper())
    destination_name = get_airport_name(destination.upper())

    if not source_name or not destination_name:
        return "Invalid airport code(s). Please enter valid codes."

    distances = dijkstra(graph, source_name)

    if destination_name not in distances:
        return f"No path found from {source_name} to {destination_name}."

    distance = distances[destination_name]
    return f"SHORTEST DISTANCE FROM {source_name} TO {destination_name} IS {distance}KM"

def get_shortest_time(graph, source, destination):
    source_name = get_airport_name(source.upper())
    destination_name = get_airport_name(destination.upper())

    if not source_name or not destination_name:
        return "Invalid airport code(s). Please enter valid codes."

    distances = dijkstra(graph, source_name)

    if destination_name not in distances:
        return f"No path found from {source_name} to {destination_name}."

    shortest_path = get_shortest_path_distance(graph, source_name, destination_name)
    total_time = (len(shortest_path) - 1) * 5
    return f"TIME FROM {source_name} TO {destination_name} IS {total_time} MINUTES"

def get_shortest_path_distance(graph, source, destination):
    distances = dijkstra(graph, source)
    path = [destination]
    current_vertex = destination

    while current_vertex != source:
        for neighbor, weight in graph.vertices[current_vertex].items():
            if distances[current_vertex] == distances[neighbor] + weight:
                path.append(neighbor)
                current_vertex = neighbor

    return path[::-1]

def showpath(graph, source, destination):
    source_name = get_airport_name(source.upper())
    destination_name = get_airport_name(destination.upper())

    if not source_name or not destination_name:
        return "Invalid airport code(s). Please enter valid codes."

    path_distance = get_shortest_path_distance(graph, source_name, destination_name)
    path_airports = path_distance
    path_airports = [airport for airport in path_airports if airport]

    return path_airports

def is_valid_airport(graph, input_value, input_type):
    if input_type == "code":
        return get_airport_name(input_value) in graph.vertices
    return False
def get_airport_name(airport_code):
    airport_mapping = {
        "QS": "Qasur",
        "RHK": "Rahim Yar Khan",
        "FSD": "Faisalabad",
        "PEW": "Peshawar",
        "GJ": "Gojra",
        "SGD": "Sargodha",
        "LHE": "Lahore",
        "GW": "Gujranwala",
        "LKN": "Larkana",
        "MUX": "Multan",
        "SKZ": "Sukkur",
        "BWP": "Bahawalpur",
        "ISB": "Islamabad",
        "SKT": "Sialkot",
        "KHI": "Karachi",
        "RWP": "Rawalpindi",
        "GWD": "Gwadar",
        "MDN": "Mardan",
        "SB": "Sibi",
        "TBT": "Turbat",
        "JCD": "Jacobabad",
        "TNK": "Tank",
        "BN": "Bannu",
        "KHT": "Kohat",
        "NWS": "Nowshera",
}

    return airport_mapping.get(airport_code, None)

def draw_flight_graph(graph):
    G = nx.Graph()
    for airport, connections in graph.vertices.items():
        for neighbor, weight in connections.items():
            G.add_edge(airport, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    labels = {k: f"{v}KM" for k, v in labels.items()}
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, font_color='black', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)
    plt.title("Flight Reservation System")
    plt.show()

def fareCalculator(graph, source, destination):
    source_name = get_airport_name(source.upper())
    destination_name = get_airport_name(destination.upper())

    if not source_name or not destination_name:
        return "Invalid airport code(s). Please enter valid codes."

    path_distance = get_shortest_path_distance(graph, source_name, destination_name)
    num_airports = len(path_distance)

    if num_airports == 0:
        return f"No path found from {source_name} to {destination_name}."

    fare = 20 + (num_airports - 1) * 1500
    return f"FARE FROM {source_name} TO {destination_name}  {fare} RUPEES"


class TicketBookingSystem:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.available_tickets = total_tickets
        self.passenger_records = LinkedList()
        self.waitlist = Queue()
        self.passenger_details = {}

    def book_tickets(self, num_tickets, passengers):
        if num_tickets <= self.available_tickets:
            for i in range(num_tickets):
                passenger = passengers[i]
                passenger_name = passenger.name
                self.add_passenger(passenger)
                ticket_number = f"Ticket {i + 1}"
                self.passenger_details[passenger_name] = {
                    'ticket_number': ticket_number,
                    'source_airport': passenger.source_airport,
                    'destination_airport': passenger.destination_airport
                }
            self.available_tickets -= num_tickets
            return True, []
        else:
            waiting_list = passengers[self.available_tickets:]
            for i in range(self.available_tickets):
                passenger = passengers[i]
                passenger_name = passenger.name
                self.add_passenger(passenger)
                ticket_number = f"Ticket {i + 1}"
                self.passenger_details[passenger_name] = {
                    'ticket_number': ticket_number,
                    'source_airport': passenger.source_airport,
                    'destination_airport': passenger.destination_airport
                }
            self.available_tickets = 0
            self.waitlist.enqueue(waiting_list)
            return False, waiting_list

    def check_ticket_availability(self):
        return self.available_tickets

    def get_passenger_details(self, passenger_name):
        current = self.passenger_records.head
        while current:
            if current.passenger.name == passenger_name:
                passenger_age = current.passenger.age
                passenger_phone = current.passenger.phone
                ticket_details = self.passenger_details.get(passenger_name, {}).get('ticket_number', '')
                return passenger_name, passenger_age, passenger_phone, ticket_details
            current = current.next
        return "Passenger not found"
    def add_passenger(self, passenger):
        new_node = ListNode(passenger)
        if not self.passenger_records.head:
            self.passenger_records.head = new_node
        else:
            current = self.passenger_records.head
            while current.next:
                current = current.next
            current.next = new_node

    def process_waiting_list(self, num_tickets):
        passengers_to_book = []
        for _ in range(num_tickets):
            if not self.waitlist.is_empty():
                passengers_to_book.append(self.waitlist.dequeue())

        if passengers_to_book:
            for passenger in passengers_to_book:
                self.passenger_records.add_passenger(passenger)
            self.available_tickets += num_tickets
            return True, []
        else:
            return False, []

    def add_to_waitlist(self, passenger_names):
        for name in passenger_names:
            passenger = self.passenger_records.find_passenger(name)
            if passenger:
                self.waitlist.enqueue(passenger)
            else:
                print(f"Passenger '{name}' not found in records.")

class TicketBookingPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Ticket Booking", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)
        self.airports_text_widget = tk.Text(self, height=20, width=60) 
        self.airports_text_widget.pack(pady=10)
        self.source_airport_entry = ttk.Entry(self, width=20)
        ttk.Label(self, text="Enter Source airport Code:").pack()
        self.source_airport_entry.pack(pady=5)

        self.destination_airport_entry = ttk.Entry(self, width=20)
        ttk.Label(self, text="Enter Destination airport Code:").pack()
        self.destination_airport_entry.pack(pady=5)
        button_book_tickets = ttk.Button(self, text="Book Tickets", command=self.book_tickets)
        button_book_tickets.pack(pady=10)

    def show_airports(self):
        airports = list_all_airports(self.controller.flight_graph)
        self.airports_text_widget.delete(1.0, tk.END)
        self.airports_text_widget.insert(tk.END, airports)

    def book_tickets(self, num_tickets, passengers):
        if num_tickets <= self.available_tickets:
            for i in range(num_tickets):
                passenger = passengers[i]
                passenger_name = passenger.name
                self.passenger_records.add_passenger(passenger)
                self.passenger_details[passenger_name] = f"Ticket {i + 1}"
            self.available_tickets -= num_tickets
            self.controller.ticket_booking_system.passenger_details = self.passenger_details

            return True, []
        else:
            waiting_list = passengers[self.available_tickets:]
            for i in range(self.available_tickets):
                passenger = passengers[i]
                passenger_name = passenger.name
                self.passenger_records.add_passenger(passenger)
                self.passenger_details[passenger_name] = f"Ticket {i + 1}"
            self.available_tickets = 0
            self.waitlist.enqueue(waiting_list)
            self.controller.ticket_booking_system.passenger_details = self.passenger_details

            return False, waiting_list
        
    def add_passenger(self, passenger):
     for i in range(self.total_tickets - self.available_tickets, self.total_tickets):
        passenger_name = passenger.name
        ticket_number = f"Ticket {i + 1}"
        self.passenger_details[passenger_name] = {
            'ticket_number': ticket_number,
            'source_airport': passenger.source_airport,
            'destination_airport': passenger.destination_airport
        }

        new_node = ListNode(passenger)
        if not self.passenger_records.head:
            self.passenger_records.head = new_node
        else:
            current = self.passenger_records.head
            while current.next:
                current = current.next
            current.next = new_node



class BookingHistoryPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Ticket Number", "Passenger Name", "Source airport", "Destination airport", "Fare")

        self.load_booking_history()

        button_show_details = ttk.Button(self, text="Show Details", command=self.show_ticket_details)
        button_show_details.pack(pady=10)

        button_back = ttk.Button(self, text="Back to Home", command=self.go_to_start_page)
        button_back.pack(pady=10)

        self.text_widget = tk.Text(self, height=10, width=50)
        self.text_widget.pack(pady=10)

    def load_booking_history(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        passenger_details = self.controller.ticket_booking_system.passenger_details

        if passenger_details:
            for passenger_name, details in passenger_details.items():
                ticket_number = details.get('ticket_number', '')
                source_airport = details.get('source_airport', '')
                destination_airport = details.get('destination_airport', '')
                fare = fareCalculator(self.controller.flight_graph, source_airport, destination_airport).split()[-2]  # Extract fare from the fareCalculator result
                self.tree.insert("", "end", values=(ticket_number, passenger_name, source_airport, destination_airport, fare))

            self.tree.pack(pady=10)

    def show_ticket_details(self):
        passenger_details = self.controller.ticket_booking_system.passenger_details

        if passenger_details:
            details_text = ""
            for passenger_name, details in passenger_details.items():
                if isinstance(details, dict):
                    ticket_number = details.get('ticket_number', '')
                    source_airport = details.get('source_airport', '')
                    destination_airport = details.get('destination_airport', '')
                    fare = fareCalculator(self.controller.flight_graph, source_airport, destination_airport).split()[-2] 
                    passenger_name, passenger_age, passenger_phone, _ = self.controller.ticket_booking_system.get_passenger_details(passenger_name)

                    details_text += f"Ticket Number: {ticket_number}\n"
                    details_text += f"Passenger Name: {passenger_name}\n"
                    details_text += f"Age: {passenger_age}\n"
                    details_text += f"Phone Number: {passenger_phone}\n"
                    details_text += f"Source airport: {source_airport}\n"
                    details_text += f"Destination airport: {destination_airport}\n"
                    details_text += f"Fare: {fare} RUPEES\n\n"
                else:
                    details_text += f"Ticket Number: {details}\n"
                    details_text += f"No additional details available.\n\n"

            if details_text:
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, details_text)
            else:
                messagebox.showinfo("No Tickets", "No tickets to display details.")
        else:
            messagebox.showinfo("No Tickets", "No tickets to display details.")

    def go_to_start_page(self):
        self.controller.show_frame("StartPage")

class SeatAvailabilityPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Seat Availability", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        button_check_availability = ttk.Button(self, text="Check Seat Availability", command=self.check_seat_availability)
        button_check_availability.pack(pady=10)

        button_back = ttk.Button(self, text="Back to Home", command=self.go_to_start_page)
        button_back.pack(pady=10)

    def check_seat_availability(self):
        available_tickets = self.controller.ticket_booking_system.check_ticket_availability()
        messagebox.showinfo("Seat Availability", f"Available Seats: {available_tickets}")

    def go_to_start_page(self):
        self.controller.show_frame("StartPage")

class flightApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("655x500")

        self.flight_graph = Graph()
        self.create_flight_map()
        self.ticket_booking_system = TicketBookingSystem(total_tickets=200)

        self.frames = {}
        for F in (TicketBookingPage, BookingHistoryPage, SeatAvailabilityPage, StartPage):
            frame = F(self, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.frames["StartPage"].ticket_booking_page = self.frames["TicketBookingPage"]

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_flight_map(self):
        
        self.flight_graph.add_vertex("Lahore")
        self.flight_graph.add_vertex("Karachi")
        self.flight_graph.add_vertex("Faisalabad")
        self.flight_graph.add_vertex("Multan")
        self.flight_graph.add_vertex("Sialkot")
        self.flight_graph.add_vertex("Bahawalpur")
        self.flight_graph.add_vertex("Quetta")
        self.flight_graph.add_vertex("Peshawar")
        self.flight_graph.add_vertex("Gujranwala")
        self.flight_graph.add_vertex("Rawalpindi")
        self.flight_graph.add_vertex("Sukkur")
        self.flight_graph.add_vertex("Mardan")
        self.flight_graph.add_vertex("Qasur")
        self.flight_graph.add_vertex("Okara")
        self.flight_graph.add_vertex("Jhang")
        self.flight_graph.add_vertex("Gojra")
        self.flight_graph.add_vertex("Larkana")
        self.flight_graph.add_vertex("Sargodha")
        self.flight_graph.add_vertex("Rahim Yar Khan")
        self.flight_graph.add_vertex("Sheikhupura")
        self.flight_graph.add_vertex("Hyderabad")
        self.flight_graph.add_vertex("Islamabad")
        self.flight_graph.add_vertex("Gwadar")
        self.flight_graph.add_vertex("Turbat")
        self.flight_graph.add_vertex("Sibi")
        self.flight_graph.add_vertex("Jacobabad")
        self.flight_graph.add_vertex("Gujrat")
        self.flight_graph.add_vertex("Jhelum")
        self.flight_graph.add_vertex("Chakwal")
        self.flight_graph.add_vertex("Khushab")
        self.flight_graph.add_vertex("Charsadda")
        self.flight_graph.add_vertex("Swabi")
        self.flight_graph.add_vertex("Attock")
        self.flight_graph.add_vertex("Dera Ismail Khan")
        self.flight_graph.add_vertex("Tank")
        self.flight_graph.add_vertex("Bannu")
        self.flight_graph.add_vertex("Kohat")
        self.flight_graph.add_vertex("Nowshera")
        self.flight_graph.add_vertex("Mianwali")
        self.flight_graph.add_vertex("Toba Tek Singh")

        self.flight_graph.add_edge("Islamabad", "Faisalabad", 300)  
        self.flight_graph.add_edge("Karachi", "Hyderabad", 160)  # Approx. 160 km
        self.flight_graph.add_edge("Hyderabad", "Sukkur", 320)  # Approx. 320 km
        self.flight_graph.add_edge("Sukkur", "Multan", 220)  # Approx. 220 km
        self.flight_graph.add_edge("Multan", "Faisalabad", 260)  # Approx. 260 km
        self.flight_graph.add_edge("Faisalabad", "Islamabad", 300)  # Approx. 300 km
        self.flight_graph.add_edge("Islamabad", "Rawalpindi", 15)  # Approx. 15 km
        self.flight_graph.add_edge("Rawalpindi", "Peshawar", 180)  # Approx. 180 km
        self.flight_graph.add_edge("Peshawar", "Quetta", 850)  # Approx. 850 km
        self.flight_graph.add_edge("Quetta", "Gwadar", 610)  # Approx. 610 km
        self.flight_graph.add_edge("Gwadar", "Turbat", 150)  # Approx. 150 km
        self.flight_graph.add_edge("Turbat", "Sibi", 300)  # Approx. 300 km
        self.flight_graph.add_edge("Sibi", "Jacobabad", 260)  # Approx. 260 km
        self.flight_graph.add_edge("Jacobabad", "Sukkur", 210)  # Approx. 210 km
        self.flight_graph.add_edge("Sukkur", "Rahim Yar Khan", 300)  # Approx. 300 km
        self.flight_graph.add_edge("Rahim Yar Khan", "Bahawalpur", 160)  # Approx. 160 km
        self.flight_graph.add_edge("Bahawalpur", "Lahore", 400)  # Approx. 400 km
        self.flight_graph.add_edge("Lahore", "Gujranwala", 80)  # Approx. 80 km
        self.flight_graph.add_edge("Gujranwala", "Sialkot", 40)  # Approx. 40 km
        self.flight_graph.add_edge("Sialkot", "Gujrat", 40)  # Approx. 40 km
        self.flight_graph.add_edge("Gujrat", "Jhelum", 70)  # Approx. 70 km
        self.flight_graph.add_edge("Jhelum", "Rawalpindi", 100)  # Approx. 100 km
        self.flight_graph.add_edge("Rawalpindi", "Chakwal", 120)  # Approx. 120 km
        self.flight_graph.add_edge("Chakwal", "Khushab", 140)  # Approx. 140 km
        self.flight_graph.add_edge("Khushab", "Sargodha", 160)  # Approx. 160 km
        self.flight_graph.add_edge("Sargodha", "Faisalabad", 80)  # Approx. 80 km
        self.flight_graph.add_edge("Faisalabad", "Jhang", 90)  # Approx. 90 km
        self.flight_graph.add_edge("Jhang", "Toba Tek Singh", 90)  # Approx. 90 km
        self.flight_graph.add_edge("Toba Tek Singh", "Sargodha", 80)  # Approx. 80 km
        self.flight_graph.add_edge("Sargodha", "Mianwali", 190)  # Approx. 190 km
        self.flight_graph.add_edge("Mianwali", "Dera Ismail Khan", 240)  # Approx. 240 km
        self.flight_graph.add_edge("Dera Ismail Khan", "Tank", 140)  # Approx. 140 km
        self.flight_graph.add_edge("Tank", "Bannu", 80)  # Approx. 80 km
        self.flight_graph.add_edge("Bannu", "Kohat", 160)  # Approx. 160 km
        self.flight_graph.add_edge("Kohat", "Nowshera", 140)  # Approx. 140 km
        self.flight_graph.add_edge("Nowshera", "Peshawar", 50)  # Approx. 50 km
        self.flight_graph.add_edge("Peshawar", "Charsadda", 30)  # Approx. 30 km
        self.flight_graph.add_edge("Charsadda", "Mardan", 35)  # Approx. 35 km
        self.flight_graph.add_edge("Mardan", "Swabi", 50)  # Approx. 50 km
        self.flight_graph.add_edge("Swabi", "Nowshera", 40)  # Approx. 40 km
        self.flight_graph.add_edge("Nowshera", "Attock", 120)  # Approx. 120 km
        self.flight_graph.add_edge("Attock", "Rawalpindi", 90) # Approx. 90 km 

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.ticket_booking_page = controller.frames["TicketBookingPage"]
        
        label = ttk.Label(self, text="Welcome to Pak Airlines", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        options_frame = ttk.Frame(self)
        options_frame.pack()

     
        self.text_widget = tk.Text(options_frame, height=20, width=80)
        self.text_widget.grid(row=0, column=0, columnspan=3, pady=10)

        button_list_airports = ttk.Button(options_frame, text="List all airports", command=lambda: self.show_options("List all airports"))
        button_list_airports.grid(row=1, column=0, padx=10)

        button_nodes_edges = ttk.Button(options_frame, text="Nodes and Edges", command=lambda: self.show_options("Nodes and Edges"))
        button_nodes_edges.grid(row=1, column=1, padx=10)

        button_show_map = ttk.Button(options_frame, text="Show the flight map", command=lambda: self.show_options("Show the flight map"))
        button_show_map.grid(row=1, column=2, padx=10)

        button_ticket_booking = ttk.Button(options_frame, text="Ticket booking", command=lambda: self.show_options("Ticket booking"))
        button_ticket_booking.grid(row=2, column=0, padx=10)

        button_booking_history = ttk.Button(options_frame, text="Recent booking history", command=lambda: self.show_options("Recent booking history"))
        button_booking_history.grid(row=2, column=1, padx=10)


        button_check_availability = ttk.Button(options_frame, text="Check seat availability", command=lambda: self.show_options("Check seat availability"))
        button_check_availability.grid(row=2, column=2, padx=10)

        button_exit = ttk.Button(options_frame, text="Exit", command=self.controller.quit)
        button_exit.grid(row=3, column=1, pady=10)

    def show_options(self, option):
        output = ""  

        if option == "List all airports":
           
            airports = list_all_airports(self.controller.flight_graph)
            
            self.text_widget.delete(1.0, tk.END)
            
            self.text_widget.insert(tk.END, airports)

        elif option == "Nodes and Edges":
            
            nodes_and_edges_info = self.get_nodes_and_edges_info()          
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, nodes_and_edges_info)

        elif option == "Show the flight map":
           
            draw_flight_graph(self.controller.flight_graph)

        elif option == "Ticket booking":
           
            self.ticket_booking_page.show_airports()
            source_airport_code = tk.simpledialog.askstring("Source airport", "Enter the CODE OF SOURCE airport:")
            destination_airport_code = tk.simpledialog.askstring("Destination airport", "Enter the CODE OF DESTINATION airport:")

            output += f"Source airport: {get_airport_name(source_airport_code)}\n"
            output += f"Destination airport: {get_airport_name(destination_airport_code)}\n"

            output += get_shortest_distance(self.controller.flight_graph, source_airport_code, destination_airport_code) + "\n"
            output += get_shortest_time(self.controller.flight_graph, source_airport_code, destination_airport_code) + "\n"
            output += fareCalculator(self.controller.flight_graph, source_airport_code, destination_airport_code) + "\n"
            path_nodes = showpath(self.controller.flight_graph, source_airport_code, destination_airport_code)
            output += f"Path nodes: {' => '.join(path_nodes)}\n"

            confirm_booking = tk.messagebox.askquestion("Confirmation", "Do you want to confirm the booking?")
            if confirm_booking == "yes":
                num_tickets = tk.simpledialog.askinteger("Number of Tickets", "Enter the number of tickets:")
                passengers = []
                for _ in range(num_tickets):
                    name = tk.simpledialog.askstring("Passenger Name", "Enter passenger name:")
                    age = tk.simpledialog.askstring("Passenger Age", "Enter passenger age:")
                    phone = tk.simpledialog.askstring("Passenger Phone", "Enter passenger phone number:")
                    passengers.append(Passenger(name, age, phone, source_airport_code, destination_airport_code))

                success, waiting_list = self.controller.ticket_booking_system.book_tickets(num_tickets, passengers)
                if success:
                    output += "Tickets booked successfully.\n"
                    output += f"TICKETS ARE SENT TO YOUR GIVEN NUMBER\n"
                else:
                    output += f"Tickets not available. Added to waiting list.\n"

                success, _ = self.controller.ticket_booking_system.process_waiting_list(len(waiting_list))
                if success:
                    output += "Waiting list processed successfully.\n"


            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, output)

        elif option == "Recent booking history":
            self.controller.show_frame("BookingHistoryPage")

        elif option == "Check seat availability":
            self.controller.show_frame("SeatAvailabilityPage")

    def get_nodes_and_edges_info(self):
        nodes_info = "Nodes:\n"
        for airport in self.controller.flight_graph.vertices:
            nodes_info += f"- {airport}\n"

        edges_info = "\nEdges:\n"
        for airport, connections in self.controller.flight_graph.vertices.items():
            for neighbor, weight in connections.items():
                edges_info += f"- {airport} to {neighbor} (Weight: {weight}KM)\n"

        return nodes_info + edges_info
    
    def go_to_booking_history(self):
        self.controller.show_frame("BookingHistoryPage")
if __name__ == "__main__":  
    app = flightApp()
    app.mainloop()
