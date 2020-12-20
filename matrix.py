''' Matrix class '''
from exceptions import *

class Matrix:

    def __init__(self, matrix):
        '''
        Matrix class to realize addition, subtraction, multiplication and 
        transpose operation.
        The matrix has to have at least one column and one row.

        Parameters
        --------
        matrix: List
            A two dimensional list
        '''
        self.matrix = matrix

        if len(self.matrix) == 0:
            raise ZeroRowsMatrixError()
        self.rows = len(matrix)

        try:
            self.cols = len(matrix[0])
        except Exception as e:
            raise e
        
        if self.cols == 0:
            raise ZeroColsMatrixError()
