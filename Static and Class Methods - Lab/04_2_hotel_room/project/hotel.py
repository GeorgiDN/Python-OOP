from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self._find_room_by_number(room_number)
        if room:
            if room.take_room(people) is None:
                self.guests += people

    def free_room(self, room_number):
        room = self._find_room_by_number(room_number)
        if room:
            self.guests -= room.guests
            room.free_room()

    def status(self):
        result = [f"Hotel {self.name} has {self.guests} total guests"]
        result.append(f"Free rooms: {', '.join(map(str, [r.number for r in self.rooms if not r.is_taken]))}")
        result.append(f"Taken rooms: {', '.join(map(str, [r.number for r in self.rooms if r.is_taken]))}")
        return "\n".join(result)

    def _find_room_by_number(self, room_number):
        found_room = next((r for r in self.rooms if r.number == room_number), None)
        return found_room
