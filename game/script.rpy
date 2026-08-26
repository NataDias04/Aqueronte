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

    Kael "Minha Visão está ficando turva, não consigo enxergar nada, vejo apenas um vermelho forte carmesim que cobre meu rosto"

    show personagem_brutos at right with easeinright

    Brutus "Rápido!!! levem ele ao curandeiro o mais rápido possível, precisamos estancar o sangramento"

    Kael "Brutus, aonde estão os outros?"

    Brutus "Esuqece os outros por enquanto, você tá sangrando muito, a gente precisa parar o sangramento."

    Kael "Você tá escutando isso?"

    Brutus "O que?"

    Kael "Uma voz, é como se ela tivesse me chamando"

    Brutus "Kael!!, fica comigo, Não escute essa voz"

    Brutus "Kael!!, Não disista!!"

    Kael "Eu sinto muito..."

    Brutus "KAEL!!!!"
    
    hide personagem_brutos with easeoutright

    jump rio

label rio:

    scene bg_cenario_rio_neutro

    with Dissolve(1.5)

    #"Você arcoda e escuta um som de aguá batendo contra a madeira, um som reconfortante, faz te lembrar de casa"

    #"Ao mesmo tempo, trás uma angústia, você se sente culpado por não ter completado seu objetivo, você ainda não entende aonde está, derrepnte, você escuta uma voz"

    show personagem_caronte at right with easeinright

    Caronte "Querida criança, já arcodou?"

    Kael "Quem é você? Onde eu estou?"

    Caronte "Eu? sou um apenas um humilde barqueiro, Enquanto o local que estamos, Você está no lugar para onde todos os caminhos acabam levando, Kael."

    Kael "O que?"

    Caronte "Um rio separa o que você foi daquilo que não pode mais ser. Aqui, não existem exércitos. Não existem ordens. Não existem inimigos para matar ou pessoas para proteger."

    Kael "Então estou morto, Eu...Eu não posso está morto"

    Caronte "Mas está"

    Kael "Não posso está morto, eu tenho que voltar"

    Caronte "É curioso, a morte raramente pergunta se estamos prontos para recebe-la. Ela simplismente chega... quando o último instante decide que já foi o suficiente"

    Caronte "O que significa a morte para você?"

    Caronte "É o fim de tudo? Uma batalha que não pode ser vencida? Ou apenas uma outra porta que ainda não aprendeu a abrir?"
         

    hide personagem_caronte with easeoutright

    menu:
        "Talvez seja apenas um julgamento":
            $ Rota_guerra += 1

            scene bg_cenario_rio_avanco

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "Interessante, você pensa como um verdadeiro guerreiro."

        "Talvez seja apenas meu destino":
            $ Rota_morte += 1

            scene bg_cenario_rio_avanco

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright
            
            Caronte "Vejo que você aceitou muito rápido sua situação atual."

        "Talvez seja apenas o fim de uma luta.":
            $ Rota_paz += 1

            scene bg_cenario_rio_avanco

            with Dissolve(1.5)
            
            show personagem_caronte at right with easeinright

            Caronte "Pode ser, ou as vezes, pode ser o começo de outra"
            



    show personagem_leonidas at left with easeinleft

    Leonidas "Vejo que mais um guerreiro foi derrotado"

    Kael "Quem é você, já estou enloquecendo neste lugar"

    Caronte "É apenas uma alma penada, as vezes, certas almas que vagam por este local podem interagir conosco"

    Leonidas "Para você ter chegado aqui tão jovem, deve ter sido péssimo em batalhas"

    Kael "Eu lutei em uma guerra por mais de dois anos, além de ter derrotado diversos inimigos, mas se você está aqui também, seu destino não deve ter sido muito diferente do meu"

    Leonidas "Pelo menos morri com honra, nunca abandonei uma guerra, não importava nosso destino, eu e meus homens nunca desistimos de uma batalha"

    Caronte "Vejo que Leonidas não mudou nada, nunca tem temor a vida e nem aos custos que seus sacrificios terão"

    Leonidas "Como assim?"

    Caronte "Vidas que foram jogadas foras, só para a resolução do conflito dos homens, jovens que vão guerriar sem nem saber o sentido da batalha."

    Caronte "Entes queridos sentem uma grande tristeza no coração enquanto, os com alto poder sentam em suas cadeiras vendo o sangue ser espalhado pelo chão sem mexer um dedo"

    Leonidas "Você diz que meu sacrificio foi em vão?"

    Caronte "Será?, a que custo você acha que vale o sacrificio de uma vida Kael?"

    hide personagem_leonidas with easeoutleft

    hide personagem_caronte with easeoutright

    menu:
        "Escolha 01":
            $ Rota_guerra += 1

            scene bg_cenario_rio_avanco

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

        "Escolha 02":
            $ Rota_paz += 1

            scene bg_cenario_rio_avanco

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

        "Escolah 03":
            $ Rota_morte += 1

            scene bg_cenario_rio_avanco

            with Dissolve(1.5)

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

            scene bg_cenario_rio_escolha

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

            if Rota_morte == 3:
                jump morte

        "Escolha 02":
            $ Rota_paz += 1

            scene bg_cenario_rio_escolha

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

            if Rota_paz == 3:
                jump paz

        "Escolha 03":
            $ Rota_guerra += 1

            scene bg_cenario_rio_escolha

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

            if Rota_guerra == 3:
                jump guerra

    Caronte "dialogo"

    Caronte "dialogo"

    Kael "dialogo"

    Caronte "dialogo"

    hide personagem_caronte with easeoutright

    menu:
        "Escolha 01":
            $ Rota_paz += 1

            scene bg_cenario_rio_retorno_paz

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

            if Rota_paz == 3:
                jump paz

        "Escolha 02":
            $ Rota_guerra += 1

            scene bg_cenario_rio_retorno_guerra

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

            if Rota_guerra == 3:
                jump guerra

        "Escolah 03":
            $ Rota_morte += 1

            scene bg_cenario_rio_inferno_de_dante

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "dialogo"

            if Rota_morte == 3:
                jump morte
                
    $ rota = compara_rota(Rota_guerra,Rota_morte,Rota_paz)   

    jump expression rota

label guerra:

    scene bg_cenario_volta_a_guerra

    with Dissolve(1.5)

    show personagem_caronte at right with easeinright

    Kael "dialogo"

    Caronte "dialogo"

    return

label morte:

    scene bg_cenario_inferno_de_dante

    with Dissolve(1.5)

    show personagem_caronte at right with easeinright

    Kael "dialogo"

    Caronte "dialogo"

    return

label paz:

    scene bg_cenario_de_retorno_paz

    with Dissolve(1.5)

    show personagem_caronte at right with easeinright

    Kael "dialogo"

    Caronte "dialogo"

    return