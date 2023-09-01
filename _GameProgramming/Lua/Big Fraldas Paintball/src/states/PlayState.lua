PlayState = Class {__includes = BaseState}

local clock = 120

function PlayState:init()

    self.playerAim = PlayerAim()

    self.ammoPacks = {}
    self.ammoPackResetTime = 45
    self.ammoPackTimer = 20

    self.enemies = {}

    self.song = math.random(1, 10)

    gSounds[gCurrentSong]:stop()
    gSounds['song' .. self.song]:play()
    gCurrentSong = 'song' .. self.song

    clock = 180
end

function PlayState:update(dt)

    -- game timer
    clock = clock - dt

    -- time to spawn new ammo packs
    self.ammoPackTimer = self.ammoPackTimer - dt
    if self.ammoPackTimer <= 0 then
        table.insert(self.ammoPacks, AmmoPack())
        self.ammoPackTimer = math.random(20, self.ammoPackResetTime)
    end

    -- adds new enemy on screen
    if #self.enemies < ENEMY_COUNT then
        table.insert(self.enemies, Enemy())
    end

    -- game over condition
    if self.playerAim.ammo <= 0 or clock <= 0 then
        gStateMachine:change('start')
    end

    -- check if player shot enemy or power up
    if love.mouse.wasPressed(1) then
        self.playerAim.ammo = self.playerAim.ammo - 1
        for k, enemy in pairs(self.enemies) do
            if enemy:collides(self.playerAim) then

                if self.playerAim.ammo <= 2 then
                    chance = math.random(0, 100)
                    if chance <= 80 then
                        self.playerAim.ammo = self.playerAim.ammo + 2
                    end
                end

                if clock <= 30 then
                    if chance <= 20 then
                        timer = timer + 15
                    end
                end

                self.playerAim.score = self.playerAim.score + enemy.scoreValue
                table.remove(self.enemies, k)
            end
        end

        for k, pack in pairs(self.ammoPacks) do
            if pack:collides(self.playerAim) then
                self.playerAim.ammo = self.playerAim.ammo + pack.ammo
                table.remove(self.ammoPacks, k)
            end
        end
    end

    -- updates enemies
    for k, enemy in pairs(self.enemies) do
        enemy:update(dt)
    end

    -- updates playerAim
    self.playerAim:update(dt)

end

function PlayState:render()

    -- background
    local backgroundWidth = gTextures['pbackground']:getWidth()
    local backgroundHeight = gTextures['pbackground']:getHeight()

    love.graphics.draw(gTextures['pbackground'],
        0, 0,
        0,
        VIRTUAL_WIDTH / (backgroundWidth - 1), VIRTUAL_HEIGHT / (backgroundHeight - 1))

    -- player score
    love.graphics.setFont(gFonts['medium'])
    love.graphics.print('SCORE: ' .. self.playerAim.score, VIRTUAL_WIDTH - 170, 10)

    -- game timer
    love.graphics.setFont(gFonts['medium'])
    if clock >= 60 then
        love.graphics.print(math.floor(clock / 60) .. ":" .. math.floor(clock % 60), VIRTUAL_WIDTH - 170, 30)
    else
        love.graphics.print(00 .. ":" .. math.floor(clock % 60), VIRTUAL_WIDTH - 170, 30)
    end

    -- player ammo
    love.graphics.setFont(gFonts['medium'])
    love.graphics.print('PAINTGUN AMMO: ' .. self.playerAim.ammo, VIRTUAL_WIDTH - 170, VIRTUAL_HEIGHT - 20)

    -- ammo packs
    for k, pack in pairs(self.ammoPacks) do
        pack:render()
    end

    for k, enemy in pairs(self.enemies) do
        enemy:render()
    end

    -- draw playerAim
    self.playerAim:render()

end