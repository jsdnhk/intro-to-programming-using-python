from tkinter import *  # Import tkinter

SIZE = 8  # The size of the chessboard


class EightQueens:
    def __init__(self):
        self.fn_count = 0
        self.queens = SIZE * [-1]  # Queen positions
        self.search(0)  # Search for a solution from row 0

        # Display solution in queens
        window = Tk()  # Create a window
        window.title("Eight Queens")  # Set a title

        print(str(self.queens))     # The location of a queen for each row, 8 in total
        print("Total fn_count = %s" % (self.fn_count))
        image = PhotoImage(file="image/chinaIcon.gif")
        for i in range(SIZE):
            for j in range(SIZE):
                if self.queens[i] == j:
                    Label(window, image=image).grid(row=i, column=j)
                else:
                    Label(window, width=1, height=1, bg="black").grid(row=i, column=j)

        window.mainloop()  # Create an event loop

    # Search for a solution starting from a specified row[0-7], all the result stored in var: queens(list)
    def search(self, row):
        print("search(%s, %s) - %s" % (self, row, str(self.queens)))
        self.fn_count += 1
        if row == SIZE:  # Stopping condition(overflow)
            print("A solution found to place 8 queens")
            return True

        for column in range(SIZE):
            self.queens[row] = column  # Place it at (row, column)
            if self.isValid(row, column) and self.search(row + 1):
                print("Found and exit for loop")
                return True

        print("No solution for a queen placed at any column of this row")
        return False

    # Check if a queen can be placed at row i and column j
    def isValid(self, row, column):
        """
        checking whether conflict about queen new location
        in upper rows checking, but not the lower rows

        :param row: the test queen location(row)[0-7]
        :param column: the test queen location(column)[0-7]
        :return: Boolean
        """
        for i in range(1, row + 1):
            if (self.queens[row - i] == column  # N
                or self.queens[row - i] == column - i   #NW
                or self.queens[row - i] == column + i):    #NE
                return False  # There is a conflict

        return True  # No conflict, requires to check all the upper rows


EightQueens()  # Create GUI
