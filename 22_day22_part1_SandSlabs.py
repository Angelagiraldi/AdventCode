from collections import namedtuple
from dataclasses import dataclass

Cube = namedtuple('Cube', ['x', 'y', 'z'])

@dataclass
class Brick:
    start: Cube
    end: Cube
    brick_id: int

# Initialize the world as an empty dictionary
world = {}

def add_brick_to_world(brick_id, brick):
    for x, y, z in cubes(brick_id):
        world[(x, y, z)] = brick_id

def is_occupied(x, y, z):
    return (x, y, z) in world
       

def cubes(brick_id: int) -> list[Cube]:
    brick = bricks[brick_id]
    if brick.start.x != brick.end.x:
        for x in range(min(brick.start.x, brick.end.x), max(brick.start.x, brick.end.x)+1):
            yield (x, brick.start.y, brick.start.z)
    elif brick.start.y != brick.end.y:
        for y in range(min(brick.start.y, brick.end.y), max(brick.start.y, brick.end.y)+1):
            yield (brick.start.x, y, brick.start.z)
    else:
        for z in range(min(brick.start.z, brick.end.z), max(brick.start.z, brick.end.z)+1):
            yield (brick.start.x, brick.start.y, z)

# Function to check if there's a supporting brick below a given position
def has_support_below(x, y, z):
    brick_id_below = world.get((x, y, z-1))
    return brick_id_below not in [None, -1]
    
def is_falling(brick: Brick, invisible_brick_id: int = -1) -> bool:
    # Immediate return for an invisible brick
    if brick.brick_id == invisible_brick_id:
        return False

    # # Check for support for each cube in the brick
    # for cube in cubes(brick.brick_id):
    #     x, y, z = cube
    #     # If the brick or any part of it is at the ground level, it's not falling
    #     if z == 1 or has_support_below(x, y, z):
    #         return False
    
    # # If no part of the brick is supported, it is considered to be falling
    # return True


    if brick.brick_id == invisible_brick_id:
        return False
    is_vertical_brick = brick.start.z != brick.end.z
    if is_vertical_brick:
        z = min(brick.start.z, brick.end.z)
        if z == 1:
            return False
        brick_id_below = world.get((brick.start.x, brick.start.y, z-1))
        return brick_id_below in [None, invisible_brick_id]
    else:
        if brick.start.z == 1:
            return False
        for x, y, z in cubes(brick.brick_id):
            brick_id_below = world.get((x, y, z-1))
            if brick_id_below not in [None, invisible_brick_id]:
                return False
        return True

def drop_tick(invisible_brick_id: int = -1) -> set[int]:
    falling_brick_ids = set()  # return value
    max_z = max(z for _, _, z in world.keys())
    min_z = 1 if invisible_brick_id == - 1 \
        else max(bricks[invisible_brick_id].start.z, bricks[invisible_brick_id].end.z) + 1

    for z in range(min_z, max_z+1):
        current_bricks = (brick for brick in bricks
                          if brick.start.z == z or brick.end.z == z)
        for brick in current_bricks:
            if not is_falling(brick, invisible_brick_id=invisible_brick_id):
                continue
            falling_brick_ids.add(brick.brick_id)
            for x, y, z in cubes(brick.brick_id):
                del world[(x, y, z)]
                world[(x, y, z-1)] = brick.brick_id
            if invisible_brick_id != -1:
                continue
            brick.start = Cube(brick.start.x, brick.start.y, brick.start.z-1)
            brick.end = Cube(brick.end.x, brick.end.y, brick.end.z-1)

    return falling_brick_ids


def drop_until_done():
    while len(drop_tick()) > 0:
        pass


if __name__ == "__main__":
    input_file = "22_day22_input.txt"  # Specify the input file name.

    try:
        # Attempt to open and read the input file.
        with open(input_file, 'r') as file:
            grid = file.read().splitlines()
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print("File not found. Please enter a valid file name.")

    bricks = []

    for line in grid:
        start, end = line.split('~')
        start = Cube(*[int(coords) for coords in start.split(',')])
        end = Cube(*[int(coords) for coords in end.split(',')])
        brick = Brick(start, end, brick_id=len(bricks))
        bricks.append(brick)
        add_brick_to_world(brick.brick_id, brick)
        for x, y, z in cubes(brick.brick_id):
            world[(x, y, z)] = brick.brick_id

    drop_until_done()

    num_disintegratable_bricks = 0
    for brick in bricks:
        world_copy = world.copy()
        falling_brick_ids = drop_tick(invisible_brick_id=brick.brick_id)
        if len(falling_brick_ids) == 0:
            num_disintegratable_bricks += 1
        world = world_copy
    print(num_disintegratable_bricks)