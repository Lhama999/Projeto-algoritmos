import copy
import pyxel
import random
def seta(x,y,clr):
 pyxel.line(x,y+2,x+2,y+5,0)
 pyxel.line(x,y+2,x+2,y-1,0)
class inimigo:
 def __init__(self,nome,HP,DEF,ATK,DECK):
  self.nome=nome
  self.HP=HP
  self.HP_max=HP
  self.DEF_base=DEF
  self.ATK_base=ATK
  self.DECK=DECK
  self.escudo_atri=0
  self.eco_atri=[]
  self.buff_atri=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  self.debuff_atri=[0,0,0,0,0,0,0,0,0,0]
  self.ven_atri=[]
  self.vivo=1
  self.local=0
  self.opcao_item=0
  self.demo_buff=0
class item_ind:
 def __init__(self,nome,HP,escu,dano,efeito,duracao,stack,preco,id):
  self.HP=HP
  self.nome=nome
  self.escu=escu
  self.dano=dano
  self.efeito=efeito
  self.duracao=duracao
  self.stack=stack
  self.preco=preco
  self.id=id
  self.categ="item"
class agrupar:
 def __init__(self,nome,carta1,carta2):
  self.nome=nome
  self.carta1=carta1
  self.carta2=carta2
  self.categ="grupo"
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
  self.categ="combinar"
protagonista=inimigo("PROTAG",100,10,10,[])
class arma:
 def __init__(self,cartas,nome):
  self.cartas=cartas
  self.premium=0
  self.nome=nome
class artefato_ind:
 def __init__(self,preco,imagem):
  self.preco=preco
  self.nome=imagem
  self.obtido=0
  self.categ="art"
