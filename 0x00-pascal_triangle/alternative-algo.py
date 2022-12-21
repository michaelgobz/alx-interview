from math import factorial
def pascal_triangle(n):
    """
    prints the pascal triangle from the realiszation the the 
    elements are cumulative combination of the number of elements in the given parameteres per
    row 
    """
    for i in range(n):
        for j in range(n-i+1):
 
        # for left spacing
            print(end=" ")
 
        for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
        # for new line
        print()
