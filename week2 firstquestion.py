import random
def fun(A):
	Squarelist=[]
	a=1
	for i in range(A):
		s=a**2
		a=a+1
		if s<=A:
			Squarelist.append(s)
			highestperfectSquare = Squarelist[len(Squarelist)-1]
	else:
		pass
	return highestperfectSquare
	
A=int(input("plz input a value"))
print(fun(A))


#Pseudocode
"""HIGHEST-PERFECT-SQUARE(A)
     Squarelist<-[]
     a<-1
     FOR i <- 1 to A
           s<-a**2
           a<-a+1
           IF s< or = A
                 append s to Squarelist
                 highestperfectSquare<- Squarelist[Length[Squarelist]-1]
           ENDIF
        RETURN highestperfectSquare """
