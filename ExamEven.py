class Matrix:

    matrix = []

    def __init__(self):
        self.row = int(input("Enter rows : "))
        self.column = int(input("Enter columns : "))

    def Rows(self):
        print("Rows : ", self.row)

    def Columns(self):
        print("Columns : ", self.column)

    def setAll(self):
        self.matrix = [[0] * self.row] * self.column

        # getting input for each row...
        x = list()
        for i in range(0, self.column):
            for j in range(0, self.row):
                x.append(int(input(f'Enter input for {i} columns and row no. {j}: ')))
            self.matrix[i] = x.copy()
            x.clear()

    # addition of two matrices...
    def add(self, matrix):
        # checking the validity of instance....
        if isinstance(matrix, Matrix):
            # checking the validity of cols and rows....
            if matrix.column == self.column and matrix.row == self.row:
                # performing the addition...
                C = self
                for rows in range(0, self.column):
                    for cols in range(0, self.row):
                        C.matrix[rows][cols] += matrix.matrix[rows][cols]

                return C
            else:
                print("Addition cannot be performed because no. of rows and columns does not matches!")
        else:
            print("Please pass object of Matrix class for addition.")

    # transpose of a matrix...
    def transpose(self):
        # temporary metrix...
        C = Matrix()

        # iterating over self matrix...
        for i in range(0, self.row):
            # temporary list, as column
            x = list()
            for j in range(0, self.column):
                # appending the items from each column as index i
                x.append(self.matrix[j][i])
            C.matrix.append(x.copy())
            x.clear()
        return C

    # setting an index, particular column and row...
    def set(self, i, j):
        try:
            x = self.matrix[i][j]
        except IndexError:
            print("Invalid cols or rows detected in passed parameter")
        else:
            self.matrix[i][j] = int(input(f"Enter value for column {i} and row {j} : "))

    def printMatrix(self):
        for i in range(0, self.column):
            print(self.matrix[i])


A = Matrix()
print("Enter values for matrix A")
A.setAll()

B = Matrix()
print("Enter values for matrix B")
B.setAll()

C = A.add(B)

A.printMatrix()
B.printMatrix()
C.printMatrix()
