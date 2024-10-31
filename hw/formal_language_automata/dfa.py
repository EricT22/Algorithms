def build_transitions():
    nstates = 6
    nsymbols = 3
    state_transitions = [[0 for x in range(nsymbols)] for i in range(nstates)]

    state_transitions[0][0] = 2
    state_transitions[1][0] = 3
    state_transitions[2][0] = 4
    state_transitions[3][0] = 3
    state_transitions[4][0] = 1
    state_transitions[5][0] = 1
    
    state_transitions[0][1] = 4
    state_transitions[1][1] = 4
    state_transitions[2][1] = 2
    state_transitions[3][1] = 1
    state_transitions[4][1] = 4
    state_transitions[5][1] = 5
    
    state_transitions[0][2] = 6
    state_transitions[1][2] = 2
    state_transitions[2][2] = 2
    state_transitions[3][2] = 5
    state_transitions[4][2] = 6
    state_transitions[5][2] = 4

    return state_transitions


def dfa(string, state_transitions:list[list[int]]):
    state = 1
    print(f'Initial State: {state}')
    
    for i in range(len(string)):
        input = ord(string[i]) - ord('a')

        try:
            state = state_transitions[state - 1][input]
        except IndexError:
            state = -1
        
        print(f'State {i + 1} (\'{string[i]}\'): {state}')

    return state == 3 or state == 5


if __name__ == "__main__":
    st = build_transitions()

    strings = ["", "abc", "acbcacb", "bacbcac", "cabcabbc", "bacbcaab", "cbcbbcab", "bccbacbc"]

    for i in range(len(strings)):
        print(f'{chr(ord('a') + i)}) Word \"{strings[i]}\" is {"accepted" if dfa(strings[i], st) else "rejected"}')
        print(f'{"-" * 20}')