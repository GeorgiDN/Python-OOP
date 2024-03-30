from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        found_room = self._find_room_by_number(room_number)
        if found_room is not None:
            if found_room.take_room(people) is None:
                self.guests += people

    def free_room(self, room_number):
        found_room = self._find_room_by_number(room_number)
        if found_room is not None:
            self.guests -= self.guests
            return found_room.free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(map(str, free_rooms))}\n"
                f"Taken rooms: {', '.join(map(str, taken_rooms))}")

    # Helper method
    def _find_room_by_number(self, room_num):
        searched_room = next((r for r in self.rooms if r.number == room_num), None)
        return searched_room
