define Kael = Character("Kael", color="#c0a675")

define Brutus = Character("Brutus", color="#8A9EA7")

define Caronte = Character("Caronte", color="#1d232b")

define Leonidas = Character("Leonidas", color="#b90707")

define Musashi = Character("Musashi", color="#589430")

default Rota_guerra = 0
default Rota_morte = 0
default Rota_paz = 0

init python:
         
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

    def decide_cenario(rota1,rota2,rota3):
        if rota1 > rota2 and rota1 > rota3:
            return "bg_cenario_rio_retorno_guerra"
        elif rota2 > rota1 and rota2 > rota3:
            return "bg_cenario_rio_inferno_de_dante"
        elif rota3 > rota1 and rota3 > rota2:
            return "bg_cenario_rio_retorno_paz"
        else:
            return "bg_cenario_rio_escolha"

    def decide_destino(rota1,rota2,rota3):
        if rota1 == rota2 and rota1 > rota3:
            return True
        elif rota1 == rota3 and rota1 > rota2:
            return True
        elif rota2 == rota3 and rota2 > rota1:
            return True
        elif rota1 == rota2 and rota2 == rota3:
            return True        
        else:
            return False

label start:

    scene bg_cenario_de_guerra_inicial with dissolve

    play music "audio/som_guerra.mp3" volume 0.3 fadein 1.0

    Kael "Minha visão está ficando turva... Não consigo enxergar a luz, apenas o carmesim denso que escorre sobre meu rosto."

    show personagem_brutos:
        xalign 1.1
        yalign 1.0
    with easeinright

    Brutus "Rápido!!! Levem-no ao curandeiro agora! Precisamos estancar este sangramento!"

    Kael "Brutus... onde... onde estão os outros?"

    Brutus "Esqueça os outros, maldito seja! Foco em mim! Você está se esvaindo em sangue!"

    Kael "Você não escuta isso? Esse sussurro no ar..."

    Brutus "Do que você está falando?! Não há voz nenhuma!"

    Kael "Ela chama o meu nome... Como um eco vindo do fundo de uma caverna..."

    Brutus "Kael! Fica comigo! Não dê ouvidos ao vazio!"

    Brutus "Kael!!, Não disista!!"

    Kael "Eu sinto muito... A lâmina foi mais funda do que minha vontade..."

    Brutus "KAEL!!!!"
    
    hide personagem_brutos with easeoutright

    stop music fadeout 2.0

    jump rio

