image_dimensions = (10,12)
corner_points = [
    (1.5, 1.5),  # (x, y)
    (4.0, 1.5),  # (x, y)
    (1.5, 8.0),  # (x, y)
    (4.0, 8.0)]  # (x, y)

import numpy as np

def calculatePixels(image_dimensions, corner_points):
    max_xy = max(corner_points, key=lambda x: (x[0], x[1]))
    min_xy = min(corner_points, key=lambda x: (x[0], x[1]))
    max_xy
    min_xy
    
    top_left = [min_xy[0], max_xy[1]]
    bottom_left = [min_xy[0], min_xy[1]]
    top_right = [max_xy[0], max_xy[1]]
    bottom_right = [max_xy[0], min_xy[1]]
    
#finding the minimum and maximum x and y points to find the 4 corner points of the rectangle
    min_x = min_xy[0]
    max_x = max_xy[0]
    min_y = min_xy[1]
    max_y = max_xy[1]

#based on our x dimensions, find the x-value points
    x_dim = image_dimensions[0]
    x_dist = max_x - min_x
    x_space = (x_dist) / (x_dim-1)
    x_pts = [float(min_x)]
    for i in range(1, image_dimensions[0]):
        x_pts.append(float(x_pts[i-1]+x_space))

#based on our y dimensions, find the y-value points
    y_dim = image_dimensions[1]
    y_dist = max_y - min_y
    y_space = (y_dist) / (y_dim-1)
    y_pts = [float(min_y)]
    for i in range(1, image_dimensions[1]):
        y_pts.append(float(y_pts[i-1]+y_space))

#merging the x pts and y pts based on our dimensions.
    solution = np.zeros((image_dimensions[1], image_dimensions[0], 2))
    for i in range(0, image_dimensions[1]):
        for j in range(0, image_dimensions[0]):
            solution[i][j] += [x_pts[j], y_pts[image_dimensions[1]-i-1]]
    return solution


solution = calculatePixels(image_dimensions, corner_points)
np.set_printoptions(precision=4)
print(solution)

image_dimensions = (3,3)
corner_points = [
    (1, 1), 
    (3, 1), 
    (1, 3), 
    (3, 3)] 
solution = calculatePixels(image_dimensions, corner_points)
np.set_printoptions(precision=4)
print(solution)