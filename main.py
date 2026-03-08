@namespace
class SpriteKind:
    trap = SpriteKind.create()
    KEY = SpriteKind.create()
    Anomaly = SpriteKind.create()
    beta = SpriteKind.create()
    Npc = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global level
    sprites.destroy(key)
    level = 3
    Caver()
scene.on_overlap_tile(SpriteKind.KEY,
    assets.tile("""
        myTile7
        """),
    on_overlap_tile)

def on_on_overlap(sprite5, otherSprite):
    global forever2
    key.follow(mySprite, 50)
    forever2 = 1
    music.play(music.create_song(assets.song("""
            KeyCollect
            """)),
        music.PlaybackMode.IN_BACKGROUND)
    pause(5000)
sprites.on_overlap(SpriteKind.player, SpriteKind.KEY, on_on_overlap)

def on_on_overlap2(sprite6, otherSprite2):
    global enemyizer, mySprite5, mySprite6
    if otherSprite2 == trap2:
        if level == 2:
            sprites.destroy(sprite6)
            sprites.destroy(otherSprite2)
            enemyizer = 0
            info.change_score_by(150)
        if level == 3:
            sprites.destroy(sprite6)
            sprites.destroy(otherSprite2)
            enemyizer += -1
            info.change_score_by(200)
        if level == 4:
            sprites.destroy(sprite6)
            sprites.destroy(otherSprite2)
            enemyizer += -1
            info.change_score_by(400)
        if sprite6 == mySprite4:
            sprites.destroy(sprite6)
            mySprite5 = sprites.create(img("""
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
                    """),
                SpriteKind.enemy)
            mySprite6 = sprites.create(img("""
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
                    """),
                SpriteKind.enemy)
            mySprite5.follow(mySprite, 15)
            mySprite6.follow(mySprite, 15)
            info.change_score_by(750)
            music.play(music.create_song(assets.song("""
                    mySong1
                    """)),
                music.PlaybackMode.IN_BACKGROUND)
    if otherSprite2 == projectile:
        if sprite6 == mySprite3:
            sprites.destroy(otherSprite2)
            info.change_score_by(1500)
        if level == 5:
            tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
            info.change_score_by(-13)
            music.play(music.create_song(hex("""
                    0078000408020600001c00010a006400f401640000040000000000000000000000000005000004060008000c00012701001c000f05001202c102c2010004050028000000640028000314000602000406000c001000012004001c00100500640000041e000004000000000000000000000000000a040004060008000c00011906001c00010a006400f4016400000400000000000000000000000000000000020c000000040001240c001000012407001c00020a006400f4016400000400000000000000000000000000000000030c0000000400012504000800012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8000600040005000109
                    """)),
                music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap2)

