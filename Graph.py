import matplotlib.pyplot as plt

x_values = []
y_values = []

n = int(input("How many points do you want to plot? "))

for i in range(n):
    x, y = map(float, input(f"Enter point {i+1} (x y): ").split())
    x_values.append(x)
    y_values.append(y)

plt.scatter(x_values, y_values, color="red")

used_connections = set()

for i in range(n):
    min_distance = float("inf")
    nearest = -1
    
    for j in range(n):
        if i != j and (i, j) not in used_connections and (j, i) not in used_connections:
            distance = ((x_values[i] - x_values[j]) ** 2 + (y_values[i] - y_values[j]) ** 2) ** 0.5
            
            if distance < min_distance:
                min_distance = distance
                nearest = j

    if nearest != -1:
        plt.plot([x_values[i], x_values[nearest]], [y_values[i], y_values[nearest]], "b-")
        used_connections.add((i, nearest))

plt.title("Nearest Neighbor Connections")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
