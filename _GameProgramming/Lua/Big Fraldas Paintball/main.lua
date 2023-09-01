   --[[
    Big-Fralda's Paintball
    Author: Breno Aguirres
    brenoaguirres1998@gmail.com

    This game was made after a suggestion from a friend in a bar conversation.
    The challenge was to make a game based on his suggestion before 6 A.M of
    the same day. 
    [24/09/22]
    
    Credit for graphics ():
    https://opengameart.org/users/buch
    Credit for music (Oh, these songs brings so many memories...):
    Corona - Minutemen:
    https://www.youtube.com/watch?v=gOFOqOjJ9Wk
    You - Bad Religion:
    https://www.youtube.com/watch?v=2s7paN4AHpE
    All My Friends Are Dead - Turbonegro
    https://www.youtube.com/watch?v=o6EFg5eWWlM
    Police Truck - Dead Kennedys
    https://www.youtube.com/watch?v=H1Ad3oABt-c
    Superman - Goldfinger
    https://www.youtube.com/watch?v=XvziPPpryv0
    Amoeba - Adolescents
    https://www.youtube.com/watch?v=k2JFpfTPHvo
    Ace of Spades - Motorhead
    https://www.youtube.com/watch?v=86Iwytfa6ms
    Breaking the Law - Judas Priest
    https://www.youtube.com/watch?v=BXtPycm5dGc
    Reach for the Sky - Social Distortion
    https://www.youtube.com/watch?v=fzWSlcuJOoY
    Noots - Sum 41
    https://www.youtube.com/watch?v=xcCkpYB-81E
]]

-- dependencies file
require 'src/Dependencies'

function love.load()

    love.graphics.setDefaultFilter('nearest', 'nearest')

    math.randomseed(os.time())

    love.window.setTitle("Big-Fralda's Paintball")

    -- initializing fonts
    gFonts = {
        ['small'] = love.graphics.newFont('fonts/font.ttf', 8),
        ['medium'] = love.graphics.newFont('fonts/font.ttf', 16),
        ['large'] = love.graphics.newFont('fonts/font.ttf', 32)
    }
    love.graphics.setFont(gFonts['small'])

    -- initializing graphics
    gTextures = {
        ['background'] = love.graphics.newImage('graphics/background.png'),
        ['cbackground'] = love.graphics.newImage('graphics/fieldbackground.png'),
        ['pbackground'] = love.graphics.newImage('graphics/city.png'),
        ['cannon'] = love.graphics.newImage('graphics/cannon.png'),
        ['character'] = love.graphics.newImage('graphics/character.png'),
        ['enemy'] = love.graphics.newImage('graphics/enemy.png'),
        ['ammo-pack'] = love.graphics.newImage('graphics/ammo-pack.png'),
    }

    -- initializing sounds
    gSounds = {
        ['song1'] = love.audio.newSource('sounds/ace-of-spades.mp3', 'static'),
        ['song2'] = love.audio.newSource('sounds/amoeba.mp3', 'static'),
        ['song3'] = love.audio.newSource('sounds/breaking-the-law.mp3', 'static'),
        ['song4'] = love.audio.newSource('sounds/corona.mp3', 'static'),
        ['song5'] = love.audio.newSource('sounds/noots.mp3', 'static'),
        ['song6'] = love.audio.newSource('sounds/police-truck.mp3', 'static'),
        ['song7'] = love.audio.newSource('sounds/reach-for-the-sky.mp3', 'static'),
        ['song8'] = love.audio.newSource('sounds/superman.mp3', 'static'),
        ['song9'] = love.audio.newSource('sounds/all-my-friends-are-dead.mp3', 'static'),
        ['song10'] = love.audio.newSource('sounds/you.mp3', 'static'),
    }
    gSounds['song4']:play()
    gCurrentSong = 'song4'

    -- setups screen virtual size with push
    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        vsync = true,
        resizable = true,
        fullscreen = false
    })

    -- initializing statemachine
    gStateMachine = StateMachine {
        ['start'] = function() return StartState() end,
        ['cutscene'] = function() return CutsceneState() end,
        ['play'] = function() return PlayState() end,
        ['gameover'] = function() return GameOverState() end
    }
    gStateMachine:change('start')

    love.keyboard.keysPressed = {}
    love.mouse.buttonPressed = {}

end

function love.resize(w, h)

    push:resize(w, h)

end


function love.keypressed(key)
    
    love.keyboard.keysPressed[key] = true
    
end

function love.mousepressed(x, y, button)
    
    love.mouse.buttonPressed[button] = true
    
end

function love.keyboard.wasPressed(key)
    
    return love.keyboard.keysPressed[key]
    
end

function love.mouse.wasPressed(button)
    
    return love.mouse.buttonPressed[button]
    
end

function love.update(dt)

    gStateMachine:update(dt)

    -- quits game
    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end

    -- reset table that contain pressed keys and buttons
    love.keyboard.keysPressed = {}
    love.mouse.buttonPressed = {}

end

function love.draw()

    push:apply('start')

    gStateMachine:render()

    displayFPS()

    push:apply('end')

end

function displayFPS()

    love.graphics.setFont(gFonts['small'])
    love.graphics.setColor(0, 1, 0, 1)
    love.graphics.print("FPS: " .. tostring(love.timer.getFPS()), 5, 5)

    --reset
    love.graphics.setColor(1, 1, 1, 1)

end