def on_b_pressed():
    global trap2, cd
    if cd >= 5:
        trap2 = sprites.create_projectile_from_sprite(assets.image("""
            myImage1
            """), mySprite, 0, 0)
        cd = 0
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap3(sprite2, otherSprite3):
    global DIalogue, True_Win
    if True_Win >= 1:
        DIalogue = True
        music.play(music.create_song(hex("""
                0078000408040600001c00010a006400f401640000040000000000000000000000000005000004300000000400011d0400080001250c001000012210001400012518001c00012a1c00200001222400280001257c008000011d01001c000f05001202c102c201000405002800000064002800031400060200040c0014001800012a2c003000012505001c000f0a006400f4010a0000040000000000000000000000000000000002060008000c00012506001c00010a006400f401640000040000000000000000000000000000000002180068006c00011b6c007000012070007400011974007800012507001c00020a006400f401640000040000000000000000000000000000000003480034003800011b38003c00011e3c004000012240004400012544004800012948004c00012c4c005000012a50005400012754005800012458005c0001205c006000011d60006400011909010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80013006c006d0001077400750001057c007d00020004
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        game.show_long_text("Hello.", DialogLayout.BOTTOM)
        game.show_long_text("you've done it.", DialogLayout.BOTTOM)
        game.show_long_text("Now... i believe we can talk uninterrupted.",
            DialogLayout.BOTTOM)
        for index in range(5):
            story.show_player_choices("The Monsters",
                "The Slime",
                "Being Chased ",
                "You",
                "Family")
            if story.check_last_answer("The Monsters"):
                game.show_long_text("The monsters are simply previous adventurers that were changed.",
                    DialogLayout.BOTTOM)
                game.show_long_text("I'd presume the slime killed them himself and transformed them.",
                    DialogLayout.BOTTOM)
                game.show_long_text("They never truly die, though. So you didn't murder them.",
                    DialogLayout.BOTTOM)
                game.show_long_text("The one with the eye used light magic, so maybe they're drawn to what they used to harness.",
                    DialogLayout.BOTTOM)
                game.show_long_text("I don't know about the rest though.", DialogLayout.BOTTOM)
                game.show_long_text("Also. the reason i know what happened to her is because...",
                    DialogLayout.BOTTOM)
                spritenew.set_image(assets.image("""
                    talkinghatblush
                    """))
                game.show_long_text("she was... uh.", DialogLayout.BOTTOM)
                game.show_long_text("she was my...", DialogLayout.BOTTOM)
                game.show_long_text("nevermind.", DialogLayout.BOTTOM)
                spritenew.set_image(assets.image("""
                    talkinghat
                    """))
            elif story.check_last_answer("The Slime"):
                game.show_long_text("That slime has already left.", DialogLayout.BOTTOM)
                game.show_long_text("You weren't meant to survive, after all.",
                    DialogLayout.BOTTOM)
                game.show_long_text("He and I once were friends.", DialogLayout.BOTTOM)
                game.show_long_text("I don't fully know what changed him, but I did try to stop him.",
                    DialogLayout.BOTTOM)
                game.show_long_text("He was my only Friend.", DialogLayout.BOTTOM)
            elif story.check_last_answer("Being Chased "):
                game.show_long_text("You mean that monster?", DialogLayout.BOTTOM)
                game.show_long_text("i have no idea.", DialogLayout.BOTTOM)
                game.show_long_text("though if we go on the notion that the monsters are souless...",
                    DialogLayout.BOTTOM)
                game.show_long_text("it could be a culmination of their emotions and spirits.",
                    DialogLayout.BOTTOM)
            elif story.check_last_answer("You"):
                game.show_long_text("I'm just a talking hat.", DialogLayout.BOTTOM)
                game.show_long_text("My name, if you want to know though, is Woodrow.",
                    DialogLayout.BOTTOM)
                game.show_long_text("About my powers...", DialogLayout.BOTTOM)
                game.show_long_text("I am not really that strong.", DialogLayout.BOTTOM)
                game.show_long_text("I didn't even make this place.", DialogLayout.BOTTOM)
                game.show_long_text("I can go invisible though.", DialogLayout.BOTTOM)
            elif story.check_last_answer("Family"):
                game.show_long_text("My... Family?", DialogLayout.BOTTOM)
                game.show_long_text("Well... They're all hats.", DialogLayout.BOTTOM)
                game.show_long_text("Maybe one day you can meet them, but i don't think it's important right now.",
                    DialogLayout.BOTTOM)
        game.show_long_text("Now... Was that all you wanted to hear?",
            DialogLayout.BOTTOM)
        story.show_player_choices("Yes", "No")
        if story.check_last_answer("Yes"):
            game.show_long_text("Very Well.", DialogLayout.BOTTOM)
            game.show_long_text("You may go.", DialogLayout.BOTTOM)
            game.set_game_over_effect(True, effects.none)
            game.set_game_over_message(True, "Finished.")
            game.game_over(True)
        elif story.check_last_answer("No"):
            spritenew.set_image(assets.image("""
                talkinghatuhm
                """))
            game.show_long_text("Well... uh..", DialogLayout.BOTTOM)
            game.show_long_text("i dont know what you'd want now...", DialogLayout.BOTTOM)
            game.show_long_text("but ask away! i guess.", DialogLayout.BOTTOM)
            game.show_long_text("(i wasn't prepared for this)", DialogLayout.TOP)
            story.show_player_choices("Advice", "Hobbies", "Goodbye", "Restart")
            spritenew.set_image(assets.image("""
                talkinghat
                """))
            if story.check_last_answer("Advice"):
                game.show_long_text("I'd say...", DialogLayout.BOTTOM)
                game.show_long_text("Spend time with those you love when you can.",
                    DialogLayout.BOTTOM)
            elif story.check_last_answer("Hobbies"):
                game.show_long_text("Well... I like to read, and Garden", DialogLayout.BOTTOM)
                game.show_long_text("I can grab things without hands, which is how I do that!",
                    DialogLayout.BOTTOM)
            elif story.check_last_answer("Goodbye."):
                mySprite.set_image(assets.image("""
                    talkinghat0
                    """))
                game.show_long_text("Goodbye, Friend!", DialogLayout.BOTTOM)
                game.show_long_text("You can always come back, so don't be shy!",
                    DialogLayout.BOTTOM)
                game.show_long_text("Just whisper my name.", DialogLayout.BOTTOM)
                game.set_game_over_message(True, "The True Ending.")
                game.game_over(True)
            elif story.check_last_answer("Restart"):
                game.show_long_text("You want me to send you back?", DialogLayout.BOTTOM)
                game.show_long_text("I mean... I can do that... but why?", DialogLayout.BOTTOM)
                game.show_long_text("...", DialogLayout.BOTTOM)
                game.show_long_text("do you really want to?", DialogLayout.BOTTOM)
                story.show_player_choices("I do.", "I don't")
                if story.check_last_answer("I do."):
                    True_Win += -1
                    game.set_game_over_message(False, "You may feel a tingle...")
                    game.set_game_over_effect(True, effects.dissolve)
                    game.game_over(False)
                elif story.check_last_answer("I don't."):
                    game.show_long_text("Okay.", DialogLayout.BOTTOM)
                    game.show_long_text("I'm tired, however.", DialogLayout.BOTTOM)
                    game.show_long_text("You can come back another time.", DialogLayout.BOTTOM)
                    game.set_game_over_message(True, "The day's end.")
                    game.game_over(True)
    else:
        music.stop_all_sounds()
        music.play(music.create_song(assets.song("""
                discordance
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        game.show_long_text("hey, I know you don't know me.", DialogLayout.BOTTOM)
        game.show_long_text("you probably never will.", DialogLayout.BOTTOM)
        game.show_long_text("but you can't trust beta fein.", DialogLayout.BOTTOM)
        game.show_long_text("he is the reason the monsters are here.",
            DialogLayout.BOTTOM)
        game.show_long_text("not in the sense that the monsters spawned in his basement over time,",
            DialogLayout.BOTTOM)
        game.show_long_text("but... nevermind.", DialogLayout.BOTTOM)
        game.show_long_text("these monsters are something else.", DialogLayout.BOTTOM)
        game.show_long_text("i can't tell you yet though.", DialogLayout.BOTTOM)
        game.show_long_text("now, i must leave.", DialogLayout.BOTTOM)
        spritenew.say_text("Good Luck.")
        sprites.destroy(spritenew)
        music.stop_all_sounds()
        pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.Npc, on_on_overlap3)

def on_overlap_tile2(sprite3, location2):
    Render.toggle_view_mode()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Teleport1
        """),
    on_overlap_tile2)

def on_a_pressed():
    global projectile, cd
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        light
        """), mySprite, 0, 0)
    cd += 1
    mySprite2.follow(projectile, 100)
    info.change_score_by(-25)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile3(sprite7, location5):
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles13,
    on_overlap_tile3)

