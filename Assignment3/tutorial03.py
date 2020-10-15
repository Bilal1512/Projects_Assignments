import csv
import os
import shutil

def valid_roll(roll_number):
    for i in range(0,4):
        if not 48<=ord(roll_number[i])<=57:
            return False
    for i in range(4,6):
        if not 97<=ord(roll_number[i])<=122:
            return False
    for i in range(6,8):
        if not 48<=ord(roll_number[i])<=57:
            return False
    return True