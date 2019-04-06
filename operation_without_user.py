import numpy
x=numpy.array([[1,2,3],[1,2,3]])
y=numpy.array([[4,5,6],[7,8,9]])

#add()
print("the element wise of addition of matrix is :")
print(numpy.add(x,y))

#subtract()
print("the element wise of subtraction of matrix is :")
print(numpy.subtract(x,y))

#divide()
print("the element wise of divided of matrix is :")
print(numpy.divide(x,y))

#multiply() :  This function is used to perform element wise matrix multiplication.
print("the element wise of multiply of matrix is :") 
print(numpy.multiply(x,y))

#sqrt() : This function is used to compute the square root of each element of matrix.
print ("The element wise square root is : ") 
print (numpy.sqrt(x)) 

#"T" : This argument used to transpose a specified matrix.
print ("The transpose of given matrix is : ") 
print (x.T) 


