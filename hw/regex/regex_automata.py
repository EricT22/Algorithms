def build_transitions():
    nstates = 4
    nsymbols = 5
    state_transitions = [[0 for x in range(nsymbols)] for i in range(nstates)]

    state_transitions[0][0] = 1
    state_transitions[1][0] = 2
    state_transitions[2][0] = 2
    state_transitions[3][0] = 3
    
    state_transitions[0][1] = 1
    state_transitions[1][1] = 2
    state_transitions[2][1] = 2
    state_transitions[3][1] = 3
    
    state_transitions[0][2] = 1
    state_transitions[1][2] = 2
    state_transitions[2][2] = 2
    state_transitions[3][2] = 3

    state_transitions[0][3] = 3
    state_transitions[1][3] = 2
    state_transitions[2][3] = 2
    state_transitions[3][3] = 3
    
    state_transitions[0][4] = 3
    state_transitions[1][4] = 3
    state_transitions[2][4] = 3
    state_transitions[3][4] = 3
    
    return state_transitions


def jregex_table_driven(string, state_transitions:list[list[int]]):
    state = 0
    print(f'Initial State: {state}')
    
    for i in range(len(string)):
        chr_code = ord(string[i])

        if (chr_code >= ord('a') and chr_code <= ord('z')):
            input = 0
        elif (chr_code >= ord('A') and chr_code <= ord('Z')):
            input = 1
        elif (chr_code == ord('$') or chr_code == ord('_')):
            input = 2
        elif (chr_code >= ord('0') and chr_code <= ord('9')):
            input = 3
        else:
            input = 4

        state = state_transitions[state][input]

        print(f'State {i + 1} (\'{string[i]}\'): {state}')

    return state == 1 or state == 2


def jregex_switch_driven(string):
    state = 0

    for i in range(len(string)):
        chr_code = ord(string[i])

        match state:
            case 0:
                if (chr_code >= ord('a') and chr_code <= ord('z')) or \
                    (chr_code >= ord('A') and chr_code <= ord('Z')) or \
                    (chr_code == ord('$') or chr_code == ord('_')):
                    state = 1
                else:
                    state = 3
            case 1:
                if (chr_code >= ord('a') and chr_code <= ord('z')) or \
                    (chr_code >= ord('A') and chr_code <= ord('Z')) or \
                    (chr_code == ord('$') or chr_code == ord('_')) or \
                    (chr_code >= ord('0') and chr_code <= ord('9')):
                    state = 2
                else:
                    state = 3
            case 2:
                if (chr_code >= ord('a') and chr_code <= ord('z')) or \
                    (chr_code >= ord('A') and chr_code <= ord('Z')) or \
                    (chr_code == ord('$') or chr_code == ord('_')) or \
                    (chr_code >= ord('0') and chr_code <= ord('9')):
                    state = 2
                else:
                    state = 3
            case 3:
                state = 3

    return state == 1 or state == 2


if __name__ == "__main__":
    st = build_transitions()

    var_names = ["Temp123", "temp123", "$temp_variable", "9temp_variable$"]

    for i in range(len(var_names)):
        # print(f'{chr(ord('a') + i)}) Variable name \"{var_names[i]}\" is {"accepted" if jregex_table_driven(var_names[i], st) else "rejected"}')
        print(f'{chr(ord('a') + i)}) Variable name \"{var_names[i]}\" is {"accepted" if jregex_switch_driven(var_names[i]) else "rejected"}')
        print(f'{"-" * 20}')