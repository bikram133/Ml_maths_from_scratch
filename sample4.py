#dot product
def dot_product(a, b):
    m1,n1 = a.shape
    m2,n2 = b.shape
    if n1 != m2:
        raise ValueError("Incompatible dimensions for dot product")
    result=np.zeros((m1,n2))
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                result[i][j] += a[i][k] * b[k][j]
    return result