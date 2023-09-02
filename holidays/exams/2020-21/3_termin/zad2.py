from zad2testy import runtests
class Node():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.end=False
        self.is_prefix=False

def double_prefix( L ):
    n=len(L)
    a=Node('0')
    b=Node('1')

    for i in range(n):
        if L[i][0]=='0':
            p=a
        else:
            p=b
        for j in range(1,len(L[i])):
            if L[i][j]=='0':
                if p.left==None:
                    p.left=Node('0')
                p=p.left
            else:
                if p.right==None:
                    p.right=Node('1')
                p=p.right
        p.end=True
        
    p=a
    R=[]
    word=''
    # def rec1(p,word):
    #     if p==None:
    #         return 
    #     if p.end:
    #         print(word+p.val)
    #     rec1(p.left,word+p.val)
    #     rec1(p.right,word+p.val)
    # rec1(p,word)
    # rec1(b,word)
        
    def rec(p,word):
        nonlocal a,b
        if p==None:
            return
        word+=p.val

        if p.right!=None and p.left!=None:
            # print(word)
            put1=False
            put2=False
            if (p.left.left==None or p.left.right==None):
                if p.left.left!=None or p.left.right!=None:
                    if not p.left.end:
                        put1=True
                else:
                    put1=True

            if  (p.right.left==None or p.right.right==None):
                if p.right.left!=None or p.right.right!=None:
                    if not p.right.end:
                        put2= True
                else:
                    put2= True
            if put1 and put2:
                R.append(word)
                word=''
                return
        elif (p.right!=None or p.left!=None) and p.end:
            put1=True
            put2=True
            if p.left!=None:
                put1=False
                if (p.left.left==None or p.left.right==None):
                    if p.left.left!=None or p.left.right!=None:
                        if not p.left.end:
                            put1=True
                    else:
                        put1=True
            if p.right!=None:
                put2=False
                if  (p.right.left==None or p.right.right==None):
                    if p.right.left!=None or p.right.right!=None:
                        if not p.right.end:
                            put2= True
                    else:
                        put2= True
            if put1 and put2:
                R.append(word)
                word=''
                return


        rec(p.left,word)
        rec(p.right,word)
        # else:
        #     R.append(word)
        #     word=''

    rec(a,word)
    rec(b,word)
    return R

            
            



# runtests( double_prefix )

L=['0100','0110','1010','1']
L=['00111', '0010001', '00001', '0101111', '0001000', '0100010', '001011', '0010010']
T=['000101', '0001101', '0001110', '0010001', '0010010', '0010100', '0010101', '0010110', '00110001', '001101', '0011101', '00111111', '010100', '010101', '0101101', '0101110', 
   '10110001', '1011010', '10111100', '11010011', '110101', '11011101', '11100010', '1110010', '11100111', '11101011', '1110110', '11101111']
L=['010110111', '0001000011', '0101110', 
   '1101001100', '111000100', '1101101101', '010100', '001011', '0010100', '1110010011', '111010111', 
   '0010001101', '1110110', '110100', '10111101', '001000101', '0001110', '0011110100', '10111100', 
   '1110001011', '11100110', '1011010100', '10110001', '111001111', 
   '1110011101', '1110001', '0011010110', '001110111', '001110', '0010010110', 
   '11101100', '111000', '0001101', '101100011', '0010010011', '00111111', '001011101', '1011110010', 
   '00100110', '001111111', '000110100', '000111', '11101010', '111001010', '111001', '0010010', '110111010', 
   '11011101', '0001011', '0011000110', '11010011', '0010110', '1110011', '1011110000', '001010', '1110111110', 
   '001011001', '0010101', '110101', '001101', '00101001', '1101000111', '101101001', '0010000', '00101000', 
   '001100010', '0101011100', '0101001', '111011', '0101010000', '010111011', '01011010', '0001100101', '010110011',
    '111010', '000101', '110101110', '11101111', '00101010', '0001010010', '0001110111', '111000111', '001110100', '10110000', '1110101100', '1110100', '1011001110']
A=double_prefix(L)
print(A)
print(T)

for i in range(len(A)):
    if not A[i] in T:
        print(A[i])
        if A[i] in L:
            print(True)