def on_overlap_tile4(sprite9, location7):
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles7,
    on_overlap_tile4)

def on_on_overlap4(sprite10, otherSprite32):
    sprites.destroy(sprite10)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    sprites.destroy(otherSprite32)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.projectile, on_on_overlap4)

def on_countdown_end():
    game.set_game_over_message(False, "Out of Time!")
    game.game_over(False)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile5(sprite22, location22):
    global level
    level = 0.5
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        teleport2
        """),
    on_overlap_tile5)

def on_overlap_tile6(sprite8, location6):
    global level
    sprites.destroy(key)
    level = 2
    Caver()
scene.on_overlap_tile(SpriteKind.KEY,
    assets.tile("""
        myTile4
        """),
    on_overlap_tile6)

def on_overlap_tile7(sprite4, location3):
    global win
    win += 1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile7)

def on_on_overlap5(sprite14, otherSprite5):
    music.stop_all_sounds()
    music.play(music.create_song(assets.song("""
            beta fein
            """)),
        music.PlaybackMode.IN_BACKGROUND)
    game.show_long_text("hey its me, beta fein", DialogLayout.BOTTOM)
    game.show_long_text("now, I HOPE you read the controls at the beginning, and yes you can spawn lights with space bar",
        DialogLayout.BOTTOM)
    game.show_long_text("look, some enemies target you, the light, or more behaviors",
        DialogLayout.BOTTOM)
    game.show_long_text("now there's one consistent thing, all traps kill all enemies",
        DialogLayout.BOTTOM)
    game.show_long_text("also you need 5 lights to spawn a trap",
        DialogLayout.BOTTOM)
    game.show_long_text("DO NOT PLACE A LIGHT ON A TRAP, YOU ARE WASTING OUR VALUABLE INVESTORS MONEY!!!!!!!!!!!!!",
        DialogLayout.BOTTOM)
    game.show_long_text("remember now, you will rage a lot... hey wait am i breaking the 4th wall.",
        DialogLayout.BOTTOM)
    game.show_long_text("wait let me get my script!", DialogLayout.BOTTOM)
    game.show_long_text("\"Hello trapper! I hired you to take care of the monsters in my basement\" (dont ask)",
        DialogLayout.BOTTOM)
    game.show_long_text("\"ill pay you well\"", DialogLayout.BOTTOM)
    game.show_long_text("\"here's how to get to the cave: go straight, and go left.",
        DialogLayout.BOTTOM)
    game.show_long_text("\"And then turn left to get to the first level\"",
        DialogLayout.BOTTOM)
    game.show_long_text("\"By the way, you have limited time.\"",
        DialogLayout.BOTTOM)
    music.stop_all_sounds()
    pause(1000)
sprites.on_overlap(SpriteKind.beta, SpriteKind.player, on_on_overlap5)

def on_overlap_tile8(sprite15, location10):
    global level
    level = 1
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles14,
    on_overlap_tile8)

def on_overlap_tile9(sprite13, location9):
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles15,
    on_overlap_tile9)

def on_overlap_tile10(sprite11, location8):
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles11,
    on_overlap_tile10)

def on_on_overlap6(sprite12, otherSprite4):
    global invframes
    if invframes > 0:
        info.set_life(info.life())
    else:
        info.change_life_by(-1)
        music.play(music.create_song(assets.song("""
                lost_life
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        invframes = 3
        for index2 in range(3):
            
            def on_after():
                global invframes
                invframes += -1
            timer.after(1500, on_after)
            
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap6)

