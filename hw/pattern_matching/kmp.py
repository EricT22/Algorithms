def kmpmatch(text, sub):
    one_based_text = "-" + text
    one_based_sub = "-" + sub

    sub_loc = 1
    text_loc = 1
    fail = fail_links_zbased(sub)

    while text_loc <= len(text) and sub_loc <= len(sub):
        if sub_loc == 0 or ord(one_based_text[text_loc]) == ord(one_based_sub[sub_loc]):
            text_loc += 1
            sub_loc += 1
        else:
            sub_loc = fail[sub_loc - 1] # adjusts since fail is zero based

    if sub_loc > len(sub):
        # answer is adjusted to fit zero-based arrays
        return text_loc - len(one_based_sub)
    else:
        return -1


# works right
def build_fail_links(sub):
    fail = [0 for x in range(len(sub) + 1)]

    fail[1] = 0

    for i in range(2, len(sub) + 1):
        temp = fail[i - 1]

        while temp > 0 and ord(sub[temp - 1]) != ord(sub[i - 2]):
            temp = fail[temp]

        fail[i] = temp + 1

    return fail[1:]


# also works right
def fail_links_zbased(sub):
    fail = [0 for x in range(len(sub))]
    
    fail[0] = 0

    for i in range(1, len(sub)):
        temp = fail[i - 1]

        while temp > 0 and ord(sub[temp - 1]) != ord(sub[i - 1]):
            temp = fail[temp - 1]
        
        fail[i] = temp + 1

    return fail


if __name__ == "__main__":
    text = "hi a ababcb oijio"
    sub = "ababcb"

    print(build_fail_links(sub))
    print(fail_links_zbased(sub))
    print(f'{"-" * 20}')
    print(kmpmatch(text, sub))