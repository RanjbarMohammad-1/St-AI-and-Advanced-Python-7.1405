
import numpy as np

def main():
    print ("hi python")


    # ====================1===========================
    L=[[0,1],[2,3]]
    A=np.array(L)

    print("list L:",L)
    print("type(L) : ",type(L))
    print ("Array A:\n",A)
    print("type(A) : ",type(A))

    # print("id(L) : ",id(L)  )
    # print("id(L[1])-id(L[0]) = ",(id(L[1]))-(id(L[0])))
    # print("id(L[0][1])-id(L[0][0]) = ",id(L[0][1])-id(L[0][0]))



    # ====================2===========================
    # A=np.array([1,2,3,4])
    # print(" A.dtype  : ", A.dtype)
    # print("A.ndim: " , A.ndim)
    # print("A.shape: ",A.shape)
    # print("A.reshape((4,1)).shape = ",A.reshape((4,1)).shape)


    # ====================3===========================
    #==============initializing numpy arrays==========

    # M=np.array([[1,2,3],[4,5,6.0]])
    # print ("M =  ",M)
    # print ("M.dtype : ",M.dtype)
    # print ("M.shape",M.shape)


    # Z=np.zeros((10,10))
    # print("Z :")
    # print(Z)
    # O=np.ones((5,10))
    # print("O : ")
    # print (O)
    # I=np.identity(3)
    # print("I : ")
    # print(I)
    # print("Z.dtype : ",Z.dtype)

    # ====================4===========================
    #==============indexing and slicing===============

    # M=np.array([[0,1,2],[3,4,5]])
    # print("M : ")
    # print(M )
    # print("M[1,1] : ")
    # print(M[1,1])
    # print("M[0,-1] :")
    # print(M[0,-1])

    # print("M[0,1:] : ",M[0,1:])
    # print("M[1],M[1,:] : ",M[1],M[1,:])


    # ====================5===========================
    #=================Advanced slicing================
    # A=np.array([0,1,4,9,16,25])
    # print("A[[2,5]] : ",A[[2,5]])

    # b=A>4
    # print("b :",b)

    # print("(A[b] : ", A[b])

if __name__ == '__main__':
    main()