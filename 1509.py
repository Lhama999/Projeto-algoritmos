import pyxel
import random
def seta(x,y,clr):
 pyxel.line(x,y+2,x+2,y+5,0)
 pyxel.line(x,y+2,x+2,y-1,0)
class inimigo:
 def __init__(self,nome,HP,DEF,ATK,DECK):
  self.nome=nome
  self.HP=HP
  self.hp_max=HP
  self.DEF=DEF
  self.ATK=ATK
  self.DECK=DECK
  self.vivo=1
class agrupar:
 def __init__(self,nome,carta1,carta2):
  self.nome=nome
  self.carta1=carta1
  self.carta2=carta2
class habilidade:
 def __init__(self,numero,nome):
  self.nome=nome
  self.num=numero
class inimigo_atk:
 def __init__(self,alvo,dano,escudo,efeitoA,chanceA,stacksA,duracaoA,efeitoB,chanceB,stacksB,duracaoB,stat,tags):
  self.alvo=alvo
  self.dano=dano
  self.escudo=escudo
  self.efeitoA=efeitoA
  self.chanceA=chanceA
  self.stacksA=stacksA
  self.duracaoA=duracaoA
  self.efeitoB=efeitoB
  self.chanceB=chanceB
  self.stacksB=stacksB
  self.duracaoB=duracaoB
  self.stat=stat
  self.tags=tags
class combinacao:
 def __init__(self,nome,alvo,dano,escudo,efeitoA,chanceA,stacksA,duracaoA,efeitoB,chanceB,stacksB,duracaoB,stat,tags):
  self.nome=nome
  self.alvo=alvo
  self.dano=dano
  self.escudo=escudo
  self.efeitoA=efeitoA
  self.chanceA=chanceA
  self.stacksA=stacksA
  self.duracaoA=duracaoA
  self.efeitoB=efeitoB
  self.chanceB=chanceB
  self.stacksB=stacksB
  self.duracaoB=duracaoB
  self.stat=stat
  self.tags=tags
class arma:
 def __init__(self,cartas):
  self.cartas=cartas
  self.premium=0
class item:
 def __init__(self,preco,imagem):
  self.preco=preco
  self.imagem=imagem
  self.obtido=0
