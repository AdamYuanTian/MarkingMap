pip install folium

import folium

# Sample coordinates (latitude and longitude)
# Replace these with your own coordinates
coordinates_A = [
    (40.7128, -74.0060),  # New York City
    (34.0522, -118.2437),  # Los Angeles
]

coordinates_B = [
    (51.5074, -0.1278),  # London
    (48.8566, 2.3522),  # Paris
]

# Create a map centered around the mean of all coordinates
all_coordinates = coordinates_A + coordinates_B
m = folium.Map(location=[sum(x[0] for x in all_coordinates)/len(all_coordinates),
                          sum(x[1] for x in all_coordinates)/len(all_coordinates)],
               zoom_start=2)

# Plot red markers for coordinates in the 'red' group
for coord in coordinates_A:
    folium.Marker(location=coord, icon=folium.Icon(color='red')).add_to(m)

# Plot blue markers for coordinates in the 'blue' group
for coord in coordinates_B:
    folium.Marker(location=coord, icon=folium.Icon(color='blue')).add_to(m)

# Save the map as an HTML file
m.save("grouped_locations_map.html")

# Display the map
m
