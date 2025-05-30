import utils
import math

class Physics:
    gravity = 500
    friction = 0.1
    restitution = 0.1 #velocity *= -restitution #(Collision with Walls and Floor)    
    epsilon = 0.5
    
    @staticmethod
    def apply_restitution(ball):
        corner=ball.check_borders_collision()
        if(ball.is_colliding_borders):
            if(corner["left"]) and ball.velocity.x<=0:
                ball.position.x=ball.size
                ball.velocity.x*=-Physics.restitution   
            if(corner["right"]) and ball.velocity.x>=0:
                ball.position.x=utils.screenSize.x-ball.size
                ball.velocity.x*=-Physics.restitution
            if(corner["top"]) and ball.velocity.y<=0:
                ball.position.y=ball.size
                ball.velocity.y*=-Physics.restitution
            if(corner["bottom"]) and ball.velocity.y>=0:
                ball.position.y=utils.screenSize.y-ball.size
                ball.velocity.y*=-Physics.restitution
            


    @staticmethod
    def apply_gravity(ball):
        ball.velocity.y+=Physics.gravity*utils.deltaTime

    @staticmethod
    def apply_friction(ball):
        ball.velocity*= (1-Physics.friction*utils.deltaTime)

    @staticmethod
    def update_balls_colliding():
        from ball import Ball
        checked_ids=[]
        for ball1 in Ball.all_balls:
            for ball2 in Ball.all_balls:
                if ball1.id != ball2.id and ((ball1.id, ball2.id) not in checked_ids) and ((ball2.id, ball1.id) not in checked_ids):
                    check=(math.hypot( ball2.position.x - ball1.position.x,
                           ball2.position.y - ball1.position.y)
                           <=ball1.size+ball2.size)
                    if check:
                        Physics.collision(ball1, ball2)
                        checked_ids.append((ball1.id, ball2.id))

    @staticmethod
    def collision(ball1, ball2):
        delta_pos = ball1.position - ball2.position
        delta_vel = ball1.velocity - ball2.velocity

        distance = delta_pos.length()
        if distance == 0:
            return

        normal = delta_pos.normalize()
        
        vel_along_normal = delta_vel.dot(normal)
        
        if vel_along_normal > 0:
            return

        impulse = -2 * vel_along_normal / 2
        impulse_vector = normal * impulse

        ball1.velocity += impulse_vector
        ball2.velocity -= impulse_vector

        penetration_depth = ball1.size + ball2.size - distance
        correction = normal * (penetration_depth / 2)

        ball1.position += correction
        ball2.position -= correction

    @staticmethod
    def update():
        Physics.update_balls_colliding()
        from ball import Ball
        for ball in Ball.all_balls:
            Physics.apply_gravity(ball)
            Physics.apply_friction(ball)
            Physics.apply_restitution(ball)
            if abs(ball.velocity.x) < Physics.epsilon:
                ball.velocity.x = 0
            if abs(ball.velocity.y) < Physics.epsilon:
                ball.velocity.y = 0
        