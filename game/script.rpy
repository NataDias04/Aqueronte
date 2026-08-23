define Brutus = Character("Brutus");
define Caronte = Character("Caronte");
define Kael = Character("Kael");
define Leonidas  = Character("Leonidas");
define Musashi  = Character("Musashi");

default Rota_guerra = 0;
default Rota_morte = 0;
default Rota_paz = 0;

init python:
      
    #def compara_rota(rota1,rota2):
        #if rota1 > rota2:
            #return "guerra";
        #elif rota2 > rota1:
            #return "morte";
        #else:
            #return renpy.random.choice(["guerra", "morte"]);
    
    def compara_rota(rota1,rota2,rota3):
        if rota1 > rota2 and rota1 > rota3:
            return "guerra";
        elif rota2 > rota1 and rota2 > rota3:
            return "morte";
        elif rota3 > rota1 and rota3 > rota2:
            return "paz";
        elif rota1 == rota2 and rota1 > rota3:
            return renpy.random.choice(["guerra", "morte"]);
        elif rota1 == rota3 and rota1 > rota2:
            return renpy.random.choice(["guerra", "paz"]);
        elif rota2 == rota3 and rota2 > rota1:
            return renpy.random.choice(["paz", "morte"]);
        else:
            return renpy.random.choice(["guerra", "morte", "paz"]);

label start:

    scene bg room

    show eileen happy

    Kael "dialogo"

    Brutus "dialogo"

    jump rio;

label rio:

    scene bg room

    show eileen happy

    Caronte "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    menu:
        "Escolha 01":
            $ Rota_guerra += 1
            Caronte "dialogo"

        "Escolha 02":
            $ Rota_morte += 1
            Caronte "dialogo"

        "Escolah 03":
            $ Rota_paz += 1
            Caronte "dialogo"

    show eileen happy

    Leonidas "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    menu:
        "Escolha 01":
            $ Rota_guerra += 1
            Caronte "dialogo"

        "Escolha 02":
            $ Rota_paz += 1
            Caronte "dialogo"

        "Escolah 03":
            $ Rota_morte += 1
            Caronte "dialogo"

    show eileen happy

    Musashi "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    menu:
        "Escolha 01":
            $ Rota_morte += 1
            Caronte "dialogo"

        "Escolha 02":
            $ Rota_paz += 1
            Caronte "dialogo"

        "Escolah 03":
            $ Rota_guerra += 1
            Caronte "dialogo"

    show eileen happy

    Caronte "dialogo"

    Caronte "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    menu:
        "Escolha 01":
            $ Rota_paz += 1
            Caronte "dialogo"
            if Rota_paz == 3:
                jump paz;

        "Escolha 02":
            $ Rota_guerra += 1
            Caronte "dialogo"
            if Rota_guerra == 3:
                jump guerra;

        "Escolah 03":
            $ Rota_morte += 1
            Caronte "dialogo"
            if Rota_morte == 3:
                jump morte;
    $ rota = compara_rota(Rota_guerra,Rota_morte,Rota_paz);     

    jump expression rota;

label guerra:

    scene bg room

    show eileen happy

    Kael "dialogo"

    Caronte "dialogo"

    return;

label morte:

    scene bg room

    show eileen happy

    Kael "dialogo"

    Caronte "dialogo"

    return;

label paz:

    scene bg room

    show eileen happy

    Kael "dialogo"

    Caronte "dialogo"

    return;