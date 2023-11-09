# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input()) # Read the number of elements

    # Read integers as a space-separated string, convert to integers, and create a tuple.
    integer_list = tuple(map(int, input().split()))
    
    # Print the hash of the tuple
    print(hash(integer_list))