test = ["(){}[]",
"{[()]}",
"([)]",#F
"[{]()",
""]
def valid_parenthesis2(string):
    dic_p = {")":"(",
    "]":"[",
    "}":"{"}
    parenthesis_list = []
    for ch in string:
        if ch in "([{":
            parenthesis_list.append(ch)
        if ch in ")]}":
            if len(parenthesis_list) > 0:
                ch2 = parenthesis_list.pop()
                ch1 = dic_p[ch]
                if ch1 != ch2:
                    return False

    if len(parenthesis_list) > 0:
        return False
    else:
        return True

for t in test:
    print(valid_parenthesis2(t))
