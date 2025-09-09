def main():
    shows = [
        " Avatar: the last airbender",
        "Ben 10",
        "Arthur",
        " Spongebob Squarepants",
        "Phineas and ferb",
        "Kim possible",
        "Jimmy Neutron ",
        "the Proud family"
    ]
    shows_fixed = fix_shows(shows)
    print(", ".join(shows_fixed))
    # for i in range(len(shows)):
    #     print(shows[i])


def fix_shows(shows):
    for i in range(len(shows)):
        shows[i] = shows[i].strip().title()
    return shows

main()