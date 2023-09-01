PlayState = Class {__includes = BaseState}

PIPE_SPEED = 60
PIPE_HEIGHT = 288
PIPE_WIDTH = 70

BIRD_WIDTH = 38
BIRD_HEIGHT = 24

function PlayState:init()

    self.bird = Bird()
    self.pipePairs = {}
    self.timer = 0

    -- keeps track of player score
    self.score = 0

    -- initialize our last recorded Y value for a gap placement to base other gaps off of
    self.lastY = -PIPE_HEIGHT + math.random(80) + 20

end

function PlayState:update(dt)

    self.timer = self.timer + dt
        
    -- spawn a new pipe if the timer is past 2 seconds
    if self.timer > 2 then
        -- modify the last Y coordinate we placed so pipe gaps aren't too far apart
        -- no higher than 10 pixels below the top edge of the screen,
        -- and no lower than a gap length (90 pixels) from the bottom
        local y = math.max(-PIPE_HEIGHT + 10,
            math.min(self.lastY + math.random(-20, 20), VIRTUAL_HEIGHT - 90 - PIPE_HEIGHT))
        self.lastY = y

        table.insert(self.pipePairs, PipePair(y))
        self.timer = 0
    end

    -- for every pipe in the scene
    for k, pair in pairs(self.pipePairs) do
        if not pair.scored then
            if pair.x + PIPE_WIDTH < self.bird.x then
                self.score = self.score + 1
                pair.scored = true
                sounds['score']:play()
            end
        end
        
        pair:update(dt)
    end
    
    -- if the pipe is no longer visible past left edge, remove it from the scene
    for k, pair in pairs(self.pipePairs) do
        if pair.x < -PIPE_WIDTH then
            pair.remove = true
        end
    end

    -- remove any flagged pipes
    -- we need this second loop, rather than deleting in the previous loop, because
    -- modifying the table in-place without explicit keys will result in skipping the
    -- next pipe, since all implicit keys (numerical indices) are automatically shifted
    -- down after a table removal
    for k, pair in pairs(self.pipePairs) do
        if pair.remove then
            table.remove(self.pipePairs, k)
        end
    end

    -- update bird for input and gravity
    self.bird:update(dt)

    for k, pair in pairs(self.pipePairs) do
        -- check to see if the bird collided with pipe
        for l, pipe in pairs(pair.pipes) do
            if self.bird:collides(pipe) then
                -- mix of sound effects
                sounds['explosion']:play()
                sounds['hurt']:play()

                
                gStateMachine:change('score', {
                    score = self.score
                })
            end
        end
    end
        
    
    -- check collision with the ground
    if self.bird.y > (VIRTUAL_HEIGHT - 15) then
        sounds['explosion']:play()
        sounds['hurt']:play()

        gStateMachine:change('score', {
            score = self.score
        })
    end

end

function PlayState:render()

    -- render all the pipes in our scene
    for k, pair in pairs(self.pipePairs) do
        pair:render()
    end

    love.graphics.setFont(flappyFont)
    love.graphics.print('Score: ' .. tostring(self.score), 8, 8)

    self.bird:render()

end