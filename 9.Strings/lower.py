# Convert to lower case

def lower1(string):
    result = ""
    for ch in string:
        ascii_code = ord(ch)
        if ascii_code >= 65 and ascii_code <= 90:
            ascii_code = ascii_code + 32 #65 +32==97 so 97 is ascii of small "a" 
            new_char = chr(ascii_code)#yaha pe nw char may asci code ko char may convo krkr store kr raha
            result += new_char#yaha wo convertd char store hoga
        else:
            result += ch #yaha jo alredy small h wo add hoga
    return result

a = "ANIruDh$#^*   !@@#@000ADWKAhhdkwa   ___++"
print(lower1(a))