# pylint: disable=missing-module-docstring
# I am creating a short example of "Subscribe to ____" project by Kylie 
# To express String concatenation

# YOUTUBER = "Bruno"
# print("Subscribe to " + YOUTUBER)
# print("Subscribe to {}".format(YOUTUBER))
# print(f"Subscribe to {YOUTUBER}")

name = input("name: ")
job = input("job: ")
hobby = input("hobby: ")

description = f"Hi, I am {name}. I am a {job}. \
My favorite activity is {hobby}."

print(description)
