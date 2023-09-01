SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480
MAX_METEOR = 12
FIM_JOGO = false
METEORS_HIT = 0
METEORS_OBJECTIVE = 100

aviao_14bis = {
    src = "imagens/14bis.png",
    width = 55,
    height = 63,
    x = (SCREEN_WIDTH / 2) - (64 / 2),
    y = SCREEN_HEIGHT - 64,
    speed = 2,
    firedBullets = {},
}

meteoros = {}

function movePlayer()

    if love.keyboard.isDown('w') then
        aviao_14bis.y = aviao_14bis.y - aviao_14bis.speed
    end

    if love.keyboard.isDown('a') then
        aviao_14bis.x = aviao_14bis.x - aviao_14bis.speed
    end

    if love.keyboard.isDown('s') then
        aviao_14bis.y = aviao_14bis.y + aviao_14bis.speed
    end

    if love.keyboard.isDown('d') then
        aviao_14bis.x = aviao_14bis.x + aviao_14bis.speed
    end

end

function airplaneShoot()
    
    shooting_sfx:play()

    local bullet = {
        x = aviao_14bis.x + aviao_14bis.width / 2,
        y = aviao_14bis.y,
        width = 16,
        height = 16,
        speed = 5,
    }

    table.insert(aviao_14bis.firedBullets, bullet)
end

function moveBullets()
    for i = #aviao_14bis.firedBullets, 1, -1 do
        if aviao_14bis.firedBullets[i].y > 0 then
            aviao_14bis.firedBullets[i].y = aviao_14bis.firedBullets[i].y - aviao_14bis.firedBullets[i].speed
        else
            table.remove(aviao_14bis.firedBullets, i)
        end
    end
end

function killPlayer()

    crashing_sfx:play()

    aviao_14bis.src = "imagens/explosao_nave.png"
    aviao_14bis.imagem = love.graphics.newImage(aviao_14bis.src)
    aviao_14bis.width = 67
    aviao_14bis.height = 77
    
end

function spawnMeteor()
    meteoro = {
        src = "imagens/meteoro.png",
        width = 50,
        height = 44,
        x = math.random(SCREEN_WIDTH),
        y = -64,
        weight = math.random(0,1),
        horizontal_offset = math.random(-1, 1),
        speed = 0.5,
    }
    table.insert(meteoros, meteoro)
end

function moveMeteor()
    for k, meteoro in pairs(meteoros) do
        meteoro.y = meteoro.y + meteoro.speed + meteoro.weight
        meteoro.x = meteoro.x + meteoro.horizontal_offset
    end
end

function removeMeteor()
    for i = #meteoros, 1, -1 do
        if meteoros[i].y > SCREEN_HEIGHT then
            table.remove(meteoros, i)
        end
    end
end

function hasCollision(X1, Y1, L1, A1, X2, Y2, L2, A2)
    
    return  X2 < X1 + L1 and
            X1 < X2 + L2 and
            Y1 < Y2 + A2 and
            Y2 < Y1 + A1

end

function checkPlayerCollision()

    for k, meteoro in pairs(meteoros) do
        if hasCollision(meteoro.x, meteoro.y, meteoro.width, meteoro.height,
                            aviao_14bis.x, aviao_14bis.y, aviao_14bis.width, aviao_14bis.height) then
            
            changeBGM()
            killPlayer()
            FIM_JOGO = true
        end
    end

end

function checkBulletCollision()

    for i = #aviao_14bis.firedBullets, 1, -1 do
        for j = #meteoros, 1, -1 do
            if hasCollision(aviao_14bis.firedBullets[i].x, aviao_14bis.firedBullets[i].y, 
                            aviao_14bis.firedBullets[i].width, aviao_14bis.firedBullets[i].height, meteoros[j].x, 
                            meteoros[j].y, meteoros[j].width, meteoros[j].height) then
    
                METEORS_HIT = METEORS_HIT + 1
                table.remove(aviao_14bis.firedBullets, i)
                table.remove(meteoros, j)
                break
            end
        end
    end

end

function checkCollision()

    checkPlayerCollision()
    checkBulletCollision()

end

function checkWinCondition()
    if METEORS_HIT >= METEORS_OBJECTIVE then
        WINNER = true
        changeBGM()
    end
end

function changeBGM()
    ambience_ost:stop()
    if FIM_JOGO then
        game_over_ost:play()
    elseif WINNER then
        winner_ost:play()
    end
end


function love.load()

    love.window.setMode(SCREEN_WIDTH, SCREEN_HEIGHT, {resizable = false})
    love.window.setTitle("14bis")

    math.randomseed(os.time())

    background = love.graphics.newImage("imagens/background.png")
    gameover_img = love.graphics.newImage("imagens/gameover.png")
    winner_img = love.graphics.newImage("imagens/vencedor.png")

    aviao_14bis.imagem = love.graphics.newImage(aviao_14bis.src)
    meteoro_img = love.graphics.newImage("imagens/meteoro.png")
    bullet_img = love.graphics.newImage("imagens/tiro.png")

    ambience_ost = love.audio.newSource("audios/ambiente.wav", "static")
    ambience_ost:setLooping(true)
    ambience_ost:play()

    crashing_sfx = love.audio.newSource("audios/destruicao.wav", "static")
    game_over_ost = love.audio.newSource("audios/game_over.wav", "static")
    winner_ost = love.audio.newSource("audios/winner.wav", "static")
    shooting_sfx = love.audio.newSource("audios/disparo.wav", "static")

end

function love.update(dt)

    if not FIM_JOGO and not WINNER then

        if love.keyboard.isDown('w', 'a', 's', 'd') then
            movePlayer()
        end

        removeMeteor()

        if #meteoros < MAX_METEOR then
            spawnMeteor()
        end
        
        moveMeteor()
        moveBullets()

        checkCollision()
        checkWinCondition()

    end
end

function love.keypressed(tecla)
    if tecla == "escape" then
        love.event.quit()
    elseif tecla == "space" then
        airplaneShoot()
    end
end

function love.draw()

    love.graphics.draw(background, 0, 0)
    love.graphics.draw(aviao_14bis.imagem, aviao_14bis.x, aviao_14bis.y)

    love.graphics.print("Remaining Meteors: " .. METEORS_OBJECTIVE - METEORS_HIT, 0, 0)

    for k, meteoro in pairs(meteoros) do
        love.graphics.draw(meteoro_img, meteoro.x, meteoro.y)
    end

    for k,bullet in pairs(aviao_14bis.firedBullets) do
        love.graphics.draw(bullet_img, bullet.x, bullet.y)
    end

    if FIM_JOGO then
        love.graphics.draw(gameover_img, SCREEN_WIDTH / 2 - gameover_img:getWidth() / 2, SCREEN_HEIGHT / 2 - gameover_img:getHeight() / 2)
    end
    
    if WINNER then
        love.graphics.draw(winner_img, SCREEN_WIDTH / 2 - winner_img:getWidth() / 2, SCREEN_HEIGHT / 2 - winner_img:getHeight() / 2)
    end
end