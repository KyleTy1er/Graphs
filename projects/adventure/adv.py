from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
player = Player(world.starting_room)

# Print an ASCII map
# world.print_rooms()

# list to hold the best path
path_list = []
# list to hold room traversals
room_stack = []
# add starting room to the list
room_stack.append(player.current_room.id)
# instantiate a set to keep track of visited rooms
visited = set()
'''

print(player.current_room.id)
print(room_list)
print(len(world.rooms))
current_room = room_list[-1]

neighbors = room_graph[current_room][1]
current_room = room_list[-1]
print(current_room)
visited.add(current_room)
print(visited)
neighbors = room_graph[current_room][1]
print(neighbors)
print(room_graph[current_room][1])
print(room_graph[current_room])
for direction, room in neighbors.items():
    print(f" {direction}, {room}")
for _, room in neighbors.items():
    print(_, room)
queue = []
for direction, room in neighbors.items():
    if room not in visited:
        queue.append(room)
'''

# so long as the length of our visited rooms does not surpass
# the length of our world the while loop continues:
while len(visited) != len(world.rooms):
    current_room = room_stack[-1]
    # current room is the value at the end of the list
    # add it to the visited list:
    visited.add(current_room)
    # neighbors of the current room,
    # returns a dict with directions and adjacent room #s:
    neighbors = room_graph[current_room][1]
    # list to hold the room #'s
    neighbor_queue = []
    # if the room has not been visited,
    # add it to the neighbor queue:
    for _, room in neighbors.items():
        if room not in visited:
            neighbor_queue.append(room)
    # append (queue) the next room to the queue
    if len(neighbor_queue) > 0:
        # dequeue and add to stack
        # this variable used to traverse to next room
        next_room = neighbor_queue[0]
        room_stack.append(next_room)
    else:
        # start dqing to eventually exit the while loop
        room_stack.pop()
        next_room = room_stack[-1]
    # for building path list as we traverse
    for direction, room in neighbors.items():
        # next_room is the zeroth item from neighbor_queue
        # neighbor_queue is built on a condition of being unvisited
        # if the room is the unvisited zeroth item from neighbor queue
        # then append that direction to the path list
        if room == next_room:
            path_list.append(direction)

traversal_path = path_list


# #
# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)
#
# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)
#
# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
