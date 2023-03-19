def greet(names):
    """Tailor greeting to the greetees."""
    match names:
        case [name]:
            return f"Hello, {name.title()}"
        case [name, name2]:
            return f"Hello, {name.title()} and {name2.title()}"
        case [name, name2, name3]:
            names = [name.title() for name in names]
            names[-1] = "and " + names[-1]
            return f"Hello, {', '.join(names)}"
        case _:
            return f"I don't know how to greet {names}!"
