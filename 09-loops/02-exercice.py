command = ''
started = False
while True:
  command = input('>').lower()
  if command == 'start':
    if started:
      print('Car is already started')
    else:
      started = True
      print('Car started...')
  elif command == 'stop':
    if not started:
      print ("Car is already stopped")
    else:
      started = False
      print("Car stopped")
  elif command == 'help':
    print('''
start -> start to start the car     
stop -> stop to stop the car     
quit -> quit to exit the game     
          ''')
  if command == 'quit':
      break
  else:
    print ("i cant't understand this command...")