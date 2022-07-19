#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given n scores. Store them in a list and find the score of the runner-up (i.e. 2nd best score).

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    sort = sorted(arr, reverse = True)
    for i in range(n):
        if sort[i+1]==sort[i]:
            continue
        else:
            print(sort[i+1])
            break
    
