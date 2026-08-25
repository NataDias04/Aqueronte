define Brutus = Character("Brutus")
define Caronte = Character("Caronte")
define Kael = Character("Kael")
define Leonidas  = Character("Leonidas")
define Musashi  = Character("Musashi")

default Rota_guerra = 0
default Rota_morte = 0
default Rota_paz = 0

init python:
      
    #def compara_rota(rota1,rota2):
        #if rota1 > rota2:
            #return "guerra"
        #elif rota2 > rota1:
            #return "morte"
        #else:
            #return renpy.random.choice(["guerra", "morte"])
    
    def compara_rota(rota1,rota2,rota3):
        if rota1 > rota2 and rota1 > rota3:
            return "guerra"
        elif rota2 > rota1 and rota2 > rota3:
            return "morte"
        elif rota3 > rota1 and rota3 > rota2:
            return "paz"
        elif rota1 == rota2 and rota1 > rota3:
            return renpy.random.choice(["guerra", "morte"])
        elif rota1 == rota3 and rota1 > rota2:
            return renpy.random.choice(["guerra", "paz"])
        elif rota2 == rota3 and rota2 > rota1:
            return renpy.random.choice(["paz", "morte"])
        else:
            return renpy.random.choice(["guerra", "morte", "paz"])

label start:

    scene bg_cenario_de_guerra_inicial

    Kael "dialogo"

    show personagem_brutos at right with easeinright

    Brutus "dialogo"

    hide personagem_brutos with easeoutright

    jump rio

label rio:

    scene bg_cenario_rio_neutro

    show personagem_caronte at right with easeinright

    Caronte "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    hide personagem_caronte with easeoutright

    menu:
        "Escolha 01":
            $ Rota_guerra += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

        "Escolha 02":
            $ Rota_morte += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

        "Escolah 03":
            $ Rota_paz += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

    show personagem_leonidas at left with easeinleft

    Leonidas "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    hide personagem_leonidas with easeoutleft

    hide personagem_caronte with easeoutright

    menu:
        "Escolha 01":
            $ Rota_guerra += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

        "Escolha 02":
            $ Rota_paz += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

        "Escolah 03":
            $ Rota_morte += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

    show personagem_musashi at left with easeinleft

    Musashi "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    hide personagem_musashi with easeoutleft

    hide personagem_caronte with easeoutright

    menu:
        "Escolha 01":
            $ Rota_morte += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

        "Escolha 02":
            $ Rota_paz += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

        "Escolah 03":
            $ Rota_guerra += 1
            show personagem_caronte at right with easeinright
            Caronte "dialogo"

    show personagem_caronte at right with easeinright

    Caronte "dialogo"

    Caronte "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    hide personagem_caronte with easeoutright

    menu:
        "Escolha 01":
            $ Rota_paz += 1
            Caronte "dialogo"
            if Rota_paz == 3:
                jump paz

        "Escolha 02":
            $ Rota_guerra += 1
            Caronte "dialogo"
            if Rota_guerra == 3:
                jump guerra

        "Escolah 03":
            $ Rota_morte += 1
            Caronte "dialogo"
            if Rota_morte == 3:
                jump morte
    $ rota = compara_rota(Rota_guerra,Rota_morte,Rota_paz)   

    jump expression rota

label guerra:

    scene bg_cenario_volta_a_guerra

    show personagem_caronte at right with easeinright

    Kael "dialogo"

    Caronte "dialogo"

    return

label morte:

    scene bg_cenario_inferno_de_dante

    show personagem_caronte at right with easeinright

    Kael "dialogo"

    Caronte "dialogo"

    return

label paz:

    scene bg room

    show personagem_caronte at right with easeinright

    Kael "dialogo"

    Caronte "dialogo"

    return