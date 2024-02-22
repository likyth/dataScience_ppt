import numpy as np

class Checkers:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.turn = 1  # Player 1 starts
        self.game_over = False

    def reset(self):
        self.board = np.zeros((8, 8), dtype=int)
        for i in range(0, 3):
            for j in range(0, 8):
                if (i+j) % 2 != 0:
                    self.board[i][j] = 1
        for i in range(5, 8):
            for j in range(0, 8):
                if (i+j) % 2 != 0:
                    self.board[i][j] = 2
        self.turn = 1
        self.game_over = False
        return self.board

    def step(self, action):
        if self.game_over:
            raise Exception("Game over, please reset the environment.")

        x, y, new_x, new_y = action
        player = self.board[x][y]
        if player != self.turn:
            raise ValueError("It's not player {}'s turn.".format(self.turn))
        
        if self.board[new_x][new_y] != 0:
            raise ValueError("Invalid move, target position is not empty.")

        # Regular move
        if abs(new_x - x) == 1 and abs(new_y - y) == 1:
            self.board[new_x][new_y] = player
            self.board[x][y] = 0

        # Switch turn
        self.turn = 1 if self.turn == 2 else 2

        return self.board, 0, self.game_over, {}

    def render(self):
        print(self.board)

    def is_game_over(self):
        # Implement check for game over condition
        pass

    def get_valid_moves(self):
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == self.turn:
                    # Check for valid moves for the current player's pieces
                    if j - 1 >= 0 and self.board[i][j - 1] == 0:  # Left move
                        valid_moves.append((i, j, i, j - 1))
                    if j + 1 < 8 and self.board[i][j + 1] == 0:  # Right move
                        valid_moves.append((i, j, i, j + 1))
                    # Add more conditions for valid moves (e.g., diagonal moves for kings)
        return valid_moves if valid_moves else None

# Random agent
class RandomAgent:
    def __init__(self):
        pass

    def choose_action(self, valid_moves):
        return valid_moves[np.random.randint(0, len(valid_moves))]

# Main loop
if __name__ == "__main__":
    env = Checkers()
    agent = RandomAgent()

    state = env.reset()
    done = False
    while not done:
        valid_moves = env.get_valid_moves()
        if valid_moves is None:
            print("No valid moves available. Game over.")
            break
        action = agent.choose_action(valid_moves)
        next_state, reward, done, _ = env.step(action)
        env.render()
