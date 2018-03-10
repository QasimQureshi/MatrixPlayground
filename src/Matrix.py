# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:55:38 2018

@author: ME
"""
from math import pow
from copy import deepcopy

class Matrix(object):
   def __init__(self,values):
       try:
         if not values:
          raise ValueError
             
         for x in range(len(values)-1):
               if not len(values[x]) == len(values[x+1]):
                 raise ValueError
                 
         self.values = list(values)
         self.m = len(values)
         self.n = len(self.values[0])
         self.order = (self.m,self.n)
       except ValueError:
         raise ValueError('The Matrix must be nonempty and every row must have same column')
           
   def __str__(self):
     a = "\n"
     for x in range(self.m):
       for y in range(self.n):
         a = a + str(self.values[x][y]) + " "
       a = a + "\n"
     return a
  
   def __getitem__(self,key):
     return self.values[key] 
   
   def transpose(self):
     return Matrix([[self[j][i] for j in range(self.m)]for i in range(self.n)])

   
   def plus(self, v):
       try:
         if not self.order == v.order:
           raise ValueError  
         new_values = [[self[i][j] + v[i][j] for j in range(self.n)] for i in 
                        range(self.m)]
         return Matrix(new_values)
       except ValueError:
         raise ValueError('Order of matrices must be same')
   
   def minus(self, v):
       try:
         if not self.order == v.order:
           raise ValueError  
         new_values = [[self[i][j] - v[i][j] for j in range(self.n)] for i in 
                        range(self.m)]
         return Matrix(new_values)
       except ValueError:
         raise ValueError('Order of matrices must be same')
   
   def times_scalar(self, c):
        new_values = [[c * self[i][j] for j in range(self.n)] for i in 
                       range(self.m)]
        return Matrix(new_values)
    
   def dot_Product(self, c):
        try:
         if self.order != c.order:
            raise ValueError         
         return Matrix([[c[i][j]*self[i][j] for j in range(self.n)] for i in range(self.m)])
        except ValueError:
          raise ValueError('Both Matrices must have same order')
   
   def times_Matrix(self, c):
        try:
         if self.n != c.m:
            raise ValueError
         temp = Matrix([[sum([c[i][j]*self[a][b] for b,i in zip(range(self.n),range(c.m))]) for j in range(c.n)] for a in range(self.m)])
         return Matrix([["{0:.2f}".format(temp[i][j]) for j in range(temp.n)] for i in range(temp.m)])
        except ValueError:
          raise ValueError('Columns of firt matrix must be equal to rows of second')
   
   def __eq__(self,v):
       return self.values == v.values
   
   def inverse(self):
     try:
       determinant_Matrix = (self.determinant())
       if determinant_Matrix == 0:
         raise ValueError
       cofactor_Matrix = deepcopy(self)
       for i in range(self.m):
          for j in range(self.n):
            cofactor_Matrix[i][j] = self.cofactor(i,j)
       transposed_Matrix = cofactor_Matrix.transpose()
       return Matrix([[round(transposed_Matrix[i][j]/determinant_Matrix,2) for j in 
                       range(self.n)] for i in range(self.m)])
     except ValueError:
       raise ValueError('Division by zero occured,inverse not possible')
       
   def cofactor(self,i,j):
        New_Matrix = Matrix([[self[a][b] for b in range(self.n) if b != j] for 
                              a in range(self.m) if a != i] )
        return round((pow(-1,i+j) * (New_Matrix.determinant())),2)
      
   def determinant(self):
    try:
      if self.m != self.n:
        raise ValueError
      Mag = 0
      if self.order == (2,2): 
        return (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
      else:
        for i in range(self.n):
          New_Matrix = Matrix([[self[a][b] for b in range(self.n) if b != i] 
            for a in range(self.m) if a != 0])
          Mag = Mag + (pow(-1,i) * (self[0][i]) * (New_Matrix.determinant()))
        return(round(Mag,2))
    except ValueError:
      raise ValueError('Matrix must be square')      
z = Matrix([[1,2,1,1],[1,1,-1,-2],[1,-1,-1,2],[1,-2,1,-1]])
a = z.inverse()
print('A 4x4 Matrix',z)
print('Its Determinant:', z.determinant())
print('Its Inverse:', a)
print('Its product with its inverse:', z.times_Matrix(a))
print('Its dot product with its inverse:', z.dot_Product(a))