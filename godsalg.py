#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
from sys import exit
import time
import os 
import random

try: 
  if os.name == 'nt':
        os.system("cls")
  else:
        os.system("clear")
  time.sleep(0.3)
  print()
  print()   #\033[0m\033[38;2;157;34;53m\033[48;2;220;220;220m
  print()
  print("\033[38;2;220;220;220m")
  print("    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
  print("\033[0m    \033[38;2;220;220;220m┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                                                                    \033[0m\033[38;2;220;220;220m ┃")

  print("\033[0m    \033[38;2;220;220;220m┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ▄▄▄ ▄▄▄           ▄▄▄       ▄▄▄ ▄▄▄▄▄▄▄   ▐     ▄▄▄▄            \033[0m\033[38;2;220;220;220m ┃") 
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███ ███           ███       ███ ███████  ██     ████            \033[0m\033[38;2;220;220;220m ┃")                
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███           ███     ███   ███     ███      ███                \033[0m\033[38;2;220;220;220m ┃")
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███    ▄▄▄▄   ███     ███   ███     ███      ███                \033[0m\033[38;2;220;220;220m ┃") 
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███    ████   ███     ███   ███     ███      ███  ███           \033[0m\033[38;2;220;220;220m ┃")
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███     ███   ███     ███   ███     ███           ███           \033[0m\033[38;2;220;220;220m ┃")
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███ ▄▄▄ ███   ███ ▄▄▄ ███   ███ ▄▄▄▄███       ▄▄▄▄███           \033[0m\033[38;2;220;220;220m ┃")
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m    ███ ███ ███       ███       ███ ███████       ████              \033[0m\033[38;2;220;220;220m ┃")

  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                                                                    \033[0m\033[38;2;220;220;220m ┃")
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                                                                    \033[0m\033[38;2;220;220;220m ┃")


  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                       ▄▄▄       ▄▄▄          ▄▄▄ ▄▄▄               \033[0m\033[38;2;220;220;220m ┃")                             
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                       ███       ███          ███ ███               \033[0m\033[38;2;220;220;220m ┃")                                                   
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                   ▄▄▄ ▄▄▄ ▄▄▄   ███          ███                   \033[0m\033[38;2;220;220;220m ┃")                                                       
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                   ███ ███ ███   ███          ███    ▄▄▄▄           \033[0m\033[38;2;220;220;220m ┃")                                                            
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                   ███     ███   ███          ███    ████           \033[0m\033[38;2;220;220;220m ┃")                                                                                  
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                   ███     ███   ███          ███     ███           \033[0m\033[38;2;220;220;220m ┃")                                                                                
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                   ███     ███   ███ ▄▄▄▄▄▄   ███ ▄▄▄ ███           \033[0m\033[38;2;220;220;220m ┃")                                                                                         
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                   ███     ███   ███ ██████   ███ ███ ███           \033[0m\033[38;2;220;220;220m ┃")  
  print("\033[0m    ┃ \033[38;2;157;34;53m\033[48;2;220;220;220m                                                                    \033[0m\033[38;2;220;220;220m ┃")
                                                                                                    
  print("\033[0m    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
  time.sleep(0.8)                                                                                                             
  


                                                                         
  print()
  print()                                                                          
  print()
  print("\033[38;2;200;200;200m  ┌┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┐")
  print("\033[38;2;200;200;200m  ┊ ###### Ciphering and de-ciphering program #####          ┊\033[0m")
  print("\033[38;2;200;200;200m  └┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┘")            
  time.sleep(0.8)
  print()
  print("\033[1;36m                                   Author\033[0m\033[1;32m:-\033[0m\033[1;33mrav0007  \033[0m")
  print()




  def calc_hash_256(filename):
      
      
        sha256_hash = hashlib.sha256()

        with open(filename,"rb") as f:

	    

                     for byte_block in iter(lambda: f.read(4096),b""):

                              sha256_hash.update(byte_block)

        return(sha256_hash.hexdigest())
  
  def veri_hash_256(filename):
      
      
        sha256_hash = hashlib.sha256()

        with open(filename,"rb") as f:

	  
                     f.seek(32)
                     for byte_block in iter(lambda: f.read(4096),b""):

                           sha256_hash.update(byte_block)

        return(sha256_hash.hexdigest())
      
  def veri_hash_512(filename):
      
      
        sha256_hash = hashlib.sha512()

        with open(filename,"rb") as f:


                     f.seek(32)
                     for byte_block in iter(lambda: f.read(4096),b""):

                             sha256_hash.update(byte_block)

        return(sha256_hash.hexdigest())
      
        
  def calc_hash_512(filename):
      
      
        sha256_hash = hashlib.sha512()

        with open(filename,"rb") as f:


                     for byte_block in iter(lambda: f.read(4096),b""):

                          sha256_hash.update(byte_block)

        return(sha256_hash.hexdigest())    
  

  def hex_to_dot(i):
     base={  '0' : '....' , 
             '1' : '... ' , 
             '2' : '.. .' , 
             '3' : '..  ' , 
             '4' : '. ..' , 
             '5' : '. . ' , 
             '6' : '.  .' , 
             '7' : '.   ' , 
             '8' : ' ...' , 
             '9' : ' .. ' , 
             'a' : ' . .' , 
             'b' : ' .  ' , 
             'c' : '  ..' , 
             'd' : '  . ' , 
             'e' : '   .'  , 
             'f' : '    ' } 
     result= base.get(i,"GONE wrong")
     return (result)
  
  def hex_to_dot_int(i):
     base={  '0' : '....' , 
             '1' : '... ' , 
             '2' : '.. .' , 
             '3' : '..  ' , 
             '4' : '. ..' , 
             '5' : '. . ' , 
             '6' : '.  .' , 
             '7' : '.   ' , 
             '8' : ' ...' , 
             '9' : ' .. ' , 
             '10' : ' . .' , 
             '11' : ' .  ' , 
             '12' : '  ..' , 
             '13' : '  . ' , 
             '14' : '   .'  , 
             '15' : '    ' } 
     result= base.get(i,"GONE wrong")
     return (result)    
    
  def dot_to_hex(i):
     base={ '....' : '0',
            '... ' : '1',
            '.. .' : '2',
            '..  ' : '3',
            '. ..' : '4',
            '. . ' : '5',
            '.  .' : '6',
            '.   ' : '7',
            ' ...' : '8',
            ' .. ' : '9',
            ' . .' : 'a',
            ' .  ' : 'b',
            '  ..' : 'c',
            '  . ' : 'd',
            '   .' : 'e',
            '    ' : 'f' } 
     result= base.get(i,"GONE wrong")
     return (result) 
 
    
  def int_to_hex(i):
     base={ 0 : '0',
            1 : '1',
            2 : '2',
            3 : '3',
            4 : '4',
            5 : '5',
            6 : '6',
            7 : '7',
            8 : '8',
            9 : '9',
            10 : 'a',
            11 : 'b',
            12 : 'c',
            13 : 'd',
            14 : 'e',
            15 : 'f' } 
     result= base.get(i,"GONE wrong")
     return (result)

 
  def hex_to_int(i):
     base={  '0' : 0,
             '1' : 1,
             '2' : 2,
             '3' : 3,
             '4' : 4,
             '5' : 5,
             '6' : 6,
             '7' : 7,
             '8' : 8,
             '9' : 9,
             'a' : 10,
             'b' : 11,
             'c' : 12,
             'd' : 13,
             'e' : 14,
             'f' : 15 } 
     result= base.get(i,"GONE wrong in hi")
     return (result) 

    
  def get_256(str):      
      str=str[-4:] 
      bin_not = conv_hash(str)
      return(bin_not)


  
  def  rano():
    global dict 
    dict = { x : ' ' for x in range(256) }
    ran = random.randint(0,255)
    generated_ran = ran 
    i=0
    for x in range(256):
          if  i==4:
              ran=(ran+1)%256 
              i=1
              dict[x] = ran
          else:
              dict[x] =(ran + (i*64))%256
              i+=1
    return generated_ran
  
    
  def get_dict_value(nume):
       return( dict.get(nume,"gone wrong"))
  
  def get_inv_dict_value(nume):  
      return(inv_dict.get(nume,256))  
    
  def  inv_rano(num):
    global inv_dict 
    inv_dict = { x : ' ' for x in range(256) }
    i=0
    for x in range(256): 
          if  i==4:
              num=(num+1)%256  
              i=1
              inv_dict[x] = num
          else:
              inv_dict[x] =( num + (i*64))%256 
              i+=1
    arr=[]
    for a in range(256): 
          arr.append(inv_dict[a])
    for j in range(256): 
           inv_dict[arr[j]] = j
    
  def get_the_ran_at_de(x):
       f=x[0]+x[1] 
       s = x[2]+x[3]
       t= x[4] + x[5]
       f = int(chr(int(f)))
       s= int(chr(int(s)))
       t= int(chr(int(t)))
       return(f*100+s*10+t)
       
  def conv_inv_hash(str):
        result=''
        for i in {0,4,8,12}:
                  result+=dot_to_hex(str[i]+str[i+1]+str[i+2]+str[i+3]) 
        return(result)


  
  def get_512(str):      
      str=str[:4] 
      bin_not = conv_hash(str)
      return(bin_not)
    
  def verify(shastring,fil):
      sha256 = shastring[16:]
      sha512 = shastring[:16] 
      calc256 = veri_hash_256(fil) 
      calc256 = calc256[-4:] 
      calc512 = veri_hash_512(fil)
      calc512 = calc512[:4]
      x = conv_inv_hash(sha256) 
      y = conv_inv_hash(sha512) 
      sha2 = x[0]+x[2]+x[1]+x[3] 
      sha5 = y[0] + y[2] + y[1] + y[3] 
      if sha2 == calc256 and sha5 == calc512 :
          return True
      return False
      
  def conv_hash(str):
      result=''
      for i in str:
          result+=hex_to_dot(i)
      return(result)
  
  
  def randomize():
   if random.randint(0,100) > 45:
       x = random.randint(256,512)

       f = int2byte(x)
       k = ' '
       for i in range(len(f)):
            if f[i] == '0':
                k = k +'.'
            if f[i] == '1':
                k = k + ' '
       return(k)
   return

  def pass_detect():
   
       x = random.randint(256,512)

       f = int2byte(x)
       k = ' '
       for i in range(len(f)):
            if f[i] == '0':
                k = k +'.'
            if f[i] == '1':
                k = k + ' '
       return(k)
   
 
    
  def gods_notation(var):
        ch = get_dict_value(ord(var)) 
        f = int2byte(ch)
        k = '.'
        for i in range(len(f)):
            if f[i] == '0':
                k = k +'.'
            if f[i] == '1':
                k = k + ' '
        
        return(k)
  


  def call_pass_dict(num):
    global pass_dictt 
    pass_dictt = { x : ' ' for x in range(16) }
    i=0
    for x in range(16): 
          if  i==4:
              num=(num+1)%16  
              i=1
              pass_dictt[x] = num
          else:
              pass_dictt[x] =( num + (i*4))%16 
              i+=1
    arr=[]
    for a in range(16): 
          arr.append(pass_dictt[a])
    for j in range(16): 
           pass_dictt[arr[j]] = j
           
          
      
      
  def get_pass_dict_value(nume):
       
       return( pass_dictt.get(nume,"gone wrong"))    
  
  def get_conv_pass_len(le):
      x=len(le.encode().hex()) 
      return(int(x/2))
      
  def get_conv_pass(pas,num):
      
      retpass = '' 
      byte_pass = pas.encode().hex()
      
      ln  =  len(byte_pass) 
      call_pass_dict(num)
      
      for i in range(ln):
          retpass +=  hex_to_dot_int(str(get_pass_dict_value(hex_to_int(byte_pass[i]))))
      return(retpass)
         

  def gods_notation_for_rano(var):
        ch = ord(var) 
        f = int2byte(ch)
        k = '.'
        for i in range(len(f)):
            if f[i] == '0':
                k = k +'.'
            if f[i] == '1':
                k = k + ' '
        
        return(k)
  


  def int2byte(num):
       byte=''
       for i in range(8):
           x = num % 2
           num = num //2
           byte  += str(x)
       byte= byte[::-1]    
       return byte



  def int6byte(num):
       byte=''
       for i in range(6):
           x = num % 2
           if x == 0:
               x = '.'
           else:
               x = ' '
           num = num //2
           byte  += str(x)
       byte= byte[::-1]    
       return byte

  def gods_message(var):
          z=''
          index = 0
          for i in range(9):
              c = var[i] 
              if not c:
                   return
  
              if c == '.':
                 z = z + '0'
              if c == ' ':
                 z = z + '1' 
           
          for i in range(9):
                 if z[i] == '1':
                     index = i
                     break
          code = z[index:]
          p = get_inv_dict_value(bin_str_2_dec(code))
          if p < 256:
              return(bytes([p]))
  
  def gods_message_for_ran(var):
          z=''
          index = 0
          for i in range(9):
              c = var[i] 
              if not c:
                   return
  
              if c == '.':
                 z = z + '0'
              if c == ' ':
                 z = z + '1' 
           
          for i in range(9):
                 if z[i] == '1':
                     index = i
                     break
          code = z[index:]
          p = bin_str_2_dec(code)
          if p < 256:
               return(str(p))
              
       
          
  def bin_str_2_dec(var):
         val=0
         for i in range(len(var)):
             if var[i] == '1':
                  val = val + pow(2,len(var)-i-1) 
         return(val)

  def dot_str_2_dec(var):
         val=0
         
         for i in range(len(var)):
             if var[i] == ' ':
                  val = val + pow(2,len(var)-i-1) 
         return(val)

  def get_ext(str):
     temp =  str[::-1]
     res=''
     for i in temp:
         if i!= '.':
              res += i 
         if i == '.':
               break
     if len(res)!=len(str):
           return(res[::-1])

  def put_ext(str):
     temp =  str[::-1]
     res=''
     for i in temp:
         if i!= '-':
              res += i 
         if i == '-':
               break
     if len(res)!=len(str):
           return(res[::-1])

  def com_str_of(p,r):
      
      l = int6byte(p)
      returnn = l[5]+l[4]+r[3]+l[3]+l[2]+r[2]+l[1]+r[1]+l[0]+r[0]
      return(returnn)
  
  def int_do(x):
      s=''
      for a in range(len(x)):
          if a == ' ':
              s += '1'
          else:
              s+= '0'    
      return(s)
      
      
  while True:
      print("\033[48;2;255;255;255m\033[0m\033[38;2;255;255;255m ┌──────────────────────────────────────────┐\033[0m\033[1;33m\033[0m")
      print (" \033[38;2;255;255;255m│\033[48;2;255;255;255m\033[38;2;0;0;0m* Enter a choice among following options  \033[1;31m\033[0m\033[38;2;255;255;255m│")
      print("\033[1;33m\033[0m\033[38;2;255;255;255m │──────────────────────────────────────────\033[0m\033[1;33m\033[0m\033[38;2;255;255;255m│\033[0m\033[1;33m\033[0m")
      print(' \033[38;2;255;255;255m│\033[48;2;255;255;255m \033[1;31m1)\033[0m│\033[48;2;255;255;255m \033[1;31mCipher the file\033[0m\033[48;2;255;255;255m   \033[38;2;255;255;255m                   \033[0m│')
      print(' \033[38;2;255;255;255m│\033[0m───│──────────────────────────────────────│ ')
      print(" \033[38;2;255;255;255m│\033[48;2;255;255;255m \033[1;31m2)\033[0m│\033[48;2;255;255;255m \033[1;31mDe-cipher the file\033[0m\033[48;2;255;255;255m\033[38;2;255;255;255m                   \033[0m│ ")
      print(' \033[38;2;255;255;255m│\033[0m───│──────────────────────────────────────│ ')
      print(" \033[38;2;255;255;255m│\033[48;2;255;255;255m \033[1;31m3)\033[0m│\033[48;2;255;255;255m \033[1;31mHelp\033[0m\033[48;2;255;255;255m   \033[38;2;255;255;255m                              \033[0m│    ")
      print(' \033[38;2;255;255;255m│\033[0m───│──────────────────────────────────────│ ')
      print(" \033[38;2;255;255;255m│\033[48;2;255;255;255m \033[1;31m4)\033[0m│\033[48;2;255;255;255m \033[1;31mLicense\033[0m\033[38;2;255;255;255m\033[48;2;255;255;255m                              \033[0m│ ")
      print(' \033[38;2;255;255;255m│\033[0m───│──────────────────────────────────────│ ')
      print(" \033[38;2;255;255;255m│\033[0m\033[48;2;255;255;255m \033[1;31m5)\033[0m│\033[48;2;255;255;255m \033[1;31mExit the program                     \033[0m\033[38;2;255;255;255m│  ")
      print("\033[1;33m\033[0m\033[38;2;255;255;255m └──────────────────────────────────────────┘\033[0m\033[1;33m\033[0m")
      try:
                        choice = int((input("\033[1;36m>>>> \033[0m")))
      except ValueError:
                        try: 
                              choice = int((input("\033[1;36m>>>> \033[0m")))
                        except ValueError:
                              continue
      if choice == 1: 
                      try:
                          global last_str
                          global pas
                          pas=''
                          last_str= '' 
                          x=input("\n\t\b\bEnter the name of the file in present directory/ABS path\n\033[1;33m-->\033[0m")
                          if (os.stat(x).st_size ==0):  
                                time.sleep(0.8)
                                print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                print("\033[1;36m\t┃\033[0m\033[1;35mNo point in ciphering an empty file \033[0m\033[1;36m┃\033[0m")
                                print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                print()
                                time.sleep(1);break
                          else: 
                                ifile = open(x,"rb")
                                ofile = open(".oldfile","w")
                                gen = rano()
                                gen = str(gen) 
                                if len(gen) == 2:
                                      gen = '0'+gen 
                                conv_gen = ''    
                                for t in range(len(gen)):      
                                      conv_gen += gods_notation_for_rano(gen[t])
                                ofile.write(conv_gen)  
                                
                                
                                
                                print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220mDo you want to keep a password to this ? (y/n) \033[0m\033[1;36m┃\033[0m")
                                print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                inpu= input("\033[1;36m>>>> \033[0m")
                                if inpu  == 'Y' or inpu == 'y':
                                                 print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                 print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220mEnter password! [ < 16(utf-8)]                 \033[0m\033[1;36m┃\033[0m")
                                                 print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                 
                                                 global notepoint 
                                                 global passbytes
                                                 notepoint = 0
                                                 pas = (input("\033[1;33m>>>> \033[0m"))
                                                 passbytes = pas.encode()
                                                 if len(passbytes) > 48:
                                                             print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                             print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220m Password is greater than 16 bytes, Enter again\033[0m\033[1;36m┃\033[0m")
                                                             print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                             pas = (input("\033[1;33m>>>> \033[0m"))
                                                             passbytes = pas.encode()
                                                             if len(passbytes) > 48:
                                                                   print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                                   print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220m Password is greater than 32 bytes, Enter again( 1 more try left) \033[0m\033[1;36m┃\033[0m")
                                                                   print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                                   pas = (input("\033[1;33m>>>> \033[0m"))
                                                                   passbytes = pas.encode()
                                                                   if len(passbytes) > 48:
                                                                              print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                                              print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220m Password is greater than  bytes, Enter again( 0 more try left)   \033[0m\033[1;36m┃\033[0m")
                                                                              print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                                              pas = (input("\033[1;33m>>>> \033[0m"))
                                                                              passbytes = pas.encode()
                                                                              if len(passbytes) > 48:
                                                                                     time.sleep(0.8)
                                                                                     print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                                                     print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                                                                     print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                                                     print()
                                                                                     time.sleep(1)
                                                                                     exit() 
                                                                              else: 
                                                                                   notepoint = 1      
                                                                   elif notepoint == 1: 
                                                                       pass
                                                             elif notepoint == 1:
                                                                         pass
                                                 else :
                                                    pass  
                                elif   inpu  == 'N' or inpu == 'n':
                                      pass
                                else :
                                      print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                      print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220mEnter 'y' or 'n' next time !                   \033[0m\033[1;36m┃\033[0m")
                                      print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                      print()
                                      continue 
                                if len(pas.encode().hex()) != 0:
                                      randoo = random.randint(0,15)
                                      
                                      pass_conv = get_conv_pass(pas,randoo)
                                      
                                      randoo_conv = hex_to_dot(int_to_hex(randoo))
                                      
                                      pass_len_conv = get_conv_pass_len(pas)
                                      
                                      com_str =  com_str_of(pass_len_conv,randoo_conv)
                                      pass_det = pass_detect()
                                      last_str=pass_det+com_str+pass_conv
                                      
                                
                                
                                if last_str!= None:
                                    ofile.write(last_str)
                                else:
                                    pass
                                ext=get_ext(x)

                                while True:
                                            
                                    c=ifile.read(1)
                                    if not c:
                                                break
                                    y = gods_notation(c)
                                    ofile.write(y) 
                                    y = randomize()
                                    if y:
                                        ofile.write(y)
                        
                                ifile.close()
                                ofile.close()
                                sha256=calc_hash_256(".oldfile")
                                app256 = get_256(sha256) 
                                sha512=calc_hash_512(".oldfile")
                                app512 = get_512(sha512) 
                                appsha=app512+app256
                                    
                                file = 'ciphered_file'
                                if ext != None :
                                          file = 'ciphered_file-'+ext
                                newf = open(file,'w')
                                newf.write(appsha+open('.oldfile','r').read())
                                newf.close()
                                os.remove(".oldfile")
                                if ext!= None:
                                
                                           print("\033[1;36m\t┏━━━━━━━━━"+len(ext)*'━'+"━━━━━━━━━━━━━━━━┓\033[0m")
                                           print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mCreated \033[1;33mciphered_file-"+ext+"   \033[0m\033[0m\033[1;36m┃\033[0m")
                                           print("\033[1;36m\t┗━━━━━━━━━"+len(ext)*'━'+"━━━━━━━━━━━━━━━━┛ \033[0m")
                                           print
                                           time.sleep(0.5)
                                           print("\t\b\033[1;37mSuggestion\033[1;36m >>\033[1;35m Compress the \033[1;33mciphered_file\033[1;35m, \n\t\t\t\b\bBecause compression factor will be around \033[1;33m87\033[1;35m percent\033[0m"  )
                                           print("\t\b\033[1;37mRecommandation\033[1;36m >> \033[1;33mbzip2")
                                           time.sleep(0.8)
                                           print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                           print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                           print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                           print
                                           time.sleep(1)
                                           exit() 
                                
                                else :
                                           print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                           print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mCreated \033[1;33mciphered_file \033[0m\033[0m\033[1;36m┃\033[0m")
                                           print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                           print()
                                           time.sleep(0.5)
                                           print("\t\b\033[1;37mSuggestion\033[1;36m >>\033[1;35m Compress the \033[1;33mciphered_file\033[1;35m, \n\t\t\t\b\bBecause compression factor will be around \033[1;33m87\033[1;35m percent\033[0m"  )
                                           print("\t\b\033[1;37mRecommandation\033[1;36m >> \033[1;33mbzip2")
                                           time.sleep(0.8)
                                           print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                           print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                           print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                           print()
                                           time.sleep(1)
                                           exit()           





                      except (ValueError,OSError,IOError):
                                 print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                 print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mFile Import error        \033[0m\033[1;36m┃\033[0m")
                                 print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                 print()



                                                            
                           
      elif choice == 2:
               
                      try:
                                print("\n\t\b\bEnter the name of the file in present directory/ABS path\n")
                                file_name2 = input("\033[1;33m-->>\033[0m")
                                if (os.stat(file_name2).st_size ==0):  
                                    time.sleep(0.8)
                                    print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                    print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mCan't de-cipher an empty file \033[0m\033[1;36m┃\033[0m")
                                    print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                    print()
                                    time.sleep(1);break
                                else:
                                  ifile2 = open(file_name2,"r")
                                  ext =  put_ext(file_name2) 
                                  out_file = "de-ciphered_file"
                                  if ext != None: 
                                      out_file = "de-ciphered_file." + ext 
                                  ofile2 = open(out_file,"wb")
                                  shaveri=ifile2.read(32)  
                                  boole = verify(shaveri,file_name2)
                                  get_the_ran = ''
                                  for k in range(3):
                                          get_the_ran += gods_message_for_ran(ifile2.read(9))
                                  val_ran_obt =  get_the_ran_at_de(get_the_ran)     
                                  inv_rano(val_ran_obt)
                                  if boole:
                                        gg= ifile2.read(9)
                                        if gg[0] == ' ':
                                           marking = ifile2.read(10) 
                                           rano = marking[9]+marking[7]+marking[5]+marking[2] 
                                           lenth_pass = marking[8] + marking[6] + marking[4] + marking[3] + marking[1] + marking[0] 
                                           
                                           pass_total_len = dot_str_2_dec(lenth_pass)
                                           
                                           print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                           print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220mEncrypted with password, Enter the password ! \033[0m\033[1;36m ┃\033[0m")
                                           print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                           inpu= input("\033[1;36m>>>> \033[0m")
                                           pass_d_str = ifile2.read(2*pass_total_len*4);  
                                          
                                           
                                           final_con = get_conv_pass(inpu,hex_to_int(dot_to_hex(rano))) 
                                           
                                           if final_con == pass_d_str:
                                                print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220mDecryption Successful !                        ┃\033[0m\033[1;36m\033[0m")
                                                print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                           else: 
                                                print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                print("\033[1;36m\t┃\033[0m\033[1;31m\033[48;2;220;220;220mDecryption Unsuccessful, Try Again !           \033[0m\033[1;36m┃\033[0m")
                                                print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m") 
                                                continue;
                                        
                                        else :
                                            ifile2.seek(59,0)
                                        
                                        
                                        while True :
                                                c=ifile2.read(9)
                                                if not c:
                                                      break
                                                y=gods_message(c)
                                                if y:
                                                   ofile2.write(y)
                                          
                                        ifile2.close()
                                        ofile2.close()
                                             
                                        if ext == None :                                             
                                                  print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                  print("\033[1;36m\t┃\033[0m\033[1;35mCreated \033[1;33mde-ciphered_file\033[0m\033[0m\033[1;36m  ┃\033[0m")
                                                  print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                  print
                                                  time.sleep(0.8)
                                                  print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                  print("\033[1;36m\t┃\033[0m\033[1;35mQuitting the program\033[0m\033[1;36m    ┃\033[0m")
                                                  print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                  print()
                                                  time.sleep(1)
                                                  exit()
                                                  
                                        else:
                                                  print("\033[1;36m\t┏━━━━━━━━━━━━━"+len(ext)*'━'+"━━━━━━━━━━━━━━┓\033[0m")
                                                  print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mCreated \033[1;33mde-ciphered_file."+ext+"  \033[0m\033[0m\033[1;36m┃\033[0m")
                                                  print("\033[1;36m\t┗━━━━━━━━━━━━━"+len(ext)*'━'+"━━━━━━━━━━━━━━┛ \033[0m")
                                                  print()
                                                  time.sleep(0.8)
                                                  print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                                  print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                                  print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                                  print()
                                                  time.sleep(1)
                                                  exit()
                                  else :
                                        print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                        print("\033[1;36m\t┃\033[0m\033[1;35mFile integrity error    \033[0m\033[0m\033[1;36m  ┃\033[0m")
                                        print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                        print()
                                        print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                        print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                        print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                        print()
                                        time.sleep(0.8)
                                        
                                        time.sleep(1)
                                        exit()




                      except (IOError):
                                 print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                 print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mFile Import error        \033[0m\033[1;36m┃\033[0m")
                                 print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                 print()
      
                                

                      
                      except(ValueError,IndexError,OSError):            
                                        print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                        print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mFile integrity error    \033[0m\033[0m\033[1;36m  ┃\033[0m")
                                        print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                        print()
                                        time.sleep(0.8)
                                        print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                        print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                        print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                        print()
                                        
                                        
                                        time.sleep(1)
                                        exit()
      elif choice == 4:
                  if os.name == 'nt':
                    os.system("cls")
                  else:
                    os.system("clear")    
                  print()
                  print(" \033[1;31m +\033[0m\033[1;32m--------------------------------------------------------------------------------------\033[0m\033[1;31m+")
                  print("""  \033[1;32m|\033[38;2;255;255;255m  MIT License                                   \033[1;32m                                      |
  \033[1;32m|                                                                                      \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  Copyright (c) 2018 Ravish B.C                                                     \033[1;32m  |
  \033[1;32m|                                                                                      \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  Permission is hereby granted, free of charge, to any person obtaining a copy  \033[1;32m      |
  \033[1;32m|\033[38;2;255;255;255m  of this software and associated documentation files (the "Software"), to deal\033[1;32m       |
  \033[1;32m|\033[38;2;255;255;255m  in the Software without restriction, including without limitation the rights \033[1;32m       |
  \033[1;32m|\033[38;2;255;255;255m  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell \033[1;32m          |
  \033[1;32m|\033[38;2;255;255;255m  copies of the Software, and to permit persons to whom the Software is   \033[1;32m            |
  \033[1;32m|\033[38;2;255;255;255m  furnished to do so, subject to the following conditions:      \033[1;32m                      |
  \033[1;32m|                                                                                      \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  The above copyright notice and this permission notice shall be included in all     \033[1;32m |
  \033[1;32m|\033[38;2;255;255;255m  copies or substantial portions of the Software.                \033[1;32m                     |
  \033[1;32m|                                                                                      \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR          \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,            \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE         \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER              \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,       \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE       \033[1;32m|
  \033[1;32m|\033[38;2;255;255;255m  SOFTWARE.                                                                           \033[1;32m|
  \033[1;31m+\033[0m\033[1;32m--------------------------------------------------------------------------------------\033[0m\033[1;31m+""")
                  print()
        
        
        
        
        
      elif choice == 3:
                     if os.name == 'nt':
                        os.system("cls")
                     else:
                        os.system("clear")
                     print()
                     print()
                     print(" \033[1;36m +\033[0m\033[38;2;255;255;255m----------------------------------------------------------------------------------\033[0m\033[1;36m+")
                     print("""  \033[38;2;255;255;255m|\033[0m \033[1;36m THIS PROGRAM CIPHERS THE CONTENT OF INPUT FILES\033[0m                                 \033[38;2;255;255;255m|\033[0m""")
                     print("  \033[1;36m+\033[0m\033[38;2;255;255;255m----------------------------------------------------------------------------------\033[0m\033[1;36m+")
                     print("  \033[38;2;255;255;255m|\033[0m\033[48;2;230;230;230m\033[1;38;2;157;34;53m                **********  \033[38;2;0;0;0m   PROGRAM USAGE GUIDE  \033[1;38;2;157;34;53m    *************             \033[0m\033[38;2;255;255;255m|\033[0m")
                     print("  \033[1;36m+\033[0m\033[38;2;255;255;255m----------------------------------------------------------------------------------\033[0m\033[1;36m+")
                     print("  \033[38;2;255;255;255m|\033[0m    \033[1;31mOPTION\033[0m \033[1;37m1\033[0m                                                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m This option should be selected, if you need to cipher the file.       \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m Absolute/Relative path of the file should be given at the prompt      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m Just the file name does the job,                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m            -if the file is present in working directory                          \033[38;2;255;255;255m|\033[0m")
                     print("""  \033[38;2;255;255;255m|\033[0m\033[1;39m             *\033[0m This creates "ciphered_file",which could be highly compressed      \033[38;2;255;255;255m|\033[0m""")
                     print("  \033[38;2;255;255;255m|\033[0m\033[1;36m__________________________________________________________________________________\033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m                                                                                  \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m    \033[1;31mOPTION\033[0m \033[1;37m2\033[0m                                                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m This option should be selected, if you need to De-cipher the file.    \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m Absolute/Relative path of the file should be given at the prompt.     \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m Just the file name does the job,                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m            -if the file is present in working directory.                         \033[38;2;255;255;255m|\033[0m")
                     print("""  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m This creates "de-ciphered_file",                                      \033[38;2;255;255;255m|\033[0m""")
                     print("  \033[38;2;255;255;255m|\033[0m            -whose SHASUM is equal to the original file.                          \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m\033[1;36m__________________________________________________________________________________\033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m                                                                                  \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m    \033[1;31mOPTION\033[0m \033[1;37m3\033[0m                                                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m This option, simply displays the usage of the program.                \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m And the program is not CLI based, because to provide friendly         \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m            -Environment to NON-LINUX users.                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m Program's initial commit is done by python3.                          \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m\033[1;36m__________________________________________________________________________________\033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m                                                                                  \033[38;2;255;255;255m|\033[0m")
                     print(" \033[38;2;255;255;255m |\033[0m    \033[1;31mOPTION\033[0m \033[1;37m4\033[0m                                                                      \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m This option is to exit from the program.                              \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m Can be done by pressing CTRL + D/C                                    \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m          \033[1;39m*\033[0m CTRL + Z, Suspends the program.                                       \033[38;2;255;255;255m|\033[0m")
                     print("  \033[38;2;255;255;255m|\033[0m                                                                                  \033[38;2;255;255;255m|\033[0m")
                     print("  \033[1;36m+\033[0m\033[38;2;255;255;255m----------------------------------------------------------------------------------\033[0m\033[1;36m+\033[0m")
                     print()
                     print()
      elif choice == 5:
                     print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                     print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                     print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                     print()
                     time.sleep(1)
                     exit()
                     
                     
                   
      else:
              print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
              print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mEnter a valid choice    \033[0m\033[1;36m┃\033[0m")
              print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
 
except (KeyboardInterrupt,EOFError):
                                        print()                                        
                                        print("\033[1;36m\t┏━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
                                        print("\033[1;36m\t┃\033[0m\033[7;35m\033[2;37mQuitting the program    \033[0m\033[1;36m┃\033[0m")
                                        print("\033[1;36m\t┗━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[0m")
                                        print()
                                        time.sleep(1)