def on_life_zero():
    music.play(music.create_song(assets.song("""
            DeathSound
            """)),
        music.PlaybackMode.IN_BACKGROUND)
    if level == 5:
        game.set_game_over_message(False,
            "I want to go home why is this happening this is torture let me out let me out let me out")
        game.game_over(False)
    else:
        if deathtext == 1:
            game.set_game_over_message(False, "lol get better")
        elif deathtext == 2:
            game.set_game_over_message(False, "dont hug them maybe?")
        elif deathtext == 3:
            game.set_game_over_message(False, "beta would NOT be proud.")
        elif deathtext == 4:
            game.set_game_over_message(False, "\"skill issue\"")
        elif deathtext == 5:
            game.set_game_over_message(False, "do not the monsters")
        elif deathtext == 6:
            game.set_game_over_message(False, "L trapper am i right")
        elif deathtext == 7:
            game.set_game_over_message(False, "67 hahaha *dies*")
        elif deathtext == 8:
            game.set_game_over_message(False, "noob vs pro vs MONSTER")
        elif deathtext == 9:
            game.set_game_over_message(False, "my 99 year hardcore world!")
        else:
            game.set_game_over_message(False, ">:(")
        game.game_over(False)
info.on_life_zero(on_life_zero)

def on_overlap_tile11(sprite42, location4):
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles10,
    on_overlap_tile11)

def on_overlap_tile12(sprite32, location32):
    global level
    level = 0.5
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_south,
    on_overlap_tile12)

def on_overlap_tile13(sprite16, location11):
    global level
    level = 0.5
    Caver()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile13)

