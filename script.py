from gameplay import display_board

#Create welcome message
print(
"TTT"+ " III" + " CCC" + "   TTT"+" AAA"+" CCC"+"   TTT"+" OOO"+" EEE"+"\n"
" T" + "   I" + "  C" + "      T"+"  A A"+" C"+"      T"+"  O O"+" E"+"\n"
" T" + "   I" + "  C" + "      T"+"  AAA"+" C"+"      T"+"  O O"+" EE"+"\n"
" T" + "   I" + "  C" + "      T"+"  A A"+" C"+"      T"+"  O O"+" E"+"\n"
" T" + "  III" + " CCC" + "    T"+"  A A"+" CCC"+"    T"+"  OOO"+" EEE"+ "\n"
)
print("Welcome to Tic Tac Toe! A game you can play by yourself or with another.")
print("")
players = input("How many players? (1 or 2)\n")
print("You have selected a " + players + "-player game.\n")

board = [" "," "," "," "," "," "," "," "," "]


display_board(board)