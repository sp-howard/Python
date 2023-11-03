# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    command_list = []
    list = []
    
    # Create list of commands
    for command in range(N):
        command_list.append(input().split(' '))
    
    # Iterate through command list and execute functions
    for command in command_list:
        if command[0] == 'print':
            print(list)
        elif command[0] == 'sort':
            list.sort()
        elif command[0] == 'pop':
            list.pop()
        elif command[0] == 'reverse':
            list.reverse()
        elif command[0] == 'append':
            list.append(int(command[1]))
        elif command[0] == 'remove':
            list.remove(int(command[1]))
        elif command[0] == 'insert':
            list.insert(int(command[1]), int(command[2]))