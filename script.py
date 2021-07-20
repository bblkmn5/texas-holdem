from gameplay import Play_Game


#Create welcome message
print(
"TTT"+ " III" + " CCC" + "   TTT"+" AAA"+" CCC"+"   TTT"+" OOO"+" EEE"+"\n"
" T" + "   I" + "  C" + "      T"+"  A A"+" C"+"      T"+"  O O"+" E"+"\n"
" T" + "   I" + "  C" + "      T"+"  AAA"+" C"+"      T"+"  O O"+" EE"+"\n"
" T" + "   I" + "  C" + "      T"+"  A A"+" C"+"      T"+"  O O"+" E"+"\n"
" T" + "  III" + " CCC" + "    T"+"  A A"+" CCC"+"    T"+"  OOO"+" EEE"+ "\n"
)
print("Welcome to Tic Tac Toe! A 2 person game.")

new_game = Play_Game()
new_game.play()