# Advent of Code, Day 5, Part a
# Lee Cattarin

maze = []

# Create the maze
for line in open("input.txt", "r"):
    maze.append(int(line.strip()))

now = 0
prev = None
steps = 0

while not now < 0 and not now >= len(maze):
    step = maze[now]

    if step > 2:
        maze[now] -= 1
    else:
        maze[now] += 1
        
    now += step
    steps += 1

print(steps)
