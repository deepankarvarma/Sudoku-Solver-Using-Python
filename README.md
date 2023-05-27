# Sudoku Solver

This repository contains code for a Sudoku solver implemented in Python. The solver uses a backtracking algorithm to find the solution for a given Sudoku puzzle. The solution is hosted using Streamlit, allowing users to input their Sudoku puzzle and get the solution instantly.

## Usage

To use the Sudoku solver:

1. Access the Streamlit app using the following link: [Sudoku Solver App](https://deepankarvarma-sudoku-solver-using-python-app-z3hyw0.streamlit.app/).

2. Once on the app, you will see a Sudoku grid displayed on the screen.

3. Enter the numbers for your Sudoku puzzle in the corresponding cells. Use 0 to represent empty cells.

4. After entering the puzzle, click the "Solve" button.

5. The solver will attempt to find a solution for the puzzle. If a solution exists, it will be displayed on the screen.

6. If the puzzle is invalid or cannot be solved, an appropriate error message will be shown.

## Code Explanation

The code consists of the following main components:

- `solve_sudoku(board)`: This function implements the backtracking algorithm to solve the Sudoku puzzle. It recursively tries different numbers in empty cells until a valid solution is found.

- `is_valid(board, row, col, num)`: This function checks if a number is valid in a given cell based on Sudoku rules. It checks the row, column, and the 3x3 box to ensure the number is not already present.

- `display_board(board)`: This function is responsible for displaying the Sudoku board using Streamlit. It formats the board and prints it in a user-friendly manner.

- `main()`: The main function sets up the Streamlit app, initializes the Sudoku board, takes user input, and calls the solver function when the "Solve" button is clicked.

## Contributing

If you'd like to contribute to this Sudoku solver, feel free to fork the repository and submit a pull request. Any improvements or bug fixes are welcome.

## License

The code in this repository is available under the [MIT License](LICENSE).
