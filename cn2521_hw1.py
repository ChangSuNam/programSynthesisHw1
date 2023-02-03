#userInput the input in integer
#userOutput the desired output in integer
def check(userInput, userOutput):
    print("input is: " + str(userInput))
    print("output is: " + str(userOutput))
    ansFunction = ""
    if userInput != 0 and userOutput != 0 and userOutput % userInput == 0:
      ansFunction = ("*"+str(userOutput/userInput))
      print(ansFunction)
      print("eval: " + str(eval(str(userInput)+"*" + str(userOutput/userInput))))

    if userInput > userOutput:
      ansFunction = ("-"+str(userInput-userOutput))
      print(ansFunction)
      print("eval: " + str(eval(str(userInput)+"-"+str(userInput-userOutput))))

    if userInput < userOutput:
      ansFunction = ("+"+str(userOutput-userInput))
      print(ansFunction)
      print("eval: " + str(eval(str(userInput)+"+"+str(userOutput-userInput))))

    if userOutput != 0 and userInput != 0 and userInput % userOutput == 0:
      ansFunction = ("/"+str(userInput/userOutput))
      print(ansFunction)
      print("eval: " + str(eval(str(userInput)+"/"+str(userInput/userOutput))))


check(0, 2)
check(0, 9)
check(3, 9)
check(4, 2)
