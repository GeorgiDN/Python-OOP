from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician = self._get_object_by_name(self.musicians, name)
        if musician in self.musicians:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self._get_object_by_name(self.bands, name)

        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_concert_by_place(self.concerts, place)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_object_by_name(self.musicians, musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self._get_object_by_name(self.bands, band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_object_by_name(self.bands, band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self._get_object_by_name(band.members, musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = self._get_concert_by_place(self.concerts, concert_place)
        band = self._get_object_by_name(self.bands, band_name)

        required_members_types = ["Singer", "Guitarist", "Drummer"]
        found_members = [member for member in band.members]

        if not found_members:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        found_members_types = [member.TYPE for member in band.members]

        for curr_member in required_members_types:
            if curr_member not in found_members_types:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            needed_concert_skills = {
                "Drummer": "play the drums with drumsticks",
                "Singer": "sing high pitch notes",
                "Guitarist": "play rock"
            }

        elif concert.genre == "Metal":
            needed_concert_skills = {
                "Drummer": "play the drums with drumsticks",
                "Singer": "sing low pitch notes",
                "Guitarist": "play metal"
            }

        elif concert.genre == "Jazz":
            needed_concert_skills = {
                "Drummer": "play the drums with drum brushes",
                "Singer": ["sing high pitch notes", "sing low pitch notes"],
                "Guitarist": "play jazz"
            }

        message_exception = f"The {band_name} band is not ready to play at the concert!"
        for member in found_members:
            required_skill = needed_concert_skills.get(member.TYPE)
            if required_skill:
                if isinstance(required_skill, list):
                    if not all(skill in member.skills for skill in required_skill):
                        raise Exception(message_exception)
                else:
                    if required_skill not in member.skills:
                        raise Exception(message_exception)

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        result = f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
        return result

    @staticmethod
    def _get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object

    @staticmethod
    def _get_concert_by_place(concerts_list, place):
        found_concert = next((c for c in concerts_list if c.place == place), None)
        return found_concert
