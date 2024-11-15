import heapq
import time

# Define a graph of Tamil Nadu districts with distances in kilometers
graph = {
    'Chennai': [('Vellore', 140), ('Tiruvallur', 42), ('Kanchipuram', 72)],
    'Vellore': [('Chennai', 140), ('Krishnagiri', 120), ('Dharmapuri', 85)],
    'Tiruvallur': [('Chennai', 42), ('Kanchipuram', 66)],
    'Kanchipuram': [('Chennai', 72), ('Tiruvallur', 66), ('Vellore', 90)],
    'Krishnagiri': [('Vellore', 120), ('Dharmapuri', 55)],
    'Dharmapuri': [('Krishnagiri', 55), ('Salem', 65)],
    'Salem': [('Dharmapuri', 65), ('Erode', 100), ('Namakkal', 60)],
    'Erode': [('Salem', 100), ('Coimbatore', 100), ('Tiruppur', 56)],
    'Coimbatore': [('Erode', 100), ('Tiruppur', 55), ('Madurai', 210)],
    'Tiruppur': [('Coimbatore', 55), ('Erode', 56)],
    'Namakkal': [('Salem', 60), ('Karur', 35)],
    'Karur': [('Namakkal', 35), ('Tiruchirappalli', 60)],
    'Tiruchirappalli': [('Karur', 60), ('Madurai', 135)],
    'Madurai': [('Tiruchirappalli', 135), ('Dindigul', 65), ('Theni', 76)],
    'Dindigul': [('Madurai', 65), ('Theni', 75)],
    'Theni': [('Madurai', 76), ('Dindigul', 75), ('Virudhunagar', 88)],
    'Virudhunagar': [('Theni', 88), ('Ramanathapuram', 113)],
    'Ramanathapuram': [('Virudhunagar', 113), ('Sivaganga', 50)],
    'Sivaganga': [('Ramanathapuram', 50), ('Madurai', 40)],
    'Tirunelveli': [('Thoothukudi', 48), ('Madurai', 170)],
    'Thoothukudi': [('Tirunelveli', 48)],
}

def dijkstra(graph, start, end):
    # Initialize distances, queue, and path tracking
    distances = {district: float('inf') for district in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    came_from = {}
    
    # Start timer for performance tracking
    start_time = time.time()

    while priority_queue:
        current_distance, current_district = heapq.heappop(priority_queue)

        # Early exit if reached the destination
        if current_district == end:
            break

        # Check all neighbors of the current district
        for neighbor, distance in graph[current_district]:
            total_distance = current_distance + distance
            if total_distance < distances[neighbor]:  # Found a shorter path
                distances[neighbor] = total_distance
                came_from[neighbor] = current_district
                heapq.heappush(priority_queue, (total_distance, neighbor))

    # Reconstruct the path from end to start
    path = []
    current = end
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    # Calculate total time taken
    end_time = time.time()
    time_taken = end_time - start_time

    return {
        'distance': distances[end],
        'path': path,
        'path_length': len(path),
        'time_taken': time_taken
    }

# Input and Output
start_district = input("Enter the starting district: ")
end_district = input("Enter the ending district: ")

# Ensure the districts are in the graph
if start_district not in graph or end_district not in graph:
    print("One or both of the districts are not in the graph.")
elif start_district == end_district:
    print("Start and end districts are the same. Distance: 0 km.")
else:
    result = dijkstra(graph, start_district, end_district)
    if result['distance'] == float('inf'):
        print("No path exists between the selected districts.")
    else:
        print(f"Shortest distance from {start_district} to {end_district}: {result['distance']} km")
        print("Path:", " -> ".join(result['path']))
        print(f"Number of nodes in path: {result['path_length']}")
        print(f"Time taken: {result['time_taken']:.5f} seconds")
