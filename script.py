from gameplay import play

#Create welcome message
print(
"TTT"+ " III" + " CCC" + "   TTT"+" AAA"+" CCC"+"   TTT"+" OOO"+" EEE"+"\n"
" T" + "   I" + "  C" + "      T"+"  A A"+" C"+"      T"+"  O O"+" E"+"\n"
" T" + "   I" + "  C" + "      T"+"  AAA"+" C"+"      T"+"  O O"+" EE"+"\n"
" T" + "   I" + "  C" + "      T"+"  A A"+" C"+"      T"+"  O O"+" E"+"\n"
" T" + "  III" + " CCC" + "    T"+"  A A"+" CCC"+"    T"+"  OOO"+" EEE"+ "\n"
)
print("Welcome to Tic Tac Toe! A 2 person game.")

board = ["0","1","2","3","4","5","6","7","8"]

play(board)