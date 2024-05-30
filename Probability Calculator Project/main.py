import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        
        ball_count = {color: drawn_balls.count(color) for color in expected_balls}
        
        success = all(ball_count.get(color, 0) >= count for color, count in expected_balls.items())
        
        if success:
            successful_experiments += 1
    
    probability = successful_experiments / num_experiments
    return probability

# Example usage:
hat = Hat(blue=5, red=4, green=2)
probability = experiment(
    hat=hat,
    expected_balls={"red": 1, "green": 2},
    num_balls_drawn=4,
    num_experiments=2000
)


print(probability)
