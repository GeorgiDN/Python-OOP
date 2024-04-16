class store_results:
    _file_store = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        result = f"Function '{self.function.__name__}' was called. Result: {self.function(*args)}"

        with open(self._file_store, "a") as file:
            file.write(result + "\n")

        return self.function(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
