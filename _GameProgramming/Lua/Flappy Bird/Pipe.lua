--[[ Pipe Class
-- [Flappy Bird Remake]
--
-- Author: Breno Aguirres
-- brenoaguirres1998@gmail.com
-- 20/09/22
-- Based on Colton Ogden's code shown on Harvard's Introduction to Game Development [2018]

   The Pipe class is essentialy the main obstacle to the player. These pipes spawn randomly
   on top or bottom of the screen, with random gap sizes between them. If the player collides
   with them, then it's game over. The pipes scroll towards the player to give the illusion of
   movement. 
]]

Pipe = Class{}

-- we've imported this sprite outside of init() to have just one memory allocation thus saving performance
local PIPE_IMAGE = love.graphics.newImage('/sprites/pipe.png')

function Pipe:init(orientation, y)

    self.x = VIRTUAL_WIDTH
    self.y = y
    
    self.width = PIPE_IMAGE:getWidth()
    self.height = PIPE_HEIGHT

    self.orientation = orientation

end

function Pipe:update(dt)

end

function Pipe:render()

    love.graphics.draw(PIPE_IMAGE, self.x,
        (self.orientation == 'top' and self.y + PIPE_HEIGHT or self.y),
        0, -- rotation
        1, -- x scale
        self.orientation == 'top' and -1 or 1) -- y scale (-1 will mirror the sprite)

end