label rio:

    scene bg_cenario_rio_neutro with dissolve

    with Dissolve(1.5)

    play music "audio/som_rio.mp3" volume 0.3 fadein 1.0

    "Você desperta sob um céu cinzento. O som ritmado da água colidindo contra a madeira de um barco traz uma estranha calma — o embalo suave que lembra a infância."

    "Contudo, o peito pesa. Um nó de culpa o estrangula por ter deixado o campo de batalha antes da vitória. Ao olhar para a névoa, uma figura alta segura um remo."

    show personagem_caronte at right with easeinright

    Caronte "Alma jovem... o repouso finalmente alcançou seus olhos inquietos?"

    Kael "Quem é você? Que lugar esquecido por Deus é este?"

    Caronte "Eu sou apenas o condutor da madeira sobre o esquecimento. E este lugar... é a margem onde todas as ambições dos homens afundam."

    Kael "A névoa... o silêncio... Eu fui derrotado?"

    Caronte "O rio não julga quem venceu ou quem tombou. Aqui, exércitos viram cinzas e reis perdem suas coroas. Não há ordens para seguir, nem escudos para erguer."

    Kael "Então é isso... Eu morri. Eu não posso ter morrido agora!"

    Caronte "A morte é a única certeza que os vivos fingem não ver. Ela nunca pede licença; apenas cobra a dívida quando o último suspiro se esgota."

    Caronte "Diga-me, soldado... Quando você olha para as águas do fim, o que enxerga?"

    Caronte "É o fim de tudo? Uma batalha que não pode ser vencida? Ou apenas uma outra porta que ainda não aprendeu a abrir?"

    hide personagem_caronte with easeoutright

    menu:
        #"Talvez seja apenas um julgamento":
        "Resposta guerra":

            $ Rota_guerra += 1

            scene bg_cenario_rio_avanco with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "Vejo que o aço ainda ecoa na sua alma. Você busca julgamento porque ainda se sente um prisioneiro da guerra."

        #"Talvez seja apenas meu destino":
        "Resposta morte":
            $ Rota_morte += 1

            scene bg_cenario_rio_avanco with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright
            
            Caronte "A resignação é um manto frio, Kael. Você se entrega ao abismo sem ao menos tentar lutar contra a corrente."

        #"Talvez seja apenas o fim de uma luta.":
        "Resposta paz":
            $ Rota_paz += 1

            scene bg_cenario_rio_avanco with dissolve

            with Dissolve(1.5)
            
            show personagem_caronte at right with easeinright

            Caronte "Buscar o repouso é a sabedoria dos exaustos. Mas desarmar o peito exige mais coragem do que empunhar uma lança."
            



    show personagem_leonidas at left with easeinleft

    Leonidas "Um verdadeiro guerreiro nunca chora pela própria queda! Veja só... mais um rapaz que deixou a lança cair antes da hora."

    Kael "Quem é você? Outra ilusão criada por este inferno?"

    Caronte "Apenas o eco de um rei que mediu o valor do mundo em pilhas de cadáveres e escudos quebrados."

    Leonidas "Medir o mundo? Eu meço o mundo pela HONRA! Caí em Termópilas coberto pelo sangue dos meus inimigos e cercado pelos meus irmãos de armas. Nós nunca recuamos!"

    Kael "Eu lutei por dois anos ininterruptos! Vi meus companheiros serem massacrados na lama! Não venha me falar sobre honra quando tudo o que resta é a podridão!"

    Leonidas "Se a sua causa era justa, o sangue derramado não foi em vão! A morte em combate é o selo imortal da glória. Prefere apodrecer na velhice a tombar como um leão?"

    Caronte "Gloriosa ignorância... Quantos jovens foram devorados pela terra apenas para nutrir o orgulho de reis em tronos de ouro?"

    Caronte "A glória que você prega, Leônidas, é apenas o pranto de viúvas e órfãos soprado pelo vento. Que valor tem uma vitória esculpida em túmulos?"

    Leonidas "O valor da liberdade! De não ajoelhar perante tiranos! O sacrifício é o preço que os fortes pagam pela eternidade!"

    Caronte "Escute o rei dos mortos, Kael... A que custo você acredita que vale a pena entregar a única vida que lhe foi concedida?"

    hide personagem_leonidas with easeoutleft

    hide personagem_caronte with easeoutright

    menu:
        "Resposta guerra":
            $ Rota_guerra += 1

            scene bg_cenario_rio_avanco with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "Você se prende ao fogo da glória... Mas a chama que queima por propósito também consome quem a carrega."

        "Resposta paz":
            $ Rota_paz += 1

            scene bg_cenario_rio_avanco with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "Você enxerga a futilidade do orgulho dos homens. A verdadeira paz começa quando a ambição morre."

        "Resposta morte":
            $ Rota_morte += 1

            scene bg_cenario_rio_avanco with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "Um olhar sombrio e desprovido de esperança. Você contempla o abismo e permite que ele o defina."

    show personagem_musashi at left with easeinleft

    Musashi "Percebe como o aço e o sangue deixam as pessoas cegas? Querem controlar a vida e a morte como se fossem donos do vento."

    Kael "E você... quem é para falar com tanta calma no meio do esquecimento?"

    Caronte "Ele é a lâmina que cortou mil homens apenas para descobrir que o verdadeiro inimigo sempre esteve do lado de dentro."

    Musashi "Cortei corpos, alcancei o topo e olhei para o nada. A espada que mata não traz respostas; ela apenas abre um vazio que sangue nenhum pode preencher."

    Musashi "Você caminha nesta névoa carregando o peso da sua espada quebrada, jovem. Se quer atravessar este rio, precisa primeiro entender o Caminho."

    Kael"Eu só queria defender o que era meu! Mas a guerra devorou tudo..."

    Musashi "A água não luta contra a pedra; ela a contorna e a molda. Quando você aceita o fluxo do universo, não há vitória nem derrota. Há apenas o Ser."

    Caronte "O andarilho fala da fluidez, mas esquece de dizer que, no fim, até o fluxo do rio deságua na imobilidade da morte."

    Musashi "A morte é apenas a espada bainhada. O importante é saber: enquanto sua alma segurava a lâmina, você lutava por ganância ou buscando a verdade?"

    hide personagem_musashi with easeoutleft

    hide personagem_caronte with easeoutright

    menu:
        "Resposta morte":
            $ Rota_morte += 1

            if Rota_morte == 3:
                stop music fadeout 2.0
                jump morte

            scene bg_cenario_rio_escolha with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "A ferramenta se tornou o mestre. Você se esvaziou de humanidade muito antes de entrar no meu barco."

        "Resposta paz":
            $ Rota_paz += 1

            if Rota_paz == 3:
                stop music fadeout 2.0
                jump paz

            scene bg_cenario_rio_escolha with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "Manchar as mãos para manter a luz... O fardo da compaixão costuma ser o mais pesado de carregar."

        "Resposta guerra":
            $ Rota_guerra += 1

            if Rota_guerra == 3:
                stop music fadeout 2.0
                jump guerra

            scene bg_cenario_rio_escolha with dissolve

            with Dissolve(1.5)

            show personagem_caronte at right with easeinright

            Caronte "A determinação dos obstinados. Você se recusa a curvar a espinha, mesmo diante da eternidade."

    #Caronte "A névoa está se dissipando... O destino não é mais um caminho distante, mas a margem que se aproxima."

    #Caronte "Olhe para as águas. Suas escolhas anteriores moldaram o tom deste rio."

    #Kael "Eu sinto como se o próprio ar ao meu redor estivesse mudando... Para onde estamos indo?"

    Caronte "Para o reflexo da sua própria essência. É hora da sua última palavra nesta margem."

    hide personagem_caronte with easeoutright

    menu:
        "Resposta paz":

            $ Rota_paz += 1

            $ cenario_atual = decide_cenario(Rota_guerra, Rota_morte, Rota_paz)
            $ renpy.scene()
            $ renpy.show(cenario_atual)
            with Dissolve(1.5)

            if Rota_paz >= 3:
                stop music fadeout 2.0
                jump paz

            show personagem_caronte at right with easeinright

            if decide_destino(Rota_guerra, Rota_morte, Rota_paz) :
                Caronte "Sua mente vacilou entre o sangue, o descanso e o abismo... Caberá ao próprio rio ditar para onde sua alma será arrastada."
            else:
                Caronte "Sua intenção ecoa com clareza na quietude das águas. Que assim seja."

        "Resposta guerra":

            $ Rota_guerra += 1

            $ cenario_atual = decide_cenario(Rota_guerra, Rota_morte, Rota_paz)
            $ renpy.scene()
            $ renpy.show(cenario_atual)
            with Dissolve(1.5)

            if Rota_guerra >= 3:
                stop music fadeout 2.0
                jump guerra

            show personagem_caronte at right with easeinright

            if decide_destino(Rota_guerra, Rota_morte, Rota_paz) :
                Caronte "Sua mente vacilou entre o sangue, o descanso e o abismo... Caberá ao próprio rio ditar para onde sua alma será arrastada."
            else:
                Caronte "Sua intenção ecoa com clareza na quietude das águas. Que assim seja."

        "Resposta morte":

            $ Rota_morte += 1

            $ cenario_atual = decide_cenario(Rota_guerra, Rota_morte, Rota_paz)
            $ renpy.scene()
            $ renpy.show(cenario_atual)
            with Dissolve(1.5)

            if Rota_morte >= 3:
                stop music fadeout 2.0
                jump morte

            show personagem_caronte at right with easeinright

            if decide_destino(Rota_guerra, Rota_morte, Rota_paz) :
                Caronte "Sua mente vacilou entre o sangue, o descanso e o abismo... Caberá ao próprio rio ditar para onde sua alma será arrastada."
            else:
                Caronte "Sua intenção ecoa com clareza na quietude das águas. Que assim seja."

    $ rota = compara_rota(Rota_guerra,Rota_morte,Rota_paz)   

    jump expression rota

