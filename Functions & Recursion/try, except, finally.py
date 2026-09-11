# ---try/except/finally---
try:
    number = int(3)
    print("That's an integer!")
except ValueError:
    print("Oops! That wasn't a valid number. ")
finally:
    print("Execution Finished! ")
