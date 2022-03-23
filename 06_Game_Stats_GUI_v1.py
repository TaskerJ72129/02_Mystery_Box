from tkinter import *
from functools import partial # To prevent unwanted windows
import random

 

class Game:
    def __init__(self, parent):
        
        # Formatting variables
        self.game_stats_list = [50, 6]

        # List for holding statistics
        self.round_stats_list = ['copper ($1) | copper ($1) | copper ($1) - Cost: $5 | Payback: $3 | Current Balance: $48']
        
        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Stats Button (row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats",
                                  font="Arial 14", padx=10, pady=10, 
                                  command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class GameStats:
    def __init__(self, partner, game_history, game_stats):
    
        print(game_history)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up stats heading row 0
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_intructons = Label(self.stats_frame,
                                       text="instructions go here", wrap=250,
                                       font="arial 10 italic", justify=LEFT,
                                       fg="green", padx=10, pady=10)
        self.export_intructons.grid(row=1)

        # Starting Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Statrting balance (row 2.0)

        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # Current Balance (row 2.2)
        self.current_balance_label = Label(self.details_frame,
                                         text="Current Balance:", font=heading,
                                         anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[1]),
                                               anchor="w")
        self.current_balance_value_label.grid(row=1, column=1, padx=0) 

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            #win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            #win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.win_loss_label = Label(self.details_frame, text=win_loss,
                                     font=heading, anchor="e")
        self.win_loss_label.grid(row=2, column=0, padx=0)

        self.win_loss_value_label = Label(self.details_frame, text="$ {}".format(amount),
                                     font=content, anchor="w")
        self.win_loss_value_label.grid(row=2, column=1, padx=0)

        # Rounds Played (row 2.4)
        self.games_played_label = Label(self.details_frame, text="Rounds Played",
                                        font=heading, anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, text=len(game_history),
                                        font=content, anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                    font="arial 10 bold",
                                    command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=3, column=1)

    def close_stats(self, partner):
        # Put stats button back to normal..
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


        
class Help:
    def __init__(self, partner):

        background = "white smoke"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Rules",
                                    font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                                justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", fg="white",
                                    width=10, bg="#808080", font="arial 10 bold",
                                    command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal..
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()
    

# Main Routine
if __name__ == "__main__":
    root= Tk() 
    root.title("Mystery Box Game")
    something = Game(root)
    root.mainloop()
