print('importing urlify')


def urlify(s):
    return "%20".join(s.split())


if __name__ == "__main__":
    s = "Hello Dear  World    "
    print("{} {}".format(s, urlify(s)))
