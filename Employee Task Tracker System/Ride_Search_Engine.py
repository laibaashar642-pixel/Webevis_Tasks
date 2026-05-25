#We have three mainly people to deal Driver,Riders,Request
drivers={}
riders={}
requests={}
request_counter=1
def add_driver(driver_id,name,location):
    if driver_id in drivers:
        print("Driver Already Exists")
        return
    print(f"Driver '{name}'added successfully")
    drivers[driver_id]={   
        "name":name,
       "location":location,
         "available":True,
         "rating":5.0,
         "ride_complete":0,}
   
def add_rider(rider_id,name,location):
    if rider_id in riders:
        print(f" Error{rider_id} Already Exists")
        return
    riders[rider_id]={
      "name":name,
     "location":location,}
    print(f"Rider '{name}' added successfully")
def request_ride(rider_id,pickup,drop):
    global request_counter
    if rider_id not in riders:
        print(f"Error: Rider'{rider_id}'  Not Found!")
        return
    req_id=f"REQ{request_counter}"
    requests[req_id]={
        "rider_id":rider_id,
         "pickup":pickup,
         "drop":drop,
         "driver_id":None,
         "fare":0,

    }
    request_counter += 1
    print(f"Ride Requested!:Request_Id{req_id}")
    return req_id

def find_nearest(pickup_location):
    nearest_id=None
    min_distance=float('inf') #Starting from Infinity
    for driver_id,drivers in drivers.items():
        if drivers["avaialble"]:
            dist = calculate_distance(pickup_location,drivers["location"])
            if dist <min_distance:
                min_distance=dist
                nearest_id=driver_id
    if nearest_id:
       print(f"Nearest Drivers{drivers[nearest_id]['name']}(distance:{min_distance:.2f})")
    else:
     print("No Available Drivers Found!")
    return nearest_id
def match_driver(request_id):
    if request_id not in requests:
        print(f"Error:Request{request_id} Not Found!")
        return
    req= requests[request_id]
    if req["status"]!="Requested":
        print(f"Error:Request is already{req['status']}")
        nearest=find_nearest(req["pickup"])
        if not nearest:
            print("Not Nearest driver Available")
            return
        requests["driver_id"]=nearest
        requests["status"]="Matched"
        drivers[nearest]["available"]=False


def start_ride(request_id):
    if request_id not in requests:
        print(f"Error:{request_id}not found!")
        return
    req=requests[request_id]
    req["status"]="STARTED"
    print(f"Ride '{request_id}'Started!")

def complete_ride(request_id):
    if request_id not in requests:
        print(f"Error:'{request_id}'not found!")
        return
    dist = calculate_distance(requests["pickup"],requests["drop"])
    requests["fare"]=round(dist*10,2)
    requests["status"]="COMPLETED"
    driver_id=requests["driver_id"]
    drivers[driver_id]["available"]=True
    drivers[driver_id]["rides_completed"]+=1
    print(f"Ride'{request_id}completed! Fare:{requests['fare']}coins")
def cancel_ride(request_id):
    if request_id not in requests:
        print(f"Error:'{request_id}'not found!")
        return
    if requests["driver_id"]:
        drivers[requests["driver_id"]["available"]]=True
        requests["status"]="CANCELED"
        print(f"Ride'{request_id}' got cancelled!")
def rate_driver(request_id,rating):
    if request_id not in requests:
        print(f"Error:Request'{request_id}'Not found!")
        return
    request=requests[request_id]
    if request["status"]!="COMPLETED":
        print("Error: can only rate complete rides!")
        return
    driver_id=request[driver_id]
    driver=drivers[driver_id]
    rides=driver["rides completed"]
    driver[rating]=round

add_driver("D1","Ali",(2,3))
add_driver("D2","Umair",(4,5))
add_rider("R1","Ahmed",(2,3))
add_rider("R2","Sara",(4,5))