from zad2testy import runtests


def robot( L, A, B ):
    n=len(L)
    m=len(L[0])
    F=[[float('inf') for _ in range(m)]for _ in range(n)]
    G=[[0 for _ in range(m)]for _ in range(n)]
    F[A[1]][A[0]]=0





    
runtests( robot )


