import streamlit as st

def solve_sudoku(board):
    """
    Function to solve Sudoku using backtracking.
    """
    # Find empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row, col = i, j
                break
        else:
            continue
        break
    else:
        # No empty cell
        return True
    
    # Try numbers 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
            
    return False

def is_valid(board, row, col, num):
    """
    Function to check if the given number is valid in the given cell.
    """
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check box
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def display_board(board):
    """
    Function to display the Sudoku board.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            st.write('-' * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                st.write('|', end=' ')
            st.write(board[i][j], end=' ')
        st.write()
        
def main():
    """
    Main function to run the Sudoku solver app.
    """
    st.title("Sudoku Solver")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaper.dog/large/973641.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    # Initialize board with zeros
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Get input from user
    for i in range(9):
        cols = st.text_input(f"Row {i+1} (0 means empty)", value='0 0 0 0 0 0 0 0 0', key=i)
        board[i] = list(map(int, cols.split()))
    
    if st.button("Solve"):
        # Check if Sudoku is solvable
        is_solvable = solve_sudoku(board)
        if is_solvable:
            # Display solution
            st.write("Solution:")
            st.table(board)
        else:
            # Display error message
            st.write("Invalid Sudoku. Please enter a valid Sudoku.")


if __name__ == '__main__':
    main()
