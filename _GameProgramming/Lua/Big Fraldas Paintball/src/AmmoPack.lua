--[[
    GD50
    Big Fralda's Paintball
    -- AmmoPack Class --
    Author: Breno Aguirres
    brenoaguirres1998@gmail.com

    This pack can be shot to give player more ammunition
]]

AmmoPack = Class {}

function AmmoPack:init()

    
    -- sprite
    self.sprite = gTextures['ammo-pack']
    
    -- dimensions
    self.width = self.sprite:getWidth()
    self.height = self.sprite:getHeight()
    
    -- positions
    self.x = math.random(0 + self.width, VIRTUAL_WIDTH - self.width)
    self.y = math.random(0 + self.height, VIRTUAL_HEIGHT - self.height)

    self.ammo = 10

end

function AmmoPack:collides(target)

    if self.x > target.x + target.width or target.x > self.x + self.width then
        return false
    end

    if self.y > target.y + target.height or target.y > self.y + self.height then
        return false
    end

    return true

end

function AmmoPack:render()

    love.graphics.draw(self.sprite, self.x, self.y)

end