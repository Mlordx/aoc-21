#!/usr/bin/python3
from queue import PriorityQueue
from copy import deepcopy
from collections import defaultdict

starting_corridor = [None] * 11
starting_rooms_1 = {
    'A': ['C', 'D'],
    'B': ['A', 'B'],
    'C': ['D', 'C'],
    'D': ['B', 'A']
}
starting_rooms_2 = {
    'A': ['C', 'D', 'D', 'D'],
    'B': ['A', 'B', 'C', 'B'],
    'C': ['D', 'A', 'B', 'C'],
    'D': ['B', 'C', 'A', 'A']
}
room_position = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}
value = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}
ROOM_SIZE = 2
ENTRY_COUNT = 1


def state_hash(corridor, rooms):
    hash = ''

    for c in corridor:
        if c:
            hash += c
        else:
            hash += '.'

    for key in rooms:
        for _ in range(ROOM_SIZE - len(rooms[key])):
            hash += '_'

        for i in range(len(rooms[key])-1, -1, -1):
            hash += rooms[key][i]

    return hash


def is_room_available(amphipod, room):
    if len(room) < ROOM_SIZE:
        for a in room:
            if a != amphipod:
                return False
        return True

    return False


def can_amphipod_move(i, j, corridor):
    if i < j:
        for k in range(i+1, j+1):
            if corridor[k] is not None:
                return False
    else:
        for k in range(j, i):
            if corridor[k] is not None:
                return False

    return True


def is_solution(rooms):
    for key in rooms:
        if len(rooms[key]) != ROOM_SIZE:
            return False

        for a in rooms[key]:
            if a != key:
                return False

    return True


def how_far_away(rooms):
    target = 'A' * ROOM_SIZE + 'B' * ROOM_SIZE + 'C' * ROOM_SIZE + 'D' * ROOM_SIZE
    current = ''
    diff = 0
    for key in rooms:
        for _ in range(ROOM_SIZE - len(rooms[key])):
            current += '_'

        for i in range(len(rooms[key])-1, -1, -1):
            current += rooms[key][i]

    for i, c in enumerate(current):
        if c != target[i]:
            diff += 1

    return diff


def is_room_solved(rooms, key):
    for a in rooms[key]:
        if a != key:
            return False

    return True


def get_valid_moves(corridor, rooms):
    valid_moves = []
    for i in [0, 1, 3, 5, 7, 9, 10]:  # corridor -> room
        if corridor[i] is not None:
            amphipod = corridor[i]
            room_available = is_room_available(amphipod, rooms[amphipod])
            can_move = can_amphipod_move(i, room_position[amphipod], corridor)

            if room_available and can_move:
                new_corridor = deepcopy(corridor)
                new_rooms = deepcopy(rooms)

                new_corridor[i] = None
                new_rooms[amphipod].append(amphipod)

                cost = (abs(i - room_position[amphipod]) + ROOM_SIZE - len(rooms[amphipod])) \
                    * value[amphipod]

                valid_moves.append((cost, how_far_away(new_rooms), new_corridor, new_rooms))

    for key in rooms:  # room -> corridor
        if not is_room_solved(rooms, key):
            amphipod = rooms[key][-1]
            if amphipod == key:
                if len(rooms[key]) == 1:
                    continue
                solved_below = True
                for k in range(len(rooms[key])-1, -1, -1):
                    if rooms[key][k] != key:
                        solved_below = False

                if solved_below:
                    continue

            for j in [0, 1, 3, 5, 7, 9, 10]:
                if can_amphipod_move(room_position[key], j, corridor):
                    new_corridor = deepcopy(corridor)
                    new_rooms = deepcopy(rooms)
                    new_corridor[j] = amphipod
                    new_rooms[key].pop()
                    cost = (abs(j - room_position[key]) + ROOM_SIZE - len(rooms[key]) + 1) \
                        * value[amphipod]

                    valid_moves.append((cost, how_far_away(new_rooms), new_corridor, new_rooms))

    return valid_moves


def get_default_value():
    return float('inf')


def dijkstra(starting_corridor, starting_rooms):
    global ENTRY_COUNT
    pq = PriorityQueue()
    pq.put((0, how_far_away(starting_rooms),  0, (starting_corridor, starting_rooms)))
    lowest_cost = defaultdict(get_default_value)

    while not pq.empty():
        cost, _, _, (corridor, rooms) = pq.get()

        if is_solution(rooms):
            return cost

        valid_moves = get_valid_moves(corridor, rooms)

        for cost_and_move in valid_moves:
            move_cost, new_how_far,  new_corridor, new_rooms = cost_and_move

            if cost + move_cost < lowest_cost[state_hash(new_corridor, new_rooms)]:
                lowest_cost[state_hash(new_corridor, new_rooms)] = cost + move_cost
                pq.put((cost + move_cost, new_how_far,  ENTRY_COUNT, (new_corridor, new_rooms)))
                ENTRY_COUNT += 1


def answer1():
    global ROOM_SIZE, ENTRY_COUNT
    ROOM_SIZE = 2
    ENTRY_COUNT = 1
    return dijkstra(starting_corridor, starting_rooms_1)


def answer2():
    global ROOM_SIZE
    ROOM_SIZE = 4
    return dijkstra(starting_corridor, starting_rooms_2)


print(answer1())
print(answer2())
