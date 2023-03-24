def pythagorean_pants(triangle):
    sort_triangle = sorted(triangle)
    print(((sort_triangle[0] ** 2) + (sort_triangle[1] ** 2)) == (sort_triangle[2] ** 2))


pythagorean_pants([5, 3, 4])
pythagorean_pants([6, 8, 10])
pythagorean_pants([100, 3, 65])
