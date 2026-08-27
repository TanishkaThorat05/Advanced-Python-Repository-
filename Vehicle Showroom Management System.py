class Vehicle:
    def __init__(self, vehicle_number, brand, price, category):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = category

    def display(self):
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")
        print("-" * 30)


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully!")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
        else:
            print("\n--- All Vehicles ---")
            for vehicle in self.vehicles:
                vehicle.display()


# Create showroom
showroom = Showroom()

# Add vehicles
v1 = Vehicle("MH12AB1234", "BMW", 7500000, "Luxury")
v2 = Vehicle("MH14CD5678", "Maruti Suzuki", 800000, "Economy")
v3 = Vehicle("MH12EF9012", "Mercedes", 9000000, "Luxury")
v4 = Vehicle("MH14GH3456", "Tata", 700000, "Economy")

showroom.add_vehicle(v1)
showroom.add_vehicle(v2)
showroom.add_vehicle(v3)
showroom.add_vehicle(v4)

# Display all vehicles
showroom.display_all_vehicles()
