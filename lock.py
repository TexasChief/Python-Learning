passcode = 486450

tries = 1
if tries <= 3:
  while tries <= 3:
    code = input('Input your code:')
    tries = tries + 1
    if code == passcode:
      print ("Access Granted")
      break
    else:
      print ("Access Denied")
  else:
    print ("System locked. Contact SysAdmin")
