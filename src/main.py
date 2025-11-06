def greet(name: str) -> str:
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    bye: str = "See you later!"
    return f"{bye}, {name}!"


if __name__ == "__main__":
    print(greet("Python"))
    print(farewell("Python"))
