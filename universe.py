import pygame, random, math

WIDTH = 800
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy")
FPS = 200
particle_num = 200




class galaxy:
    def __init__(self):
        self.particles = []
        WINDOW.fill((0, 0, 0))

    def particle_matrix(self):
        return [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]

    def draw_particles(self, i):
        return pygame.draw.circle(WINDOW, "Red", (self.particles[i][0], self.particles[i][1]), 4, width=0)

    def lentiler(self):
        clock = pygame.time.Clock()
        for i in range(particle_num):
            print(i)
            self.particles.append(galaxy.particle_matrix(self))
        print(self.particles)

        iter = True
        while iter:
            WINDOW.fill((0, 0, 0))
            clock.tick(FPS)
            #Drawing the particles
            for i in range(particle_num):
                galaxy.draw_particles(self, i)
            for i in range(particle_num):
                sum_x = []
                sum_y = []
                for m in range(particle_num):
                    if i != m:
                        delta_x = self.particles[m][0] - self.particles[i][0]
                        delta_y = self.particles[m][1] - self.particles[i][1]

                        distance = math.sqrt((delta_y)**2 + (delta_x)**2)
                        acceleration = 500/(FPS*(distance)**1.618)

                        y_sum = delta_y/distance * acceleration
                        sum_y.append(y_sum)

                        x_sum = delta_x/distance * acceleration
                        sum_x.append(x_sum)
                self.particles[i] = [self.particles[i][0] + 100 * sum(sum_x), self.particles[i][1] + 100 * sum(sum_y)]

            # print(self.particles)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    iter = False
            pygame.display.update()


uni = galaxy()

uni.lentiler()

