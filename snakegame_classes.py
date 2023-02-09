import pygame
import random

pygame.init() #Initialise Pygame

#Colours
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 80)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (102, 255, 255)

#Display Screen Settings
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Yi's Snake Game")
font_style = pygame.font.SysFont("comicsansms", 45)
score_font = pygame.font.SysFont("comicsansms", 25)
high_score_font = pygame.font.SysFont("comicsansms", 30)

class Player:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.snake_blocksize = 10
        self.snake_speed = 25
        self.high_scores_list = [0]*5

    def snake_body(self, snake_blocksize, snake_list): # Draw the snake body
        for block in snake_list:
            pygame.draw.rect(dis, green,[block[0], block[1], snake_blocksize, snake_blocksize]) # coordinates, rect size

    def score_counter(self, score_count): #Displays current score
        value = score_font.render("Your Score: " + str(score_count), True, white)
        dis.blit(value, [10,0])

    def message(self, msg, colour): #Displays Game Over message
        mesg = font_style.render(msg, True, colour)
        dis.blit(mesg,[40, 50])

    def high_score(self, high_scores_list, colour): # Displays top 5 highest scores
        value = high_score_font.render("High Score:", True, colour)
        dis.blit(value, [dis_width / 2.5, 150])
        index = 1
        for number in high_scores_list:
            value = high_score_font.render("#" + str(index) + " - " + str(number), True, colour)
            dis.blit(value, [dis_width / 2.5, 50*(index+3)])
            index += 1

    def gameloop(self): # Run the game
        game_over = False
        game_close = False

        snake_x = dis_width / 2
        snake_y = dis_height / 2
        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1
        score_count = 0

        food_x = random.randrange(0, dis_width - self.snake_blocksize, 10)
        food_y = random.randrange(0, dis_height - self.snake_blocksize, 10)

        while not game_close:
            run_once = 0
            while game_over == True: # When player loses
                while run_once == 0:
                    self.high_scores_list.append(score_count)
                    self.high_scores_list.sort(reverse=True)
                    self.high_scores_list.pop()
                    run_once += 1
                self.message("GAME OVER! Press R to play again.", yellow)
                self.high_score(self.high_scores_list, cyan)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Closes when click on 'X' button
                        game_close = True
                        game_over = False
                        print(game_close)
                    if event.type == pygame.KEYDOWN:  # Replay if press 'R'
                        if event.key == pygame.K_r:
                            self.gameloop()


            for event in pygame.event.get(): #All actions are tracked
                if event.type == pygame.QUIT: #Closes when click on 'X' button
                    game_close = True
                if event.type == pygame.KEYDOWN: # Arrow keys to control snake direction
                    if event.key == pygame.K_LEFT and x_change <= 0: # Stops the snake from doing 180 degree turn
                        x_change = -self.snake_blocksize
                        y_change = 0
                    elif event.key == pygame.K_RIGHT and x_change >= 0:
                        x_change = self.snake_blocksize
                        y_change = 0
                    elif event.key == pygame.K_UP and y_change <= 0:
                        x_change = 0
                        y_change = -self.snake_blocksize
                    elif event.key == pygame.K_DOWN and y_change >= 0:
                        x_change = 0
                        y_change = self.snake_blocksize

            if snake_x < 0 or snake_x > dis_width - self.snake_blocksize or snake_y < 0 or snake_y > dis_height - self.snake_blocksize: # If snake head hits boundary
                game_over = True

            snake_x += x_change #Update snake location
            snake_y += y_change
            dis.fill(black)

            pygame.draw.rect(dis, white, [food_x, food_y, self.snake_blocksize, self.snake_blocksize]) # Display food

            snake_head = [snake_x, snake_y]
            snake_list.append(snake_head)
            self.snake_body(self.snake_blocksize, snake_list)
            for block in snake_list[:-1]: # If the snake head crashes into it's body
                if snake_head == block:
                    game_over = True

            self.score_counter(score_count)
            pygame.display.update()

            if snake_x == food_x and snake_y == food_y: # If snake head touches food
                print("Yum")
                score_count += 1
                length_of_snake += 1
                snake_list.append(snake_head)
                food_x = random.randrange(0, dis_width - self.snake_blocksize, 10) # Change food location
                food_y = random.randrange(0, dis_height - self.snake_blocksize, 10)
            else:
                snake_list.pop(0)

            self.clock.tick(self.snake_speed) # snake speed by frames per second

        pygame.quit()
        quit()

player_1 = Player()
player_1.gameloop()