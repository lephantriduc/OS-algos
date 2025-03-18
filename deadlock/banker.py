# I haven't tested this :)
def banker(available: list[int], max: list[list[int]], allocation: list[list[int]]) -> bool:
    n, m = len(max), len(max[0])

    need = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - allocation[i][j]
    
    work = available    
    finish = [False for i in range(n)]

    for _ in range(n): # repeat the search for AT MOST n times :3
        for i in range(n): # iterate through all n processes to find one to allocate
            all_finished = False
            if not finish[i]:
                all_finished = False
                can_allocate = True
                for j in range(m):
                    if need[i][j] > work[j]:
                        can_allocate = False
                        break
                if not can_allocate: 
                    continue
                else: 
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
            
            if all_finished:
                return True
    
    return False
        