class jogo:
 def __init__(self):
  pyxel.init(640,480,fps=120,title="AAAAAAAHH")
  self.state="menu"
  self.opcao=1
  self.opcao_menu=1
  self.room=0
  self.x=60
  self.hp_max=100
  self.hp=self.hp_max
  self.atk_base=10
  self.def_base=10
  self.sala1=0
  self.sala2=0
  self.sala3=0
  self.max_carta=6
  self.max_jogavel=2
  self.armas=[espada,escudo,varinha,e_luz]
  self.baralho=[]
  self.turno=0
  pyxel.run(self.update,self.draw)
 def enter_loja(self):
  self.room="loja"
  self.produtos=[]
  while len(self.produtos)<6:
   self.aleatorio_a=random.randint(1,15)
   self.produtos.append(self.aleatorio_a)
 def enter_evento(self):
  self.room="evento"
  self.aleatorio_a=random.randint(1,20)
  self.evento=self.aleatorio_a
  self.opcao=0
 def iniciar_turno(self):
  self.a_opcao=0
  self.opcao=0
  self.usando=[]
  self.turno="aliado"
  self.baralho=[]
  self.mao_real=[]
  self.mao=[]
  self.l_alvos=[]
  for i in self.armas:
   for h in i.cartas:
    self.baralho.append(h)
  while len(self.mao_real)<self.max_carta:
   self.aleatorio_i=random.randint(1,len(self.baralho))
   self.aleatorio_i=self.aleatorio_i-1
   self.mao_real.append(self.baralho[self.aleatorio_i])
  for i in self.mao_real:
   self.mao.append(i)
 def enter_elite_battle(self):
  self.room="batalha"
  self.iniciar_turno()
  self.enemy=[]
  self.aleatorio_a=random.randint(0,1)
  if self.aleatorio_a==0:
   self.aleatorio_b=random.randint(0,3)
   self.inimigoA=inimigo_elite[self.aleatorio_b]
   self.aleatorio_b=random.randint(0,3)
   self.inimigoB=inimigo_elite[self.aleatorio_b]
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
  else:
   self.aleatorio_a=random.randint(0,4)
   self.inimigoA=inimigo[self.aleatorio_a]
   self.aleatorio_b=random.randint(0,3)
   self.inimigoB=inimigo_elite[self.aleatorio_b]
   self.aleatorio_a=random.randint(0,4)
   self.inimigoC=inimigo[self.aleatorio_a]
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
   self.enemy.append(self.inimigoC)
 def enter_battle(self):
  self.iniciar_turno()
  self.enemy=[]
  self.room="batalha"
  self.aleatorio_a=random.randint(0,1)
  if self.aleatorio_a==1:
   self.aleatorio_a=random.randint(0,4)
   self.inimigoA=inimigo[self.aleatorio_a]
   self.aleatorio_a=random.randint(0,4)
   self.inimigoB=inimigo[self.aleatorio_a]
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
  else:
   self.aleatorio_a=random.randint(0,4)
   self.inimigoA=inimigo[self.aleatorio_a]
   self.aleatorio_a=random.randint(0,4)
   self.inimigoB=inimigo[self.aleatorio_a]
   self.aleatorio_a=random.randint(0,4)
   self.inimigoC=inimigo[self.aleatorio_a]
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
   self.enemy.append(self.inimigoC)
 def enter_map(self):#0.vazio 1.batalha,2.evento,3.loja,4.batalha elite, 5.aleatorio
  self.vazio=0
  self.opcao=0
  self.sala1=random.randint(0,5)
  if self.sala1==0:
   self.vazio=1
  if self.vazio==1:
   self.sala2=random.randint(1,5)
  else:
   self.sala2=random.randint(0,5)
  if self.sala2==0:
   self.vazio=1
  self.sala3=random.randint(0,5)
  if self.vazio==1:
   self.sala3=random.randint(1,5)
 def update(self):
  self.ret=0
  if pyxel.btnp(pyxel.KEY_U):#tirar depois do teste    
   self.state=="jogo"
   self.enter_elite_battle()
  if pyxel.btnp(pyxel.KEY_O):#A
   self.state=="jogo"
   self.enter_battle()
  if pyxel.btnp(pyxel.KEY_KP_ENTER):
   if self.state!=("menu" or "menu_jogo"):
    self.state="menu_jogo"
    self.opcao_menu=1
   if self.state=="menu_jogo":
    self.state=="jogo"
  if self.state=="menu":
   if self.opcao_menu<3 and pyxel.btnp(pyxel.KEY_S):
    self.opcao_menu=self.opcao_menu+1
   elif self.opcao_menu==3 and pyxel.btnp(pyxel.KEY_S):
    self.opcao_menu=1
   if self.opcao_menu>1 and pyxel.btnp(pyxel.KEY_W):
    self.opcao_menu=self.opcao_menu-1
   elif self.opcao_menu==1 and pyxel.btnp(pyxel.KEY_W):
    self.opcao_menu=3
   if pyxel.btnp(pyxel.KEY_RETURN):
    if self.opcao_menu==1:
     self.state="jogo"
     self.room="mapa"
     self.enter_map()
    if self.opcao_menu==2:
     self.state="opcoes"
    if self.opcao_menu==3:
     pyxel.quit()
  if self.state=="menu_jogo":
   if self.opcao_menu<3 and pyxel.btnp(pyxel.KEY_S):
    self.opcao_menu=self.opcao_menu+1
   elif self.opcao_menu==3 and pyxel.btnp(pyxel.KEY_S):
    self.opcao_menu=1
   if self.opcao_menu>1 and pyxel.btnp(pyxel.KEY_W):
    self.opcao_menu=self.opcao_menu-1
   elif self.opcao_menu==1 and pyxel.btnp(pyxel.KEY_W):
    self.opcao_menu=3
   if pyxel.btnp(pyxel.KEY_RETURN):
    if self.opcao_menu==1:
     self.state="jogo"
     self.ret=1
    if self.opcao_menu==2:
     self.state="menu"
    if self.opcao_menu==3:
     pyxel.quit()
  if self.state=="jogo":#jogo começa aqui
   if self.room=="mapa":
    if self.opcao==0:
     self.mostrar=0
    if self.opcao==1:
     self.mostrar=self.sala1
    if self.opcao==2:
     self.mostrar=self.sala2
    if self.opcao==3:
     self.mostrar=self.sala3
    if pyxel.btnp(pyxel.KEY_Q):
     self.opcao=1
    if pyxel.btnp(pyxel.KEY_W):
     self.opcao=2
    if pyxel.btnp(pyxel.KEY_E):
     self.opcao=3
    if pyxel.btnp(pyxel.KEY_S):
     self.opcao=0
    if pyxel.btnp(pyxel.KEY_RETURN) and self.ret==0:#sinalizador para n repetir enter
     self.ret=1
     if self.mostrar==1:
      self.enter_battle()
     if self.mostrar==2:
      self.enter_evento()
     if self.mostrar==3:
      self.enter_loja()
     if self.mostrar==4:
      self.enter_elite_battle()
     if self.mostrar==5:
      self.aleatorio_a=random.randint(1,4)
      if self.aleatorio_a==1:
       self.enter_battle()
      if self.aleatorio_a==2:
       self.enter_evento()
      if self.aleatorio_a==3:
       self.enter_loja()
      if self.aleatorio_a==4:
       self.enter_elite_battle()
   if self.room=="batalha":
    if self.turno=="aliado":
     if len(self.enemy)==2:
      if pyxel.btnp(pyxel.KEY_Q):
       if self.a_opcao==0:
        if self.inimigoB.vivo==1:
         self.a_opcao=1
       elif self.inimigoA.vivo==1:
        self.a_opcao=0     
      if pyxel.btnp(pyxel.KEY_E):
       if self.a_opcao==0:
        if self.inimigoB.vivo==1:
         self.a_opcao=1
       elif self.inimigoA.vivo==1:
        self.a_opcao=0
     if pyxel.btnp(pyxel.KEY_Q):
      if len(self.enemy)==3:
       if self.a_opcao==0:
        if self.inimigoC.vivo==1:
         self.a_opcao=2
        elif  self.inimigoB.vivo==1:
         self.a_opcao=1
       elif self.a_opcao==1:
        if self.inimigoA.vivo==1:
         self.a_opcao=0
        elif  self.inimigoC.vivo==1:
         self.a_opcao=2
       elif self.a_opcao==2:
        if self.inimigoB.vivo==1:
         self.a_opcao=1
     if pyxel.btnp(pyxel.KEY_E):
      if len(self.enemy)==3:
       if self.a_opcao==0:
        if self.inimigoB.vivo==1:
         self.a_opcao=1
        elif  self.inimigoC.vivo==1:
         self.a_opcao=2
       elif self.a_opcao==1:
        if self.inimigoC.vivo==1:
         self.a_opcao=2
        elif  self.inimigoA.vivo==1:
         self.a_opcao=0
       elif self.a_opcao==2:
        if self.inimigoA.vivo==1:
         self.a_opcao=0
        elif  self.inimigoB.vivo==1:
         self.a_opcao=1
     self.opcao_max=len(self.mao)-1
     if pyxel.btnp(pyxel.KEY_A):
      if self.opcao>0:
       self.opcao=self.opcao-1
      else:
       self.opcao=self.opcao_max
     if pyxel.btnp(pyxel.KEY_D):
      if self.opcao<self.opcao_max:
       self.opcao=self.opcao+1
      else:
       self.opcao=0
     if pyxel.btnp(pyxel.KEY_W):
      if len(self.mao)>0 and len(self.usando)<(self.max_jogavel*2):
       self.usando.append(self.mao[self.opcao])
       del self.mao[self.opcao]
       self.l_alvos.append(self.a_opcao)
       self.opcao=0
       self.ret=1
     if pyxel.btnp(pyxel.KEY_S):
      self.mao=[]
      self.usando=[]
      self.l_alvos=[]
      for i in self.mao_real:
       self.mao.append(i)
     #if pyxel.btnp(pyxel.KEY_RETURN):
      #if self.ret==0:
       #self.ret=1
       #self.terminar_turno()
 def draw(self):#draw
  if self.state=="menu":
   pyxel.cls(3)
   pyxel.text(20,50,"JOGAR",0)
   pyxel.text(20,60,"DECK",0)
   pyxel.text(20,70,"SAIR",0)
   if self.opcao_menu==1:
    seta(50,50,0)
   if self.opcao_menu==2:
    seta(50,60,0)
   if self.opcao_menu==3:
    seta(50,70,0)
  if self.state=="opcoes":
   pyxel.cls(9)
  if self.state=="menu_jogo":
   pyxel.cls(3)
   pyxel.text(10,50,"CONTINUAR",0)
   pyxel.text(10,60,"REINICIAR",0)
   pyxel.text(20,70,"SAIR",0)
   if self.opcao_menu==1:
    seta(50,50,0)
   if self.opcao_menu==2:
    seta(50,60,0)
   if self.opcao_menu==3:
    seta(50,70,0)
  if self.state=="jogo":
   if self.room=="mapa":
    pyxel.cls(1)
    self.num=str(self.mostrar)#tirar no futuro
    pyxel.text(20,50,self.num,0)
    if self.opcao==1:
     pyxel.tri(40,360,170,360,105,100,16)
     pyxel.elli(40,340,130,40,5)
     self.x=105
     self.y=270
     self.mostrar=self.sala1
    if self.opcao==2:
     pyxel.tri(210,360,340,360,270,100,16)
     pyxel.elli(210,340,130,40,5)
     self.x=270
     self.y=270
     self.mostrar=self.sala2
    if self.opcao==3:
     pyxel.tri(380,360,510,360,440,100,16)
     pyxel.elli(380,340,130,40,5)
     self.x=440
     self.y=270
     self.mostrar=self.sala3
    if self.opcao==0:
     self.mostrar=-1
    if self.opcao!=0:
     if self.mostrar==0:
      pyxel.circ(self.x,self.y,5,1)
     if self.mostrar==1:
      pyxel.circ(self.x,self.y,5,2)
     if self.mostrar==2:
      pyxel.circ(self.x,self.y,5,3)
     if self.mostrar==3:
      pyxel.circ(self.x,self.y,5,4)
     if self.mostrar==4:
      pyxel.circ(self.x,self.y,5,5)
     if self.mostrar==5:
      pyxel.circ(self.x,self.y,5,6)
   if self.room=="batalha": #batalhas
    pyxel.cls(2)
    if len(self.enemy)==2:
     pyxel.text(200,150,self.inimigoA.nome,0)
     pyxel.text(375,150,self.inimigoB.nome,0)
    if len(self.enemy)==3:
     pyxel.text(100,150,self.inimigoA.nome,0)
     pyxel.text(250,150,self.inimigoB.nome,0)
     pyxel.text(400,150,self.inimigoC.nome,0)
    if self.turno=="aliado":
     if len(self.enemy)==2:
      if self.a_opcao==0:
       pyxel.text(200,150,self.inimigoA.nome,16)
      if self.a_opcao==1:
       pyxel.text(375,150,self.inimigoB.nome,16)
     if len(self.enemy)==3:
      if self.a_opcao==0:
       pyxel.text(100,150,self.inimigoA.nome,16)      
      if self.a_opcao==1:
       pyxel.text(250,150,self.inimigoB.nome,17)
      if self.a_opcao==2:
       pyxel.text(400,150,self.inimigoC.nome,16)
     self.usando_comb=[]
     if len(self.usando)>0:
      self.max_carta=len(self.usando)
      self.carta_x=0
      self.carta_y=1
      while self.carta_x<self.max_carta:
       if self.carta_x+1>=self.max_carta:
        self.usando_comb.append(individuais[self.usando[self.carta_x].num])
        self.carta_x=self.carta_x+1
       else:
        self.usando_comb.append(lista_ataque[self.usando[self.carta_x].num][self.usando[self.carta_y].num])
        self.carta_x=self.carta_x+2
        self.carta_y=self.carta_x+1
     if len(self.usando_comb)>0:
      self.x=150
      for i in self.usando_comb:
       pyxel.text(self.x,250,i.nome,0)
       self.x=self.x+50
     if self.ret==0:
      if len(self.mao)>4:
       self.i=self.mao[self.opcao].nome
       if self.opcao-1==-1:
        self.e=self.mao[self.opcao_max].nome
       else:
        self.e=self.mao[self.opcao-1].nome
       if self.opcao-2==-2:
        self.a=self.mao[self.opcao_max-1].nome
       elif self.opcao-2==-1:
        self.a=self.mao[self.opcao_max].nome
       else:
        self.a=self.mao[self.opcao-2].nome#continua aqui
       if self.opcao+1==self.opcao_max+1:
        self.o=self.mao[0].nome
       else:
        self.o=self.mao[self.opcao+1].nome
       if self.opcao+2==self.opcao_max+2:
        self.u=self.mao[1].nome
       elif self.opcao+2==self.opcao_max+1:
        self.u=self.mao[0].nome
       else:
        self.u=self.mao[self.opcao+2].nome
       pyxel.text(200,390,self.a,17)
       pyxel.text(250,390,self.e,17)
       pyxel.text(300,390,self.i,17)
       pyxel.text(350,390,self.o,17)
       pyxel.text(400,390,self.u,17)
      else:
       self.x=200
       self.y=0
       for i in self.mao:
        if self.y==self.opcao:
         pyxel.text(self.x,375,i.nome,0)
        else:
         pyxel.text(self.x,390,i.nome,17)
        self.x=self.x+50
        self.y=self.y+1
   if self.room=="evento":
    pyxel.cls(3)
   if self.room=="loja":
    pyxel.cls(4)
