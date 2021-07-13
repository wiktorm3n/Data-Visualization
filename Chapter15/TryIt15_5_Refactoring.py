from random import choice


class RandomWalk:
    '''A class to generate random walk'''

    def __init__(self, num_points=5000):
        '''Initialize attributes for walk'''
        self.num_points = num_points
        '''All walks starsts at (0,0)'''
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance
        y_step = y_direction * y_distance
        return x_step
        return y_step
    

    def fill_walk(self):
        '''
        Calculate all the points in the walk
        Keep taking steps untill the walk reaches the desired length
        '''
        while len(self.x_values) < self.num_points:
            """Decide which direction to go and how far to go in that direction"""
            x_step = self.get_step()
            y_step = self.get_step()

            '''Reject moves that go nowhere'''
            if x_step == 0 and y_step == 0:
                continue

            '''Calculate new position'''
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
