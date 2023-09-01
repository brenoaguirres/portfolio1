--[[ Bird Class
-- [Flappy Bird Remake]
--
-- Author: Breno Aguirres
-- brenoaguirres1998@gmail.com
-- 20/09/22
-- Based on Colton Ogden's code shown on Harvard's Introduction to Game Development [2018]

   The Bird is the main character in the game and is controlled via mouse clicking or hitting
   the space bar; When moving it, it'll fly a little bit and then will fall affected by gravity.
   If the Bird hits the ground or a pipe, the game is over.
]]

Bird = Class{}

local GRAVITY = 20
local JUMP = 5

function Bird:init()

    -- load bird image and assign its width and height
    self.image = love.graphics.newImage('/sprites/bird.png')
    self.width = self.image:getWidth()
    self.height = self.image:getHeight()

    -- position bird in the middle of the screen
    self.x = VIRTUAL_WIDTH / 2 - (self.width / 2)
    self.y = VIRTUAL_HEIGHT / 2 - (self.height / 2)

    -- Y velocity; gravity
    self.dy = 0

end

function Bird:collides(obj)

    -- the 2's are left and top offsets
    -- the 4's are right and bottom offsets
    -- both offsets are used to shrink the bounding box to give the player
    -- a little bit of leeway with the collision
    if (self.x + 2) + (self.width - 4) >= obj.x and self.x + 2 <= obj.x + PIPE_WIDTH then
        if (self.y + 2) + (self.height - 4) >= obj.y and self.y + 2 <= obj.y + PIPE_HEIGHT then
            return true
        end
    end

    return false

end

function Bird:update(dt)

    -- apply gravity to velocity; 
    self.dy = self.dy + GRAVITY * dt

    -- apply current velocity to Y position
    self.y = self.y + self.dy

    -- adds negative gravity (jump) if space was hit
    if love.keyboard.wasPressed('space') or love.mouse.wasPressed(1) then
        self.dy = - JUMP
        sounds['jump']:play()
    end

end

function Bird:render()
   
    love.graphics.draw(self.image, self.x, self.y)

end