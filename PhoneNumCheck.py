def isPhoneNumber(text): # Input: 415-555-1234
    if len(text) != 12:
        return False # Check if text is the correct phone# size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # Missing dash
        if text[3] != '-':
            return False # Checks if phone# has dash
        for i in range (4, 7):
            if not text[i].isdecimal():
                return False # Checks 2nd part of phone# is dec.
        if text[7] != '-':
            return False # Missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # Checks if last 4 digits are dec.
    return True # True if we have our correct phone number)

print(isPhoneNumber('415-555-1234')) 
