USED MINIMAL AMOUNT OF AI POSSIBLE

Problems faced:
    1.  Earlier I tried to loop through all 8 surrounding boxes but for corner and edge piece there are only
        3 and 5 respectively which meant that there were either indexing errors or out of bound errors. 
    S:  Made a function which counts live neighbours and also checks for these cases. Once these have been
        checked I change ct and change board[i][j] to alive to dead
    
    2.  If statements checking the original board and not the changed version.
    S:  Made new_board which would be looped through by the conditional statements. 

    3.  Original render function kept printing new board instead of clearing the screen
    S:  used os.clear (USED AI FOR THIS :(  )

As of 19/6/26, doesn't make very good looking arts. Will have to add text file paths for that and load the board

21.6.26 -> Added a gun txt file