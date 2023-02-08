import pygame
import random

pygame.init()

#Colours
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 80)
green = (0, 255, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Yi's Snake Game")

clock = pygame.time.Clock()

snake_blocksize = 10
snake_speed = 25

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

def snake_body(snake_blocksize, snake_list):
    for block in snake_list:
        pygame.draw.rect(dis, green,[block[0], block[1], snake_blocksize, snake_blocksize]) # coordinates, rect size

def score_counter(score_count):
    value = score_font.render("Your Score: " + str(score_count), True, white)
    dis.blit(value, [0,0])

def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg,[dis_width/4, dis_height/2])

def gameloop():

    game_over = False
    game_close = False

    snake_x = dis_width / 2
    snake_y = dis_height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1
    score_count = 0

    food_x = random.randrange(0, dis_width - snake_blocksize, 10)
    food_y = random.randrange(0, dis_height - snake_blocksize, 10)

    while not game_close:
        while game_over == True:
            message("GAME OVER! Press R to play again.", yellow)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Closes when click on 'X' button
                    game_close = True
                    game_over = False
                    print(game_close)
                if event.type == pygame.KEYDOWN:  # Replay if press 'R'
                    if event.key == pygame.K_r:
                        gameloop()


        for event in pygame.event.get(): #All actions are tracked
            if event.type == pygame.QUIT: #Closes when click on 'X' button
                game_close = True
            if event.type == pygame.KEYDOWN: # Arrow keys to control snake direction
                if event.key == pygame.K_LEFT and x_change <= 0: # Stops the snake from doing 180 degree turn
                    x_change = -snake_blocksize
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change >= 0:
                    x_change = snake_blocksize
                    y_change = 0
                elif event.key == pygame.K_UP and y_change <= 0:
                    x_change = 0
                    y_change = -snake_blocksize
                elif event.key == pygame.K_DOWN and y_change >= 0:
                    x_change = 0
                    y_change = snake_blocksize

        if snake_x < 0 or snake_x > dis_width - snake_blocksize or snake_y < 0 or snake_y > dis_height - snake_blocksize: # If snake head hits boundary
            game_over = True

        snake_x += x_change #Update snake location
        snake_y += y_change
        dis.fill(black)

        pygame.draw.rect(dis, white, [food_x, food_y, snake_blocksize, snake_blocksize]) # Display food

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        snake_body(snake_blocksize, snake_list)

        for block in snake_list[:-1]: # If the snake head crashes into it's body
            if snake_head == block:
                game_over = True

        score_counter(score_count)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y: # If snake head touches food
            print("Yum")
            score_count += 1
            length_of_snake += 1
            snake_list.append(snake_head)
            food_x = random.randrange(0, dis_width - snake_blocksize, 10) # Change food location
            food_y = random.randrange(0, dis_height - snake_blocksize, 10)
        else:
            snake_list.pop(0)

        clock.tick(snake_speed) # snake speed by frames per second

    pygame.quit()
    quit()

gameloop()