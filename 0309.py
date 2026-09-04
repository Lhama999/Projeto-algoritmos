import pyxel
import random
def seta(x,y,clr):
 pyxel.line(x,y+2,x+2,y+5,0)
 pyxel.line(x,y+2,x+2,y-1,0)
class inimigo:
 def __init__(HP,DEF,ATK,DECK):
  self.HP=HP
  self.DEF=DEF
  self.ATK=ATK
  self.DECK=DECK
class habilidade:
 def __init__(self,numero,nome):
  self.nome=nome
  self.num=numero
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
  self.opcao=0
  self.usando=[]
  self.turno="aliado"
  self.baralho=[]
  self.mao_real=[]
  self.mao=[]
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
   while len(self.enemy)<2:
    self.aleatorio_b=random.randint(0,4)
    self.enemy.append(inimigo_elite[self.aleatorio_b])
  else:
   self.aleatorio_a=random.randint(0,5)
   self.enemy.append(inimigo[self.aleatorio_a])
   self.aleatorio_b=random.randint(0,4)
   self.enemy.append(inimigo_elite[self.aleatorio_b])
   self.aleatorio_a=random.randint(0,5)
   self.enemy.append(inimigo[self.aleatorio_a])
 def enter_battle(self):
  self.iniciar_turno()
  self.enemy=[]
  self.room="batalha"
  self.aleatorio_a=random.randint(0,1)
  if self.aleatorio_a==1:
   self.x=3
  else:
   self.x=2
  while len(self.enemy)<self.x:
   self.aleatorio_a=random.randint(0,5)
   self.enemy.append(inimigo[self.aleatorio_a])
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
     self.opcao_max=len(self.mao)-1
     if pyxel.btnp(pyxel.KEY_Q):
      if self.opcao>0:
       self.opcao=self.opcao-1
      else:
       self.opcao=self.opcao_max
     if pyxel.btnp(pyxel.KEY_E):
      if self.opcao<self.opcao_max:
       self.opcao=self.opcao+1
      else:
       self.opcao=0
     if pyxel.btnp(pyxel.KEY_W):
      if len(self.mao)>0 and len(self.usando)<(self.max_jogavel*2):
       self.usando.append(self.mao[self.opcao])
       self.mao.pop(self.opcao)
       self.opcao=0
       self.ret=1
     if pyxel.btnp(pyxel.KEY_S):
      self.mao=[]
      self.usando=[]
      for i in self.mao_real:
       self.mao.append(i)
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
     pyxel.text(200,150,self.enemy[0],0)
     pyxel.text(375,150,self.enemy[1],0)
    if len(self.enemy)==3:
     pyxel.text(100,150,self.enemy[0],0)
     pyxel.text(250,150,self.enemy[1],0)
     pyxel.text(400,150,self.enemy[2],0)
    if self.turno=="aliado":
     if len(self.usando)>0:
      self.x=200
      for i in self.usando:
       pyxel.text(self.x,250,i.nome,0)
       self.x=self.x+30
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
grito=habilidade(1,"grito")
corte=habilidade(2,"corte")
bloquear=habilidade(3,"bloquear")
surrar=habilidade(4,"surrar")
encanto=habilidade(5,"encanto")
missil=habilidade(6,"missil")
jato=habilidade(7,"jato")
encharcar=(8,"encharcar")
luz=habilidade(9,"luz")
veneno=habilidade(10,"veneno")
raio=(11,"raio")
pedra=(12,"pedra")
fungo=(13,"fungos")
espada=arma([corte,grito])
escudo=arma([bloquear,surrar])
varinha=arma([encanto,missil])
jato_D_agua=arma([jato,encharcar])
e_luz=arma([luz])
e_veneno=arma([veneno])
e_eletrico=arma([raio])
e_pedra=arma([pedra])
e_fungos=arma([fungo])
inimigo=["fada","goblin","cogumelo","morcego","esqueleto","pessoa_cogumelo"]
inimigo_elite=["golem","demonio","slime","sombra","armadura","bicho_abstrato"]
items=["moeda","estilingue",]
jogo()
ataque=[["1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","1.10","1.11","1.12","1.13"],["2.1","2.2","2.3","2.4","2.5","2.6","2.7","2.8","2.9","2.10","2.11","2.12","2.13"],["3.1","3.2","3.3","3.4","3.5","3.6","3.7","3.8","3.9","3.10","3.11","3.12","3.13"],["4.1","4.2","4.3","4.4","4.5","4.6","4.7","4.8","4.9","4.10","4.11","4.12","4.13"],["5.1","5.2","5.3","5.4","5.5","5.6","5.7","5.8","5.9","5.10","5.11","5.12","5,13"],["6.1","6.2","6.3","6.4","6.5","6.6","6.7","6.8","6.9","6.10","6.11","6.12","6,13"],["7.1","7.2","7.3","7.4","7.5","7.6","7.7","7.8","7.9","7.10","7.11","7.12","7.13"],["8.1","8.2","8.3","8.4","8.5","8.6","8.7","8.8","8.9","8.10","8.11","8.12","8,13"],["9.1","9.2","9.3","9.4","9.5","9.6","9.7","9.8","9.9","9.10","9.11","9.12","9.13"],["10.1","10.2","10.3","10.4","10.5","10.6","10.7","10.8","10.9","10.10","10.11","10.12","10.13"],["11.1","11.2","11.3","11.4","11.5","11.6","11.7","11.8","11.9","11.10","11.11","11.12","11.13"],["12.1","12.2","12.3","12.4","12.5","12.6","12.7","12.8","12.9","12.10","12.11","12.12","12.13"],["13.1","13.2","13.3","13.4","13.5","13.6","13.7","13.8","13.9","13.10","13.11","13.12","13.13"]]