def Caver():
    global level, spritenew, True_Win, mySprite2, key, enemyizer, mySprite3, mySprite4, a_sprite_in_a_can
    sprites.destroy(projectile)
    level += 1
    if level == 1:
        sprites.destroy(projectile)
    if level == 1.5:
        sprites.destroy(projectile)
        tiles.set_current_tilemap(tilemap("""
            level24
            """))
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        tiles.place_on_random_tile(key, sprites.dungeon.collectible_insignia)
        spritenew = sprites.create(assets.image("""
            talkinghat
            """), SpriteKind.Npc)
        tiles.place_on_random_tile(spritenew, sprites.dungeon.floor_dark_diamond)
        if win == 1:
            if info.score() > 0:
                game.set_game_over_message(True, "you did it.")
                game.set_game_over_effect(True, effects.none)
                pause(5000)
                True_Win += 1
                game.game_over(True)
            else:
                game.show_long_text("you got the money.", DialogLayout.CENTER)
                game.set_game_over_message(True, "beta fein... is gone.")
                game.set_game_over_effect(True, effects.slash)
                pause(5000)
                game.game_over(True)
    # Changed colors to intensify level difficulty.
    if level == 2:
        sprites.destroy(projectile)
        tiles.set_current_tilemap(tilemap("""
            level27
            """))
        music.play(music.create_song(assets.song("""
                New Level
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        mySprite2 = sprites.create(assets.image("""
            monster1
            """), SpriteKind.enemy)
        tiles.place_on_random_tile(mySprite2, sprites.dungeon.floor_light4)
        mySprite2.follow(projectile, 100)
        key = sprites.create(assets.image("""
            greenkey
            """), SpriteKind.KEY)
        tiles.place_on_random_tile(key, sprites.dungeon.floor_dark0)
        enemyizer = 1
        info.start_countdown(30)
        music.play(music.create_song(assets.song("""
                Level1Ambeince
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        game.show_long_text("This monster just follows the light, try to be careful!",
            DialogLayout.CENTER)
    if level == 3:
        sprites.destroy(projectile)
        tiles.set_current_tilemap(tilemap("""
            level29
            """))
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        music.play(music.create_song(assets.song("""
                New Levelslow0
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        mySprite2 = sprites.create(assets.image("""
            monster1
            """), SpriteKind.enemy)
        tiles.place_on_random_tile(mySprite2, sprites.dungeon.floor_dark1)
        mySprite2.follow(projectile, 100)
        mySprite3 = sprites.create(assets.image("""
            monster3
            """), SpriteKind.enemy)
        tiles.place_on_random_tile(mySprite3, sprites.dungeon.floor_light3)
        mySprite3.follow(mySprite, 10)
        key = sprites.create(assets.image("""
                yellowkey - alt
                """),
            SpriteKind.KEY)
        tiles.place_on_random_tile(key, sprites.dungeon.floor_dark1)
        enemyizer = 9
        info.start_countdown(60)
        music.play(music.create_song(assets.song("""
                level2
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        game.show_long_text("This monster is very big, and very slow. Just be aware.",
            DialogLayout.CENTER)
    if level == 4:
        sprites.destroy(projectile)
        tiles.set_current_tilemap(tilemap("""
            level _ no key - grey is small monster purple is big0
            """))
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
        music.play(music.create_song(assets.song("""
                newlevel-slowest
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        mySprite4 = sprites.create(img("""
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
                """),
            SpriteKind.enemy)
        tiles.place_on_random_tile(mySprite4, sprites.swamp.swamp_tile16)
        mySprite4.follow(mySprite, 15)
        mySprite2 = sprites.create(assets.image("""
            monster1
            """), SpriteKind.enemy)
        tiles.place_on_random_tile(mySprite2, sprites.castle.rock2)
        mySprite2.follow(projectile, 100)
        mySprite3 = sprites.create(assets.image("""
            monster3
            """), SpriteKind.enemy)
        tiles.place_on_random_tile(mySprite3, sprites.swamp.swamp_tile9)
        mySprite3.follow(mySprite, 10)
        key = sprites.create(assets.image("""
            eyes
            """), SpriteKind.KEY)
        tiles.place_on_random_tile(key, sprites.builtin.brick)
        info.start_countdown(90)
        enemyizer = 9
        game.show_long_text("This monster splits after death and dissapears. Keep an eye out.",
            DialogLayout.CENTER)
        music.play(music.create_song(assets.song("""
                level 3
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
    if level == 5:
        sprites.destroy(projectile)
        tiles.set_current_tilemap(tilemap("""
            chase level maybe
            """))
        tiles.place_on_random_tile(mySprite, sprites.swamp.swamp_tile9)
        music.play(music.create_song(assets.song("""
                new
                """)),
            music.PlaybackMode.UNTIL_DONE)
        a_sprite_in_a_can = sprites.create(assets.image("""
                a sprite----in a can
                """),
            SpriteKind.enemy)
        tiles.place_on_random_tile(a_sprite_in_a_can, sprites.dungeon.collectible_insignia)
        a_sprite_in_a_can.follow(mySprite, 35)
        enemyizer = 1
        info.start_countdown(666)
        music.play(music.create_song(assets.song("""
                Limbo Lullaby
                """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        game.show_long_text("runrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrunrun",
            DialogLayout.CENTER)

def on_overlap_tile14(sprite17, location12):
    global win
    win += 1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile14)

a_sprite_in_a_can: Sprite = None
invframes = 0
mySprite3: Sprite = None
mySprite6: Sprite = None
mySprite5: Sprite = None
mySprite4: Sprite = None
trap2: Sprite = None
DIalogue = False
mySprite7: Sprite = None
deathtext = 0
cd = 0
forever2 = 0
enemyizer = 0
level = 0
mySprite: Sprite = None
projectile: Sprite = None
key: Sprite = None
mySprite2: Sprite = None
spritenew: Sprite = None
win = 0
True_Win = 0
if True_Win >= 1:
    win = 0
    tiles.set_current_tilemap(tilemap("""
        level33
        """))
    spritenew = sprites.create(assets.image("""
        talkinghat
        """), SpriteKind.Npc)
    tiles.place_on_random_tile(spritenew, assets.tile("""
        myTile2
        """))
else:
    win = 0
    Render.set_view_mode(ViewMode.RAYCASTING_VIEW)
    game.show_long_text("DISCLAIMER: This is a rage game, losing a lot is intentional.",
        DialogLayout.CENTER)
    game.show_long_text("CONTROLS: Z to place light, and go through dialogue.     X to place a trap after using light FIVE times.",
        DialogLayout.CENTER)
    game.show_long_text("And of course, arrow keys or WASD to move.",
        DialogLayout.BOTTOM)
    info.set_score(0)
    info.set_life(3)
    tiles.set_current_tilemap(tilemap("""
        level32
        """))
    Render.move_with_controller(4, 3, 0)
    mySprite2 = sprites.create(assets.image("""
        monster1
        """), SpriteKind.enemy)
    sprites.destroy(mySprite2)
    key = sprites.create(assets.image("""
            yellowkey - alt
            """),
        SpriteKind.KEY)
    sprites.destroy(key)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        light
        """), mySprite, 0, 0)
    sprites.destroy(projectile)
    mySprite = Render.get_render_sprite_variable()
    tiles.place_on_random_tile(mySprite, sprites.dungeon.floor_light0)
    level = 0
    enemyizer = -1
    forever2 = 0
    cd = 0
    sprites.destroy(projectile)
    deathtext = randint(1, 10)
    mySprite7 = sprites.create(assets.image("""
        Beta fein
        """), SpriteKind.beta)
    tiles.place_on_random_tile(mySprite7, sprites.dungeon.purple_outer_south2)
    DIalogue = False
    controller.combos.set_timeout(500)
    music.play(music.create_song(assets.song("""
            Spawn Theme
            """)),
        music.PlaybackMode.UNTIL_DONE)

def on_forever():
    scene.camera_follow_sprite(mySprite)
forever(on_forever)

def on_forever2():
    if level == 5:
        Render.toggle_view_mode()
        music.play(music.create_song(assets.song("""
                mySong
                """)),
            music.PlaybackMode.UNTIL_DONE)
forever(on_forever2)

def on_forever3():
    if DIalogue == False:
        Render.move_with_controller(4, 3, 0)
    elif DIalogue == True:
        Render.move_with_controller(0, 0, 0)
forever(on_forever3)

def on_update_interval():
    global level
    if level > 1.5:
        if enemyizer == 0:
            music.play(music.create_song(assets.song("""
                    mySong0
                    """)),
                music.PlaybackMode.IN_BACKGROUND)
            tiles.set_current_tilemap(tilemap("""
                level8
                """))
            info.stop_countdown()
        if enemyizer == 7:
            music.play(music.create_song(assets.song("""
                    mySong1
                    """)),
                music.PlaybackMode.IN_BACKGROUND)
            tiles.set_current_tilemap(tilemap("""
                level9
                """))
            info.stop_countdown()
        if enemyizer == 4:
            tiles.set_current_tilemap(tilemap("""
                chase level maybe
                """))
            info.stop_countdown()
            game.show_long_text("What???", DialogLayout.BOTTOM)
            level += 1
game.on_update_interval(100, on_update_interval)
