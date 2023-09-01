--[[ Flappy Bird Remake [with Love2D]
-- GD50
--
-- Author: Breno Aguirres
-- brenoaguirres1998@gmail.com
-- 20/09/22
-- Based on Colton Ogden's code shown on Harvard's Introduction to Game Development [2018]

    A mobile game by Dong Nguyen that went viral in 2013, utilizing a very simple 
    but effective gameplay mechanic of avoiding pipes indefinitely by just tapping 
    the screen, making the player's bird avatar flap its wings and move upwards slightly. 
    A variant of popular games like "Helicopter Game" that floated around the internet
    for years prior. Illustrates some of the most basic procedural generation of game
    levels possible as by having pipes stick out of the ground by varying amounts, acting
    as an infinitely generated obstacle course for the player.
]]

push = require 'push'

Class = require 'class'

require 'Bird'

require 'Pipe'

require 'PipePair'

require 'StateMachine'
require 'states/BaseState'
require 'states/PlayState'
require 'states/ScoreState'
require 'states/TitleScreenState'
require 'states/CountdownState'

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

-- background image and starting scroll location (x axis)
local background = love.graphics.newImage('/sprites/background.png')
local backgroundScroll = 0

-- ground image and starting scroll location (x axis)
local ground = love.graphics.newImage('/sprites/ground.png')
local groundScroll = 0

-- speed for scrolling images, scaled by dt
local BACKGROUND_SCROLL_SPEED = 30
local GROUND_SCROLL_SPEED = 60

-- point at which we should loop our background back to X 0
local BACKGROUND_LOOPING_POINT = 413

-- point at which we should loop our ground back to X 0
local GROUND_LOOPING_POINT = 514

function love.load()

    -- initialize nearest neighbor filter
    love.graphics.setDefaultFilter('nearest', 'nearest')

    -- app title
    love.window.setTitle('Flappy Bird')

    -- initialize text fonts
    smallFont = love.graphics.newFont("/fonts/font.ttf", 8)
    mediumFont = love.graphics.newFont("/fonts/flappy.ttf", 14)
    flappyFont = love.graphics.newFont("/fonts/flappy.ttf", 28)
    hugeFont = love.graphics.newFont("/fonts/flappy.ttf", 56)
    love.graphics.setFont(flappyFont)

    -- initialize audio
    sounds = {
        ['jump'] = love.audio.newSource('audio/jump.wav', 'static'),
        ['explosion'] = love.audio.newSource('audio/explosion.wav', 'static'),
        ['hurt'] = love.audio.newSource('audio/hurt.wav', 'static'),
        ['score'] = love.audio.newSource('audio/score.wav', 'static'),

        ['music'] = love.audio.newSource('audio/marios_way.mp3', 'static')
    }

    -- setup BGM and kick off
    sounds['music']:setLooping(true)
    sounds['music']:play()



    -- initialize virtual res.
    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        resizable = true,
        vsync = true
    })

    -- initialize state machine; g convention for global
    gStateMachine = StateMachine {
        ['title'] = function() return TitleScreenState() end,
        ['countdown'] = function() return CountdownState() end,
        ['play'] = function() return PlayState() end,
        ['score'] = function() return ScoreState() end
    }
    gStateMachine:change('title')

    -- initialize random seed
    math.randomseed(os.time())

    -- initialize input table
    love.keyboard.keysPressed = {}
    love.mouse.buttonsPressed = {}

end

function love.resize(w, h)

    -- resizes window
    push:resize(w, h)

end


function love.keypressed(key)
    
    -- add to our table of keys pressed this frame
    love.keyboard.keysPressed[key] = true
    
    -- press escape to close app
    if key == 'escape' then
        love.event.quit()
    end
    
end

function love.mousepressed(x, y, button)

    love.mouse.buttonsPressed[button] = true

end

function love.keyboard.wasPressed(key)
    
    return love.keyboard.keysPressed[key]
    
end

function love.mouse.wasPressed(button)

    return love.mouse.buttonsPressed[button]

end

function love.update(dt)

    -- scroll background and by preset speed values * dt, looping back to 0 after the looping point
    backgroundScroll = (backgroundScroll + BACKGROUND_SCROLL_SPEED * dt) 
        % BACKGROUND_LOOPING_POINT
    groundScroll = (groundScroll + GROUND_SCROLL_SPEED * dt)
        % GROUND_LOOPING_POINT

    -- now, we just update the state machine, which defers to the right state
    gStateMachine:update(dt)

    -- reset input table
    love.keyboard.keysPressed = {}
    love.mouse.buttonsPressed = {}

end

function love.draw()

    push:start()

    love.graphics.draw(background, -backgroundScroll, 0)
    gStateMachine:render()
    love.graphics.draw(ground, -groundScroll, VIRTUAL_HEIGHT - 16)

    push:finish()

end