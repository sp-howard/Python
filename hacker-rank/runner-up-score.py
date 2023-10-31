# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    # Convert map object to list
    arr = list(map(int, input().split()))
    
    # Sort list in descending order
    arr.sort(reverse=True)
    
    top_score = arr[0]
    runner_up = 0
    
    # Find the first instance of a value lower than the high score.
    for score in arr:
        if score < top_score:
            runner_up = score
            break
    
    print(runner_up)