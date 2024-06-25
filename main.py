import matplotlib.pyplot as plt
from textwrap import wrap
import pandas as pd
import random as r
import numpy as np
import statistics
import csv
import os



##################################### PERIPHERAL FUNCTIONS (1/4) #####################################





grid = [ # each " " represents square in grid
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

coords = { # to convert user input into grid coordinate
    '7': [0, 0],
    '8': [0, 1],
    '9': [0, 2],
    '4': [1, 0],
    '5': [1, 1],
    '6': [1, 2],
    '1': [2, 0],
    '2': [2, 1],
    '3': [2, 2]
  }

coords_keys = list(coords.keys())

def clear_console(): # clears console after each move so grid is printed only once
    os.system('cls' if os.name=='nt' else 'clear')
    

def get_grid_coord(player_input): # converts input into coordinate on grid
  return coords[str(player_input)]

def print_grid(): # prints grid and keypad
  print("\t\t\t\t\t\t┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┓")
  print("\t\t\t\t\t\t┃         ┃         ┃         ┃", "┏━━━┳━━━┳━━━┓")
  print("\t\t\t\t\t\t┃   ", grid[0][0], "   ┃", "  ", grid[0][1], "   ┃", "  ", grid[0][2], "   ┃", "┃ 7 ┃ 8 ┃ 9 ┃")
  print("\t\t\t\t\t\t┃         ┃         ┃         ┃", "┣━━━╋━━━╋━━━┫")
  print("\t\t\t\t\t\t┣━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┫", "┃ 4 ┃ 5 ┃ 6 ┃")
  print("\t\t\t\t\t\t┃         ┃         ┃         ┃", "┣━━━╋━━━╋━━━┫")
  print("\t\t\t\t\t\t┃   ", grid[1][0], "   ┃", "  ", grid[1][1], "   ┃", "  ", grid[1][2], "   ┃", "┃ 1 ┃ 2 ┃ 3 ┃")
  print("\t\t\t\t\t\t┃         ┃         ┃         ┃", "┗━━━┻━━━┻━━━┛")
  print("\t\t\t\t\t\t┣━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┫")
  print("\t\t\t\t\t\t┃         ┃         ┃         ┃")
  print("\t\t\t\t\t\t┃   ", grid[2][0], "   ┃", "  ", grid[2][1], "   ┃", "  ", grid[2][2], "   ┃")
  print("\t\t\t\t\t\t┃         ┃         ┃         ┃")
  print("\t\t\t\t\t\t┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┛")
  

def clear_grid(): # for resetting game
  grid.clear()
  blank_row = [' ', ' ', ' ']
  for i in range(3):
    grid.append(blank_row.copy())

user_score = 0
com_score = 0

player_1_score = 0
player_2_score = 0

com_1_score = 0
com_2_score = 0

draw_num = 0

total_games = []
starting_players = []
starting_positions = []
total_moves = []
wins = []
loses = []
draws = []

def player_1_win(): # returns first player win
  global user_score, player_1_score, com_1_score
  if menu_selection == 1:
    if game_end_single == False:
      user_score += 1
      print("\n" + user, "won!")
  elif menu_selection == 2:
    if game_end_multi == False:
      player_1_score += 1
      print("\n" + player_1, "wins!")
  elif menu_selection == 3:
    com_1_score += 1
    wins.append("com_1")
    loses.append("com_2")
    return True
  return False


def player_2_win(): # returns second player win
  global com_score, player_2_score, com_2_score
  if menu_selection == 1:
    if game_end_single == False:
      com_score += 1
      print("\n" + user, "lost!")
  elif menu_selection == 2:
    if game_end_multi == False:
      player_2_score += 1
      print("\n" + player_2, "wins!")
  elif menu_selection == 3:
    com_2_score += 1
    wins.append("com_2")
    loses.append("com_1")
    return True
  return False


def game_finished(): # game is finished if all squares are filled
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      if grid[row][column] == " ":
        return False
  return True

def check_win():  # checks for 3 game icons in a row
  for i in range(3):
    if grid[i][0] == grid[i][1] == grid[i][2]:
      if menu_selection == 1:
        if grid[i][0] == '╳' or grid[i][0] == gameicon_x or grid[i][0] == gameicon_x_choice:  
          player_1_win()
          return True
        elif grid[i][0] == '◯' or grid[i][0] == gameicon_o or grid[i][0] == gameicon_x_choice:
          player_2_win()
          return True
      else:
        if grid[i][0] == '╳':  
          player_1_win()
          return True
        elif grid[i][0] == '◯':
          player_2_win()
          return True
      
  for i in range(3):
    if grid[0][i] == grid[1][i] == grid[2][i]:
      if menu_selection == 1:
        if grid[0][i] == '╳' or grid[0][i] == gameicon_x or grid[0][i] == gameicon_x_choice:
          player_1_win()
          return True
        elif grid[0][i] == '◯' or grid[0][i] == gameicon_o or grid[0][i] == gameicon_x_choice:
          player_2_win()
          return True
      else:
        if grid[0][i] == '╳':  
          player_1_win()
          return True
        elif grid[0][i] == '◯':
          player_2_win()
          return True

      
  if grid[0][0] == grid[1][1] == grid[2][2]:
    if menu_selection == 1:
      if grid[0][0] == '╳' or grid[0][0] == gameicon_x or grid[0][0] == gameicon_x_choice:
        player_1_win()
        return True
      elif grid[0][0] == '◯' or grid[0][0] == gameicon_o or grid[0][0] == gameicon_x_choice:
        player_2_win()
        return True
    else:
      if grid[0][0] == '╳':  
        player_1_win()
        return True
      elif grid[0][0] == '◯':
        player_2_win()
        return True

  if grid[0][2] == grid[1][1] == grid[2][0]:
    if menu_selection == 1:
      if grid[0][2] == '╳' or grid[0][2] == gameicon_x or grid[0][2] == gameicon_x_choice:
        player_1_win()
        return True
      elif grid[0][2] == '◯' or grid[0][2] == gameicon_o or grid[0][2] == gameicon_x_choice:
        player_2_win()
        return True
    else:
      if grid[0][2] == '╳':  
        player_1_win()
        return True
      elif grid[0][2] == '◯':
        player_2_win()
        return True

      
  return False

def check_draw(): # checks for a full board with no wins
  if check_win():
    if menu_selection == 1:
      return False

  if not check_win():
    if game_finished():
      if menu_selection == 1 or menu_selection == 2:
        print("Draw!")
        return True
        
  return False


def update_grid(game_input, player = '╳'): # replaces empty square with game icon (X/O)
  grid_coord = get_grid_coord(game_input)
  col_index, row_index = grid_coord[0], grid_coord[1]
  grid_val = grid[col_index][row_index]
  
  if grid_val == ' ':
    grid[col_index][row_index] = player
    return True
  elif menu_selection == 1 or menu_selection == 2:
    print('Try again')
    return False
  else:
    return False

def scoreboard(): # prints scoreboard
  if menu_selection == 1:
    print("SINGLE PLAYER".center(125))
    print("\n\t\t\t\t\t  ---------------SCOREBOARD---------------")
    print("\n\t\t\t\t\t  " + user + "'s Score:", user_score)
    print("\n\t\t\t\t\t  Computer Score:", com_score)
    
  elif menu_selection == 2:
    print("MULTIPLAYER".center(125))
    print("\n\t\t\t\t\t  ---------------SCOREBOARD---------------")
    print("\n\t\t\t\t\t  " + player_1 + ":", player_1_score)
    print("\n\t\t\t\t\t  " + player_2 + ":", player_2_score)
    

def play_again(): # resets game
  while True:
    if menu_selection == 1 or menu_selection == 2:
      play_again = input("\nWould you like to play again? (y/n): ")
    if play_again == "y":
      clear_console()
      clear_grid()
      if menu_selection == 1:
        singleplayer()
        break
      elif menu_selection == 2:
        multiplayer()
        break
    elif play_again == "n":
      print_scoreboard = input("\nWould you like to see the final score? (y/n): ")
      if print_scoreboard == "y":
        clear_console()
        scoreboard()
        return_to_menu = input("\nReturn to main menu? (y/n): ")
        if return_to_menu == "y":
          print_menu()
        elif return_to_menu == "n":
          break
      clear_console()
      print_menu()
      break
    else:
        print("Try again")
        continue








##################################### GAME MODE FUNCTIONS (2/4) #####################################






def singleplayer(): # called to set-up and play single player
  clear_console()
  print("SINGLE PLAYER".center(125))
  clear_grid()
  print_grid()

  random_gameicon_x = ["🗴", "⨉", "χ", "✘", "✗", "☒"] 
  random_gameicon_o = ["⊘", "☢", "☯", "ⵁ", "℗", "⊛", "◍"]
  
  global game_end_single, user, gameicon_x, gameicon_o, gameicon_x_choice, gameicon_o_choice
  gameicon_x_choice = r.choice(random_gameicon_x) # chooses random game icon for x
  gameicon_o_choice = r.choice(random_gameicon_o) # chooses random game icon for o

  game_end_single = False
  user = input("\nPlease enter username: ")

  while True: # loop for input validation
    gameicon_x = input("What game icon would you like to substitute for X (default: d, random: r): ")
    if len(gameicon_x) != 1:
      print("Try again")
      continue
    else:
      break
  while True:
    gameicon_o = input("What game icon would you like to subsitute for O (default: d, random: r): ")
    if len(gameicon_o) != 1:
      print("Try again")
      continue
    elif gameicon_o != "d" and gameicon_o != "r" and gameicon_o == gameicon_x:
      print("Try again")
      continue
    else:
      break

  while game_end_single == False:
    # player moves:
    while True: # runs until player enters a valid move
      player_input = input("\nEnter a number from keypad: ")
      try:
        player_input = int(player_input)
      except ValueError: # loop for input validation
        print("Try again")
        continue
      if player_input < 1 or player_input > 9:
        print("Try again")
        continue
      break
    if gameicon_x == "d": # d for default game icon (X/O)
      if not update_grid(player_input, player = "╳"):
        print("Try again")
        continue # ask for input again
    elif gameicon_x == "r":
      if not update_grid(player_input, player = gameicon_x_choice):
        print("Try again")
        continue
    else:
      if not update_grid(player_input, player = gameicon_x):
        print("Try again")
        continue

    clear_console()
    print("SINGLE PLAYER".center(125))
    print_grid()
    if check_win():
      play_again()
      game_end_single = True
      break
    elif check_draw():
        game_end_single = True
        play_again()
        break
    
    # computer moves:
    while True:
      com_choice = r.randint(1, 9)
      if gameicon_o == "d":
        valid_move = update_grid(com_choice, player = '◯')
      elif gameicon_o == "r":
        valid_move = update_grid(com_choice, player = gameicon_o_choice)
      else:
        valid_move = update_grid(com_choice, player = gameicon_o)
      if valid_move:
        break
      if game_end_single == True:
        break
    
    clear_console()
    print("SINGLE PLAYER".center(125))
    print_grid()
    if check_win():
      game_end_single = True
      play_again()
      break
    elif check_draw():
        game_end_single = True
        play_again()
        break
   
def multiplayer():
  clear_console()
  print("MULTIPLAYER".center(125))
  clear_grid()
  print_grid()

  global game_end_multi
  game_end_multi = False

  global player_1, player_2
  player_1 = input("\nPlease enter username for Player 1: ")
  player_2 = input("\nPlease enter username for Player 2: ")
  
  while game_end_multi == False:
    print("\nTurn:", player_1)
    # player_1_input = int(input("Enter a number from keypad: "))
    while True:
      player_1_input = input("Enter a number from keypad: ")
      try:
        player_1_input = int(player_1_input)
      except ValueError:
        print("Try again")
        continue
      break
    if player_1_input < 1 or player_1_input > 9:
      continue

    if not update_grid(player_1_input, player = '╳'):
      continue # ask for input again

    clear_console()
    print("MULTIPLAYER".center(125))
    print_grid()
    if check_win():
      game_end_multi = True
      play_again()
      break
    elif check_draw():
        game_end_multi = True
        play_again()
        break
      
    print("\nTurn:", player_2)
    while True:
      player_2_input = input("Enter a number from keypad: ")
      try:
        player_2_input = int(player_2_input)
      except ValueError:
        print("Try again")
        continue
      break
    if player_2_input < 1 or player_2_input > 9:
      continue

    if not update_grid(player_2_input, player = '◯'):
      continue # ask for input again
      
    clear_console()
    print("MULTIPLAYER".center(125))
    print_grid()
    if check_win():
      game_end_multi = True
      play_again()
      break
    elif check_draw():
        game_end_multi = True
        play_again()
        break
      
def simulation_play():
  clear_console()
  print("SIMULATION PLAY".center(125))
  clear_grid()
  print_grid()

  def finish(): # collects data when game is over
    end = False
    if check_win():
      end = True
      # print("win")
      draws.append(False)
    elif game_finished():
      end = True
      draws.append(True)
      wins.append(" ")
      loses.append(" ")
      # print("draw")
    if end:
      total_moves.append(moves)
      # print("Computer 1 score: ", com_1_score) # displays score for testing
      # print("Computer 2 score: ", com_2_score)
      # print("draws:", draws)
      # print("moves:", moves)
      return True
    return False
  
  global play_times, starting_player, starting_position
  
  while True: # loop for input validation
    play_times = input("Enter the number of times you would like the game to run: ")
    try:
      play_times = int(play_times)
    except ValueError:
      print("Try again")
      continue
    break
  
  while True: # loop for input validation
    valid_starting_players = ["1", "2", "r"]
    starting_player = input("Enter starting player(1, 2, random(r)): ")
    if starting_player not in valid_starting_players:
      print("Try again")
      continue
    else:
      break

  while True: # loop for input validation
    valid_starting_positions = ["c", "m", "s", "r"]
    starting_position = input("Enter starting position(corner(c), middle(m), side(s), random(r)): ")
    if starting_position not in valid_starting_positions:
      print("Try again")
      continue
    else:
      break

  for i in range(play_times): # runs game a no. of times according to user input
    first_move = True
    moves = 0
    clear_grid()
    clear_console()
    print("SIMULATION PLAY".center(125))
    print_grid()

    for i in range(9):
      while first_move == True:
        if starting_position == "c":
          starting_positions.append("corner")
          corner_positions = [1, 3, 7, 9]
          if starting_player == "1":
            valid_move = update_grid(r.choice(corner_positions), player = '╳')
            moves += 1
            break
          elif starting_player == "2":
            valid_move = update_grid(r.choice(corner_positions), player = '◯')
            moves += 1
            break
          elif starting_player == "r":
            game_icons = ["╳", "◯"]
            valid_move = update_grid(r.choice(corner_positions), player = r.choice(game_icons))
            moves += 1
            break
        elif starting_position == "m":
          starting_positions.append("middle")
          middle_position = 5
          if starting_player == "1":
            valid_move = update_grid(middle_position, player = '╳')
            moves += 1
            break
          elif starting_player == "2":
            valid_move = update_grid(middle_position, player = '◯')
            moves += 1
            break
          elif starting_player == "r":
            game_icons = ["╳", "◯"]
            valid_move = update_grid(middle_position, player = r.choice(game_icons))
            moves += 1
            break
        elif starting_position == "s":
          starting_positions.append("side")
          side_positions = [2, 4, 6, 8]
          if starting_player == "1":
            valid_move = update_grid(r.choice(side_positions), player = '╳')
            moves += 1
            break
          elif starting_player == "2":
            valid_move = update_grid(r.choice(side_positions), player = '◯')
            moves += 1
            break
          elif starting_player == "r":
            game_icons = ["╳", "◯"]
            valid_move = update_grid(r.choice(side_positions), player = r.choice(game_icons))
            moves += 1
            break
        elif starting_position == "r":
          starting_positions.append("random")
          break      
   
      if first_move == True: # to ensure correct second player when starting player is chosen
        if starting_position != "r":
          random = False
          first_move = False
        elif starting_position == "r":
          random = True
          first_move = False
        
      while True:
        if random == False:
          random = True
          break
        if starting_player == "1":
          game_icon = "╳"
        elif starting_player == "2":
          game_icon = "◯"
        elif starting_player == "r":
          game_icons = ["╳", "◯"]
          game_icon = r.choice(game_icons)
        com_1_choice = r.randint(1, 9)
        valid_move = update_grid(com_1_choice, player = game_icon)
        if valid_move:
          moves += 1
          break
        if game_finished():
          break

      # print("SIMULATION PLAY".center(125))
      # print_grid()
  
      if finish():
        break    
        
      while True:
        if random == False:
          random = True
          break
        if starting_player == "1":
          game_icon = "◯"
        elif starting_player == "2":
          game_icon = "╳"
        elif starting_player == "r":
          game_icons = ["╳", "◯"]
          game_icon = r.choice(game_icons)
        com_1_choice = r.randint(1, 9)
        valid_move = update_grid(com_1_choice, player = game_icon)
        if valid_move:
          moves += 1
          break
        if game_finished():
          break
            
      clear_console()
      print("SIMULATION PLAY".center(125))
      print_grid()
  
      if finish():
        break

  global draw_num
  draw_num = play_times - (com_1_score + com_2_score)
  # print("Number of draws: ", draw_num)
  
def print_menu():
  clear_console()
  menu_options = [1, 2, 3]
  print()
  print("MENU".center(125), "\n")
  print("PLEASE CHOOSE AN OPTION BELOW:".center(125), "\n")
  print("(1) SINGLE PLAYER".center(125), "\n")
  print("(2) MULTIPLAYER".center(125), "\n")
  print("(3) SIMULATION PLAY".center(125), "\n")

  while True: 
    global menu_selection
    while True:
      menu_selection = input("ENTER OPTION: ")
      try:
        menu_selection = int(menu_selection)
      except ValueError:
        continue
      break
    if menu_selection in menu_options:
      break
    else:
      continue
  if menu_selection == 1:
    singleplayer()
  elif menu_selection == 2:
    multiplayer()
  elif menu_selection == 3:
    simulation_play()

print_menu()





##################################### GRAPHING USER COLLECTED DATA (3/4) #####################################





def user_model_graphs(): # graphs created by user inputs
  model_file = open("data.csv","r")
  model_rows = list(csv.reader(model_file))
  model_file.close()

  for i in range(play_times):
    total_games.append(i+1)
    if starting_player == "1":
      starting_players.append("com_1")
    elif starting_player == "2":
      starting_players.append("com_2")
    else:
      starting_players.append("random")

  model_csv_data = {
    "game_ID": total_games,
    "starting_player": starting_players,
    "starting_position": starting_positions,
    "total_moves": total_moves,
    "win": wins,
    "lose": loses,
    "draw": draws
  }

  df = pd.DataFrame.from_dict(model_csv_data)
  df.to_csv('data.csv', mode="w", index=False) # changes dict into csv
    
  move_frequencies = {
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": []
  }

  move_frequencies_keys = list(move_frequencies.keys())

  for row in model_rows[1:]: # fills move_frequencies list
    for i in range(len(move_frequencies_keys)):
      if row[3] == move_frequencies_keys[i]:
        move_frequencies[str(i+5)].append(int(row[3]))
  
  move_frequencies_lengths = []

  for key in move_frequencies_keys:
    move_frequencies_lengths.append(len(move_frequencies[key]))

  # print("Data based on user model:")
  # print("The probability of game ending in:")
  # for i in range(len(move_frequencies_lengths)):
  #   print(i+5, "moves:", (move_frequencies_lengths[i]/(len(model_rows)-1))*100)

  # mean = statistics.mean(model_csv_data["total_moves"])
  # median = statistics.median(model_csv_data["total_moves"])
  # mode = statistics.mode(model_csv_data["total_moves"])

  # print()
  # print("Mean no. of moves:", mean)
  # print("Median no. of moves:", median)
  # print("Mode no. of moves", mode)

  def get_starting_position():
    if starting_position == "c":
      return "Corner"
    if starting_position == "m":
      return "Middle"
    if starting_position == "s":
      return "Side"
    if starting_position == "r":
      return "Random"

  def user_model_barchart():
    plt.bar(move_frequencies_keys, move_frequencies_lengths)
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    plt.xlabel("moves")
    plt.ylabel("frequency")

    if starting_player == "1" or starting_player == "2":
      graph_name = str("Modelled Move Frequencies of " + get_starting_position() + " Starting Position")
    if starting_player == "r":
      graph_name = str("Modelled Move Frequencies of " + get_starting_position() + " Starting Player")
    
    plt.title(graph_name)
    plt.show()


  def user_model_pie():
    labels = ["Computer 1 wins", "Computer 2 wins", "draws"]
    game_results = [com_1_score, com_2_score, draw_num]

    plt.pie(game_results, labels = labels)

    if starting_player == "1" or starting_player == "2":
      graph_name = str("Modelled Game Results of " + get_starting_position() + " Starting Position")
    if starting_player == "r":
      graph_name = str("Modelled Game Results of " + get_starting_position() + " Random Starting Player")

    plt.title(graph_name)
    plt.show()


  def user_model_groupedbar():
    x = np.arange(1)
    y1 = [com_1_score]
    y2 = [com_2_score]
    y3 = [draw_num]
    width = 0.1
    plt.bar(x-0.1, y1, width)
    plt.bar(x, y2, width)
    plt.bar(x+0.1, y3, width)
    plt.xticks(x, ["results"])
    plt.legend(["Computer 1 wins", "Computer 2 wins", "draws"])
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)

    if starting_player == "1" or starting_player == "2":
      graph_name = str("Modelled Game Results of " + get_starting_position() + " Starting Position")
    if starting_player == "r":
      graph_name = str("Modelled Game Results of " + get_starting_position() + " Random Starting Player")

    plt.title(graph_name)
    plt.show()
  
  user_model_barchart()
  user_model_pie()
  user_model_groupedbar()

  

