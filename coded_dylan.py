def uncode(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    punctuation = [" ","!",",","'","?","."]
    uncodedString = []
    for i in string:
        if i in punctuation:
            uncodedString.append(i)
        else:
            x = alphabet.find(i)
            y = alphabet[x+offset]
            uncodedString.append(y)
    refined = "".join(uncodedString)


    return refined

def codeAString(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz !.?,"
    punctuation = [" ","!",",","'","?","."]
    codedString = []
    for i in string:
        if i in punctuation:
            codedString.append(i)
        else:
            x = alphabet.find(i,26)
            y = alphabet[(x-offset)]
            codedString.append(y)
    refined = "".join(codedString)
    return refined



def uncodev(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    punctuation = [" ","!",",","'","?","."]
    uncodedString = []
    baseOffsetList = [offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset]
    baseOffsetList1 = "".join(baseOffsetList)
    offsetList = []
    offsetAmount = (len(string))
    for i in range(len(string)):
        offsetList.append(baseOffsetList1[i])

    for i in range(len(string)):
        if string[i] in punctuation:
            uncodedString.append(string[i])
        else:
            x = string[i]
            y = offsetList[i]
            z = alphabet.find(y)
            a = alphabet.find(x)
            final = alphabet[a-z]
            uncodedString.append(final)
    refined = "".join(uncodedString)


    return refined

def makeCodev(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    punctuation = [" ","!",",","'","?","."]
    codedString = []
    baseOffsetList = [offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,offset,]
    baseOffsetList1 = "".join(baseOffsetList)
    offsetList = []
    offsetAmount = (len(string))
    for i in range(len(string)):
        offsetList.append(baseOffsetList1[i])

    for i in range(len(string)):
        if string[i] in punctuation:
            codedString.append(string[i])
        else:
            x = string[i]
            y = offsetList[i]
            z = alphabet.find(y)
            a = alphabet.find(x)
            final = alphabet[a+z]
            codedString.append(final)
    refined = "".join(codedString)


    return refined




print(uncodev("oegv fhe lf whvv jrrxgs", "dan"))









for i in range(25):
    print(uncode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", i))
