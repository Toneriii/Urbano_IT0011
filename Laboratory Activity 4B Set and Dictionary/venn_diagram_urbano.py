def create_sets():
    A = {'a', 'b', 'c', 'd', 'f', 'g'}
    B = {'b', 'c', 'd', 'f', 'h', 'l', 'm', 'o'}
    C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}
    
    return A, B, C

def venn_operations():
    A, B, C = create_sets()
    
    a_and_b = len(A.intersection(B))
    print(f"a. Elements in set A and B: {a_and_b}")
    
    b_not_a_not_c = len(B - A - C)
    print(f"b. Elements in B that are not in A and C: {b_not_a_not_c}")
    
    print("\nc. Specific combinations:")
    hijk = B.intersection(C) - A
    print(f"i. {sorted(list(hijk))}")
    
    cdf = A.intersection(B).intersection(C)
    print(f"ii. {sorted(list(cdf))}")
    
    bch = (A.intersection(B) - C).union(B.intersection(C) - A)
    print(f"iii. {sorted(list(bch))}")
    
    df = A.intersection(C) - B
    print(f"iv. {sorted(list(df))}")
    
    c_only = list(A.intersection(B).intersection(C))[0:1]
    print(f"v. {c_only}")
    
    lmo = B - A - C
    print(f"vi. {sorted(list(lmo))}")

if __name__ == "__main__":
    print("Venn Diagram Set Operations:")
    venn_operations()