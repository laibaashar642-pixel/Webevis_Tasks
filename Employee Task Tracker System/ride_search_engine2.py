import math

# ============================================================
# DATA STRUCTURES — Teen dictionaries mein sab kuch store hoga
# ============================================================
drivers = {}   # driver_id → driver info
riders = {}    # rider_id  → rider info
requests = {}  # request_id → ride ticket
request_counter = 1

# ============================================================
# HELPER FUNCTION — Distance calculate karna
# Logic: Euclidean distance formula → √((x2-x1)² + (y2-y1)²)
# ============================================================
def calculate_distance(loc1, loc2):
    return math.sqrt((loc2[0] - loc1[0])**2 + (loc2[1] - loc1[1])**2)

# ============================================================
# 1. add_driver — Naya driver add karo
# Logic: ID already exist karta hai? → error
#        Nahi karta? → dictionary mein store karo
# ============================================================
def add_driver(driver_id, name, location):
    if driver_id in drivers:
        print(f"Error: Driver '{driver_id}' already exists!")
        return
    drivers[driver_id] = {
        "name": name,
        "location": location,      # (x, y) tuple
        "available": True,          # default available
        "rating": 5.0,             # default rating
        "rides_completed": 0
    }
    print(f"Driver '{name}' added successfully!")

# ============================================================
# 2. add_rider — Naya rider add karo
# Logic: Same as add_driver
# ============================================================
def add_rider(rider_id, name, location):
    if rider_id in riders:
        print(f"Error: Rider '{rider_id}' already exists!")
        return
    riders[rider_id] = {
        "name": name,
        "location": location
    }
    print(f"Rider '{name}' added successfully!")

# ============================================================
# 3. request_ride — Rider ride maange
# Logic: Rider exist karta hai? → ride ticket banao
#        Status = REQUESTED, driver = None abhi
# ============================================================
def request_ride(rider_id, pickup, drop):
    global request_counter
    if rider_id not in riders:
        print(f"Error: Rider '{rider_id}' not found!")
        return
    req_id = f"REQ{request_counter}"
    requests[req_id] = {
        "rider_id": rider_id,
        "pickup": pickup,
        "drop": drop,
        "status": "REQUESTED",     # lifecycle start
        "driver_id": None,          # abhi koi driver nahi
        "fare": 0
    }
    request_counter += 1
    print(f"Ride requested! Request ID: {req_id}")
    return req_id

# ============================================================
# 4. find_nearest_driver — Sabse paas wala available driver
# Logic: Sabhi available drivers ki distance calculate karo
#        Minimum distance wala return karo
# ============================================================
def find_nearest_driver(pickup_location):
    nearest_id = None
    min_distance = float('inf')   # infinity se shuru karo

    for driver_id, driver in drivers.items():
        if driver["available"]:   # sirf available drivers
            dist = calculate_distance(pickup_location, driver["location"])
            if dist < min_distance:
                min_distance = dist
                nearest_id = driver_id

    if nearest_id:
        print(f"Nearest driver: {drivers[nearest_id]['name']} (distance: {min_distance:.2f})")
    else:
        print("No available drivers found!")
    return nearest_id

# ============================================================
# 5. match_driver — Request ke liye driver assign karo
# Logic: Request REQUESTED state mein honi chahiye
#        Nearest driver dhundo → assign karo → unavailable karo
# ============================================================
def match_driver(request_id):
    if request_id not in requests:
        print(f"Error: Request '{request_id}' not found!")
        return
    req = requests[request_id]
    if req["status"] != "REQUESTED":
        print(f"Error: Request is already '{req['status']}'")
        return

    nearest = find_nearest_driver(req["pickup"])
    if not nearest:
        print("No driver available to match!")
        return

    # Driver assign karo
    req["driver_id"] = nearest
    req["status"] = "MATCHED"
    drivers[nearest]["available"] = False   # driver busy ho gaya

    print(f"Driver '{drivers[nearest]['name']}' matched to request '{request_id}'!")

# ============================================================
# 6. start_ride — Ride shuru karo
# Logic: Status MATCHED honi chahiye → STARTED
# ============================================================
def start_ride(request_id):
    if request_id not in requests:
        print(f"Error: Request '{request_id}' not found!")
        return
    req = requests[request_id]
    if req["status"] != "MATCHED":
        print(f"Error: Cannot start — status is '{req['status']}'")
        return
    req["status"] = "STARTED"
    print(f"Ride '{request_id}' started!")

