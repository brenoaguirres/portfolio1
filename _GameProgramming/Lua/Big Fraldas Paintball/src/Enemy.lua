--[[
    GD50
    Big Fralda's Paintball
    -- Enemy Class --
    Author: Breno Aguirres
    brenoaguirres1998@gmail.com

    Enemies that are spawned on the map and can be shot down by the player;
]]

Enemy = Class {}

local timer = 0
local resetTime = 4

function Enemy:init()

    -- positions
    self.x = math.random(0, VIRTUAL_WIDTH)
    self.y = math.random(0, VIRTUAL_HEIGHT)

    -- velocity
    self.dx = math.random(-10, 10)
    self.dy = math.random(-10, 10)

    -- speed
    self.speed = math.random(10, 20)

    -- sprite
    self.sprite = gTextures['enemy']

    -- dimensions
    self.width = self.sprite:getWidth()
    self.height = self.sprite:getHeight()

    timer = resetTime

    self.scoreValue = math.random(200, 400)

end

function Enemy:update(dt)

    timer = timer - dt

    if timer <= 0 then
        self.dx = -self.dx
        self.dy = -self.dy
        timer = resetTime
    end

    self.x = self.x + self.dx * self.speed * dt
    self.y = self.y + self.dy * self.speed * dt

    if self.x < 0 + self.width then
        self.x = 0 + self.width
        self.dx = -self.dx
    end

    if self.x > VIRTUAL_WIDTH - self.width then
        self.x = VIRTUAL_WIDTH - self.width
        self.dx = -self.dx
    end

    if self.y < 0 + self.height then
        self.y = 0 + self.height
        self.dy = -self.dy
    end

    if self.y > VIRTUAL_HEIGHT - self.height then
        self.y = VIRTUAL_HEIGHT - self.height
        self.dy = -self.dy
    end

end

function Enemy:collides(target)

    if self.x > target.x + target.width or target.x > self.x + self.width then
        return false
    end

    if self.y > target.y + target.height or target.y > self.y + self.height then
        return false
    end

    return true

end

function Enemy:render()

    love.graphics.draw(self.sprite, self.x, self.y)

end