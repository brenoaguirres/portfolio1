CutsceneState = Class {__includes = BaseState}



function CutsceneState:init()

    self.player = {
        x = 80,
        y = VIRTUAL_HEIGHT - 128,
        dx = 100,
        dy = -50,
        speed = 4,
    }

    gSounds[gCurrentSong]:stop()
    self.startcutscene = false
end

function CutsceneState:update(dt)

    if love.keyboard.wasPressed('space') then
        self.startcutscene = true
    end
    
    if self.startcutscene then
        self.player.x = self.player.x + self.player.dx * self.player.speed * dt
        self.player.y = self.player.y + self.player.dy * self.player.speed * dt
    end

    if self.player.y <= 0 then
        gStateMachine:change('play')
    end

end

function CutsceneState:render()

-- background
local backgroundWidth = gTextures['cbackground']:getWidth()
local backgroundHeight = gTextures['cbackground']:getHeight()

love.graphics.draw(gTextures['cbackground'],
    0, 0,
    0,
    VIRTUAL_WIDTH / (backgroundWidth - 1), VIRTUAL_HEIGHT / (backgroundHeight - 1))

-- character
love.graphics.draw(gTextures['character'],
    self.player.x, self.player.y,
    0,
    1, 1)

-- cannon
love.graphics.draw(gTextures['cannon'],
    90, VIRTUAL_HEIGHT - 128,
    0,
    -1, 1)

-- instructions
love.graphics.setFont(gFonts['medium'])
love.graphics.printf("Press Space!", 0, VIRTUAL_HEIGHT / 2 + 80, VIRTUAL_WIDTH, 'center')

end