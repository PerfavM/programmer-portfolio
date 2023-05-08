#These are my ways to contact me.
#Email: contactme@pfm-cv.dev
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.dev
#GitHub: https://github.com/PerfavM

adj = str(input("Adjective: "))
verb1 = str(input("Verb: "))
verb2 = str(input("Verb: "))
famous_person = str(input("Famous person: "))
text = float(input('Select a number (1 a 10), to select a text: '))
    
if text == 1:
  madlib = f"¡1La programación de computadoras es tan '{adj}'! Me emociona mucho todo el tiempo porque. me encanta '{verb1}'. ¡Mantente hidratado y '{verb2}' como si fueras '{famous_person}'!"
elif text == 2:
  madlib = f"¡2La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 3:
  madlib = f"3¡La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 4:
  madlib = f"¡4La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 5:
  madlib = f"¡5La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 6:
  madlib = f"¡5La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 7:
  madlib = f"¡5La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 8:
  madlib = f"¡5La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 9:
  madlib = f"¡5La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
elif text == 10:
  madlib = f"¡5La programación de computadoras es tan {adj}! Me emociona mucho todo el tiempo porque. me encanta {verb1}. ¡Mantente hidratado y {verb2} como si fueras {famous_person}!"
else:
  madlib = "¡Por favor, reinicie el programa y seleccione un numero del 1 al 10!"
print(madlib)