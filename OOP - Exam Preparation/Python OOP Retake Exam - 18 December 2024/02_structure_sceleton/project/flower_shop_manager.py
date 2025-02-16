from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS = {"Flower": Flower, "LeafPlant": LeafPlant}
    VALID_CLIENTS = {"RegularClient": RegularClient, "BusinessClient": BusinessClient}

    def __init__(self):
        self.income: float = 0.0
        self.plants: list = []
        self.clients: list = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int,
                  plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")

        plant = self.VALID_PLANTS[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")

        client = self._take_client_by_phone(self.clients, client_phone_number)
        if client:
            raise ValueError("This phone number has been used!")

        new_client = self.VALID_CLIENTS[client_type](client_name, client_phone_number)
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = self._take_client_by_phone(self.clients, client_phone_number)
        if not client:
            raise ValueError("Client not found!")

        plants = self._take_all_plants_by_name(self.plants, plant_name)
        if not plants:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        plants = plants[::-1]
        order_amount = 0

        for idx in range(plant_quantity):
            curr_plant = plants.pop()
            self.income += curr_plant.price - (curr_plant.price * client.discount / 100)
            order_amount += curr_plant.price - (curr_plant.price * client.discount / 100)
            self.plants.remove(curr_plant)

        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        plant = self._take_plant_by_name(self.plants, plant_name)
        if not plant:
            return "No such plant name."
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        clients_for_remove = [client for client in self.clients if client.total_orders == 0]
        for client in clients_for_remove:
            if client in self.clients:
                self.clients.remove(client)

        return f"{len(clients_for_remove)} client/s removed."

    def shop_report(self):
        result = ["~Flower Shop Report~"]
        plants_data = {}
        for plant in self.plants:
            plant_name = plant.name
            if plant_name not in plants_data:
                plants_data[plant_name] = 0
            plants_data[plant_name] += 1

        sorted_plants_data = dict(sorted(plants_data.items(), key=lambda x: (-x[1], x[0])))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        total_orders = sum(c.total_orders for c in sorted_clients)

        result.append(f"Income: {self.income:.2f}")
        result.append(f"Count of orders: {total_orders}")

        result.append(f"~~Unsold plants: {len(self.plants)}~~")
        for plant, qty in sorted_plants_data.items():
            result.append(f"{plant}: {qty}")

        result.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted_clients:
            result.append(client.client_details())

        return "\n".join(result)

    @staticmethod
    def _take_client_by_phone(lst, phone_num):
        found_client = next((client for client in lst if client.phone_number == phone_num), None)
        return found_client

    @staticmethod
    def _take_plant_by_name(lst, plant_name):
        found_plant = next((plant for plant in lst if plant.name == plant_name), None)
        return found_plant

    @staticmethod
    def _take_all_plants_by_name(lst, plant_name):
        found_plants = [plant for plant in lst if plant.name == plant_name]
        return found_plants


# Create an instance of FlowerShopManager
manager = FlowerShopManager()

# Add plants
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Lily", 20.00, 180, "Summer"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print()

# Add clients
print(manager.add_client("RegularClient", "Alice Johnson", "1234567890"))
print(manager.add_client("RegularClient", "Bob Smith", "0987654321"))
print(manager.add_client("BusinessClient", "Greenhouse Inc.", "5647382910"))
print(manager.add_client("BusinessClient", "CoolGarden Plc.", "9647382910"))
print(manager.add_client("RegularClient", "Peter Johnson", "382910"))
print()

# Perform sales
print(manager.sell_plants("1234567890", "Rose", 3))
print(manager.sell_plants("0987654321", "Tulip", 2))
print(manager.sell_plants("5647382910", "Cactus", 1))
print()

# Get shop report
print(manager.shop_report())
print()

# Perform sales
print(manager.sell_plants("1234567890", "Lily", 2))
print(manager.sell_plants("0987654321", "Fern", 1))
print(manager.sell_plants("5647382910", "Snake Plant", 2))
print()

# Remove a plant
print(manager.remove_plant("Nonexistent"))
print(manager.remove_plant("Cactus"))
print()

# Get shop report
print(manager.shop_report())
print()

# Remove clients who have no orders
print(manager.remove_clients())
print(manager.remove_clients())



"""
Rose is added to the shop as Flower.
Rose is added to the shop as Flower.
Rose is added to the shop as Flower.
Rose is added to the shop as Flower.
Tulip is added to the shop as Flower.
Tulip is added to the shop as Flower.
Lily is added to the shop as Flower.
Cactus is added to the shop as LeafPlant.
Cactus is added to the shop as LeafPlant.
Fern is added to the shop as LeafPlant.
Fern is added to the shop as LeafPlant.
Fern is added to the shop as LeafPlant.
Snake Plant is added to the shop as LeafPlant.
Snake Plant is added to the shop as LeafPlant.

Alice Johnson is successfully added as a RegularClient.
Bob Smith is successfully added as a RegularClient.
Greenhouse Inc. is successfully added as a BusinessClient.
CoolGarden Plc. is successfully added as a BusinessClient.
Peter Johnson is successfully added as a RegularClient.

3pcs. of Rose plant sold for 46.50
2pcs. of Tulip plant sold for 24.00
1pcs. of Cactus plant sold for 8.00

~Flower Shop Report~
Income: 78.50
Count of orders: 3
~~Unsold plants: 8~~
Fern: 3
Snake Plant: 2
Cactus: 1
Lily: 1
Rose: 1
~~Clients number: 5~~
Client: Bob Smith, Phone number: 0987654321, Orders count: 1, Discount: 5%
Client: Alice Johnson, Phone number: 1234567890, Orders count: 1, Discount: 5%
Client: Greenhouse Inc., Phone number: 5647382910, Orders count: 1, Discount: 0%
Client: Peter Johnson, Phone number: 382910, Orders count: 0, Discount: 0%
Client: CoolGarden Plc., Phone number: 9647382910, Orders count: 0, Discount: 0%

Not enough plant quantity.
1pcs. of Fern plant sold for 6.17
2pcs. of Snake Plant plant sold for 24.00

No such plant name.
Removed Leaf Plant: Cactus, Price: 8.00, Watering: 50ml, Size: M

~Flower Shop Report~
Income: 108.67
Count of orders: 5
~~Unsold plants: 4~~
Fern: 2
Lily: 1
Rose: 1
~~Clients number: 5~~
Client: Bob Smith, Phone number: 0987654321, Orders count: 2, Discount: 5%
Client: Greenhouse Inc., Phone number: 5647382910, Orders count: 2, Discount: 10%
Client: Alice Johnson, Phone number: 1234567890, Orders count: 1, Discount: 5%
Client: Peter Johnson, Phone number: 382910, Orders count: 0, Discount: 0%
Client: CoolGarden Plc., Phone number: 9647382910, Orders count: 0, Discount: 0%

2 client/s removed.
0 client/s removed.

"""
