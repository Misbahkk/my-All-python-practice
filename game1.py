import gamesnake
gamesnake.init()
gameWindow = gamesnake.display.set_mode((1200,500))
gamesnake.display.set_caption("My First Game")

exit_game = False
game_over = False

while not exit_game:
    for event in gamesnake.event.get():
       if event.type==gamesnake.QUIT:
         exit_game = True

       if event.type == gamesnake.KEYDOWN:
          if event.key == gamesnake.K_RIGHT:
             print("You have pressed rifht arrow key")

gamesnake.quit()
quit()