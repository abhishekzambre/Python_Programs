def isOneBitCharacter(bits):
    i = 0
    last_one = False
    while i < len(bits)-1:
        if (bits[i] == '1') and (bits[i+1] == '0' or bits[i+1] == '1'):
            print(bits[i], bits[i+1])
            i += 2
            last_one = False
        else:
            print(bits[i])
            i += 1
            last_one = True

    print(last_one)


isOneBitCharacter("0")