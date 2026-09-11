def merge_sort(L: list[float]) -> list[int]:
    """An algorithm for sorting a list of real numbers.
    
    Arg:
        L: a list of real numbers.
    Returns:
        pi: a list such that L[pi[k]] <= L[pi[k+1]] for all k=0,...,len(L)-1.
    """
    #I am constructed merge_sort exactly as presented in Korte & Vygen (6ed)
    n = len(L)
    if n <= 1:
        return list(range(n))
    
    pi = [0]*n
    m = n//2
    rho = merge_sort(L[:m])
    sigma = merge_sort(L[m:])

    k, l = 0, 0
    while k <= m -1 and l <= n - m -1:
        if L[rho[k]] <= L[m + sigma[l]]:
            pi[k+l] = rho[k]
            k = k + 1
        else:
            pi[k+l] = m + sigma[l]
            l = l + 1
    while k <= m - 1:
        pi[k+l] = rho[k]
        k = k + 1
    while l <= n - m - 1:
        pi[k+l] = m + sigma[l]
        l = l + 1
    return pi

if __name__ == "__main__":
    L = [3.1415, -273.15, 2.7182, 9.81, 1.6180, 1.4142, 299792458]
    print(f"List: \n {L}")
    print(f"Permutation: \n {merge_sort(L)}")
