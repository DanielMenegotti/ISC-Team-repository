


def generate_floors(current_floor):
    roomNum = 0
    monster_rooms = 0
    utility_rooms = 0
    miniBoss_rooms = 0
    floor_layout = []
    while roomNum <= 5:
        if current_floor <= 2:
            monster_rooms = random.randint(0, 3)
            roomNum = roomNum + monster_rooms
            
            
        