

class Neuron:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Network:
    def __init__(self):
        self.neurons = []

        for x in range(5):
            for y in range(5):
                self.neurons.append(Neuron(x/5, y/5))
        
        
            



# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
network = Network()
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    for n in network.neurons:
        
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()