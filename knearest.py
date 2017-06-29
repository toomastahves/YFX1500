# -*- coding: utf-8 -*-
from collections import Counter
from Vectors import distance
import matplotlib.pyplot as plt

# Plotting
points = [([-122, 47], "Red"),
        ([-96, 32], "Blue"),
        ([-89, 43], "Green")]

plots = { "Red": ([], []), "Blue": ([],[]), "Green": ([], [])}
markers = {"Red": "o", "Blue": "s", "Green": "^"}
colors = {"Red": "r", "Blue": "b", "Green": "g"}

def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values() if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])

def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(labeled_points, key=lambda point_label: distance(point_label[0], new_point))
    k_nearest_labels = [label for _, label in by_distance[:k]]
    return majority_vote(k_nearest_labels)

k = 1
        
for longitude in range(-130, -60):
    for latitude in range(20, 55):
        predicted_point = knn_classify(k, points, [longitude, latitude])
        plots[predicted_point][0].append(longitude)
        plots[predicted_point][1].append(latitude)
        
for (longitude, latitude), color in points:
    plots[color][0].append(longitude)
    plots[color][1].append(latitude)
    
for points, (x, y) in plots.items():
    plt.scatter(x, y, color=colors[points], marker=markers[points], label=points, zorder=10)
    
plt.axis([-130,-60,20,55])
plt.show()