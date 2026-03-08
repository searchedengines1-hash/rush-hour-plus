namespace SpriteKind {
    export const trap = SpriteKind.create()
    export const KEY = SpriteKind.create()
    export const Anomaly = SpriteKind.create()
    export const beta = SpriteKind.create()
    export const Npc = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.KEY, assets.tile`myTile7`, function (sprite, location) {
    sprites.destroy(key)
    level = 3
    Caver()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.KEY, function (sprite5, otherSprite) {
    key.follow(mySprite, 50)
    forever2 = 1
    music.play(music.createSong(assets.song`KeyCollect`), music.PlaybackMode.InBackground)
    pause(5000)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite6, otherSprite2) {
    if (otherSprite2 == trap2) {
        if (level == 2) {
            sprites.destroy(sprite6)
            sprites.destroy(otherSprite2)
            enemyizer = 0
            info.changeScoreBy(150)
        }
        if (level == 3) {
            sprites.destroy(sprite6)
            sprites.destroy(otherSprite2)
            enemyizer += -1
            info.changeScoreBy(200)
        }
        if (level == 4) {
            sprites.destroy(sprite6)
            sprites.destroy(otherSprite2)
            enemyizer += -1
            info.changeScoreBy(400)
        }
        if (sprite6 == mySprite4) {
            sprites.destroy(sprite6)
            mySprite5 = sprites.create(img`
                . . . . . . . . . . . . . . . . 
                . . . b b d d d . . . . . . . . 
                . . b b 9 d . d . . . . . . . . 
                . . b b b b . d . . . . . . . . 
                . . . . . . . d . . . . . . . . 
                . . . . d d d d . . . . . . . . 
                . . d d d . . d . . . . . . . . 
                b b b b . . . d . . . . . . . . 
                b 5 5 b . . . d . . . . . . . . 
                b b b b . . d d . . . . . . . . 
                . . b b d d d . . . . . . . . . 
                . b b b b . . . . . . . . . . . 
                . b 2 2 b . . . . . . . . . . . 
                . b 2 2 b . . . . . . . . . . . 
                . b b b . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, SpriteKind.Enemy)
            mySprite6 = sprites.create(img`
                . . . . . . b b b b . . . . . . 
                . . . . . . b 9 b b . b b b b . 
                . . . . . . d b b . . b a a b . 
                . . . . . . d . . . . b b a b . 
                . . . . . . d d . . d d b b b . 
                . . . . . . . d d d d . . . . . 
                . . . . . . . d . . . . . . . . 
                . . . . . . . d . . . . . . . . 
                . . . . . . . d . . . . . . . . 
                . . . . . . . d d . b b b . . . 
                . . . . . . . . d . b 7 b b . . 
                . . . . . . . . . d b 7 7 b . . 
                . . . . . . . . . b b 7 7 b b . 
                . . . . . . . . . b 7 7 7 7 b . 
                . . . . . . . . . b b 7 7 b b . 
                . . . . . . . . . . b b b b . . 
                `, SpriteKind.Enemy)
            mySprite5.follow(mySprite, 15)
            mySprite6.follow(mySprite, 15)
            info.changeScoreBy(750)
            music.play(music.createSong(assets.song`mySong1`), music.PlaybackMode.InBackground)
        }
    }
    if (otherSprite2 == projectile) {
        if (sprite6 == mySprite3) {
            sprites.destroy(otherSprite2)
            info.changeScoreBy(1500)
        }
        if (level == 5) {
            tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleInsignia)
            info.changeScoreBy(-13)
            music.play(music.createSong(hex`
                                    0078000408020600001c00010a006400f401640000040000000000000000000000000005000004060008000c00012701001c000f05001202c102c2010004050028000000640028000314000602000406000c001000012004001c00100500640000041e000004000000000000000000000000000a040004060008000c00011906001c00010a006400f4016400000400000000000000000000000000000000020c000000040001240c001000012407001c00020a006400f4016400000400000000000000000000000000000000030c0000000400012504000800012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8000600040005000109
                                    `), music.PlaybackMode.UntilDone)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorOpenSouth, function (sprite32, location32) {
    level = 0.5
    Caver()
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (cd >= 5) {
        trap2 = sprites.createProjectileFromSprite(assets.image`myImage1`, mySprite, 0, 0)
        cd = 0
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite4, location3) {
    win += 1
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles10, function (sprite42, location4) {
    Caver()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`light`, mySprite, 0, 0)
    cd += 1
    mySprite2.follow(projectile, 100)
    info.changeScoreBy(-25)
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles13, function (sprite7, location5) {
    Caver()
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles7, function (sprite9, location7) {
    Caver()
})
info.onCountdownEnd(function () {
    game.setGameOverMessage(false, "Out of Time!")
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.KEY, assets.tile`myTile4`, function (sprite8, location6) {
    sprites.destroy(key)
    level = 2
    Caver()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Npc, function (sprite2, otherSprite3) {
    if (True_Win >= 1) {
        DIalogue = true
        music.play(music.createSong(hex`
                            0078000408040600001c00010a006400f401640000040000000000000000000000000005000004300000000400011d0400080001250c001000012210001400012518001c00012a1c00200001222400280001257c008000011d01001c000f05001202c102c201000405002800000064002800031400060200040c0014001800012a2c003000012505001c000f0a006400f4010a0000040000000000000000000000000000000002060008000c00012506001c00010a006400f401640000040000000000000000000000000000000002180068006c00011b6c007000012070007400011974007800012507001c00020a006400f401640000040000000000000000000000000000000003480034003800011b38003c00011e3c004000012240004400012544004800012948004c00012c4c005000012a50005400012754005800012458005c0001205c006000011d60006400011909010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80013006c006d0001077400750001057c007d00020004
                            `), music.PlaybackMode.LoopingInBackground)
        game.showLongText("Hello.", DialogLayout.Bottom)
        game.showLongText("you've done it.", DialogLayout.Bottom)
        game.showLongText("Now... i believe we can talk uninterrupted.", DialogLayout.Bottom)
        for (let index = 0; index < 5; index++) {
            story.showPlayerChoices("The Monsters", "The Slime", "Being Chased ", "You", "Family")
            if (story.checkLastAnswer("The Monsters")) {
                game.showLongText("The monsters are simply previous adventurers that were changed.", DialogLayout.Bottom)
                game.showLongText("I'd presume the slime killed them himself and transformed them.", DialogLayout.Bottom)
                game.showLongText("They never truly die, though. So you didn't murder them.", DialogLayout.Bottom)
                game.showLongText("The one with the eye used light magic, so maybe they're drawn to what they used to harness.", DialogLayout.Bottom)
                game.showLongText("I don't know about the rest though.", DialogLayout.Bottom)
                game.showLongText("Also. the reason i know what happened to her is because...", DialogLayout.Bottom)
                spritenew.setImage(assets.image`talkinghatblush`)
                game.showLongText("she was... uh.", DialogLayout.Bottom)
                game.showLongText("she was my...", DialogLayout.Bottom)
                game.showLongText("nevermind.", DialogLayout.Bottom)
                spritenew.setImage(assets.image`talkinghat`)
            } else if (story.checkLastAnswer("The Slime")) {
                game.showLongText("That slime has already left.", DialogLayout.Bottom)
                game.showLongText("You weren't meant to survive, after all.", DialogLayout.Bottom)
                game.showLongText("He and I once were friends.", DialogLayout.Bottom)
                game.showLongText("I don't fully know what changed him, but I did try to stop him.", DialogLayout.Bottom)
                game.showLongText("He was my only Friend.", DialogLayout.Bottom)
            } else if (story.checkLastAnswer("Being Chased ")) {
                game.showLongText("You mean that monster?", DialogLayout.Bottom)
                game.showLongText("i have no idea.", DialogLayout.Bottom)
                game.showLongText("though if we go on the notion that the monsters are souless...", DialogLayout.Bottom)
                game.showLongText("it could be a culmination of their emotions and spirits.", DialogLayout.Bottom)
            } else if (story.checkLastAnswer("You")) {
                game.showLongText("I'm just a talking hat.", DialogLayout.Bottom)
                game.showLongText("My name, if you want to know though, is Woodrow.", DialogLayout.Bottom)
                game.showLongText("About my powers...", DialogLayout.Bottom)
                game.showLongText("I am not really that strong.", DialogLayout.Bottom)
                game.showLongText("I didn't even make this place.", DialogLayout.Bottom)
                game.showLongText("I can go invisible though.", DialogLayout.Bottom)
            } else if (story.checkLastAnswer("Family")) {
                game.showLongText("My... Family?", DialogLayout.Bottom)
                game.showLongText("Well... They're all hats.", DialogLayout.Bottom)
                game.showLongText("Maybe one day you can meet them, but i don't think it's important right now.", DialogLayout.Bottom)
            }
        }
        game.showLongText("Now... Was that all you wanted to hear?", DialogLayout.Bottom)
        story.showPlayerChoices("Yes", "No")
        if (story.checkLastAnswer("Yes")) {
            game.showLongText("Very Well.", DialogLayout.Bottom)
            game.showLongText("You may go.", DialogLayout.Bottom)
            game.setGameOverEffect(true, effects.none)
            game.setGameOverMessage(true, "Finished.")
            game.gameOver(true)
        } else if (story.checkLastAnswer("No")) {
            spritenew.setImage(assets.image`talkinghatuhm`)
            game.showLongText("Well... uh..", DialogLayout.Bottom)
            game.showLongText("i dont know what you'd want now...", DialogLayout.Bottom)
            game.showLongText("but ask away! i guess.", DialogLayout.Bottom)
            game.showLongText("(i wasn't prepared for this)", DialogLayout.Top)
            story.showPlayerChoices("Advice", "Hobbies", "Goodbye", "Restart")
            spritenew.setImage(assets.image`talkinghat`)
            if (story.checkLastAnswer("Advice")) {
                game.showLongText("I'd say...", DialogLayout.Bottom)
                game.showLongText("Spend time with those you love when you can.", DialogLayout.Bottom)
            } else if (story.checkLastAnswer("Hobbies")) {
                game.showLongText("Well... I like to read, and Garden", DialogLayout.Bottom)
                game.showLongText("I can grab things without hands, which is how I do that!", DialogLayout.Bottom)
            } else if (story.checkLastAnswer("Goodbye.")) {
                mySprite.setImage(assets.image`talkinghat0`)
                game.showLongText("Goodbye, Friend!", DialogLayout.Bottom)
                game.showLongText("You can always come back, so don't be shy!", DialogLayout.Bottom)
                game.showLongText("Just whisper my name.", DialogLayout.Bottom)
                game.setGameOverMessage(true, "The True Ending.")
                game.gameOver(true)
            } else if (story.checkLastAnswer("Restart")) {
                game.showLongText("You want me to send you back?", DialogLayout.Bottom)
                game.showLongText("I mean... I can do that... but why?", DialogLayout.Bottom)
                game.showLongText("...", DialogLayout.Bottom)
                game.showLongText("do you really want to?", DialogLayout.Bottom)
                story.showPlayerChoices("I do.", "I don't")
                if (story.checkLastAnswer("I do.")) {
                    True_Win += -1
                    game.setGameOverMessage(false, "You may feel a tingle...")
                    game.setGameOverEffect(true, effects.dissolve)
                    game.gameOver(false)
                } else if (story.checkLastAnswer("I don't.")) {
                    game.showLongText("Okay.", DialogLayout.Bottom)
                    game.showLongText("I'm tired, however.", DialogLayout.Bottom)
                    game.showLongText("You can come back another time.", DialogLayout.Bottom)
                    game.setGameOverMessage(true, "The day's end.")
                    game.gameOver(true)
                }
            }
        }
    } else {
        music.stopAllSounds()
        music.play(music.createSong(assets.song`discordance`), music.PlaybackMode.InBackground)
        game.showLongText("hey, I know you don't know me.", DialogLayout.Bottom)
        game.showLongText("you probably never will.", DialogLayout.Bottom)
        game.showLongText("but you can't trust beta fein.", DialogLayout.Bottom)
        game.showLongText("he is the reason the monsters are here.", DialogLayout.Bottom)
        game.showLongText("not in the sense that the monsters spawned in his basement over time,", DialogLayout.Bottom)
        game.showLongText("but... nevermind.", DialogLayout.Bottom)
        game.showLongText("these monsters are something else.", DialogLayout.Bottom)
        game.showLongText("i can't tell you yet though.", DialogLayout.Bottom)
        game.showLongText("now, i must leave.", DialogLayout.Bottom)
        spritenew.sayText("Good Luck.")
        sprites.destroy(spritenew)
        music.stopAllSounds()
        pause(1000)
    }
})
sprites.onOverlap(SpriteKind.beta, SpriteKind.Player, function (sprite14, otherSprite5) {
    music.stopAllSounds()
    music.play(music.createSong(assets.song`beta fein`), music.PlaybackMode.InBackground)
    game.showLongText("hey its me, beta fein", DialogLayout.Bottom)
    game.showLongText("now, I HOPE you read the controls at the beginning, and yes you can spawn lights with space bar", DialogLayout.Bottom)
    game.showLongText("look, some enemies target you, the light, or more behaviors", DialogLayout.Bottom)
    game.showLongText("now there's one consistent thing, all traps kill all enemies", DialogLayout.Bottom)
    game.showLongText("also you need 5 lights to spawn a trap", DialogLayout.Bottom)
    game.showLongText("DO NOT PLACE A LIGHT ON A TRAP, YOU ARE WASTING OUR VALUABLE INVESTORS MONEY!!!!!!!!!!!!!", DialogLayout.Bottom)
    game.showLongText("remember now, you will rage a lot... hey wait am i breaking the 4th wall.", DialogLayout.Bottom)
    game.showLongText("wait let me get my script!", DialogLayout.Bottom)
    game.showLongText("\"Hello trapper! I hired you to take care of the monsters in my basement\" (dont ask)", DialogLayout.Bottom)
    game.showLongText("\"ill pay you well\"", DialogLayout.Bottom)
    game.showLongText("\"here's how to get to the cave: go straight, and go left.", DialogLayout.Bottom)
    game.showLongText("\"And then turn left to get to the first level\"", DialogLayout.Bottom)
    game.showLongText("\"By the way, you have limited time.\"", DialogLayout.Bottom)
    music.stopAllSounds()
    pause(1000)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function (sprite17, location12) {
    win += 1
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles14, function (sprite15, location10) {
    level = 1
    Caver()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`teleport2`, function (sprite22, location22) {
    level = 0.5
    Caver()
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles15, function (sprite13, location9) {
    Caver()
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles11, function (sprite11, location8) {
    Caver()
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite12, otherSprite4) {
    if (invframes > 0) {
        info.setLife(info.life())
    } else {
        info.changeLifeBy(-1)
        music.play(music.createSong(assets.song`lost_life`), music.PlaybackMode.InBackground)
        invframes = 3
        for (let index = 0; index < 3; index++) {
            timer.after(1500, function () {
                invframes += -1
            })
        }
    }
})
info.onLifeZero(function () {
    music.play(music.createSong(assets.song`DeathSound`), music.PlaybackMode.InBackground)
    if (level == 5) {
        game.setGameOverMessage(false, "I want to go home why is this happening this is torture let me out let me out let me out")
        game.gameOver(false)
    } else {
        if (deathtext == 1) {
            game.setGameOverMessage(false, "lol get better")
        } else if (deathtext == 2) {
            game.setGameOverMessage(false, "dont hug them maybe?")
        } else if (deathtext == 3) {
            game.setGameOverMessage(false, "beta would NOT be proud.")
        } else if (deathtext == 4) {
            game.setGameOverMessage(false, "\"skill issue\"")
        } else if (deathtext == 5) {
            game.setGameOverMessage(false, "do not the monsters")
        } else if (deathtext == 6) {
            game.setGameOverMessage(false, "L trapper am i right")
        } else if (deathtext == 7) {
            game.setGameOverMessage(false, "67 hahaha *dies*")
        } else if (deathtext == 8) {
            game.setGameOverMessage(false, "noob vs pro vs MONSTER")
        } else if (deathtext == 9) {
            game.setGameOverMessage(false, "my 99 year hardcore world!")
        } else {
            game.setGameOverMessage(false, ">:(")
        }
        game.gameOver(false)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Teleport1`, function (sprite3, location2) {
    Render.toggleViewMode()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Projectile, function (sprite10, otherSprite32) {
    sprites.destroy(sprite10)
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
    sprites.destroy(otherSprite32)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLarge, function (sprite16, location11) {
    level = 0.5
    Caver()
})
function Caver () {
    sprites.destroy(projectile)
    level += 1
    if (level == 1) {
        sprites.destroy(projectile)
    }
    if (level == 1.5) {
        sprites.destroy(projectile)
        tiles.setCurrentTilemap(tilemap`level24`)
        tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleInsignia)
        tiles.placeOnRandomTile(key, sprites.dungeon.collectibleInsignia)
        spritenew = sprites.create(assets.image`talkinghat`, SpriteKind.Npc)
        tiles.placeOnRandomTile(spritenew, sprites.dungeon.floorDarkDiamond)
        if (win == 1) {
            if (info.score() > 0) {
                game.setGameOverMessage(true, "you did it.")
                game.setGameOverEffect(true, effects.none)
                pause(5000)
                True_Win += 1
                game.gameOver(true)
            } else {
                game.showLongText("you got the money.", DialogLayout.Center)
                game.setGameOverMessage(true, "beta fein... is gone.")
                game.setGameOverEffect(true, effects.slash)
                pause(5000)
                game.gameOver(true)
            }
        }
    }
    // Changed colors to intensify level difficulty.
    if (level == 2) {
        sprites.destroy(projectile)
        tiles.setCurrentTilemap(tilemap`level27`)
        music.play(music.createSong(assets.song`New Level`), music.PlaybackMode.InBackground)
        tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleInsignia)
        mySprite2 = sprites.create(assets.image`monster1`, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite2, sprites.dungeon.floorLight4)
        mySprite2.follow(projectile, 100)
        key = sprites.create(assets.image`greenkey`, SpriteKind.KEY)
        tiles.placeOnRandomTile(key, sprites.dungeon.floorDark0)
        enemyizer = 1
        info.startCountdown(30)
        music.play(music.createSong(assets.song`Level1Ambeince`), music.PlaybackMode.LoopingInBackground)
        game.showLongText("This monster just follows the light, try to be careful!", DialogLayout.Center)
    }
    if (level == 3) {
        sprites.destroy(projectile)
        tiles.setCurrentTilemap(tilemap`level29`)
        tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleInsignia)
        music.play(music.createSong(assets.song`New Levelslow0`), music.PlaybackMode.InBackground)
        mySprite2 = sprites.create(assets.image`monster1`, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite2, sprites.dungeon.floorDark1)
        mySprite2.follow(projectile, 100)
        mySprite3 = sprites.create(assets.image`monster3`, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite3, sprites.dungeon.floorLight3)
        mySprite3.follow(mySprite, 10)
        key = sprites.create(assets.image`yellowkey - alt`, SpriteKind.KEY)
        tiles.placeOnRandomTile(key, sprites.dungeon.floorDark1)
        enemyizer = 9
        info.startCountdown(60)
        music.play(music.createSong(assets.song`level2`), music.PlaybackMode.LoopingInBackground)
        game.showLongText("This monster is very big, and very slow. Just be aware.", DialogLayout.Center)
    }
    if (level == 4) {
        sprites.destroy(projectile)
        tiles.setCurrentTilemap(tilemap`level _ no key - grey is small monster purple is big0`)
        tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleInsignia)
        music.play(music.createSong(assets.song`newlevel-slowest`), music.PlaybackMode.InBackground)
        mySprite4 = sprites.create(img`
            . . . . . . b b b . . . b b b b 
            . . . . . b b 9 b b . . b a a b 
            . . . . . b b b b b . . b b a b 
            . . . . . . . d . . . . d b b b 
            . . . . . . . d . . d d d . . . 
            . . . d d d d d d d d . . . . . 
            . . d . . . d d d . . . . . . . 
            b b b b . d d . . d . . . . . . 
            b 5 5 b . d . . . d . b b b . . 
            b b b b . d . . . d d b 7 b b . 
            . . . b b d . . . . d b 7 7 b . 
            . . b b b b . . . . b b 7 7 b b 
            . . b 2 2 b . . . . b 7 7 7 7 b 
            . . b 2 2 b . . . . b b 7 7 b b 
            . . b b b . . . . . . b b b b . 
            . . . . . . . . . . . . . . . . 
            `, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite4, sprites.swamp.swampTile16)
        mySprite4.follow(mySprite, 15)
        mySprite2 = sprites.create(assets.image`monster1`, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite2, sprites.castle.rock2)
        mySprite2.follow(projectile, 100)
        mySprite3 = sprites.create(assets.image`monster3`, SpriteKind.Enemy)
        tiles.placeOnRandomTile(mySprite3, sprites.swamp.swampTile9)
        mySprite3.follow(mySprite, 10)
        key = sprites.create(assets.image`eyes`, SpriteKind.KEY)
        tiles.placeOnRandomTile(key, sprites.builtin.brick)
        info.startCountdown(90)
        enemyizer = 9
        game.showLongText("This monster splits after death and dissapears. Keep an eye out.", DialogLayout.Center)
        music.play(music.createSong(assets.song`level 3`), music.PlaybackMode.LoopingInBackground)
    }
    if (level == 5) {
        sprites.destroy(projectile)
        tiles.setCurrentTilemap(tilemap`chase level maybe`)
        tiles.placeOnRandomTile(mySprite, sprites.swamp.swampTile9)
        music.play(music.createSong(assets.song`new`), music.PlaybackMode.UntilDone)
        a_sprite_in_a_can = sprites.create(assets.image`a sprite----in a can`, SpriteKind.Enemy)
        tiles.placeOnRandomTile(a_sprite_in_a_can, sprites.dungeon.collectibleInsignia)
        a_sprite_in_a_can.follow(mySprite, 35)
        enemyizer = 1
        info.startCountdown(666)
        music.play(music.createSong(assets.song`Limbo Lullaby`), music.PlaybackMode.LoopingInBackground)
        game.showLongText("runrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrun", DialogLayout.Center)
    }
}
let a_sprite_in_a_can: Sprite = null
let invframes = 0
let mySprite3: Sprite = null
let mySprite6: Sprite = null
let mySprite5: Sprite = null
let mySprite4: Sprite = null
let trap2: Sprite = null
let DIalogue = false
let mySprite7: Sprite = null
let deathtext = 0
let cd = 0
let forever2 = 0
let enemyizer = 0
let level = 0
let mySprite: Sprite = null
let projectile: Sprite = null
let key: Sprite = null
let mySprite2: Sprite = null
let spritenew: Sprite = null
let win = 0
let True_Win = 0
if (True_Win >= 1) {
    win = 0
    tiles.setCurrentTilemap(tilemap`level33`)
    spritenew = sprites.create(assets.image`talkinghat`, SpriteKind.Npc)
    tiles.placeOnRandomTile(spritenew, assets.tile`myTile2`)
} else {
    win = 0
    Render.setViewMode(ViewMode.raycastingView)
    game.showLongText("DISCLAIMER: This is a rage game, losing a lot is intentional.", DialogLayout.Center)
    game.showLongText("CONTROLS: Z to place light, and go through dialogue.     X to place a trap after using light FIVE times.", DialogLayout.Center)
    game.showLongText("And of course, arrow keys or WASD to move.", DialogLayout.Bottom)
    info.setScore(0)
    info.setLife(3)
    tiles.setCurrentTilemap(tilemap`level32`)
    Render.moveWithController(4, 3, 0)
    mySprite2 = sprites.create(assets.image`monster1`, SpriteKind.Enemy)
    sprites.destroy(mySprite2)
    key = sprites.create(assets.image`yellowkey - alt`, SpriteKind.KEY)
    sprites.destroy(key)
    projectile = sprites.createProjectileFromSprite(assets.image`light`, mySprite, 0, 0)
    sprites.destroy(projectile)
    mySprite = Render.getRenderSpriteVariable()
    tiles.placeOnRandomTile(mySprite, sprites.dungeon.floorLight0)
    level = 0
    enemyizer = -1
    forever2 = 0
    cd = 0
    sprites.destroy(projectile)
    deathtext = randint(1, 10)
    mySprite7 = sprites.create(assets.image`Beta fein`, SpriteKind.beta)
    tiles.placeOnRandomTile(mySprite7, sprites.dungeon.purpleOuterSouth2)
    DIalogue = false
    controller.combos.setTimeout(500)
    music.play(music.createSong(assets.song`Spawn Theme`), music.PlaybackMode.UntilDone)
}
forever(function () {
    scene.cameraFollowSprite(mySprite)
})
forever(function () {
    if (level == 5) {
        Render.toggleViewMode()
        music.play(music.createSong(assets.song`mySong`), music.PlaybackMode.UntilDone)
    }
})
forever(function () {
    if (DIalogue == false) {
        Render.moveWithController(4, 3, 0)
    } else if (DIalogue == true) {
        Render.moveWithController(0, 0, 0)
    }
})
game.onUpdateInterval(100, function () {
    if (level > 1.5) {
        if (enemyizer == 0) {
            music.play(music.createSong(assets.song`mySong0`), music.PlaybackMode.InBackground)
            tiles.setCurrentTilemap(tilemap`level8`)
            info.stopCountdown()
        }
        if (enemyizer == 7) {
            music.play(music.createSong(assets.song`mySong1`), music.PlaybackMode.InBackground)
            tiles.setCurrentTilemap(tilemap`level9`)
            info.stopCountdown()
        }
        if (enemyizer == 4) {
            tiles.setCurrentTilemap(tilemap`chase level maybe`)
            info.stopCountdown()
            game.showLongText("What???", DialogLayout.Bottom)
            level += 1
        }
    }
})
