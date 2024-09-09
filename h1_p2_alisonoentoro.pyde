# https://editor.p5js.org/thiagohersan/sketches/p6h71pXE7
class Agent: 
    def __init__(self):
        self.x = random_uniform(17, width - 17)
        self.y = random_uniform(17, height - 17)
        self.vx = choice([-2, -1, 1, 2])
        self.vy = choice([-2, -1, 1, 2])
        self.radius = random_uniform(8, 16)
        self.diam = 2 * self.radius
    
    #def update(): 
        # self.update_by_velocity()
        # self.bounce_boundary()
    
    def bounce_boundary(self): 
        if (self.x + self.radius >= width) or (self.x - self-radius <= 0):
            self.vx *= -1
        if (self.y + self.radius >= height) or (self.y - self-radius <= 0):
            self.vy *= -1
    
    def wrap_boundary(self): 
        if self.x > width: 
            self.x = self.x % width
        if self.x < 0: 
            self.x = self.x + width
        if self.y > height: 
            self.y = self.y % height 
        if self. y < 0: 
            self.y = self.y + height
    
    def reset_boundary(self): 
        if (self.x > width) or (self.x > 0) or (self.y > height) or (self.y <0):
            self.x = random(17, width - 17)
            self.y = random(17, height - 17)
            self.vx = random([-2, -1, 1, 2])
            self.vy = random([-2, -1, 1, 2])
            self.radius = random(8, 16)
            self.diam = 2 * self.radius
        
    def update_by_velocity(self):
        self.x += self.vx;
        self.y += self.vy;
        
    def update_random(self): 
        self.vx = random([-3, -2, -1, 1, 2, 3]);
        self.vy = random([-3, -2, -1, 1, 2, 3]);
        self.x += self.vx;
        self.y += self.vy;
    
    def dist_comp(self, agentA, agentB):
        distA = dist(self.x, self.y, agentA.x, agentA.y)
        distB = dist(self.x, self.y, agentB.x, agentB.y)
        return distA - distB

    #def update_nearest(self):
    # line 84-92 https://editor.p5js.org/thiagohersan/sketches/p6h71pXE7
    
    def draw_agent(self): 
        ellipse(self.x, self.y, self.diam)
        
    def draw(self): 
        if currentMode == POINT_MODE:
            stroke(0)
            self.draw_point()
        elif currentMode == FURTHEST_MODE:
            stroke(0, 8)
            self.draw_furthest()
        elif currentMode == NEAREST_MODE:
            stroke(0, 8)
            self.draw_nearest()
        elif currentMode == OVERLAP_MODE:
            stroke(0, 16)
            no_fill()
            self.draw_overlap()
            
    def  draw_point(self):
        point(self.x, self.y)
        
    def draw_furthest(self):
        # sorted_by_dist =
        # furthest_agent = 
        line(self.x, self.y, furthest_agent.x, furthest_agent.y)
        
    def draw_nearest(self):
        # sorted_by_dist = 
        # nearest_agent = 
        line(self.x, self.y, nearest_agent.x, nearest_agent.y)
        
    def draw_overlap(self):
        for other_agent in agents:
            if self != other_agent:
                t_dist = dist(self.x, self.y, other_agent.x, other_agent.y)
                if t_dist < self.radius + other_agent.radius:
                    cx = (self.x + other_agent.x) / 2
                    cy = (self.y + other_agent.y) / 2
                    ellipse(cx, cy, t_dist, t_dist)
maxAgents = 32;
agents = []

AGENT_MODE = 0
POINT_MODE = 1
FURTHEST_MODE = 2
NEAREST_MODE = 3
OVERLAP_MODE = 4\

# what is line 165 currentMode https://editor.p5js.org/thiagohersan/sketches/p6h71pXE7


def setup():
    size(windowWidth, windowHeight)
    
    for i in range(max_agents):
        agents.append(Agent())
        
def draw():
    for agent in agents:
        agent.update()

    if currentMode == AGENT_MODE:
        background(220, 20, 120)
        noStroke()
        fill(255)
        for agent in agents:
            agent.draw_agent()
    else:
        for agent in agents:
            agent.draw()

def mouseClicked():
    

def keyReleased():
