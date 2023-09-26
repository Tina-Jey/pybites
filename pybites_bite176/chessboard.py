WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""

 
    for col in range(size):
        for row in range(size):
            if (col + row) %2 == 0:
                print(WHITE, end="")
            else:
                print(BLACK, end="")
        print()

                
    
create_chessboard(8)