import tkinter as tk
from mastermind import play, select_colors, Colors, MAX_ATTEMPTS, Match, GameStatus
import platform
if platform.system() == 'Darwin':
    from tkmacosx import Button   # type: ignore
else:
    from tkinter import Button  

globals().update(Match.__members__)
globals().update(GameStatus.__members__)

color_hex_map = {
    'YELLOW': '#FFFF00',
    'RED': '#FF0000',
    'GREEN': '#008000',
    'ORANGE': '#FFA500',
    'LIME': '#00FF00',
    'PINK': '#FF1493',
    'VIOLET': '#8A2BE2',
    'BLUE': '#00BFFF',
    'CYAN': '#00FFFF',
    'MAROON': '#800000'
}

class MastermindUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")
        
        for i in range(12):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(21):  
            self.root.grid_rowconfigure(i, weight=1)

        self.selected_colors = select_colors()  
        self.attempts = 0
        self.max_attempts = MAX_ATTEMPTS
        self.guess_attempts = []  
        self.colors = list(Colors)
        self.current_guess = [None] * 6
        self.game_over = False

        self.create_widgets()
        
    def create_widgets(self):
        self.create_title()
        self.create_color_options()
        self.create_attempt_history()
        self.create_guess_grid()
        self.create_result_grid()
        self.create_restart_button()
        self.create_give_up_button()
        self.create_status_label()
    
    def update_ui(self, guess_result, status):
        self.update_guess_grid()
        self.update_result_grid(guess_result)
        self.update_attempts_label()
        self.update_message(status)
    
    def create_title(self):
        self.title_label = tk.Label(self.root, text="Mastermind Game", font=("Arial", 18))
        self.title_label.grid(row=0, column=0, columnspan=12, sticky='n', pady=10)
    
    def create_color_options(self):
        self.color_buttons_frame = tk.Frame(self.root)
        self.color_buttons_frame.grid(row=1, column=0, columnspan=12, pady=10, sticky='n')

        self.color_buttons = []
        for color in self.colors:
            hex_color = color_hex_map[color.name]
            if platform.system() == 'Darwin':
                color_button = Button(self.color_buttons_frame, text=color.name, bg=hex_color, fg='black',
                                     width=100, height=50, borderwidth=2, relief="groove",
                                     command=lambda c=color: self.add_color_to_guess(c))
            else:
                color_button = Button(self.color_buttons_frame, text=color.name, bg=hex_color, fg='black',
                                     width=10, height=2, borderwidth=2, relief="groove",
                                     command=lambda c=color: self.add_color_to_guess(c))
            color_button.pack(side=tk.LEFT, padx=5)
            self.color_buttons.append(color_button)
    
    def add_color_to_guess(self, color):
        if self.game_over:
            return
        
        for i in range(6):
            if self.current_guess[i] is None:
                self.current_guess[i] = color
                self.guess_grids[self.attempts][i].config(bg=color.value)
                break

        if None not in self.current_guess:
            self.submit_guess()
    
    def disable_color_buttons(self):
        for button in self.color_buttons:
            button.config(state=tk.DISABLED)

    def enable_color_buttons(self):
        for button in self.color_buttons:
            button.config(state=tk.NORMAL)

    def create_restart_button(self):
        self.restart_button = tk.Button(self.root, text="Restart", command=self.reset_game)
        self.restart_button.grid(row=4, column=3, padx=50, sticky='nsew')
    
    def create_give_up_button(self):
        self.give_up_button = tk.Button(self.root, text="Giveup", command=self.reset_game)
        self.give_up_button.grid(row=4, column=7, pady=10, sticky='nsew')
    
    def create_attempt_history(self):
        self.history_label = tk.Label(self.root, text="Attempts History", font=("Arial", 14))
        self.history_label.grid(row=5, column=1, columnspan=10, sticky='nsew')
    
        self.attempts_label = tk.Label(self.root, text=f"Result:\nAttempts: {self.attempts}/{self.max_attempts}", font=("Arial", 12))
        self.attempts_label.grid(row=6, column=1, columnspan=10, sticky='nsew')
    
    def create_guess_grid(self):
        self.guess_frame = tk.Frame(self.root)
        self.guess_frame.grid(row=7, column=3, columnspan=6, rowspan=20, sticky='nsew')
        self.guess_grids = self.create_grid(self.guess_frame)
    
    def create_result_grid(self):
        self.result_frame = tk.Frame(self.root)
        self.result_frame.grid(row=7, column=7, columnspan=6, rowspan=20, sticky='nsew')
        self.result_grids = self.create_grid(self.result_frame)
        
    def create_grid(self, frame): 
        grid = []
        for row in range(20):  
            row_entries = []
            for col in range(6): 
                box = tk.Label(frame, bg='white', width=3, height=1, borderwidth=1, relief="solid")
                box.grid(row=row, column=col, padx=5, pady=5)
                row_entries.append(box)
            grid.append(row_entries)
        return grid

    def create_status_label(self):
        self.status_label = tk.Label(self.root, text="", font=("Arial", 14), pady=10)
        self.status_label.grid(row=5, column=0, columnspan=12)
        
    def submit_guess(self):
        user_provided_colors = self.current_guess.copy()
        guess_result, self.attempts, status = play(self.selected_colors, user_provided_colors, self.attempts)
        self.guess_attempts.append(user_provided_colors)

        self.update_ui(guess_result, status)
        self.current_guess = [None] * 6
        
        if status == GameStatus.WON or status == GameStatus.LOST:
            self.game_over = True
            self.disable_color_buttons()
    
    def update_guess_grid(self):
        for i, attempt in enumerate(self.guess_attempts):
            for j, color in enumerate(attempt):
                hex_color = color_hex_map[color.name]
                self.guess_grids[i][j].config(bg=hex_color)
                
    def update_result_grid(self, guess_result):
        exact_matches = guess_result[Match.EXACT]
        out_of_position_matches = guess_result[Match.INCORRECT_POSITION]
        no_matches = 6 - (exact_matches + out_of_position_matches)
        result_colors = ['black'] * exact_matches + ['darkgray'] * out_of_position_matches + ['dimgray'] * no_matches

        for i in range(6): 
            self.result_grids[self.attempts - 1][i].config(bg=result_colors[i])
    
    def update_attempts_label(self):
        self.attempts_label.config(text=f"Result:\nAttempts: {self.attempts}/{self.max_attempts}")
    
    def update_message(self, status):
        if status == GameStatus.WON:
            self.status_label.config(text="Congratulations, you won!", fg="green")
        elif status == GameStatus.LOST:
            self.status_label.config(text="You've lost the game. Try again!", fg="red")          
    
    def reset_game(self): 
        self.selected_colors = select_colors()  
        self.attempts = 0
        self.guess_attempts = []
        self.current_guess = [None] * 6 
        self.game_over = False

        for row_entries in self.guess_grids:
            for box in row_entries:
                box.config(text="", bg='white')

        for row_results in self.result_grids:
            for result_box in row_results:
                result_box.config(text="", bg='white')

        self.attempts_label.config(text=f"Result:\nAttempts: {self.attempts}/{self.max_attempts}")
        self.status_label.config(text="")
        self.enable_color_buttons() 

    def show_colors(self):
        self.color_buttons_frame = tk.Frame(self.root)
        self.color_buttons_frame.grid(row=3, column=0, columnspan=12, pady=10, sticky='n')

        for color in self.selected_colors:
            hex_color = color_hex_map[color.name]
            color_button = Button(self.color_buttons_frame, text=color.name, bg=hex_color, fg='black',
                                     width=100, height=50, borderwidth=2, relief="groove")
            color_button.pack(side=tk.LEFT, padx=5)
            
if __name__ == "__main__":
    root = tk.Tk()
    game_ui = MastermindUI(root)
    root.mainloop()
    