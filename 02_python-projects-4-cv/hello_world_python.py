import time

print('''  #Email: contactme@pfm-cv.dev
  #Personal Email: moises.per.fav@gmail.com
  #Linkedin: https://www.linkedin.com/in/perez-favela-moises/
  #Portfolio Web: https://pfm-cv.dev
  #GitHub: https://github.com/PerfavM\n''')
text = '  Este es el texto que se mostrará con efecto de máquina de escribir\n  Este es el texto que se mostrará con efecto de máquina de escribir\n'

for caracter in text:
  print(caracter, end='', flush=True)
  time.sleep(0.05)

print('''\n  1.English Languaje.
  2.Idioma Español.\n''')
lan = int(input(' '))

#languaje English
if lan == 1:
  text = '\n  Este es el texto que se mostrará con efecto de máquina de escribir\n'
  for caracter in text:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
  
  #Menu English
  menu = print('''\n  01.Madlibs
  02.Guess the number(pc).
  03.Guess the number(user).
  04.Rock, Papper, Scissers.
  05.Hangman.
  06.Countdown Timer.
  07.Password Generator.
  08.Tic-Tac-Toe.\n''')
  text2 = int(input(' '))
  
  #Madlibs
  if text2 == 1:
    from hello_world_python import madlibs_en
    funcion = getattr(madlibs_en, text2)
  #Guess the number(pc)
  elif text2 == 2:
    from hello_world_python import guess_the_number_en_pc
    funcion = getattr(guess_the_number_en_pc, text2)
  #Guess the number(user)
  elif text2 == 3:
    from hello_world_python import guess_the_number_en_user
    funcion = getattr(guess_the_number_en_user, text2)
  #Rock, Papper, Scissers.
  elif text2 == 4:
    from hello_world_python import rock_paper_scissors_en
    funcion = getattr(rock_paper_scissors_en, text2)
  #Hangman.
  elif text2 == 5:
    from hello_world_python import hangman
    funcion = getattr(hangman, text2)
  #Countdown Timer.
  elif text2 == 6:
    from hello_world_python import countdown_timer
    funcion = getattr(countdown_timer, text2)
  #Password Generator.
  elif text2 == 7:
    from hello_world_python import password_generator
    funcion = getattr(password_generator, text2)
  #Tic-Tac-Toe.
  elif text2 == 8:
    from hello_world_python import tic_tac_toe
    funcion = getattr(tic_tac_toe, text2)
    
    
  else:
    text = '\nEste es el texto que se mostrará con efecto de máquina de escribir\n'
    for caracter in text:
      print(caracter, end='', flush=True)
      time.sleep(0.05)
      
#Idioma español
elif lan == 2:
  text = print('Este es el texto que se mostrará con efecto de máquina de escribir\n')
  for caracter in text:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
    
  #Menu Español
  menu = print('''\n  01.Madlibs
  02.Guess the number(pc).
  03.Guess the number(user).
  04.Rock, Papper, Scissers.
  05.Hangman.
  06.Countdown Timer.
  07.Password Generator.
  08.Tic-Tac-Toe.\n''')
  text2 = int(input('\n'))
  
  #Madlibs
  if text2 == 1:
    from hello_world_python import madlibs_en
    funcion = getattr(madlibs_en, text2)
  #Guess the number(pc)
  elif text2 == 2:
    from hello_world_python import guess_the_number_en_pc
    funcion = getattr(guess_the_number_en_pc, text2)
  #Guess the number(user)
  elif text2 == 3:
    from hello_world_python import guess_the_number_en_user
    funcion = getattr(guess_the_number_en_user, text2)
  #Rock, Papper, Scissers.
  elif text2 == 4:
    from hello_world_python import rock_paper_scissors_en
    funcion = getattr(rock_paper_scissors_en, text2)
  #Hangman.
  elif text2 == 5:
    from hello_world_python import hangman
    funcion = getattr(hangman, text2)
  #Countdown Timer.
  elif text2 == 6:
    from hello_world_python import countdown_timer
    funcion = getattr(countdown_timer, text2)
  #Password Generator.
  elif text2 == 7: 
    from hello_world_python import password_generator
    funcion = getattr(password_generator, text2)
  #Tic-Tac-Toe.
  elif text2 == 8:
    from hello_world_python import tic_tac_toe
    funcion = getattr(tic_tac_toe, text2)
    
    
  else:
    text = '\nEste es el texto que se mostrará con efecto de máquina de escribir\n'
    for caracter in text:
      print(caracter, end='', flush=True)
      time.sleep(0.05)