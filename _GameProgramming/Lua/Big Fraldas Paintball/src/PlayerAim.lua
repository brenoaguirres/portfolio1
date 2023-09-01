--[[
    GD50
    Big Fralda's Paintball
    -- PlayerAim Class --
    Author: Breno Aguirres
    brenoaguirres1998@gmail.com

    Represents the player paintgun's aim sight which the player can use to shoot
    enemy targets; Also, the paintgun has a bullet limit; if it goes down to zero,
    the game is over;
]]

PlayerAim = Class {}

function PlayerAim:init()

    -- positions
    self.x = VIRTUAL_WIDTH / 2 - 8
    self.y = VIRTUAL_HEIGHT / 2 - 8

    -- dimensions
    self.width = 16
    self.height = 16

    -- Image
    self.sprite = love.graphics.newImage('graphics/aim.png')

    self.ammo = 10

    self.score = 0

end

function PlayerAim:update(dt)

    -- place aim sight in the current cursor position
    love.mouse.setVisible(false)

    local xconverted, yconverted = push:toGame((love.mouse.getX() - 17), (love.mouse.getY() - 16))
    self.x = xconverted
    self.y = yconverted

end

function PlayerAim:render()

    love.graphics.draw(self.sprite, self.x, self.y)
    
end