# ============================================================
# 7. complete_ride — Ride complete karo
# Logic: Status STARTED honi chahiye → COMPLETED
#        Fare calculate karo — distance × 10
#        Driver free karo, rides_completed++
# ============================================================
def complete_ride(request_id):
    if request_id not in requests:
        print(f"Error: Request '{request_id}' not found!")
        return
    req = requests[request_id]
    if req["status"] != "STARTED":
        print(f"Error: Cannot complete — status is '{req['status']}'")
        return

    # Fare calculate karo
    dist = calculate_distance(req["pickup"], req["drop"])
    req["fare"] = round(dist * 10, 2)   # 10 coins per unit
    req["status"] = "COMPLETED"

    # Driver free karo
    driver_id = req["driver_id"]
    drivers[driver_id]["available"] = True
    drivers[driver_id]["rides_completed"] += 1

    print(f"Ride '{request_id}' completed! Fare: {req['fare']} coins")

# ============================================================
# 8. cancel_ride — Ride cancel karo
# Logic: REQUESTED ya MATCHED state mein cancel ho sakti hai
#        Driver ko free karo agar assigned tha
# ============================================================
def cancel_ride(request_id):
    if request_id not in requests:
        print(f"Error: Request '{request_id}' not found!")
        return
    req = requests[request_id]
    if req["status"] in ["STARTED", "COMPLETED"]:
        print(f"Error: Cannot cancel — ride is '{req['status']}'")
        return

    # Agar driver assign tha → free karo
    if req["driver_id"]:
        drivers[req["driver_id"]]["available"] = True

    req["status"] = "CANCELLED"
    print(f"Ride '{request_id}' cancelled!")

# ============================================================
# 9. rate_driver — Driver ko rate karo
# Logic: Sirf COMPLETED rides pe rating ho sakti hai
#        Average rating calculate karo
# ============================================================
def rate_driver(request_id, rating):
    if request_id not in requests:
        print(f"Error: Request '{request_id}' not found!")
        return
    req = requests[request_id]
    if req["status"] != "COMPLETED":
        print("Error: Can only rate completed rides!")
        return
    if not (1 <= rating <= 5):
        print("Error: Rating must be between 1 and 5!")
        return

    driver_id = req["driver_id"]
    driver = drivers[driver_id]
    rides = driver["rides_completed"]

    # Average rating update karo
    driver["rating"] = round(
        (driver["rating"] * (rides - 1) + rating) / rides, 2
    )
    print(f"Driver '{driver['name']}' rated {rating}/5 — New avg: {driver['rating']}")

# ============================================================
# TESTING — Poora flow test karo
# ============================================================
print("=" * 50)
print("RIDE SHARING SYSTEM — TEST")
print("=" * 50)

print("\n--- Drivers aur Riders Add karo ---")
add_driver("D1", "Ali", (0, 0))
add_driver("D2", "Umair", (5, 5))
add_driver("D3", "Hamza", (10, 10))
add_rider("R1", "Ahmed", (1, 1))
add_rider("R2", "Sara", (4, 4))

print("\n--- Duplicate test ---")
add_driver("D1", "Ali", (0, 0))   # Error aana chahiye

print("\n--- Ride Request ---")
req1 = request_ride("R1", (1, 1), (8, 8))
req2 = request_ride("R2", (4, 4), (9, 9))

print("\n--- Driver Match karo ---")
match_driver(req1)
match_driver(req2)

print("\n--- Ride Start karo ---")
start_ride(req1)

print("\n--- Ride Complete karo ---")
complete_ride(req1)

print("\n--- Driver Rate karo ---")
rate_driver(req1, 5)

print("\n--- Ride Cancel karo ---")
cancel_ride(req2)

print("\n--- Invalid ID test ---")
start_ride("REQ99")   # Error aana chahiye

print("\n--- Final Driver Status ---")
for did, d in drivers.items():
    print(f"{did}: {d['name']} | Available: {d['available']} | Rating: {d['rating']} | Rides: {d['rides_completed']}")