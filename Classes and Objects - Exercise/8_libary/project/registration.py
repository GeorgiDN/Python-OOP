from project import User
from project import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id and user.username != new_username:
                user.username = new_username
                if new_username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books.pop(user.username)
                user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user.user_id}"

            elif user.user_id == user_id and user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
      