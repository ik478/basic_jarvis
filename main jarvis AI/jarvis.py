  # from Body.Speak1 import Speak
 #  from features.clap import Tester
 #  from jarvis import MainExe


   #Tester()
   #Speak("Welcome sir! how can i help you..")
  # data =Tester()
 #  if "True-Mic" == data:
  #    MainExe()
#from brain.AiBrain import ReplyBrain
from Body.Listen import MicExecution
#from brain.QnA import QuestionAnswer
print("Loding..")
from Body.Speak import Speak
from features.clap import Tester
print("Loding..")

def MainExecution():
    
    Speak("hello sir ")
    Speak("I'm redy to assist you sir")

    while True:
        
        Data =MicExecution()
        Data = str(Data)
        print(len(Data))
 
        if len(Data)<3:
           pass
        
        
        elif "turn on fan" in Data :
            Speak ("turning on the fan")

        elif "qustion" in Data or "what is" in Data or "answer" in Data or "where is " in Data :
          Reply = QuestionAnswer(Data)
          Speak(Reply)

        elif "open" in Data or"search" in Data or "send a message" in Data or " show the message" in Data :
            from shoshalmedia.socialmedia import send_message
            import re
            pattern ='send a message to (\D*)'
            matchs = re.findall(pattern,Data)
            to = matchs
            print(to)
            Speak("what's the messege sir")
            Data = MicExecution()
            message = Data
            Reply = send_message(to,message)
            Speak(Reply)
            

        else :
           #Reply = ReplyBrain(Data)
           #Speak(Reply)
           print('hhhhhhh')
        

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print("clap Detected")
        MainExecution()
    else:
        pass
    
ClapDetect()