class jogo:
 def __init__(self):
  pyxel.init(640,480,fps=120,title="fusion master")
  self.state="menu"
  self.opcao=1
  self.opcao_menu=1
  self.room=0
  self.nivel=1
  self.art_obt=[]
  self.ret_bon=0
  self.x=60
  self.nivel=1
  self.HP_max=100
  self.AP=2
  self.enemy_ap=2
  self.boss=0
  self.gold=0
  self.buff_atri=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#0atk+,1def+,2ap+,3esqquiva,4fortalecer,5parasitar,6propagar,7nada,8endurecer,9imunnidade,10toxicidade,11sabotar,12hype,13parry,14fortificar,15intimidar,16vitalidade,17solidificar,18raiva,19parasitar,20espinho,21respingar
  self.debuff_atri=[0,0,0,0,0,0,0,0,0,0]#0petrificar,1cegueira,2atk-,,3def-,4ap-,5stun,6esporos,7corrupcao,8compartilhar,9simpatia
  self.item_lista=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#["0p_cura_s",1"p_cura_m",2"p_cura_l",3"antidoto_s","4antidoto_m",5"antidoto_l",6"i_baralho_s",7"i_baralho_m",8"i_baralho_l",9"spray_s",10"spray_m",11"spray_l",12"protection potion",13"cafe",14"p_poder",15"p_defesa",16"p_velocidade",17"virus",18"soco_e_s",19"soco_e_m",20"soco_e_l",21"lixeira",22"energético ap+",23"bomba_s",24"bomba_m",25"bomba_l",26"bomba_fumaca",27"p_escudo_s",28"p_escudo_m",29"p_escudo_l",30s]
  self.ven_atri=[]
  self.eco_atri=[]
  self.boss_m=0
  self.escudo_atri=0
  self.sala1=0
  self.sala2=0
  self.sala3=0
  self.e_room=""
  self.animar_t=0
  self.progresso=0
  self.max_carta=10
  self.max_jogavel=2
  self.baralho_atual=[]
  self.armas_g=[]
  pyxel.load("fusion_master_sprt.pyxres")
  self.armas_e=[]
  self.armas=[espada,escudo,varinha,e_luz]
  self.baralho=[]
  self.turno=0
  pyxel.run(self.update,self.draw)
 def enter_loja(self):
  self.room="loja"
  self.produtos=[]
  self.opcao=0
  self.precos=[]
  self.produtos.append("arma")
  self.precos.append(75)
  while len(self.produtos)<6:
   self.ale_i=random.randint(0,len(l_items)-1)
   self.produtos.append(copy.copy(l_items[self.ale_i]))
   self.precos.append(copy.copy(l_items[self.ale_i].preco))
  while (len(self.produtos)<8):
   self.art_obtivel=[]
   for i in l_artefatos:
    if i not in self.art_obt:
     self.art_obtivel.append(i)
   if len(self.art_obtivel)>0:
    self.ale_i=random.randint(0,len(self.art_obtivel)-1)
    self.produtos.append(l_artefatos[self.ale_i])
    self.precos.append(copy.copy(l_artefatos[self.ale_i].preco))
   else:
    self.ale_i=random.randint(0,len(l_items)-1)
    self.produtos.append(copy.copy(l_items[self.ale_i]))
    self.precos.append(copy.copy(l_items[self.ale_i].preco))
   if art_moeda in self.art_obt:
    for i in self.precos:
     i=i*0.7
     i=i//1
 def enter_evento(self):
  self.room="evento"
  self.aleatorio_a=random.randint(1,6)
  self.evento=self.aleatorio_a
  if self.evento==1:
   self.reward=random.randint(20,100)
   self.gold=self.gold+self.reward
  if self.evento==2:
   self.reward="def"
   protagonista.DEF_base=protagonista.DEF_base+3
  if self.evento==3:
   self.reward="atk"
   protagonista.ATK_base=protagonista.ATK_base+3
  if self.evento==4:
   self.reward="hp"
   protagonista.HP_max=protagonista.HP_max+20
  if self.evento==5:
   self.ganhar_arma()
   self.reward="arma"
  if self.evento==6:
   self.reward="ap"
   if self.AP<6:
    self.AP=self.AP+1
 def ganhar_arma(self):
  self.e_room="arma"
  self.pos_arma=[]
  for i in lista_arma:
   if i not in self.armas:
    self.pos_arma.append(i)
  self.escolha_arma=[]
  while len(self.escolha_arma)<3:
   self.ale_i=random.randint(0,len(self.pos_arma)-1)
   self.escolha_arma.append(self.pos_arma[self.ale_i])
   del self.pos_arma[self.ale_i]
 def troca_arma(self,arma):
  self.e_room="troca"
  if arma==(e_veneno or e_luz or e_pedra):
   self.e_room="troca_e"
  self.alterar_a=arma
 def acoes_protag(self):
  self.acoes_a=self.AP
  if protagonista.buff_atri[2]>0:
   self.acoes_a=self.acoes_a+1
  if protagonista.debuff_atri[4]>0:
   self.acoes_a=self.acoes_a-1
  self.max_jogavel=self.acoes_a
 def calcular_status(self,alvo):
  alvo.ATK=alvo.ATK_base
  if alvo.buff_atri[0]>0:
   alvo.ATK=alvo.ATK+alvo.ATK_base*0.4
  if usuario.debuff[3]>0:
   alvo.ATK=alvo.ATK-alvo.ATK_base*0.4
  if alvo.buff_atri[16]>0:
   alvo.ATK=alvo.ATK+alvo.DEF_base*0.5
  alvo.ATK=alvo.ATK//1
  alvo.DEF=alvo.DEF_base
  if alvo.buff_atri[0]>0:
   alvo.DEF=alvo.DEF+alvo.DEF_base*0.4
  if alvo.debuff[3]>0:
   alvo.ATK=alvo.ATK-alvo.ATK_base*0.4
  if alvo.buff_atri[16]>0:
   alvo.DEF=alvo.DEF+alvo.ATK_base*0.5
  alvo.DEF=alvo.DEF//1
 def true_dmg(self,alvo,dmg):
  if alvo.escudo_atri>dmg:
   alvo.escudo_atri=alvo.escudo_atri-dmg
  else:
   alvo.HP=alvo.HP-(dmg-alvo.escudo_atri)
 def aplicar_cogumelos(self,alvo,stacks):
  self.contador_cog=0
  while self.contador_cog<stacks:
   if self.boss=="cogumelo":
    self.remover_vida(protagonista,5)
   if 1==1:
    if 1==1:
     alvo=protagonista
     self.aleatorio_cog=random.randint(1,14)
     if self.aleatorio_cog==1:
      self.ganhar_buff(0,alvo,2)
     if self.aleatorio_cog==2:
      self.ganhar_buff(1,alvo,2)
     if self.aleatorio_cog==3:
      self.ganhar_debuff(2,alvo,2)
     if self.aleatorio_cog==4:
      self.ganhar_debuff(3,alvo,2)
     if self.aleatorio_cog==5:
      self.ganhar_buff(3,alvo,2)
     if self.aleatorio_cog==6:
      self.ganhar_buff(2,alvo,2)
     if self.aleatorio_cog==7:
      self.ganhar_buff(4,alvo,2)
     if self.aleatorio_cog==8:
      self.perder_buff(alvo)
     if self.aleatorio_cog==9:
      self.perder_debuff(alvo)
     if self.aleatorio_cog==10:
      self.adicionar_ven(2,2,alvo)
     if self.aleatorio_cog==11:
      self.adicionar_eco(1,2,alvo)
     if self.aleatorio_cog==12:
      self.ganhar_debuff(6,alvo,1)
     if self.aleatorio_cog==13:
      self.ganhar_debuff(7,alvo,2)
     if self.aleatorio_cog==14:
      self.ganhar_debuff(4,alvo,2)
   for i in self.enemy:
    if i.vivo==1 and i.boss!="cogumelo":
     alvo=i
     self.aleatorio_cog=random.randint(1,14)
     if self.aleatorio_cog==1:
      self.ganhar_buff(0,alvo,2)
     if self.aleatorio_cog==2:
      self.ganhar_buff(1,alvo,2)
     if self.aleatorio_cog==3:
      self.ganhar_debuff(2,alvo,2)
     if self.aleatorio_cog==4:
      self.ganhar_debuff(3,alvo,2)
     if self.aleatorio_cog==5:
      self.ganhar_buff(3,alvo,2)
     if self.aleatorio_cog==6:
      self.ganhar_buff(2,alvo,2)
     if self.aleatorio_cog==7:
      self.ganhar_buff(4,alvo,2)
     if self.aleatorio_cog==8:
      self.perder_buff(alvo)
     if self.aleatorio_cog==9:
      self.perder_debuff(alvo)
     if self.aleatorio_cog==10:
      self.adicionar_ven(2,2,alvo)
     if self.aleatorio_cog==11:
      self.adicionar_eco(1,2,alvo)
     if self.aleatorio_cog==12:
      self.ganhar_debuff(6,alvo,1)
     if self.aleatorio_cog==13:
      self.ganhar_debuff(7,alvo,2)
     if self.aleatorio_cog==14:
      self.ganhar_debuff(4,alvo,2)
 def acoes_e(self):
  if self.nivel==1:
   if self.estate=="e_battle":
    self.e_ap=3
   if self.estate=="battle":
    self.e_ap=2
  if self.nivel==1.5:
   if self.estate=="e_battle":
    self.e_ap=4
   if self.estate=="battle":
    self.e_ap=3
  if self.estate==("cogumelo" or "cacto"):
   self.e_ap=5
  self.e_ap_ma=0
  self.e_ap_me=0
  for i in self.enemy:
   if i.vivo==1:
    if i.buff_atri[2]>0:
     self.e_ap_ma=1
    if i.debuff_atri[4]>0:
     self.e_ap_me=1
  if self.e_ap_me==1:
   self.e_ap=self.e_ap-1
  if self.e_ap_ma==1:
   self.e_ap=self.e_ap+1
  self.enemy_ap=self.e_ap
 def iniciar_turno(self):
  self.a_opcao=0
  self.opcao=0
  self.usando=[]
  self.turno="aliado"
  self.baralho=[]
  self.mao_real=[]
  self.mao=[]
  self.l_alvos=[]
  if self.estate==("cog1" or "cog2" or "cacto2"):
   if self.inimigoA.vivo==0:
    if self.estate=="cacto2":
     protagonista.escu_atri=protagonista_escu_atri+10
    self.inimigoA.HP=self.inimigoA.max_HP
    for i in self.inimigoA.buff_atri:
     i=0
    for i in self.inimigoA.debuff_atri:
     i=0
    self.inimigoA.ven_atri=[]
    self.inimigoA.eco_atri=[]
   if self.inimigoC.vivo==0:
    if self.estate=="cacto2":
     protagonista.escu_atri=protagonista_escu_atri+10
    self.inimigoC.HP=self.inimigoC.max_HP
    for i in self.inimigoC.buff_atri:
     i=0
    for i in self.inimigoC.debuff_atri:
     i=0
    self.inimigoC.ven_atri=[]
    self.inimigoC.eco_atri=[]
  for i in self.armas:
   for h in i.cartas:
    self.baralho.append(h)
  while len(self.mao_real)<self.max_carta:
   self.aleatorio_i=random.randint(1,len(self.baralho))
   self.aleatorio_i=self.aleatorio_i-1
   self.mao_real.append(self.baralho[self.aleatorio_i])
  for i in self.mao_real:
   self.mao.append(i)
  self.acoes_protag()
 def usar_item(self,item):
  if item.dano>0:
   for i in self.enemy:
    if i.vivo==1:
     self.true_dmg(i,item.dano)
  if item.escu>0:
   self.aplicar_escudo(protagonista,item.escu)
  self.efeito_item(item)
  self.mao=[]
  self.usando=[]
  self.l_alvos=[]
  for i in self.mao_real:
   self.mao.append(i)
  for i in self.enemy:
   if i.HP<1:
    i.vivo=0
  self.escolhe_alvo()
 def efeito_item(self,item):#1antidoto,2baralho,3baralho universal,4veneno,5parry,6hype,7atk+,8def+,9esquiva,10 corrupcao,11eco,12descartar mao,13 ap+
  if item.efeito==1:
   self.contar_i=0
   while self.contar_i<item.stack:
    self.perder_debuff(protagonista)
  if item.efeito==2:
   self.contar_i=0
   while self.contar_i<item.stack:
    self.aleatorio_i=random.randint(1,len(self.baralho))
    self.aleatorio_i=self.aleatorio_i-1
    self.mao_real.append(self.baralho[self.aleatorio_i])
   self.mao=[]
   for i in self.mao_real:
    self.mao.append(i)
  if item.efeito==3:
   self.contar_i=0
   while self.contar_i<item.stack:
    self.aleatorio_i=random.randint(1,len(baralho_universal))
    self.aleatorio_i=self.aleatorio_i-1
    self.mao_real.append(baralho_universal[self.aleatorio_i])
   self.mao=[]
   for i in self.mao_real:
    self.mao.append(i)
  if item.efeito==4:
   for i in self.enemy:
    if i.vivo==1:
     self.adicionar_ven(duracao,stack,i)
  if item.efeito==5:
   self.ganhar_buff(13,protagonista,2)
  if item.efeito==6:
   self.ganhar_buff(12,protagonista,2)
  if item.efeito==7:
   self.ganhar_buff(0,protagonista,2)
  if item.efeito==8:
   self.ganhar_buff(1,protagonista,2)
  if item.efeito==9:
   self.ganhar_buff(3,protagonista,2)
  if item.efeito==10:
   for i in self.enemy:
    if i.vivo==1:
     self.ganhar_debuff(7,i,2)
  if item.efeito==11:
   self.adicionar_eco(stack,duracao,protagonista)
  if item.efeito==12:
   self.mao_real=[]
   for i in self.armas:
    for h in i.cartas:
     self.baralho.append(h)
   while len(self.mao_real)<self.max_carta:
    self.aleatorio_i=random.randint(1,len(self.baralho))
    self.aleatorio_i=self.aleatorio_i-1
    self.mao_real.append(self.baralho[self.aleatorio_i])
  if item.efeito==13:
   self.ganhar_buff(2,protagonista,2)
  if item.efeito==14:
   for i in self.enemy:
    if i.vivo==1:
     self.ganhar_debuff(0,i,2)
     self.ganhar_debuff(1,i,2)
 def enter_elite_battle(self):
  self.room="batalha"
  self.estate="elite"
  self.enemy=[]
  self.aleatorio_a=random.randint(0,1)
  if self.aleatorio_a==0:
   self.aleatorio_b=random.randint(0,3)
   self.inimigoA=copy.copy(inimigo_elite[self.aleatorio_b])
   self.aleatorio_b=random.randint(0,3)
   self.inimigoB=copy.copy(inimigo_elite[self.aleatorio_b])
   self.inimigoA.local=1
   self.inimigoB.local=2
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
  else:
   self.aleatorio_a=random.randint(0,3)
   self.inimigoA=copy.copy(inimigo_l[self.aleatorio_a])
   self.aleatorio_b=random.randint(0,3)
   self.inimigoB=copy.copy(inimigo_elite[self.aleatorio_b])
   self.aleatorio_a=random.randint(0,3)
   self.inimigoC=copy.copy(inimigo_l[self.aleatorio_a])
   self.inimigoA.local=1
   self.enemy.append(self.inimigoA)
   self.inimigoB.local=2
   self.inimigoC.local=3
   self.enemy.append(self.inimigoB)
   self.enemy.append(self.inimigoC)
  self.iniciar_turno()
 def ganhar_buff(self,buff,alvo,duracao):
  if buff==13:
   alvo.buff_atri[13]=alvo.buff_atri[13]+duracao
  else:
   if alvo.buff_atri[buff]<duracao:
    alvo.buff_atri[buff]=duracao
 def ganhar_debuff(self,buff,alvo,duracao):
  self.aplicar_debuff=1
  if alvo.buff_atri[9]>0:
   self.randoma=random.randint(1,100)
   if self.randoma<41:
    self.aplicar_debuff=0
  if self.aplicar_debuff==1:
   if buff==6:
    alvo.debuff_atri[6]=alvo.buff_atri[6]+duracao
   else:
    if alvo.debuff_atri[debuff]<duracao:
     alvo.debuff_atri[debuff]=duracao
 def perder_buff(self,alvo):
  self.aleatorio_max=[-1]
  for i in range(0,len(alvo.buff_atri)):
   if alvo.buff_atri[i]>0:
    self.aleatorio_max.append(i)
  self.cleanse=random.randint(0,(len(self.cleanse)-1))
  if self.cleanse==-1:
   self.contador_remocao=2
   for i in alvo.eco_atri:
    while i>0 and self.contador_remocao>0:
     i=i-1
     self.contador_remocao=self.contador_remocao-1
  else:
   alvo.buff_atri[self.aleatorio_max[self.cleanse]]=0
 def perder_debuff(self,alvo):
  self.aleatorio_max=[-1]
  for i in range(0,len(alvo.debuff_atri)):
   if alvo.debuff_atri[i]>0:
    self.aleatorio_max.append(i)
  self.cleanse=random.randint(-1,(len(self.cleanse)-1))
  if self.cleanse==-1:
   self.contador_remocao=3
   for i in alvo.ven_atri:
    while i>0 and self.contador_remocao>0:
     i=i-1
     self.contador_remocao=self.contador_remocao-1
  else:
   alvo.debuff_atri[self.aleatorio_max[self.cleanse]]=0
 def atacar_e(self,usuario,dano,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags):#continuar_aqui
  self.repetir=0
  if efeitoa=="E":
   self.repetir=1
   self.repetir_min=stacka
   self.repetir_max=duracaoa
  elif efeitob=="E":
   self.repetir=1
   self.repetir_min=stackb
   self.repetir_max=duracaob
  if self.repetir==1:
   self.random_a=random.rantint(repetir_min,repetir_max)
   self.repeticao=random_a
  else:
   self.repeticao=1
  self.contador_atk=0
  while self.contador_atk<self.repeticao:
   self.aplicar_escudo(usuario,escudo)
   self.bloquear_atk=0
   if ("debuff" in tags) and protagonista.debuff_atri[0]>0:
    self.bloquear_atk=1
   if ("buff" in tags) and protagonista.debuff_atri[0]>0:
    self.bloquear_atk=1
   if ("atk" in tags) and protagonista.debuff_atri[1]>0:
    self.bloquear_atk=1
   if ("atk" in tags) and alvo.buff_atri[3]>0:
    self.bloquear_atk=1
   if self.bloquear_atk==1:
    self.bloquear_atk=random.randint(1,100)
    if self.bloquear_atk<40:
     self.bloquear_atk=1
    else:
     self.bloquear_atk=0
   if self.bloquear_atk==0:
    self.calcular_status(protagonista)
    for i in self.enemy:
     self.calcular_status(i)
    self.aplicar_efeitos(alvo,efeitoa,chancea,stacka,duracaoa,usuario)
    self.aplicar_efeitos(alvo,efeitob,chanceb,stackb,duracaob,usuario)
   if self.bloquear_atk==0:
    if "atk" in tags:
     if protagonista.buff_atri[15]>0:
      self.ale_i=random.randint(1,100)
      if self.ale_i<30:
       self.ganhar_debuff(5,alvo,1)
    if protagonista.buff_atri[11]>0:
     self.debuff_aleatorio(1,2,alvo)
    self.calcular_status(protagonista)
    for i in self.enemy:
     self.calcular_status(i)
    self.danificar=self.gerar_dano(protagonista,alvo)
    self.remover_vida(alvo,self.danificar)
    if alvo.buff_atri[20]>0:
     self.remover_vida(usuario,(self.danificar*0.3)//1)
 def enter_battle(self):
  self.enemy=[]
  self.room="batalha"
  self.estate="normal"
  self.aleatorio_a=random.randint(0,1)
  if self.aleatorio_a==1:
   self.aleatorio_a=random.randint(0,3)
   self.inimigoA=copy.copy(inimigo_l[self.aleatorio_a])
   self.aleatorio_a=random.randint(0,3)
   self.inimigoB=copy.copy(inimigo_l[self.aleatorio_a])
   self.inimigoA.local=1
   self.inimigoB.local=2
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
  else:
   self.aleatorio_a=random.randint(0,3)
   self.inimigoA=copy.copy(inimigo_l[self.aleatorio_a])
   self.aleatorio_a=random.randint(0,3)
   self.inimigoB=copy.copy(inimigo_l[self.aleatorio_a])
   self.aleatorio_a=random.randint(0,3)
   self.inimigoC=copy.copy(inimigo_l[self.aleatorio_a])
   self.inimigoA.local=1
   self.inimigoB.local=2
   self.inimigoC.local=3
   self.enemy.append(self.inimigoA)
   self.enemy.append(self.inimigoB)
   self.enemy.append(self.inimigoC)
  self.iniciar_turno()
 def adicionar_ven(self,stack,duracao,alvo):
  while len(alvo.ven_atri)<duracao:
   alvo.ven_atri.append(0)
  alvo.ven_atri[(duracao-1)]=alvo.ven_atri[(duracao-1)]+stack
 def buff_aleatorio(self,stack,duracao,alvo):
  self.randoma=random.randint(0,3)
  if self.randoma==0:
   self.adicionar_eco(1,2,alvo)
  if self.randoma==1:
   if alvo.buff_atri[0]<2:
    alvo.buff_atri[0]=2
  if self.randoma==2:
   if alvo.buff_atri[1]<2:
    alvo.buff_atri[1]=2
  if self.randoma==3:
   if alvo.buff_atri[2]<2:
    alvo.buff_atri[2]=2
 def debuff_aleatorio(self,stack,duracao,alvo):
  self.randoma=random.randint(0,4)
  if self.randoma==0:
   self.adicionar_ven(2,2,alvo)
  if self.randoma==1:
   if alvo.debuff_atri[2]<2:
    alvo.debuff_atri[2]=2
  if self.randoma==2:
   if alvo.debuff_atri[3]<2:
    alvo.debuff_atri[3]=2
  if self.randoma==3:
   if alvo.debuff_atri[4]<2:
    alvo.debuff_atri[4]=2
  if self.randoma==4:
   alvo.debuff_atri[6]=alvo.debuff_atri[6]+1
 def gerar_dano(self,usuario,alvo,atk,escala):
  if escala=="atk":
   escala=usuario.ATK
  if escala=="def":
   escala=usuario.DEF
  if escala=="escudo":
   escala=usuario.escudo_atri
  if escala=="atk+def":
   escala="usuario.ATK+usuario.DEF"//2
  if atk>0:
   self.danificar=atk*escala
   if efeitoa=="10":
    for i in self.alvo_atual.debuff_atri:
     if i>0:
      self.danificar=self.danificar+(stacka*escala)
   if usuario.buff_atri[18]>0:
    self.danificar=self.danificar*1.5
   if self.buff_atri[10]>0:#aqui
    self.adicionar_ven(2,1,100,alvo)
   if self.alvo.buff_atri[18]>0:
    self.danificar=self.danificar*1.25
   self.danificar=self.danificar//self.alvo.DEF
   if self.alvo.buff_atri[4]>0:
    self.danificar=self.danificar*0.8
   if self.alvo.buff_atri[13]>0:
    self.danificar=0
    self.alvo_atual.buff_atri[13]=self.alvo_atual.buff_atri[13]-1
   self.dano_real=self.danificar
   return self.dano_real  
 def adicionar_eco(self,stack,duracao,alvo):
  while len(alvo.eco_atri)<duracao:
   alvo.eco_atri.append(0)
  alvo.eco_atri[(duracao-1)]=alvo.eco_atri[(duracao-1)]+stack
 def remover_vida(self,alvo,dano):
  if alvo.buff_atri[13]>0:
   alvo.buff_atri[13]=alvo.buff_atri[13]-1
   dano=0
  if alvo.escudo_atri>dano:
   alvo.escudo_atri=alvo.escudo_atri-dano
  else:
   alvo.HP=alvo.HP-(dano-alvo.escudo_atri)
   alvo.escudo_atri=0
 def atacar_p(self,usuario,alvo,dano,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags):
  self.bloquear_atk=0
  if ("debuff" in tags) and protagonista.debuff_atri[0]>0:
   self.bloquear_atk=1
  if ("buff" in tags) and protagonista.debuff_atri[0]>0:
   self.bloquear_atk=1
  if ("atk" in tags) and protagonista.debuff_atri[1]>0:
   self.bloquear_atk=1
  if ("atk" in tags) and alvo.buff_atri[3]>0:
   self.bloquear_atk=1
  if self.bloquear_atk==1:
   self.bloquear_atk=random.randint(1,100)
   if self.bloquear_atk<40:
    self.bloquear_atk=1
   else:
    self.bloquear_atk=0
  if self.bloquear_atk==0:
   self.calcular_status(protagonista)
   for i in self.enemy:
    self.calcular_status(i)
   self.aplicar_efeitos(alvo,efeitoa,chancea,stacka,duracaoa,usuario)
   self.aplicar_efeitos(alvo,efeitob,chanceb,stackb,duracaob,usuario)
  if self.bloquear_atk==0:
   if "atk" in tags:
    if protagonista.buff_atri[15]>0:
     self.ale_i=random.randint(1,100)
     if self.ale_i<30:
      self.ganhar_debuff(5,alvo,1)
   if protagonista.buff_atri[11]>0:
    self.debuff_aleatorio(1,2,alvo)
   self.calcular_status(protagonista)
   for i in self.enemy:
    self.calcular_status(i)
   self.danificar=self.gerar_dano(protagonista,alvo)
   self.remover_vida(alvo,self.danificar)
   if alvo.buff_atri[20]>0:
    self.remover_vida(protagonista,(self.danificar*0.3)//1)
   if alvo.debuff_atri[8]>0:
    for i in self.enemy:
     if i!=alvo and i.vivo==1:
      self.remover_vida(i,(self.danificar*0.3)//1)
   for i in self.enemy:
    if i.vivo==1 and i!=alvo and i.debuff_atri[9]>0:
     self.remover_vida(i,(self.danificar*0.3)//1)
   if ("atk" in tags) and alvo.nome=="cacto2":
    alvo.buff_atri[20]=2
 def aplicar_escudo(self,usuario,escudo):
  if usuario.buff_atri[14]>0:
   escudo=escudo*1.4
   escudo=escudo//1
   usuario.escudo_atri=usuario.escudo_atri+escudo
 def atacar_protag(self,usuario,alvo,alvo_real,dano,escudo,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags):
  self.repetir=0
  if art_espada in self.art_obt:
   dano=dano*1.25
  if art_escudo in self.art_obt:
   escudo=escudo*1.25
  if efeitoa=="E":
   self.repetir=1
   self.repetir_min=stacka
   self.repetir_max=duracaoa
  elif efeitob=="E":
   self.repetir=1
   self.repetir_min=stackb
   self.repetir_max=duracaob
  if self.repetir==1:
   self.random_a=random.randint(self.repetir_min,self.repetir_max)
   self.repeticao=self.random_a
  else:
   self.repeticao=1
  self.contador_atk=0
  while self.contador_atk<self.repeticao:
   self.contador_atk=self.contador_atk
   self.aplicar_escudo(protagonista,escudo)
   if alvo=="random":
    self.list_alvos=[]
    for i in self.enemy:
     if i.vivo==1:
      self.list_alvos.append(1)
    self.alvo_atk_ale=random.randint(1,len(self.list_alvos))
    self.atacar_p(protagonista,self.alvo_atk_ale,dano,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags)
   if alvo=="todos_E":
    for i in self.enemy:
     if i.vivo==1:
      self.atacar_p(protagonista,i,dano,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags)
   if alvo=="self":
    self.atacar_p(protagonista,protagonista,dano,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags)
   if alvo=="1":
    if alvo_real==1:
     alvo_real=self.inimigoA
    if alvo_real==2:
     alvo_real=self.inimigoB
    if alvo_real==3:
     alvo_real=self.inimigoC
    self.atacar_p(protagonista,alvo_real,dano,efeitoa,chancea,stacka,duracaoa,efeitob,chanceb,stackb,duracaob,escala,tags)
 def soco_ativar(self,usuario):
  self.soco_dano=5
  self.escu_soco=0
  self.ven_soco=0 
  if usuario==protagonista:
   if art_soco_a in self.art_obt:
    self.soco_dano=self.soco_dano+5
   if art_soco_b in self.art_obt:
    self.escu_soco=1
   if art_soco_c in self.art_obt:
    self.ven_soco=1
  if usuario.buff_atri[17]>0:
   self.soco_dano=self.soco_dano+5
  self.poss_alvo=[]
  for i in self.enemy:
   if i.vivo==1:
    self.poss_alvo.append(i)
  self.cont_eco=0
  self.eco_total=0
  for i in usuario.eco_atri:
   self.eco_total=self.eco_total+i
  while self.cont_eco<self.eco_total:
   if usuario==protagonista:
    self.cont_eco=self.cont_eco+1
    self.ale_i=random.randint(0,len(self.poss_alvo-1))
    self.atacar_p(protagonista,self.poss_alvo[self.ale_i],self.soco_dano,0,0,0,0,0,0,0,0,"atk",["atk"])
   else:
    self.atacar_e(usuario,5,0,0,0,0,0,0,0,0,"atk",["atk"])
 def aplicar_efeitos(self,alvo_atk,efeitoA,duracao,stack,usuario):
  if usuario.buff_atri[6]>0:
   duracao=duracao+1
   stack=stack+1
  if efeitoA=="1":
   self.adicionar_ven(stack,duracao,alvo_atk)
  if efeitoA=="2":
   self.ganhar_debuff(0,alvo_atk,duracao)
  if efeitoA=="3":
   self.ganhar_debuff(1,alvo_atk,duracao)
  if efeitoA=="4":
   self.ganhar_debuff(5,alvo_atk,duracao)
  if efeitoA=="5":
   self.aplicar_cogumelos(alvo_atk,stack)
  if efeitoA=="6":
   self.ganhar_buff(0,usuario,duracao)
  if efeitoA=="7":
   self.ganhar_buff(1,usuario,duracao)
  if efeitoA=="8":
   self.ganhar_debuff(2,alvo_atk,duracao)
  if efeitoA=="9":
   self.ganhar_debuff(3,alvo_atk,duracao)
  if efeitoA=="A":
   self.ganhar_buff(2,usuario,duracao)
  if efeitoA=="B":
   self.ganhar_buff(5,usuario,duracao)
  if efeitoA=="C":
   self.ganhar_buff(3,usuario,duracao)
  if efeitoA=="D":
   self.buff_aleatorio(stack,duracao,usuario)
  if efeitoA=="11":
   self.debuff_aleatorio(stack,duracao,alvo_atk)
  if efeitoA=="12":
   self.deplicar_debuff(alvo_atk)
  if efeitoA=="13":
   self.ganhar_debuff(6,alvo_atk,stack)
  if efeitoA=="14":
   for i in range(0,stacks):
    self.perder_debuff(usuario)
  if efeitoA=="15":
   self.ganhar_buff(8,usuario,duracao)
  if efeitoA=="17":
   self.ganhar_buff(4,usuario,duracao)
  if efeitoA=="18":
   for i in range(0,stack):
    self.ativar_dot(alvo_atk)
  if efeitoA=="19":
   for i in range(0,stack):
    if len(alvo_atk.ven_atri)>0:
     del alvo_atk.ven_atri[0]
  if efeitoA=="1A":
   self.ganhar_debuff(7,alvo_atk,duracao)
  if efeito=="1B":
   self.transferir_debuff(usuario,alvo_atk,stacks)
  if efeito=="1C":
   self.ganhar_buff(6,usuario,duracao)
  if efeito=="1D":
   self.ganhar_buff(5,usuario,duracao)
  if efeito=="1E":
   self.ganhar_buff(9,usuario,duracao)
  if efeito=="20":
   self.ganhar_buff(10,usuario,duracao)
  if efeito=="21":
   self.ganhar_buff(12,usuario,duracao)
  if efeito=="22":
   self.ganhar_buff(13,usuario,duracao)
  if efeito=="23":
   self.ganhar_buff(20,usuario,duracao)
  if efeito=="25":
   self.ganhar_buff(21,usuario,duracao)
  if efeito=="26":
   self.ganhar_buff(14,usuario,duracao)
  if efeito=="27":
   self.ganhar_buff(15,usuario,duracao)
  if efeito=="28":
   self.transferir_debuff(usuario,alvo_atk,stacks)
  if efeito=="29":
   for i in range(0,stacks):
    self.perder_buff(alvo_atk)
  if efeito=="2A":
   self.ganhar_buff(16,usuario,duracao)
  if efeito=="2B":
   self.remover_escudo_a(alvo_atk,duracao)
  if efeito=="2C":
   self.ganhar_debuff(8,alvo_atk,duracao)
  if efeito=="2D":
   self.ganhar_debuff(9,alvo_atk,duracao)
  if efeito=="2E":
   self.adicionar_eco(stack,duracao,usuario)
  if efeito=="30":
   self.ganhar_buff(17,usuario,duracao)
  if efeito=="31":
   self.ganhar_buff(18,usuario,duracao)
  if efeito=="32":
   self.ganhar_buff(11,usuario,duracao)
 def remover_escudo_a(self,alvo,porcento):
  alvo.escu_atri=alvo.escu_atri-alvo.escu_atri*porcento
 def transferir_debuff(self,usuario,alvo,quantos):
  self.conta_debuff=0
  while self.conta_debuff<quantos:
   self.debuff_pos=[]
   self.cont_dbf=0
   for i in usuario.debuff_atri:
    if usuario.debuff_atri[self.cont_dbf]>0:
     self.debuff_pos.append(self.cont_dbf)
    self.cont_dbf=self.cont_dbf+1
   self.ale_i=random.randint(0,(len(self.debuff_pos)-1))
   alvo.debuff_atri[self.debuff_pos[self.ale_i]]=usuario.debuff_atri[self.debuff_pos[self.ale_i]]
   usuario.debuff_atri[self.debuff_pos[self.ale_i]]=0
 def gerar_atk_e(self):
  self.pos_atacante=[]
  self.ataques_e=[]
  self.gerado=0
  self.atacante=[]
  for i in self.enemy:
   i.demo_buff=0
  if self.estate==("cog1" or "cog2"):
   if inimigoA.vivo==1:
    self.pos_atacante.append(self.inimigoA)
   if inimigoB.vivo==1:
    self.pos_atacante.append(self.inimigoB)
  elif self.estate!=("cacto1" or "cacto2"):
   for i in self.enemy:
    if i.vivo==1:
     self.pos_atacante.append(i)
  if self.estate==("cacto1"):
   self.ataques_e.append(a_cacto1)
   self.atacante.append(self.inimigoB)
  elif self.estate==("cacto2"):
   self.ataques_e.append(a_cacto2)
   self.atacante.append(self.inimigoB)
  elif len(self.atacante)>0:
   while self.gerado<self.enemy_ap:
    self.gerado=self.gerado+1
    self.ale_i=random.randint(0,len(self.atacante)-1)
    self.atacante.append(self.enemy[self.ale_i])
    if self.enemy[self.ale_i].nome=="demonio":
     if self.enemy[self.ale_i].demo_buff==0:
      self.enemy[self.ale_i].demo_buff=1
      self.ataques_e.append(demonio2)
     else:
      self.ataques_e.append(demonio1)
    else:
     self.ale_a=random.randint(0,len(self.enemy[self.ale_i].DECK)-1)
     self.ataques_e.append(self.enemy[self.ale_i].DECK[self.ale_a])
 def ativa_atk_e(self):
  self.atk_sprt=[]
  self.atacante_sprt=[]
  while (len(self.atacante) and len(self.ataques_e))>0:
   if self.atacante[0].debuff_atri[5]<1:
    if self.atacante[0].debuff_atri[6]>0:
     self.atacante[0].debuff_atri[6]=self.atacante[0].debuff_atri[6]-1
     self.atk_sprt.append("cog")
     self.atacar_e(self.atacante[0],0,5,100,1,2,0,0,0,0,"atk",["buff","debuff"])
     self.atacante_sprt.append(self.atacante[0])
    else:
     self.atacar_e(self.atacante[0],self.ataques_e[0].dano,self.ataques_e[0].escudo,self.ataques_e[0].efeitoA,self.ataques_e[0].chanceA,self.ataques_e[0].stackA,self.ataques_e[0].duracaoA,self.ataques_e[0].efeitoB,self.ataques_e[0].chanceB,self.ataques_e[0].stackB,self.ataques_e[0].duracaoB,self.ataques_e[0].duracaoB,self.ataques_e[0].stat,self.ataques_e[0].tags)  
     self.atk_sprt.append("1")
     self.atacante_sprt.append(self.atacante[0])
   del self.atacante[0]
   del self.ataques_e[0]
 def recompensa_g(self,nivel):
  if nivel==1:
   protagonista.ATK_base=protagonista.ATK_base+1
   protagonista.DEF_base=protagonista.DEF_base+1
   protagonista.HP_max=protagonista.HP_max+5
   self.gold=self.gold+20
 def terminar_combate(self):
  if self.estate=="elite":
   self.recompensa_g(2)
   self.estate=0
   self.enter_map()
  if self.estate=="normal":
   self.recompensa_g(1)
   self.estate=0
   self.enter_map()
  if self.estate=="cog2":
   self.recompensa_g(3)
   self.estate=0
   if self.nivel==1.5:
    self.ganhar_tela()
   else:
    self.nivel=1.5
    self.boss_m="cogumelo"
    self.estate=0
    self.enter_map()
  if self.estate=="cacto2":
   self.recompensa_g(3)
   if self.nivel==1.5:
    self.ganhar_tela()
    self.boss_m="cacto"
    self.estate=0
   else:
    self.nivel=1.5
    self.sala=1
    self.enter_map()
  if self.estate=="cog1":
   self.enter_boss("cog2")
  if self.estate=="cacto1":
   self.enter_boss("cacto2")
 def enter_boss(self,boss):
  self.enter_battle()
  if boss=="cog1":
   self.inimigoA=copy.copy(cogumelo)
   self.inimigoB=copy.copy(boss_cog)
   self.inimigoC=copy.copy(cogumelo)
   self.estate="cog1"
  if boss=="cog2":
   self.inimigoA=copy.copy(cogumelo)
   self.inimigoB=copy.copy(boss_cog)
   self.inimigoC=copy.copy(cogumelo)
   self.estate="cog2"
  if boss=="cacto1":
   self.inimigoA=copy.copy(cacto_flor)
   self.inimigoB=copy.copy(boss_cacto1)
   self.inimigoC=copy.copy(cacto_flor)
   self.inimigoC.vivo=0
   self.inimigoA.vivo=0
   self.estate="cacto1"
  if boss=="cacto2":
   self.inimigoA=copy.copy(cacto_flor)
   self.inimigoB=copy.copy(boss_cacto2)
   self.inimigoC=copy.copy(cacto_flor)
   self.estate="cacto2"
  self.enemy=[]
  self.enemy.append(self.inimigoA)
  self.enemy.append(self.inimigoB)
  self.enemy.append(self.inimigoC)
 def escolhe_alvo(self):
  self.inimigo_exite=0
  if self.enemy[0].vivo==1:
   self.a_opcao=0
   self.inimigo_exite=1
  if self.enemy[1].vivo==1:
   self.a_opcao=1
   self.inimigo_exite=1
  if len(self.enemy)==3:
   if self.enemy[2].vivo==1:
    self.a_opcao=2
    self.inimigo_exite=1
  if self.alvo_existe==0:
   self.terminar_combate()
 def ativa_atk_protag(self):
  while len(self.usando)>0 and len(self.l_alvos)>0:
   if len(self.usando)>1:
    if lista_ataque[self.usando[0].num][self.usando[1].num].categ=="combinar":
     self.atacar_protag(protagonista,lista_ataque[self.usando[0].num][self.usando[1].num].alvo,self.l_alvos[1],lista_ataque[self.usando[0].num][self.usando[1].num].dano,lista_ataque[self.usando[0].num][self.usando[1].num].escudo,lista_ataque[self.usando[0].num][self.usando[1].num].efeitoA,lista_ataque[self.usando[0].num][self.usando[1].num].chanceA,lista_ataque[self.usando[0].num][self.usando[1].num].stacksA,lista_ataque[self.usando[0].num][self.usando[1].num].duracaoA,lista_ataque[self.usando[0].num][self.usando[1].num].efeitoB,lista_ataque[self.usando[0].num][self.usando[1].num].chanceB,lista_ataque[self.usando[0].num][self.usando[1].num].stacksB,lista_ataque[self.usando[0].num][self.usando[1].num].duracaoB,lista_ataque[self.usando[0].num][self.usando[1].num].stat,lista_ataque[self.usando[0].num][self.usando[1].num].tags)
    else:
     self.atacar_protag(protagonista,lista_ataque[self.usando[0].num].alvo,self.l_alvos[1],lista_ataque[self.usando[0].num].dano,lista_ataque[self.usando[0].num].escudo,lista_ataque[self.usando[0].num].efeitoA,lista_ataque[self.usando[0].num].chanceA,lista_ataque[self.usando[0].num].stacksA,lista_ataque[self.usando[0].num].duracaoA,lista_ataque[self.usando[0].num].efeitoB,lista_ataque[self.usando[0].num].chanceB,lista_ataque[self.usando[0].num].stacksB,lista_ataque[self.usando[0].num].duracaoB,lista_ataque[self.usando[0].num].stat,lista_ataque[self.usando[0].num].tags)
     self.atacar_protag(protagonista,lista_ataque[self.usando[1].num].alvo,self.l_alvos[1],lista_ataque[self.usando[1].num].dano,lista_ataque[self.usando[1]].escudo,lista_ataque[self.usando[1]].efeitoA,lista_ataque[self.usando[1].num].chanceA,lista_ataque[self.usando[1].num].stacksA,lista_ataque[self.usando[1].num].duracaoA,lista_ataque[self.usando[1].num].efeitoB,lista_ataque[self.usando[1].num].chanceB,lista_ataque[self.usando[1].num].stacksB,lista_ataque[self.usando[1].num].duracaoB,lista_ataque[self.usando[1].num].stat,lista_ataque[self.usando[1].num].tags)
    del self.usando[0]
    del self.l_alvos[0]
   else:
     self.atacar_protag(protagonista,lista_ataque[self.usando[0].num].alvo,self.l_alvos[0],lista_ataque[self.usando[0].num].dano,lista_ataque[self.usando[0].num].escudo,lista_ataque[self.usando[0].num].efeitoA,lista_ataque[self.usando[0].num].chanceA,lista_ataque[self.usando[0].num].stacksA,lista_ataque[self.usando[0].num].duracaoA,lista_ataque[self.usando[0].num].efeitoB,lista_ataque[self.usando[0].num].chanceB,lista_ataque[self.usando[0].num].stacksB,lista_ataque[self.usando[0].num].duracaoB,lista_ataque[self.usando[0].num].stat,lista_ataque[self.usando[0].num].tags)
   del self.usando[0]
   del self.l_alvos[0]
 def terminar_turno(self):
  self.turno="a"
  if len(protagonista.eco_atri)==0:
   protagonista.eco_atri.append(0)
  if art_soco_a in self.art_obt:
   protagonista.eco_atri[0]=protagonista.eco_atri[0]+1
  if art_soco_b in self.art_obt:
   protagonista.eco_atri[0]=protagonista.eco_atri[0]+1
  if art_soco_c in self.art_obt:
   protagonista.eco_atri[0]=protagonista.eco_atri[0]+1
  self.ativa_atk_protag()
  self.ativar_dot(protagonista)
  self.soco_ativar(protagonista)
  self.gerar_atk_e()
  self.ativa_atk_e()
  for i in self.enemy:
   if i.HP<1:
    i.vivo=0
   if i.vivo==1:
    self.ativar_dot(i)
    if art_gas in self.art_obt:
     self.ativar_dot(i)
    self.soco_ativar(i)
   for j in i.buff_atri:
    if j>0:
     j=j-1
   for j in i.debuff_atri:
    if j>0:
     j=j-1
   if i.HP<1:
    i.vivo=0
   if len(i.ven_atri)>0:
    del i.ven_atri[0]
   if len(i.eco_atri)>0:
    del i.eco_atri[0]
  for j in protagonista.buff_atri:
   if j>0:
    j=j-1
  for j in protagonista.debuff_atri:
   if j>0:
    j=j-1
  if protagonista.HP<1:
   self.derrota()
  if len(protagonista.ven_atri)>0:
   del protagonista.ven_atri[0]
  if len(protagonista.eco_atri)>0:
   del protagonista.eco_atri[0]
 def duplicar_debuff(self,alvo):
  self.ven_falso=[]
  for i in alvo.ven_atri:
   self.ven_falso.append(0)
   self.ven_falso.append(i)
  alvo.ven_atri=copy.copy(self.ven_falso)
  for j in alvo.debuff_atri:
   j=j*2
 def ativar_dot(self,alvo):
  self.dano_dot=0
  for i in alvo.ven_atri:
   self.dano_dot=self.dano_dot+i
  if alvo!=protagonista:
   self.escudo=self.escudo+dano_dot
  if alvo.debuff_atri[7]>0:
   self.dot_multi=3
  else:
   self.dot_multi=2
  self.dano_dot=self.dano_dot*self.dot_multi
  if alvo.escudo>self.dano_dot:
   alvo.escudo=alvo.escudo-self.dano_dot
  else:
   alvo.HP=alvo.HP-(self.dano_dot-alvo.HP)
 def enter_map(self):#0.vazio 1.batalha,2.evento,3.loja,4.batalha elite, 5.aleatorio
  if self.progresso>7:
   self.progresso==1
  else:
   self.progresso=self.progresso+1
  self.vazio=0
  self.room="mapa"
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
  if self.progresso==8:
   self.sala1=0 
   self.sala3=0
   if self.nivel==1:
    self.sala2=10
   if self.nivel==1.5:
    self.sala2=11
 def update(self):
  if self.animar_t<0:
   self.animar_t=self.animar_t-1
  self.ret=0
  if self.ret_bon>0:
   self.ret_bon=self.ret_bon-1
  if self.ret==1:
   self.ret_bon=2
  if pyxel.btnp(pyxel.KEY_M):
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
     self.progresso=0
     self.nivel=1
     protagonista.HP_max=100
     protagonista.HP=100
     protagonista.ATK_base=10
     protagonista.DEF_base=10
     self.gold=200
     self.enter_map()
     self.armas_e=[]
     self.armas_g=[]
     self.ganhar_arma()
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
   if pyxel.btnp(pyxel.KEY_B):
    self.progresso=7
   if self.e_room=="arma":
    self.escolheu=0
    self.escolha=0
    if self.ret==0:
     if pyxel.btnp(pyxel.KEY_A):
      self.escolha=0
      self.escolheu=1
      self.ret=1
     if pyxel.btnp(pyxel.KEY_W):
      self.escolha=1
      self.ret=1
      self.escolheu=1
     if pyxel.btnp(pyxel.KEY_D):
      self.escolha=2
      self.escolheu=1
      self.ret=1
    if self.escolheu==1:
     if self.escolha_arma[self.escolha] in lista_arma_g:
      if len(self.armas_g)>1:
       self.troca_arma(self.escolha_arma[self.escolha])
      else:
       self.armas_g.append(self.escolha_arma[self.escolha])
       self.armas=[]
       self.e_room=""
     if self.escolha_arma[self.escolha] in lista_arma_e:
      if len(self.armas_e)>0:
       self.troca_arma(self.escolha_arma[self.escolha])
      else:
       self.armas_e.append(self.escolha_arma[self.escolha])
       self.e_room=""
     self.armas=[]
     for i in self.armas_e:
      self.armas.append(i)
     for i in self.armas_g:
      self.armas.append(i)
     if len(self.armas)<2:
      self.ganhar_arma()
   if self.e_room=="troca":
    self.escolheu=0
    self.escolha=0
    if self.ret==0:
     if pyxel.btnp(pyxel.KEY_A):
      self.escolha=0
      self.escolheu=1
      self.ret=1
     if pyxel.btnp(pyxel.KEY_W):
      self.escolha=1
      self.escolheu=1
      self.ret=1
     if pyxel.btnp(pyxel.KEY_D):
      self.escolha=2
      self.escolheu=1
      self.ret=1
    if self.escolheu==1:
     if self.escolha==2:
      self.e_room=""
     else:
      del self.armas_g[self.escolha]
      self.armas_g.append(self.alterar_a)
      self.e_room=""
     if len(self.armas)<2:
      self.ganhar_arma()
   if self.e_room=="troca_e":
    self.escolheu=0
    self.escolha=0
    if self.ret==0:
     if pyxel.btnp(pyxel.KEY_A):
      self.escolha=0
      self.escolheu=1
      self.ret=1
     if pyxel.btnp(pyxel.KEY_D):
      self.escolha=1
      self.escolheu=1
      self.ret=1
    if self.escolheu==1:
     if self.escolha==0:
      self.armas_e[0]=self.alterar_a
     self.e_room=""
   if self.e_room=="":
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
      if self.mostrar==10:
       self.enter_boss("cog1")
      if self.mostrar==11:
       self.enter_boss("cacto1")
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
   if self.e_room=="":
    if self.room=="evento":
     if self.ret==0:
      if pyxel.btnp(pyxel.KEY_RETURN):
       self.enter_map()
       self.ret=1
    if self.room=="loja":
     if pyxel.btnp(pyxel.KEY_D):
      self.opcao=self.opcao+1
      if self.opcao>7:
       self.opcao=0
     if pyxel.btnp(pyxel.KEY_A):
      self.opcao=self.opcao-1
      if self.opcao<0:
       self.opcao=7
     if self.produtos[self.opcao]!="x":
      if pyxel.btnp(pyxel.KEY_W):
       if self.gold>=self.precos[self.opcao]:
        self.gold=self.gold-self.precos[self.opcao]
        if self.produtos[self.opcao]=="arma":
         self.ganhar_arma()
        elif self.produtos[self.opcao].categ=="item":
         self.item_lista[self.produtos[self.opcao].id]=self.item_lista[self.produtos[self.opcao].id]+1
        elif self.produtos[self.opcao].categ=="art":
         self.produtos[self.opcao].obtido=1
         self.art_obt.append(self.produtos[self.opcaos])
        self.produtos[self.opcao]="x"
     if self.ret==0:
      if pyxel.btnp(pyxel.KEY_RETURN):
       self.enter_map()
       self.ganhar_arma()
       self.ret=1
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
     self.cont_items_a=0
     self.items_available=[]
     for i in self.item_lista:
      if i>0: 
       self.items_available.append(self.cont_items_a)
       self.cont_items_a=self.cont_items_a+1
     self.item_existe=0
     if len(self.items_available)>0:
      self.item_existe=1
     if self.item_existe==1:
      if pyxel.btnp(pyxel.KEY_O):
       self.item_opcao=self.item_opcao+1
       if len(self.items_available)-1<self.item_opcao:
        self.item_opcao=0
      if pyxel.btnp(pyxel.KEY_U):
       self.item_opcao=self.item_opcao-1
       if self.item_opcao<0:
        self.item_opcao=len(self.items_available)-1
       else:
        self.item_opcao=0
      if pyxel.btnp(pyxel.KEY_I):
       self.usar_item(l_item[self.item_available[self.item_opcao]])
       self.item_lista[self.item_available[self.item_opcao]]=self.item_lista[self.item_available[self.item_opcao]]-1
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
     if pyxel.btnp(pyxel.KEY_RETURN):
      if self.ret==0:
       self.ret=1
       self.terminar_turno()
       self.iniciar_turno()
 def draw(self):#draw
  if self.state=="menu":
   pyxel.cls(3)
   pyxel.text(20,50,"JOGAR",0)
   pyxel.text(20,60,"DECK",0)
   pyxel.text(20,70,"SAIR",0)
   pyxel.blt(200,100,2,16,7,151,20,colkey=7,scale=3)
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
   pyxel.blt(400,15,0,48,48,15,15,colkey=5)
   self.mostra_g=str(self.gold)
   pyxel.text(420,20,self.mostra_g,10)
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
   if self.e_room=="arma":
    pyxel.cls(1)
    self.arma_x=50
    self.ganha_c=0
    pyxel.blt(50,300,0,96,160,15,15,colkey=5,scale=2)
    pyxel.blt(250,300,0,80,160,15,15,colkey=5,scale=2)
    pyxel.blt(450,300,0,96,176,15,15,colkey=5,scale=2)
    while self.ganha_c<3:
     if self.escolha_arma[self.ganha_c].nome=="espada":
      pyxel.blt(self.arma_x,200,0,48,80,15,15,colkey=5,scale=4)
     if self.escolha_arma[self.ganha_c].nome=="escudo":
      pyxel.blt(self.arma_x,200,0,0,96,15,15,colkey=5,scale=4)
     if self.escolha_arma[self.ganha_c].nome=="varinha":
      pyxel.blt(self.arma_x,200,0,32,80,15,15,colkey=5,scale=4)
     if self.escolha_arma[self.ganha_c].nome=="jato":
      pyxel.blt(self.arma_x,200,0,16,96,15,15,colkey=5,scale=4)
     if self.escolha_arma[self.ganha_c].nome=="veneno":
      pyxel.blt(self.arma_x,200,0,48,32,15,15,colkey=5,scale=4)
     if self.escolha_arma[self.ganha_c].nome=="luz":
      pyxel.pal(2,7)
      pyxel.blt(self.arma_x,200,0,48,32,15,15,colkey=5,scale=4)
     if self.escolha_arma[self.ganha_c].nome=="pedra":
      pyxel.pal(2,9)
      pyxel.blt(self.arma_x,200,0,48,32,15,15,colkey=5,scale=4)
     self.ganha_c=self.ganha_c+1
     self.arma_x=self.arma_x+200
     pyxel.pal()
   if self.e_room=="":
    if self.room=="mapa":
     self.mostra_progresso=str(self.progresso)
     pyxel.text(300,10,self.mostra_progresso,2)
     pyxel.text(310,10,"de 8",2)
     pyxel.cls(1)
     if self.opcao==1:
      pyxel.tri(40,360,170,360,105,100,16)
      pyxel.elli(40,340,130,40,5)
      self.x=95
      self.y=220
      self.mostrar=self.sala1
     if self.opcao==2:
      pyxel.tri(210,360,340,360,270,100,16)
      pyxel.elli(210,340,130,40,5)
      self.x=265
      self.y=220
      self.mostrar=self.sala2
     if self.opcao==3:
      pyxel.tri(380,360,510,360,440,100,16)
      pyxel.elli(380,340,130,40,5)
      self.x=435
      self.y=220
      self.mostrar=self.sala3
     if self.opcao==0:
      self.mostrar=-1
     if self.opcao!=0:
      if self.mostrar==0:
       pyxel.blt(self.x,self.y,0,64,112,15,15,colkey=1,scale=3)
      if self.mostrar==1:
       pyxel.blt(self.x,self.y,0,16,112,15,15,colkey=1,scale=3)
      if self.mostrar==2:
       pyxel.blt(self.x,self.y,0,32,96,15,15,colkey=1,scale=3)
      if self.mostrar==4:
       pyxel.blt(self.x,self.y,0,16,112,15,15,colkey=1,scale=3)
       pyxel.blt(self.x,self.y-20,0,0,112,15,15,colkey=1,scale=3)
      if self.mostrar==3:
       pyxel.blt(self.x,self.y,0,32,112,15,15,colkey=1,scale=3)
      if self.mostrar==10:
       pyxel.blt(self.x-20,self.y+200,0,136,216,64,191,colkey=6,scale=3)
      if self.mostrar==11:
       pyxel.blt(self.x-20,self.y,1,128,128,38,38,colkey=6,scale=3)
      if self.mostrar==5:
       pyxel.pal(10,9)
       pyxel.blt(self.x,self.y,0,48,96,15,15,colkey=1,scale=3)
       pyxel.pal()
   if self.room=="batalha": #batalhas
    pyxel.cls(2)
    for i in self.enemy:
     if len(self.enemy)==2:
      if i.local==1:
       self.e_x=200
      if i.local==2:
       self.e_x=200
     if len(self.enemy)==3:
      if i.local==1:
       self.e_x=100
      if i.local==2:
       self.e_x=250
      if i.local==3:
       self.e_x=400
      if i.vivo==1:
       if i.nome=="fada":
        pyxel.blt(self.e_x-22,200,0,109,11,22,25,colkey=5,scale=2)
       if i.nome=="morcego":
        pyxel.blt(self.e_x-20,200,0,65,0,20,14,colkey=5,scale=2)
       if i.nome=="cogumelo":
        pyxel.blt(self.e_x,150,0,64,84,15,15,colkey=5,scale=2)
       if i.nome=="demonio":
        pyxel.blt(self.e_x,100,0,132,137,60,70,colkey=5,scale=3)
       if i.nome=="pessoa cogumelo":
        pyxel.blt(self.e_x,100,0,170,65,34,50,colkey=5,scale=2)
       if i.nome=="golem":
        pyxel.blt(self.e_x,100,0,200,100,54,57,colkey=5,scale=3)
       if i.nome=="armadura":
        pyxel.blt(self.e_x,100,0,80,56,34,47,colkey=5,scale=3)
       if i.nome=="slime":
        pyxel.blt(self.e_x,100,0,80,32,33,18,colkey=5,scale=3)
       if i.nome=="cogumelo mestre":
        pyxel.blt(self.e_x,100,1,0,48,63,64,colkey=2,scale=3)
       if i.nome=="cacto1":
        pyxel.blt(self.e_x,100,1,0,190,63,65,colkey=2,scale=3)
       if i.nome=="cacto2":
        pyxel.blt(self.e_x,100,1,0,120,63,71,colkey=2)
       if i.nome=="flor":
        pyxel.blt(self.e_x,200,1,64,240,15,15,colkey=2)
       self.mostrar_hp=str(i.HP)
       self.mostrar_escudo=str(i.escudo_atri)
       self.debuff_em=0
       self.buff_em=0
       self.ven_em=0
       self.eco_em=0
       for j in i.eco_atri:
        self.eco_em=self.eco_em+1
       for j in i.ven_atri:
        self.ven_em=self.ven_em+1
       for j in i.buff_atri:
        if  j>0:
         self.buff_em=self.buff_em+1
       for j in i.debuff_atri:
        if  j>0:
         self.debuff_em=self.debuff_em+1

       self.mostrar_buff=str(self.buff_em)
       self.mostrar_debuff=str(self.debuff_em)
       self.mostrar_ven=str(self.ven_em)
       self.mostrar_eco=str(self.eco_em)
       pyxel.text(self.e_x,200,self.mostrar_hp,3)
       pyxel.text(self.e_x-5,200,self.mostrar_escudo,6)
       pyxel.text(self.e_x-10,200,self.mostrar_buff,7)
       pyxel.text(self.e_x+5,200,self.mostrar_debuff,14)
       pyxel.text(self.e_x+10,200,self.mostrar_ven,2)
       pyxel.text(self.e_x+15,200,self.mostrar_eco,10)
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
     if self.ret_bon==0:
      self.opcao_max=len(self.mao)-1
      if len(self.mao)>0:
       self.i=self.mao[self.opcao].nome
       if self.opcao-1==-1:
        self.e=self.mao[self.opcao_max].nome
       else:
        self.e=self.mao[self.opcao-1].nome
       if self.opcao+1==self.opcao_max+1:
        self.o=self.mao[0].nome
       else:
        self.o=self.mao[self.opcao+1].nome
       pyxel.text(250,390,self.e,17)
       pyxel.text(300,390,self.i,17)
       pyxel.text(350,390,self.o,17)
   if self.e_room=="":
    if self.room=="evento":
     pyxel.cls(1)
     pyxel.blt(265,300,0,112,160,15,15,colkey=5,scale=2)
     if self.reward=="atk":
      pyxel.pal(8,9)
      pyxel.pal()
      pyxel.blt(265,265,0,216,0,15,15,colkey=5,scale=3)
     elif self.reward=="def":
      pyxel.blt(265,265,0,96,128,15,15,colkey=5,scale=3)
     elif self.reward=="hp":
      pyxel.blt(265,265,0,80,128,15,15,colkey=5,scale=3)
     elif self.reward=="ap":
      pyxel.blt(265,265,0,136,112,15,15,colkey=5,scale=3)
     elif self.reward=="arma":
      pyxel.blt(265,265,0,48,96,15,15,colkey=1,scale=3)
     else:
      self.reward=str(self.reward)
      pyxel.text(365,365,self.reward,10)
    if self.room=="loja":
     pyxel.cls(4)
     self.loja_x=1
     self.loja_y=1
     self.prod_atual=0
     for i in self.produtos:
      self.x_fin=16
      self.y_fin=16
      self.clr_spr=0
      if i=="arma":
       self.x_ini=216
       self.y_ini=0
       self.x_fin=15
       self.y_fin=15
      if type(i)==str:
       self.abbsc=1
      elif i.nome==("cura_s" or "antidoto_s" or "spray_s" or "soco_s" or "escudo_s"):
       self.x_ini=8
       self.y_ini=32
       self.x_fin=8
       self.y_fin=8
      elif i.nome==("cura_m" or "antidoto_m" or "spray_m" or "soco_m" or "escudo_m" or "defesa" or "poder" or "protecao" or "cafe" or "velocidade" or "energetico"):
       self.x_ini=32
       self.y_ini=32
       self.x_fin=15
       self.y_fin=15
      elif i.nome==("cura_l" or "antidoto_l" or "spray_l" or "soco_l" or "escudo_l"):
       self.x_ini=0
       self.y_ini=48
       self.x_fin=15
       self.y_fin=15
      elif i.nome==("bomba_s" or "fumaca"):
       self.x_ini=0
       self.y_ini=32
       self.x_fin=8
       self.x_fin=8
      elif i.nome=="bomba_m":
       self.x_ini=16
       self.y_ini=32
       self.clr_spr=0
      elif i.nome=="bomba_l":
       self.x_ini=0
       self.y_ini=16
       self.clr_spr=0
      elif i.nome=="lixeira":
       self.x_ini=32
       self.y_ini=16
       self.clr_spr=0
      elif i.nome=="virus":
       self.x_ini=48
       self.y_ini=16
       self.clr_spr=0
      elif i.nome=="coffe":
       self.x_ini=16
       self.y_ini=48
       self.clr_spr=0
      elif i.nome=="moeda":
       self.x_ini=32
       self.y_ini=48
       self.clr_spr=0
      elif i.nome=="gaz venenoso":
       self.x_ini=16
       self.y_ini=80
       self.clr_spr=0
      elif i.nome==("soco a"  or "soco b" or "soco c"):
       self.x_ini=16
       self.y_ini=64
      elif i.nome==("baralho_s" or "baralho_m" or "baralho_l"):
       self.x_ini=0
       self.y_ini=80
       self.clr_spr=0
      elif i.nome=="baralho_x":
       self.x_ini=48
       self.y_ini=112
       self.clr_spr=0
      elif i.nome=="armadura enferrujada":
       self.x_ini=48
       self.y_ini=64
       self.clr_spr=0
      elif i.nome=="espada enferrujada":
       self.x_ini=32
       self.y_ini=64
       self.clr_spr=0
      if i!="arma":
       if i.nome==("cura_s" or "cura_m" or "cura_l"):
        self.clr_spr=0
       if i.nome==("antidoto_s" or "antidoto_m" or "antidoto_l"):
        self.clr_spr=7
       if i.nome==("spray_s" or "spray_m" or "spray_l"):
        self.clr_spr=2
       if i.nome==("fumaca" or "energetico"):
        self.clr_spr=13
       if i.nome==("soco_s" or "soco_m" or "soco_l"):
        self.clr_spr=10
       if i.nome==("escudo_s" or "escudo_m" or "escudo_l"):
        self.clr_spr=12
       if i.nome=="velocidade":
        self.clr_spr=11
       if i.nome=="velocidade":
        self.clr_spr=9
       if i.nome=="defesa":
        self.clr_spr=3
       if i.nome=="protecao":
        self.clr_spr=6
      pyxel.pal()
      if self.clr_spr!=0:
       pyxel.pal(8,self.clr_spr)
       pyxel.pal(10,self.clr_spr)
       pyxel.pal(1,self.clr_spr)
      if self.opcao+1==self.loja_x*self.loja_y:
       pyxel.circ(100+self.loja_x*40,150*self.loja_y,30,0)
      pyxel.blt(100+self.loja_x*100,150*self.loja_y,0,self.x_ini,self.y_ini,self.x_fin,self.y_fin,colkey=5,scale=3)
      self.mostra_preco=self.loja_x*self.loja_y
      self.mostra_preco=str(self.precos[self.mostra_preco-1])
      pyxel.text(100+self.loja_x*100,(150*self.loja_y)+20,self.mostra_preco,0)
      self.loja_x=self.loja_x+1
      if self.loja_x>4:
       self.loja_x=1
       self.loja_y=self.loja_y+1
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
espada=arma([corte,grito],"espada")
escudo=arma([bloquear,surrar],"escudo")
varinha=arma([encanto,missil],"varinha")
jato_D_agua=arma([jato,encharcar],"jato")
e_luz=arma([luz],"luz")
e_veneno=arma([envenenar],"veneno")
e_pedra=arma([pedra],"pedra")
e_fungos=arma([fungo],"pedra")
lista_arma=(espada,escudo,varinha,jato_D_agua,e_luz,e_veneno,e_pedra)
lista_arma_g=(espada,escudo,varinha,jato_D_agua)
lista_arma_e=(e_luz,e_veneno,e_pedra)
baralho_universal=[corte,grito,bloquear,surrar,encanto,missil,jato,encharcar,luz,envenenar,pedra]
#efeito:0 nada, 1 veneno,2 petrificar-40% de buffs errarem, 3 cegueira-40% de atks errarem, 4 stun, 5 colecao de esporos(atk-,atk+,def-, def+,ap+,ap-,esquiva,remover1buff,remover1debuff,veneno,eco,fortalecer,esporos,corrupcao), 6 atack up, 7 def up, 8 atk down, 9 def down, A ap+(6max), B parasitar, C esquiva, D conjunto de buffs(atk,def,esquiva,ap+(6max)), E repetir, 10 dano extra, 11 colecao de debuffs(,atk-,def-,ap-,descuido), 12 duplicar debuffs,13 esporos, 14 purificar. 15 endurecer, 16 roubo de hp, 17 fortalecer-30% dano recebido, 18 ativar dot, 19 remover duracao, 1A corruption- 1.5 dano de dot, 1B transferencia de efeitos, 1C propagar-"30% da carta ter efeitos dobrados", 1D parasitar- 1 escudo ao ativar veneno, 1E imunidade, 20 toxicidade, 21 hype- repete uma carta aleatória no final do turno,22 parry- bloqueia 1 dano,23espinho-24reflete 30% do dano,25respingar,26 fortificar-50% mais escudo,27 intimidar-20% de chance de stun por ataque, 28 enviar efeitos negativos,29-remover buffs,2A vitalidade-atk+50%def,def+50%atk,2B remove% de escudo,2C comparilha dano recebido 25%,2D atrai dano dos outros 25%, 2E lança 1 soco pr stack ao final do turno, 30-solidificar-- aumenta o dano dos socos em 2x, 31 raiva- aumenta dano dado e recebido em 1.5x,32-sabotagem- aplica 1 colecao de debuffs por atk
corte2=combinacao("corte","1",60,0,0,0,0,0,0,0,0,0,"atk",["atk"])
grito2=combinacao("grito","self",0,0,"6",100,3,2,0,0,0,0,"atk",["buff"])
destruir=combinacao("destruir","todos_E",55,0,0,0,0,0,0,0,0,0,"atk",["atk"])
esmagar=combinacao("esmagar","1",25,0,0,0,0,0,0,0,0,0,"escudo",["atk"])
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
pedra2=combinacao("endurecer","self",0,"5",15,100,2,1,0,0,0,0,"def",["buff"])
fungos2=combinacao("felicidade","self",0,0,"5",100,2,2,13,100,1,1,"atk",["buff","debuff"])
consumir=combinacao("consumir","1",50,0,"16",70,1,1,0,0,0,0,"atk+def",["atk","buff"])
fortalecer=combinacao("fortalecer","self",0,"25",17,100,1,2,0,0,0,0,"atk",["buff"])
ativador=combinacao("ativador","1",0,0,18,100,2,1,19,100,1,1,"atk",["debuff"])
corromper=combinacao("corromper","1",0,0,"1A",100,1,2,0,0,0,0,"atk",["debuff"])
curse=combinacao("amaldicoar","1",0,0,"1B",100,"random",1,0,0,0,0,"atk",["debuff"])
propagar=combinacao("propagar","self",0,0,"1C",100,1,2,0,0,0,0,"atk",["buff"])
cegar=combinacao("cegar","1",0,0,"3",100,1,2,0,0,0,0,"atk",["debuff"])
parasitar=combinacao("parasitar","self",0,20,"1D",100,1,2,0,0,0,0,"def",["buff"])
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
endurecer=combinacao("vitalidade","self",0,0,"2A",100,1,2,0,0,0,0,"atk",["buff"])
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
pedra_s=combinacao("pedra","self",0,0,15,50,2,1,0,0,0,0,"def",["buff"])
fungos_s=combinacao("fungo","todos",0,0,5,100,1,2,0,0,0,0,"atk",["buff","debuff"])
#ataque monstros
fada1=inimigo_atk("aliados_t",0,0,"D",100,1,2,0,0,0,0,"atk",["buff"])
fada2=inimigo_atk("1",15,0,"E",100,2,4,0,0,0,0,"atk",["atk"])
golem1=inimigo_atk("self",0,15,0,0,0,0,0,0,0,0,"def",["buff"])
golem2=inimigo_atk("1",60,0,0,0,0,0,0,0,0,0,"atk",["atk"])
cogumelo1=inimigo_atk("self",0,0,5,100,2,2,13,100,1,1,"atk",["buff","debuff"])
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
pessoac_2=inimigo_atk("self",0,0,5,100,2,2,13,100,1,1,"atk",["buff","debuff"])
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
inimigo_l=[fada,cogumelo,morcego,pessoac]#combinacoes acabam aqui
inimigo_elite=[golem,demonio,slime,i_armadura]
i_cura_s=item_ind("cura_s",20,0,0,0,0,0,20,0)
i_cura_m=item_ind("cura_m",45,0,0,0,0,0,35,1)
i_cura_l=item_ind("cura_l",70,0,0,0,0,0,55,2)
i_antidoto_s=item_ind("antidoto_s",0,0,0,1,1,1,20,3)
i_antidoto_m=item_ind("antidoto_m",0,0,0,1,2,1,30,4)
i_antidoto_l=item_ind("antidoto_l",0,0,0,1,4,1,60,5)
i_baralho_s=item_ind("baralho_s",0,0,0,2,1,1,20,6)
i_baralho_m=item_ind("baralho_m",0,0,0,2,2,1,30,7)
i_baralho_l=item_ind("baralho_l",0,0,0,2,4,1,40,8)
i_baralho_x=item_ind("baralho_x",0,0,0,3,4,1,60,9)
i_spray_s=item_ind("spray_s",0,0,0,4,2,2,20,10)
i_spray_m=item_ind("spray_m",0,0,0,4,4,2,40,11)
i_spray_l=item_ind("spray_l",0,0,0,4,7,2,60,12)
i_protecao=item_ind("protecao",0,0,0,5,1,1,40,13)
i_cafe=item_ind("coffe",0,0,0,6,1,2,50,14)
i_poder=item_ind("poder",0,0,0,7,1,2,35,15)
i_defesa=item_ind("defesa",0,0,0,8,1,2,35,16)
i_velocidade=item_ind("velocidade",0,0,0,9,1,2,40,17)
i_virus=item_ind("virus",0,0,0,10,1,2,40,18)
i_soco_e_s=item_ind("soco_s",0,0,0,11,1,2,35,19)
i_soco_e_m=item_ind("soco_m",0,0,0,11,2,2,50,20)
i_soco_e_l=item_ind("soco_l",0,0,0,11,4,2,65,21)
i_lixeira=item_ind("lixeira",0,0,0,12,1,1,40,22)
i_energetico=item_ind("energia",0,0,0,13,2,1,50,23)
i_bomba_s=item_ind("bomba_s",0,0,20,0,0,0,30,24)
i_bomba_m=item_ind("bomba_m",0,0,40,0,0,0,50,25)
i_bomba_l=item_ind("bomba_l",0,0,60,0,0,0,70,26)
i_bomba_f=item_ind("fumaca",0,0,0,14,2,1,30,27)
i_escudo_s=item_ind("escudo_s",0,15,0,0,0,0,30,28)
i_escudo_m=item_ind("escudo_m",0,35,0,0,0,0,50,29)
i_escudo_l=item_ind("escudo_l",0,50,0,0,0,0,70,30)
art_moeda=artefato_ind(75,"moeda")
art_soco_a=artefato_ind(75,"soqueira a")
art_soco_b=artefato_ind(75,"soqueira b")
art_soco_c=artefato_ind(75,"soqueira c")
art_gas=artefato_ind(75,"gas venenoso")
art_escudo=artefato_ind(75,"armadura enferrujada")
art_espada=artefato_ind(75,"espada enferrujada")
boss_cog=inimigo("cogumelo mestre",250,14,10,(cogumelo1,cogumelo2))
boss_cacto1=inimigo("cacto",200,14,10,[cogumelo1,cogumelo2])
boss_cacto2=inimigo("cacto2",200,14,10,[cogumelo1,cogumelo2])
cacto_flor=inimigo("flor",50,102,8,[cogumelo1,cogumelo2])
a_cacto1=inimigo_atk("self",0,0,"23",100,2,1,0,0,0,0,"atk",["buff"])
a_cacto2=inimigo_atk("1",40,0,"2B",100,50,1,0,0,0,0,"atk",["atk"])
l_artefatos=[art_moeda,art_soco_a,art_soco_b,art_soco_c,art_gas,art_escudo,art_espada]
l_items=[i_cura_s,i_cura_m,i_cura_l,i_antidoto_s,i_antidoto_m,i_antidoto_l,i_baralho_s,i_baralho_m,i_baralho_l,i_baralho_x,i_spray_s,i_spray_m,i_spray_l,i_protecao,i_cafe,i_poder,i_defesa,i_velocidade,i_virus,i_soco_e_s,i_soco_e_m,i_soco_e_l,i_lixeira,i_energetico,i_bomba_s,i_bomba_m,i_bomba_l,i_bomba_f,i_escudo_s,i_escudo_m,i_escudo_l]
individuais=[corte_s,grito_s,bloquear_s,surrar_s,encanto_s,missil_s,jato_s,encharcar_s,luz_s,veneno_s,pedra_s,fungos_s]
lista_ataque=[[corte2,destruir,consumir,tremor,receptor,pesado,esplosao,compartilhar,rebater,expurgo,quebrar,cor_f],[destruir,grito2,intimidar,fortalecer,raiva,refletir,bolha,sabotar,bencao,toxicidade,endurecer,gr_f],[consumir,fortalecer,bloquear2,esmagar,eco,acolher,recochete,cobertura,impenetravel,parasitar,fortificar,es_f],[tremor,intimidar,esmagar,surrar2,solidificar,meteoritos,pressao,apedrejar,converter,respingo,pedrada,sur_f],[receptor,raiva,eco,solidificar,encanto2,barragem,barreira,propagar,animar,curse,parede,enc_f],[pesado,refletir,acolher,meteoritos,barragem,missil2,raios,metralhar,estrela,chuva,granizo,mis_f],[esplosao,bolha,recochete,pressao,barreira,raios,jato2,imundar,transferencia,ativador,corroer,jat_f],[compartilhar,sabotar,cobertura,apedrejar,propagar,metralhar,imundar,encharcar2,cegar,corromper,petrificar,ench_f],[rebater,bencao,impenetravel,converter,animar,estrela,transferencia,cegar,luz2,v_l,p_l,l_f],[expurgo,toxicidade,parasitar,respingo,curse,chuva,ativador,corromper,v_l,envenenar2,v_p,v_f],[quebrar,endurecer,fortificar,pedrada,parede,granizo,corroer,petrificar,p_l,v_p,pedra2,p_f],[cor_f,gr_f,es_f,sur_f,enc_f,enc_f,jat_f,ench_f,l_f,v_f,p_f,fungos2]]
jogo()
