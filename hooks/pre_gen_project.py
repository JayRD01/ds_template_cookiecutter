import datetime
import os
import json

def inject_current_year():
    """
    Injects the current year into the cookiecutter context by writing a .year file.
    This file will be read during templating (in any template file).
    """
    year = str(datetime.datetime.now().year)
    with open("year.txt", "w") as f:
        f.write(year)

if __name__ == "__main__":
    inject_current_year()
