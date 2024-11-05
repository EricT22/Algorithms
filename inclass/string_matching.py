def strmatch(text, sub):
    sub_loc = 0
    text_loc = 0
    text_start = 0

    while text_loc < len(text) and sub_loc < len(sub):
        if ord(text[text_loc]) == ord(sub[sub_loc]):
            text_loc += 1
            sub_loc += 1
        else:
            text_start += 1
            text_loc = text_start
            sub_loc = 0

    if sub_loc == len(sub):
        return text_start
    else:
        return -1
    

if __name__ == "__main__":
    text = "woeifjweo they kwaofmaewofnowe iowfe"
    sub = "they"

    print(strmatch(text, sub))