import tkinter as gui
from tkinter import *
import random

root = gui.Tk()
root.title('Nifty Key Generator')
root.geometry("800x600")
root.config(background="#4874AA")

# One day Key Verification
def verifyonedaykey(key):
    global score
    score =0

    # define the check digit
    check_special_digit = key[0]
    check_special_digit_count = 0

    # Separate key string into chunks or sections using the split method
    chunks = key.split('-')

    # loop through the chunks and count the special characters
    for chunk in chunks:
        if len(chunk) != 4:
            return False
        for char in chunk:
            # Increase the special_digit_count
            if char == check_special_digit:
                check_special_digit_count += 1
            # Get the score of the ANSCII characters
            score += ord(char)
    # Check for validation rule
    # One day license key have to have a score between 1600 and 1800
    if score > 1600 and score < 1800 and check_special_digit_count ==3:
        return True
    else:
        return False

# One week Key Verification
def verifyoneweekkey(key):
    global score
    score =0

    # define the check digit
    check_special_digit = key[1]
    check_special_digit_count = 0

    # Separate key string into chunks or sections using the split method
    chunks = key.split('-')

    # loop through the chunks and count the special characters
    for chunk in chunks:
        if len(chunk) != 4:
            return False
        for char in chunk:
            # Increase the special_digit_count
            if char == check_special_digit:
                check_special_digit_count += 1
            # Get the score of the ANSCII characters
            score += ord(char)
    # Check for validation rule
    # One day license key have to have a score between 1800 and 1900
    if score > 1800 and score < 1900 and check_special_digit_count ==3:
        return True
    else:
        return False

# Two weeks Key Verification
def verifytwoweekskey(key):
    global score
    score =0

    # define the check digit
    check_special_digit = key[2]
    check_special_digit_count = 0

    # Separate key string into chunks or sections using the split method
    chunks = key.split('-')

    # loop through the chunks and count the special characters
    for chunk in chunks:
        if len(chunk) != 4:
            return False
        for char in chunk:
            # Increase the special_digit_count
            if char == check_special_digit:
                check_special_digit_count += 1
            # Get the score of the ANSCII characters
            score += ord(char)
    # Check for validation rule
    # One day license key have to have a score between 1900 and 2000
    if score > 1900 and score < 2000 and check_special_digit_count ==3:
        return True
    else:
        return False

# One Month Key Verification
def verifyonemonthkey(key):
    global score
    score =0

    # define the check digit
    check_special_digit = key[3]
    check_special_digit_count = 0

    # Separate key string into chunks or sections using the split method
    chunks = key.split('-')

    # loop through the chunks and count the special characters
    for chunk in chunks:
        if len(chunk) != 4:
            return False
        for char in chunk:
            # Increase the special_digit_count
            if char == check_special_digit:
                check_special_digit_count += 1
            # Get the score of the ANSCII characters
            score += ord(char)
    # Check for validation rule
    # One day license key have to have a score between 1700 and 1800
    if score > 2000 and score < 2100 and check_special_digit_count ==3:
        return True
    else:
        return False



# One day key generator
def generateonedaykey():
    # Clear key Label
    key_label.delete(0, END)
    verify_label.config(text="")

    # Create key variables
    key = ''
    section = ''
    check_digit_count = 0
    alphabet ='abcdefghijklmnopqrstuvwxyz1234567890'

    # key = aaaa-bbb-ccc-dddd-1112 // 24 characters
    while len(key) < 25:
        # pick random characters from alphabet string
        char =random.choice(alphabet)
        # add random characters to key
        key +=char
        # Add the same randomly picked characters to section
        section += char

        # Add the "-" to key
        if len(section) == 4 :
            # append hyphen to key
            key += '-'
            # reset the section variable to empty
            section = ''
    # set key to 24 characters ( 25- 1)
    key = key[:-1]

    # output the key into the key label
    # key_label.insert(0, key)
    if verifyonedaykey(key):
        # key is verified
        key_label.insert(0, key.upper())
        verify_label.config(text ="Valid One day Key found")
        score_label.config(text=f'Score: {score}')
    else:
        # key is not verified
        # Run the generate function again till key meets validation rules.
        generateonedaykey()

