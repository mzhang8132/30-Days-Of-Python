# Day 12: 30 Days of python programming

from random import randint
import string


def random_user_id():
    chars = string.ascii_lowercase + string.digits
    id = ""
    for i in range(6):
        id.append(chars[randint(0, len(chars) - 1)])
    return id

def user_id_gen_by_user():
    length = input("Enter id length: ")
    num_id = input("Enter number of IDs: ")
    chars = string.ascii_lowercase + string.digits
    ids = []
    for i in range(num_id):
        id = ""
        for j in range(length):
            id.append(chars[randint(0, len(chars) - 1)])
        ids.append(id)
    return ids

def rgb_color_gen():
    return f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})"

def list_of_hexas_colors(num):
    chars = string.ascii_lowercase[:6] + string.digits
    hexs = []
    for i in range(num):
        hex = "#"
        for j in range(6):
            hex.append(chars[randint(0,15)])
        hexs.append(hex)
    return hexs

def list_of_rgb_colors(num):
    rgbs = []
    for i in range(num):
        rgb = "rgb({},{},{})".format(randint(0,255), randint(0,255), randint(0,255))
        rgbs.append(rgb)
    return rgbs

def generate_colors(option, num):
    if option == "hexa":
        return list_of_hexas_colors(num)
    else:
        return list_of_rgb_colors(num)
    
def shuffle_list(arr):
    shuffled = []
    for i in range(len(arr)):
        index = randint(0, len(arr) - 1)
        shuffled.append(arr[index])
        arr.remove(arr[index])
    return shuffled

def sev_random():
    values = []
    numbers = string.digits
    for i in range(7):
        index = randint(0, len(numbers) - 1)
        values.append(numbers[index])
        numbers.remove(numbers[index])
    return values