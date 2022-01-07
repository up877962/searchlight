from collections import Counter

# This is a sample Python script.
'''
Please note most of this code was found openly on the internet at 
https://stackoverflow.com/questions/70276776/searchlight-inefficient-compression-scheme
not sure if you left it there but I fixed what was there to correctly output the compressed data from user input and I
traced through the code so that I understand the dataflow through it and refactored for PEP where appropriate.

Ive intentionally left print statements/stuff attempted so you can see the thought process involved.

'''

text = ""

key = []


# to run with harcoded data uncomment line below and comment line 115 /getinputs function call
# text = "Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail. Mind! I don’t mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country’s done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail."


def initcompute(data):  # here i am finding the unique chars and its occurrence to find the popular char
    uchar = list(set(data))
    xcount = dict(Counter(data))
    xcount = dict(sorted(xcount.items(), key=lambda item: item[1], reverse=True))

    # print("comptest", uchar, xcount)

    return len(uchar), xcount


def compute(data, keylist, datadict):  # assigning the hex value(key) to the each characters
    j = 0
    comdict = {}
    decdict = {}
    sol = ""

    for k in datadict:
        comdict[k] = [keylist[j], datadict[k]]
        decdict[keylist[j]] = k
        j += 1
    for c in data:
        sol += comdict[c][0]
    # print("sol", sol)
    return sol, decdict


def decompression(keydict,
                  cdata):  # this is to find the decompressed data by having the dict of
    # hex value assigned to char and compressed data as inputs
    sol = ""
    fnib = ""
    for s in cdata:
        if s == 'f':
            fnib += s
        else:
            fnib += s
            sol += keydict[fnib]
            fnib = ""

    return sol


def compression():  # find the key(hex value) and framing the compressed data
    i = 0
    fac = 16
    pwr = 1
    # text.strip('\n')
    keylen, ddict = initcompute(text)
    # print("dict", ddict)
    # for key, value in dict(dDict).items():
    #     if value == '\n':
    #         del dDict[key]
    while len(key) <= keylen:
        if i <= (fac - 2):
            key.append(str(hex(i))[2:])  # finding the hex value and storing in key
            i += 1
        else:
            pwr += 1
            fac = pow(16, pwr)
            i = fac - 16
    sol, newdict = compute(text, key, ddict)
    print("Assigned hex values for each character: ")
    print(newdict)
    return sol, newdict, keylen


# gets the multiline user input and removes characters appended in the process
def getinputs():
    print("Enter/Paste your content. Ctrl-D/Ctrl-Z to save it.")
    contents = []
    global text
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    x = '\n'.join(contents)
    x = x.replace('\n', '')
    x = x.replace('\t', '')
    # print("x", x)
    # x = str(contents)
    # text = map(lambda s: s.strip(), x)
    # text = text.strip('\n')
    text = x

    # print("x",contents)
    return text


if __name__ == '__main__':
    getinputs()
    # text = input("Input your Data here: ")  # input
    compressed_data, new_dict, key_len = compression()
    print("Compressed data: ", compressed_data)
    # print(compressed_data)
    print("Decompressed data:")
    print(decompression(new_dict, compressed_data))
