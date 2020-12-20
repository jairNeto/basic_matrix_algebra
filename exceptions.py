'''Exceptions module.'''


class ZeroColsMatrixError(Exception):
    '''
        Exception raised for errors when the matrix has zero columns dimension.
    '''

    def __init__(self, message='The matrix needs to have at least one column'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class ZeroRowsMatrixError(Exception):
    '''
        Exception raised for errors when the matrix has zero rows dimension.
    '''

    def __init__(self, message='The matrix needs to have at least one row'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'