# One week key generator
def generateoneweekkey():
    # Clear key Label
    key_label.delete(0, END)
    verify_label.config(text="")

    # Create key variables
    key = ''
    section = ''
    check_digit_count = 0
    alphabet ='abcdefghijklmnopqrstuvwxyz1234567890'

    # key = aaaa-bbb-ccc-dddd-1112 // 24 characters
    while len(key) < 25:
        # pick random characters from alphabet string
        char =random.choice(alphabet)
        # add random characters to key
        key +=char
        # Add the same randomly picked characters to section
        section += char

        # Add the "-" to key
        if len(section) == 4 :
            # append hyphen to key
            key += '-'
            # reset the section variable to empty
            section = ''
    # set key to 24 characters ( 25- 1)
    key = key[:-1]

    # output the key into the key label
    # key_label.insert(0, key)
    if verifyoneweekkey(key):
        # key is verified
        key_label.insert(0, key.upper())
        verify_label.config(text ="Valid one week Key found")
        score_label.config(text=f'Score: {score}')
    else:
        # key is not verified
        # Run the generate function again till key meets validation rules.
        generateoneweekkey()


# Two weeks key Generator
def generatetwoweekskey():
    # Clear key Label
    key_label.delete(0, END)
    verify_label.config(text="")

    # Create key variables
    key = ''
    section = ''
    check_digit_count = 0
    alphabet ='abcdefghijklmnopqrstuvwxyz1234567890'

    # key = aaaa-bbb-ccc-dddd-1112 // 24 characters
    while len(key) < 25:
        # pick random characters from alphabet string
        char =random.choice(alphabet)
        # add random characters to key
        key +=char
        # Add the same randomly picked characters to section
        section += char

        # Add the "-" to key
        if len(section) == 4 :
            # append hyphen to key
            key += '-'
            # reset the section variable to empty
            section = ''
    # set key to 24 characters ( 25- 1)
    key = key[:-1]

    # output the key into the key label
    # key_label.insert(0, key)
    if verifytwoweekskey(key):
        # key is verified
        key_label.insert(0, key.upper())
        verify_label.config(text ="Valid two weeks Key found")
        score_label.config(text=f'Score: {score}')
    else:
        # key is not verified
        # Run the generate function again till key meets validation rules.
        generatetwoweekskey()

# one month key Generator
def generateonemonthkey():
    # Clear key Label
    key_label.delete(0, END)
    verify_label.config(text="")

    # Create key variables
    key = ''
    section = ''
    check_digit_count = 0
    alphabet ='abcdefghijklmnopqrstuvwxyz1234567890'

    # key = aaaa-bbb-ccc-dddd-1112 // 24 characters
    while len(key) < 25:
        # pick random characters from alphabet string
        char =random.choice(alphabet)
        # add random characters to key
        key +=char
        # Add the same randomly picked characters to section
        section += char

        # Add the "-" to key
        if len(section) == 4 :
            # append hyphen to key
            key += '-'
            # reset the section variable to empty
            section = ''
    # set key to 24 characters ( 25- 1)
    key = key[:-1]

    # output the key into the key label
    # key_label.insert(0, key)
    if verifyonemonthkey(key):
        # key is verified
        key_label.insert(0, key.upper())
        verify_label.config(text ="Valid One month Key found")
        score_label.config(text=f'Score: {score}')
    else:
        # key is not verified
        # Run the generate function again till key meets validation rules.
        generateonemonthkey()


############################## Buildingint the layout ###################################################

# Create Buttons
onedaykey_button = Button(root, text="1 Day key", width=15, height=2, command=generateonedaykey)
onedaykey_button.grid(row=1, column=1, padx= 10, pady=30, columnspan=1)

oneweekkey_button = Button(root, text="1 Week key",  width=15, height=2, command=generateoneweekkey)
oneweekkey_button.grid(row=1, column=2, pady=30)

twoweekskey_button = Button(root, text="2 Weeks key",  width=15, height=2, command=generatetwoweekskey)
twoweekskey_button.grid(row=1, column=3, pady=30)

onemonthkey_button = Button(root, text="1 Month key",  width=15, height=2, command=generateonemonthkey)
onemonthkey_button.grid(row=1, column= 4, pady=30)

# Key Label
key_label = Entry(root, font=("Helvetica", 22), bd=1, bg="systembuttonface", width=28 )
key_label.grid(row=6, column=2, columnspan=4, pady= 50)

# Verify Label
verify_label = Label(root, text="Waiting...", bg="#4874AA")
verify_label.grid(row=8, column=3 )

# Score_label
score_label = Label(root, text="Score: ", font=("Helvetica", 32))
score_label.grid(row=10, column=3)


root.mainloop()