corte=habilidade(0,"corte")
grito=habilidade(1,"grito")
bloquear=habilidade(2,"bloquear")
surrar=habilidade(3,"surrar")
encanto=habilidade(4,"encanto")
missil=habilidade(5,"missil")
jato=habilidade(6,"jato")
encharcar=(7,"encharcar")
luz=habilidade(8,"luz")
envenenar=habilidade(9,"veneno")
pedra=(10,"pedra")
fungo=(11,"fungos")
espada=arma([corte,grito])
escudo=arma([bloquear,surrar])
varinha=arma([encanto,missil])
jato_D_agua=arma([jato,encharcar])
e_luz=arma([luz])
e_veneno=arma([envenenar])
e_pedra=arma([pedra])
e_fungos=arma([fungo])
#efeito:0 nada, 1 veneno,2 petrificar-40% de buffs errarem, 3 cegueira-40% de atks errarem, 4 stun, 5 colecao de esporos(atk-,atk+,def-, def+,ap+,ap-,esquiva,remover1buff,remover1debuff,veneno,eco,fortalecer,esporos,corrupcao), 6 atack up, 7 def up, 8 atk down, 9 def down, A ap+(6max), B parasitar, C esquiva, D conjunto de buffs(atk,def,esquiva,ap+(6max)), E repetir, 10 dano extra, 11 colecao de debuffs(,atk-,def-,ap-,descuido), 12 duplicar debuffs,13 esporos, 14 purificar. 15 endurecer, 16 roubo de hp, 17 fortalecer-30% dano recebido, 18 ativar dot, 19 remover duracao, 1A corruption- 1.5 dano de dot, 1B transferencia de efeitos, 1C propagar-"30% da carta ter efeitos dobrados", 1D parasitar- 1 escudo ao ativar veneno, 1E imunidade, 20 toxicidade, 21 hype- repete uma carta aleatória no final do turno,22 parry- bloqueia 1 dano,23espinho-24reflete 30% do dano,25respingar,26 fortificar-50% mais escudo,27 intimidar-20% de chance de stun por ataque, 28 enviar efeitos negativos,29-remover buffs,2A endurecer-atk+50%def,def+50%atk,2B remove% de escudo,2C comparilha dano recebido 25%,2D atrai dano dos outros 25%, 2E lança 1 soco pr stack ao final do turno, 30-solidificar-- aumenta o dano dos socos em 2x, 31 raiva- aumenta dano dado e recebido em 1.5x,32-sabotagem- aplica 1 colecao de debuffs por atk
corte2=combinacao("corte","1",60,0,0,0,0,0,0,0,0,0,"atk",["atk"])
grito2=combinacao("grito","self",0,0,"6",100,3,2,0,0,0,0,"atk",["buff"])
destruir=combinacao("destruir","todos_E",75,0,0,0,0,0,0,0,0,0,"atk",["atk"])
esmagar=combinacao("esmagar","1",75,0,0,0,0,0,0,0,0,0,"escudo",["atk"])
bloquear2=combinacao("bloquear","self",0,15,0,0,0,0,0,0,0,0,"def",["buff"])
surrar2=combinacao("surrar","1",25,0,"4",75,1,1,0,0,0,0,"def",["debuff","atk"])
encanto2=combinacao("encanto","self",0,0,"D",100,3,2,0,0,0,0,"atk",["buff"])
missil2=combinacao("missil","1",15,0,"E",100,2,4,0,0,0,0,"atk",["atk"])
barragem=combinacao("barragem","aleatorio",15,0,"E",100,1,5,"D",80,1,2,"atk",["buff","atk"])
jato2=combinacao("jato","1",10,0,"10",100,10,1,0,0,0,0,"atk",["atk"])
encharcar2=combinacao("encharcar","1",0,0,11,100,3,2,0,0,0,0,"atk",["debuff"])
imundar=combinacao("imundar",1,0,0,12,100,1,1,0,0,0,0,"atk",["debuff"])
envenenar2=combinacao("envenenar",1,0,0,1,100,3,3,0,0,0,0,"atk",["debuff"])
luz2=combinacao("purificar","self",0,0,14,100,3,1,0,0,0,0,"atk",["buff"])
pedra2=combinacao("endurecer","self",0,5,15,100,2,1,0,0,0,0,"def",["buff"])
fungos2=combinacao("felicidade","todos",0,0,5,100,2,2,13,100,1,1,"atk",["buff","debuff"])
consumir=combinacao("consumir","1",50,0,16,70,1,1,0,0,0,0,"atk+def/2",["atk","buff"])
fortalecer=combinacao("fortalecer","self",0,25,17,100,1,2,0,0,0,0,"atk",["buff"])
ativador=combinacao("ativador","1",0,0,18,100,2,1,19,100,1,1,"atk",["debuff"])
corromper=combinacao("corromper","1",0,0,"1A",100,1,2,0,0,0,0,"atk",["debuff"])
curse=combinacao("amaldicoar","1",0,0,"1B",100,"random",1,0,0,0,0,"atk",["debuff"])
propagar=combinacao("propagar","self",0,0,"1C",100,1,2,0,0,0,0,"atk",["buff"])
cegar=combinacao("cegar","1",0,0,"3",100,1,2,0,0,0,0,"atk",["debuff"])
parasitar=combinacao("parasitar","self",0,0,"1D",100,1,2,0,0,0,0,"def",["buff"])
bencao=combinacao("bencao","todos_E",0,0,"29",100,2,1,0,0,0,0,"atk",["debuff"])
toxicidade=combinacao("toxicidade","self","20",0,0,100,1,2,0,0,0,0,"atk",["buff"])
meteoritos=combinacao("meteoritos","random",10,0,"E",100,1,3,"4",60,1,1,"def",["atk","debuff"])
animar=combinacao("animar","self",0,0,"21",100,1,2,0,0,0,0,"atk",["buff"])
chuva=combinacao("chuva toxica","random",5,0,"E",100,1,4,"1",100,1,2,"atk",["atk","debuff"])
barreira=combinacao("barreira","self",0,0,"22",100,1,1,0,0,0,0,"def",["buff"])
expurgo=combinacao("expurgo","1",40,0,"18",100,1,0,0,0,0,0,"atk",["atk","debuff"])
cobertura=combinacao("cobertuta","self",0,5,"23",100,1,2,0,0,0,0,"def",["buff"])
respingo=combinacao("respingo","self",0,"5","25",100,1,2,0,0,0,0,"def",["buff"])
fortificar=combinacao("fortificar","self",0,5,"26",100,1,2,0,0,0,0,"def",["buff"])
intimidar=combinacao("intimidar","self",0,0,"27",100,1,2,0,0,0,0,"atk",["buff"])
raios=combinacao("raios","1",1,0,"E",100,1,4,"10",100,5,1,"atk",["atk"])
transferencia=combinacao("transferencia","1",20,0,"28",100,2,1,0,0,0,0,"atk",["atk","buff","debuff"])
rebater=combinacao("rebater","1",50,0,"28",100,1,1,0,0,0,0,"atk",["atk","buff","debuff"])
converter=combinacao("converter","self",0,12,"14",75,2,1,0,0,0,0,"def",["buff"])
impenetravel=combinacao("impenetravel","self",0,0,"1E",100,1,2,0,0,0,0,"def",["buff"])
estrela=combinacao("estrelas cadentes","random",5,0,"E",100,1,3,"29",100,1,1,"atk",["atk","debuff"])
pressao=combinacao("alta pressao","1",7,0,"10",100,7,1,0,0,0,0,"def",["atk"])
pedrada=combinacao("pedrada","1",40,0,4,100,1,1,0,0,0,0,"def",["atk","debuff"])
petrificar=combinacao("petrificar","1",0,0,"3",100,1,2,0,0,0,0,"atk",["debuff"])
endurecer=combinacao("endurecer","self",0,0,"2A",100,1,2,0,0,0,0,"atk",["buff"])
quebrar=combinacao("quebrar","1",40,0,"2B",100,50,1,0,0,0,0,"atk",["atk"])
corroer=combinacao("corroer","1",0,0,"2B",100,75,1,0,0,0,0,"atk",["atk"])
metralhar=combinacao("metralhar","random",0,0,"E",100,2,5,"11",100,1,2,"atk",["debuff"])
tremor=combinacao("tremor","todos_E",30,0,0,0,0,0,0,0,0,0,"atk+def/2",["atk"])
granizo=combinacao("granizo","random",0,0,"E",100,2,7,"2B",100,10,1,"atk",["atk"])
compartilhar=combinacao("compartilhar","1",0,0,"2D",100,1,2,0,0,0,0,"atk",["debuff"])
receptor=combinacao("receptor","1",0,0,"2C",100,1,2,0,0,0,0,"atk",["debuff"])
pesado=combinacao("tiro pesado","1",30,0,"E",100,1,3,0,0,0,0,"atk",["atk"])
esplosao=combinacao("esplosao","todos",5,0,"10",100,5,1,0,0,0,0,"atk",["atk"])
parede=combinacao("parede","self",0,7,"E",100,1,3,0,0,0,0,"atk",["buff"])
eco=combinacao("eco","self",0,0,"2E",100,1,2,0,0,0,0,"atk",["buff"])
solidificar=combinacao("solidificar","self",0,0,"30",100,1,2,0,0,0,0,"atk",["buff"])
raiva=combinacao("raiva","self",0,0,"31",100,1,2,0,0,0,0,"atk",["buff"])
apedrejar=combinacao("apedrejar","1",10,0,"E",100,1,4,0,0,0,0,"escudo",["atk"])
refletir=combinacao("refletir","self",0,7,0,0,0,0,0,0,0,0,"atk",["buff"])
sabotar=combinacao("sabotar","self",0,0,"32",100,1,1,0,0,0,0,"atk",["buff"])
bolha=combinacao("bolha","self",0,7,0,0,0,0,0,0,0,0,"atk",["buff"])
recochete=combinacao("recochete","self",0,0,"2E",100,1,2,0,0,0,0,"atk",["buff"])
acolher=combinacao("acolher","self",0,0,14,100,3,1,0,0,0,0,"atk",["buff"])
corte_s=combinacao("corte","1",20,0,0,0,0,0,0,0,0,0,"atk",["atk"])
grito_s=combinacao("grito","self",0,0,"6",70,1,2,0,0,0,0,"atk",["buff"])
bloquear_s=combinacao("bloquear","self",0,5,0,0,0,0,0,0,0,0,"def",["buff"])
surrar_s=combinacao("surrar","1",10,0,"4",20,1,1,0,0,0,0,"def",["debuff","atk"])
encanto_s=combinacao("encanto","self",0,0,"D",100,1,2,0,0,0,0,"atk",["buff"])
missil_s=combinacao("missil","1",15,0,"E",100,1,2,0,0,0,0,"atk",["atk"])
jato_s=combinacao("jato","1",3,0,"10",100,3,1,0,0,0,0,"atk",["atk"])
encharcar_s=combinacao("encharcar","1",0,0,11,100,1,2,0,0,0,0,"atk",["debuff"])
veneno_s=combinacao("veneno","1",0,0,1,100,1,3,0,0,0,0,"atk",["debuff"])
luz_s=combinacao("luz","self",0,0,14,100,1,1,0,0,0,0,"atk",["buff"])
pedra_s=combinacao("pedra","self",0,00,15,50,2,1,0,0,0,0,"def",["buff"])
fungos_s=combinacao("fungo","todos",0,0,5,100,1,2,0,0,0,0,"atk",["buff","debuff"])
#ataque monstros
fada1=inimigo_atk("aliados_t",0,0,"D",100,1,2,0,0,0,0,"atk",["buff"])
fada2=inimigo_atk("1",15,0,"E",100,2,4,0,0,0,0,"atk",["atk"])
golem1=inimigo_atk("self",0,15,0,0,0,0,0,0,0,0,"def",["buff"])
golem2=inimigo_atk("1",60,0,0,0,0,0,0,0,0,0,"atk",["atk"])
cogumelo1=inimigo_atk("todos",0,0,5,100,2,2,13,100,1,1,"atk",["buff","debuff"])
cogumelo2=inimigo_atk("1",0,0,"13",100,1,1,0,0,0,0,"atk",["debuff"])
morcego1=inimigo_atk("1",0,0,"3",100,1,2,0,0,0,0,"atk",["debuff"])
morcego2=inimigo_atk("1",60,0,0,0,0,0,0,0,0,0,"atk",["atk"])
slime1=inimigo_atk("1",0,0,1,100,3,3,0,0,0,0,"atk",["debuff"])
slime2=inimigo_atk("1",40,0,"18",100,1,0,0,0,0,0,"atk",["atk","debuff"])
demonio1=inimigo_atk("1",90,0,0,0,0,0,0,0,0,0,"atk",["atk"])
demonio2=inimigo_atk("self",0,0,"31",100,1,2,0,0,0,0,"atk",["buff"])
goblin1=inimigo_atk("1",0,0,11,100,3,2,0,0,0,0,"atk",["debuff"])
goblin2=inimigo_atk("1",60,0,0,0,0,0,0,0,0,0,"atk",["atk"])
armadura1=inimigo_atk("1",40,0,"2B",100,50,1,0,0,0,0,"atk",["atk"])
armadura2=inimigo_atk("self",0,25,17,100,1,2,0,0,0,0,"atk",["buff"])
pessoac_1=inimigo_atk("self",0,0,"2E",100,1,2,0,0,0,0,"atk",["buff"])
pessoac_2=inimigo_atk("todos",0,0,5,100,2,2,13,100,1,1,"atk",["buff","debuff"])
es_f=agrupar("escudo/fungo",12,3)
gr_f=agrupar("grito/fungo",12,2)
cor_f=agrupar("corte/fungo",12,1)
sur_f=agrupar("surrar/fungo",12,4)
mis_f=agrupar("missil/fungo",12,6)
enc_f=agrupar("encanto/fungo",12,5)
jat_f=agrupar("jato/fungo",12,7)
ench_f=agrupar("encharcar/fungo",12,8)
v_f=agrupar("veneno/fungo",12,10)
l_f=agrupar("luz/fungo",12,9)
p_f=agrupar("pedra/fungo",12,11)
v_l=agrupar("venen/luz",10,9)
v_p=agrupar("veneno/pedra",10,11)
p_l=agrupar("pedra/luz",11,9)
fada=inimigo("fada",80,14,10,[fada1,fada2])
goblin=inimigo("goblin",80,14,10,[goblin1,goblin2])
morcego=inimigo("morcego",80,14,10,[morcego1,morcego2])
cogumelo=inimigo("cogumelo",80,14,10,[cogumelo1,cogumelo2])
pessoac=inimigo("pessoa cogumelo",80,14,10,[pessoac_1,pessoac_2])
slime=inimigo("slime",200,20,17,[slime1,slime2])
demonio=inimigo("demonio",170,17,23,[demonio1,demonio2])
i_armadura=inimigo("armadura",170,10,25,[armadura1,armadura2])
golem=inimigo("golem",170,17,17,[golem1,golem2])
inimigo=[fada,goblin,cogumelo,morcego,pessoac]#combinacoes acabam aqui
inimigo_elite=[golem,demonio,slime,i_armadura]
l_artefatos=["moeda","estilingue","soqueira_a","soqueira_b","soqueira_c","gas_venenoso","armadura","espada enferrujada"]
l_items=["p_cura_s","p_cura_m","p_cura_l","antidoto_s","antidoto_m","antidoto_l","i_baralho_s","i_baralho_m","i_baralho_l","spray_s","spray_m","spray_l","protection potion","cafe","p_poder","p_defesa","p_velocidade","virus","soco_e_s","soco_e_m","soco_e_l","lixeira","energético ap+","bomba_s","bomba_m","bomba_l","bomba_fumaca","p_escudo_s","p_escudo_m","p_escudo_l"]
individuais=[corte_s,grito_s,bloquear_s,surrar_s,encanto_s,missil_s,jato_s,encharcar_s,luz_s,veneno_s,pedra_s,fungos_s]
lista_ataque=[[corte2,destruir,consumir,tremor,receptor,pesado,esplosao,compartilhar,rebater,expurgo,quebrar,cor_f],[destruir,grito2,intimidar,fortalecer,raiva,refletir,bolha,sabotar,bencao,toxicidade,endurecer,gr_f],[consumir,fortalecer,bloquear2,esmagar,eco,acolher,recochete,cobertura,impenetravel,parasitar,fortificar,es_f],[tremor,intimidar,esmagar,surrar2,solidificar,meteoritos,pressao,apedrejar,converter,respingo,pedrada,sur_f],[receptor,raiva,eco,solidificar,encanto2,barragem,barreira,propagar,animar,curse,parede,enc_f],[pesado,refletir,acolher,meteoritos,barragem,missil2,raios,metralhar,estrela,chuva,granizo,mis_f],[esplosao,bolha,recochete,pressao,barreira,raios,jato2,imundar,transferencia,ativador,corroer,jat_f],[compartilhar,sabotar,cobertura,apedrejar,propagar,metralhar,imundar,encharcar2,cegar,corromper,petrificar,ench_f],[rebater,bencao,impenetravel,converter,animar,estrela,transferencia,cegar,luz2,v_l,p_l,l_f],[expurgo,toxicidade,parasitar,respingo,curse,chuva,ativador,corromper,v_l,envenenar2,v_p,v_f],[quebrar,endurecer,fortificar,pedrada,parede,granizo,corroer,petrificar,p_l,v_p,pedra2,p_f],[cor_f,gr_f,es_f,sur_f,enc_f,enc_f,jat_f,ench_f,l_f,v_f,p_f,fungos2]]
jogo()
