define Brutus = Character("Brutus");
define Caronte = Character("Caronte");
define Kael = Character("Kael");
define Leonidas  = Character("Leonidas");
define Musashi  = Character("Musashi");

define Rota_guerra = 0;
define Rota_morte = 0;
#define Rota_paz = 0;

init python:
    def adicao(rota):
        rota = rota += 1;
        
    def compara_rota(rota1,rota2):
        if rota1 > rota2:
            return "guerra";
        elif rota2 > rota1:
            return "morte";
        else:
            return renpy.random.choice(["guerra", "morte"]);
    
    # Sobrecarga da função para o jogo com três finais
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

    Kael "You've created a new Ren'Py game."

    Kael "Once you add a story, pictures, and music, you can release it to the world!"

    return;