if menu_selection == 3:
  user_model_graphs()





##################################### GRAPHING COLLECTED DATA (4/4) #####################################







def my_model_graphs(): # models created from previously collected game data

  collected_data = pd.read_csv("collected-data.csv") # previously collected data

  saved_data = { # contains freq
      "Random Starting Player": {
          "Random Starting Position":{},
      },
      "Constant Starting Player": {
          "Random Starting Position": {},
          "Corner Starting Position": {},
          "Middle Starting Position": {},
          "Side Starting Position": {}
      }
  }

  # structure of the saved_data nested dictionary
  '''
    saved_data = { 
      "Random Starting Player": {
        "Random Starting Position": {
          "move_frequency": {
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
          },
          "results": [],
          "wins": 0,
          "loses": 0,
          "draws": 0
        }
      },
      "Constant Starting Player": {
        "Random Starting Position": {
            etc.
        }
      }
    }
  '''

  starting_players_title = ["Random Starting Player", "Constant Starting Player"]
  starting_positions_title = ["Random Starting Position", "Corner Starting Position", "Middle Starting Position", "Side Starting Position"]
  starting_positions_csv = ["random", "corner", "middle", "side"]
  results_keys = ["win", "lose", "draw"]
  results = ["com_1", "com_1", True]
  moves = ["5", "6", "7", "8", "9"]


  saved_data["Random Starting Player"]["Random Starting Position"]["move_frequency"] = {} 
  saved_data["Random Starting Player"]["Random Starting Position"]["results"] = []

  for i in range(len(moves)): # to fill first dictionary in saved_data
      sum_condition = (collected_data['starting_player'] == "random") & (collected_data['starting_position'] == "random") & (collected_data["total_moves"] == int(moves[i]))
      saved_data["Random Starting Player"]["Random Starting Position"]["move_frequency"][moves[i]] = len(collected_data[sum_condition])
      for j in range(len(collected_data[sum_condition])):
          saved_data["Random Starting Player"]["Random Starting Position"]["results"].append(moves[i])
  for i in range(len(results_keys)):
      condition = (collected_data['starting_player'] == "random") & (collected_data['starting_position'] == "random") & (collected_data[results_keys[i]] == results[i])
      saved_data["Random Starting Player"]["Random Starting Position"][results_keys[i]] = len(collected_data[condition])
      

  for i in range(len(starting_positions_csv)): # to fill second dictionary in saved data
      for j in range(len(results_keys)):
          saved_data["Constant Starting Player"][starting_positions_title[i]]["move_frequency"] = {} # "move_frequency": {}
          saved_data["Constant Starting Player"][starting_positions_title[i]]["results"] = [] # "results": []
          for k in range(len(moves)):
              sum_condition = (collected_data['starting_player'] == "com_1") & (collected_data['starting_position'] == starting_positions_csv[i]) & (collected_data["total_moves"] == int(moves[k]))
              saved_data["Constant Starting Player"][starting_positions_title[i]]["move_frequency"][moves[k]] = len(collected_data[sum_condition])
              for m in range(len(collected_data[sum_condition])):
                  saved_data["Constant Starting Player"][starting_positions_title[i]]["results"].append(moves[k])
          condition = (collected_data['starting_player'] == "com_1") & (collected_data['starting_position'] == starting_positions_csv[i]) & (collected_data[results_keys[j]] == results[j])
          saved_data["Constant Starting Player"][starting_positions_title[i]][results_keys[j]] = len(collected_data[condition])


  def my_model_barchart():
    for i in range(len(starting_players_title)):
        frequency = [[], []]
        for j in range(len(moves)):
            frequency[i].append(saved_data[starting_players_title[i]]["Random Starting Position"]["move_frequency"][moves[j]])
            
        # for j in range(len(frequency)):
        #   for k in range(len(frequency[j])):
        #     print("Probability of game ending in", k + 5, "moves", (frequency[i][k]/1000)*100)
        title = "Moves per Game with " + starting_players_title[i]
        figure = starting_players_title[i] + " Move Frequency - Bar"
        plt.bar(moves, frequency[i])
        plt.title(title)
        plt.grid(color='#71797E', linestyle='--', linewidth=2, axis='y', alpha=0.1)
        plt.xlabel("moves")
        plt.ylabel("frequency")
        plt.ylim(top=400)
        plt.savefig(figure)
        plt.show()

    frequency = [[], [], [], []]

    for i in range(len(starting_positions_title)):
        for j in range(len(moves)):
            frequency[i].append(saved_data["Constant Starting Player"][starting_positions_title[i]]["move_frequency"][moves[j]])

    # for i in range(len(frequency[0])):
    #   print("Probability of game ending in", i + 5, "moves", (frequency[0][i]/1000)*100)

    fig, axs = plt.subplots(2,2)
    fig.suptitle("Moves per Game for each Starting Position")
    axs[0, 0].bar(moves, frequency[0])
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    axs[0, 0].set_title(starting_positions_title[0])
    axs[1, 0].bar(moves, frequency[1])
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    axs[1, 0].set_title(starting_positions_title[1])
    axs[0, 1].bar(moves, frequency[2])
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    axs[0, 1].set_title(starting_positions_title[2])
    axs[1, 1].bar(moves, frequency[3])
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    axs[1, 1].set_title(starting_positions_title[3])
    fig.tight_layout()
    for ax in axs.flat:
        ax.set(xlabel='moves', ylabel='frequency')
    plt.savefig("Starting Position Move Frequency - Bar")
    plt.show()


  def my_model_pie():
    for i in range(len(starting_players_title)):
        game_results = [[], []]
        for j in range(len(results_keys)):
            game_results[i].append(saved_data[starting_players_title[i]]["Random Starting Position"][results_keys[j]])
        title = starting_players_title[i] + " Game Results"
        figure = starting_players_title[i] + " Game Results - Pie"
        plt.pie(game_results[i], labels=results_keys)
        plt.title(title)
        plt.savefig(figure)
        plt.show()

    game_results = [[], [], [], []]

    for i in range(len(starting_positions_title)):
        for j in range(len(results_keys)):
            game_results[i].append(saved_data["Constant Starting Player"][starting_positions_title[i]][results_keys[j]])

    figure = "Starting Position Game Results - Pie"
    fig, axs = plt.subplots(2,2)
    fig.suptitle("Starting Position Game Results")
    axs[0, 0].pie(game_results[0], labels=results_keys)
    axs[0, 0].set_title(starting_positions_title[0])
    axs[1, 0].pie(game_results[1], labels=results_keys)
    axs[1, 0].set_title(starting_positions_title[1])
    axs[0, 1].pie(game_results[2], labels=results_keys)
    axs[0, 1].set_title(starting_positions_title[2])
    axs[1, 1].pie(game_results[3], labels=results_keys)
    axs[1, 1].set_title(starting_positions_title[3])
    fig.tight_layout()
    plt.savefig(figure)
    plt.show()


  def my_model_groupedbar():
    game_results = [[], [], []]

    for i in range(len(starting_players_title)):
        for j in range(len(results_keys)):
            game_results[j].append(saved_data[starting_players_title[i]]["Random Starting Position"][results_keys[j]])

    print("Probability of winning if you go first:", round(((game_results[0][1])/1000)*100, 2), "%")

    x = np.arange(2)
    width = 0.2
    plt.bar(x-0.2, game_results[0], width)
    plt.bar(x, game_results[1], width)
    plt.bar(x+0.2, game_results[2], width)
    plt.xticks(x, ["Random", "Constant"])
    plt.xlabel("Starting Player")
    plt.ylabel("frequency")
    plt.title("Starting Player Game Results")
    plt.legend(results_keys)
    plt.ylim(top=750)
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    plt.savefig("Starting Player Game Results - Grouped Bar")
    plt.show()

    position_game_results = [[], [], []]

    for i in range(len(starting_positions_title)):
        for j in range(len(results_keys)):
            position_game_results[j].append(saved_data["Constant Starting Player"][starting_positions_title[i]][results_keys[j]])

    for i in range(len(starting_positions_title)):
      print("Probability of winning for", starting_positions_title[i] + ":", round((position_game_results[0][i]/1000)*100,2), "%")

    y = np.arange(4)
    width = 0.2
    plt.bar(y-0.2, position_game_results[0], width)
    plt.bar(y, position_game_results[1], width)
    plt.bar(y+0.2, position_game_results[2], width)
    plt.xticks(y, ["Random", "Corner", "Middle", "Side"])
    plt.xlabel("Starting Position")
    plt.ylabel("frequency")
    plt.title("Starting Position Game Results")
    plt.legend(results_keys)
    plt.ylim(top=750)
    plt.grid(color='grey', linestyle='--', linewidth=2, axis='y', alpha=0.1)
    plt.savefig("Starting Position Game Results - Grouped Bar")
    plt.show()

  my_model_barchart()
  my_model_pie()
  my_model_groupedbar()

if menu_selection == 3:
  my_model_graphs()
  while True:
    return_to_menu = input("\nReturn to main menu? (y/n): ")
    if return_to_menu == "y":
      clear_console()
      print_menu()
    elif return_to_menu == "n":
      break
    else:
      print("Try again")
      continue