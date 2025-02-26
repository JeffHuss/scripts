def main():
    spacecraft = {"name": "Voyager 1",
                  "distance": 163,
    }
    print(create_report(spacecraft))
    selection = input("Would you like to see the spacecraft's name or distance? ")
    print(f"{selection}: {spacecraft.get(selection, "Unknown")}")


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Description: {spacecraft.get("description", "Unknown")}

    ==========================
    """


main()