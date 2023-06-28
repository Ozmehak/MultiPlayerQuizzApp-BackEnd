import random
import string

'''This is the utils file for the app. It contains functions that are used in the api'''

def generate_room_code():
    '''Generate a random 6-digit room code'''
    characters = string.digits
    room_code = ''.join(random.choice(characters) for _ in range(6))
    return room_code
