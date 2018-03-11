def f(x):
    """
    :param x:
    :return: 3x+1
    """
    return 3 * x + 1


print(f(2))

g = lambda x: 3*x + 1

print(g(2))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("abhisHek", "zambre"))

author = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke",
          "Frank Herbert", "Douglas Adams"]

author.sort(key=lambda name: name.split(" ")[-1].lower())

print(author)
