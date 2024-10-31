def machine(string):
    state = 1

    for i in range(len(string)):
        c = string[i]

        match state:
            case 1:
                match c:
                    case 'a': 
                        state = 2
                    case 'b':
                        state = 3
                    case _:
                        state = 5
            case 2:
                match c:
                    case 'a': 
                        state = 1
                    case 'b':
                        state = 4
                    case _:
                        state = 5
            case 3:
                match c:
                    case 'a': 
                        state = 4
                    case 'b':
                        state = 1
                    case _:
                        state = 5
            case 4:
                match c:
                    case 'a': 
                        state = 3
                    case 'b':
                        state = 2
                    case _:
                        state = 5
                break

    return state == 4


def better_machine(string, state_transitions:list[list[int]]):
    state = 1
    
    for i in range(len(string)):
        input = ord(string[i]) - ord('a')

        try:
            state = state_transitions[state - 1][input]
        except IndexError:
            state = 5

    return state == 4

if __name__ == "__main__":
    print(machine("ab"))

    nstates = 4
    nsymbols = 2
    state_transitions = [[0 for x in range(nsymbols)] for i in range(nstates)]