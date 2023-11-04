# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    
    count = 0
    occurance = 0

    while True:
        # Find the next occurrence of the sub_string, starting from 'occurance'
        occurance = string.find(sub_string, occurance)
        
        # If sub_string is not found, break the loop
        if occurance == -1:
            break

        # Otherwise, increment the count and adjust 'occurance' to look for the next occurrence
        count += 1
        occurance += 1  # increment occurance by 1 to avoid finding the same sub-string

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)