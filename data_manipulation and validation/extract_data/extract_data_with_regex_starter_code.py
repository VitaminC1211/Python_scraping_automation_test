import re

phoneNumRex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "The phone number is 123-456-7890"

result = phoneNumRex.search(example)

if result:
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])