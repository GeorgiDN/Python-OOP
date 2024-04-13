def vowel_filter(function):
    def wrapper():
        result = function()
        filtered_vowels = [char for char in result if char.lower() in "aeiou"]
        return filtered_vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


# No decorator
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# result = get_letters()
# filtered = [x for x in result if x.lower() in "aeiou"]
# print(filtered)