label guerra:

    scene bg_cenario_volta_a_guerra with dissolve

    with Dissolve(1.5)

    play music "audio/som_fogo.mp3" volume 0.3 fadein 1.0

    show personagem_caronte at right with easeinright

    Kael "O ar aqui cheira a enxofre e metal queimado... Eu conheço este lugar. É o calor da batalha me chamando de volta!"

    Caronte "Você escolheu o martelo e a forja. Sua alma não buscou a redenção, mas a eternidade do combate. Retorne ao mundo dos vivos e que sua lâmina nunca conheça o descanso."

    stop music fadeout 2.0
    return

label morte:

    scene bg_cenario_inferno_de_dante with dissolve

    with Dissolve(1.5)

    play music "audio/som_vento.mp3" volume 0.3 fadein 1.0

    show personagem_caronte at right with easeinright

    Kael "O silêncio aqui é absoluto... É tão frio... Não sinto mais meu próprio peito rebater."

    Caronte "Você não combateu a escuridão; abraçou-a. Aqui, sob o sopro do vento esquecido, sua memória se dissolve no abismo das almas que desistiram de existir."

    stop music fadeout 2.0

    return

label paz:

    scene bg_cenario_de_retorno_paz with dissolve

    with Dissolve(1.5)

    play music "audio/som_paz.mp3" volume 0.3 fadein 1.0

    show personagem_caronte at right with easeinright

    Kael "A névoa se abriu... Vejo uma luz dourada tocando os campos além do rio. O fardo da minha espada finalmente sumiu."

    Caronte "Você desarmou o espírito perante o inevitável. Atravesse o vau, Kael. Além destas águas, a guerra é apenas uma lembrança distante."

    stop music fadeout 2.0

    return