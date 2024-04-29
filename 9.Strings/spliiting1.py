def rev(string):
    words= string.split()
    return " ".join(i[::-1] for i in words)