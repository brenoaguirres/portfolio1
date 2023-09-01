StartState = Class{__includes = BaseState}

function StartState:update(dt)

    -- changes scene to cutscene
    if love.keyboard.wasPressed('space') then
        gStateMachine:change('cutscene')
    end

end

function StartState:render()

    -- background
    local backgroundWidth = gTextures['background']:getWidth()
    local backgroundHeight = gTextures['background']:getHeight()

    love.graphics.draw(gTextures['background'],
        0, 0,
        0,
        VIRTUAL_WIDTH / (backgroundWidth - 1), VIRTUAL_HEIGHT / (backgroundHeight - 1))

    -- title
    love.graphics.setFont(gFonts['large'])
    love.graphics.setColor(1, 1, 0, 1)
    love.graphics.printf("BIG FRALDA'S PAINTBALL", 0, VIRTUAL_HEIGHT / 3, VIRTUAL_WIDTH, 'center')

    -- instructions
    love.graphics.setFont(gFonts['medium'])
    love.graphics.setColor(1, 1, 1, 1)
    love.graphics.printf("Press Space to Start!", 0, VIRTUAL_HEIGHT / 2 + 80, VIRTUAL_WIDTH, 'center')

end