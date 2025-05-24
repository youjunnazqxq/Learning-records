#Q2Email
class Email:
    def __init__(self,msg,sender_name,recipient_name):
        self.msg=msg
        self.sender_name=sender_name
        self.recipient_name=recipient_name

class Server:
    def __init__(self):
        self.clients={}
    def send(self,email):
        client=self.clients[email.recipient_name]
        client.receive(email)
    def register_client(self,client,client_name):
        self.clients[client_name]=client
class Client:
    def __init__(self,server,name):
        self.inbox=[]
        self.server=server
        self.name=name
        server.register_client(self,self.name)
    def compose(self,msg,recipient_name):
        email=Email(msg,self.name,recipient_name)
        self.server.send(email)
    def receive(self,email):
        self.inbox.append(email)


#Q3
class Button:
 def __init__(self, pos, key):
    self.pos = pos
    self.key = key
    self.times_pressed = 0
 class Keyboard:

    def __init__(self, *args):
        self.buttons={}
        for button in args:
            self.buttons[button.pos]=button
    def press(self, pos):
        if pos in self.buttons :
            b=self.buttons[pos]
            b.times_pressed+=1
            return b.key
        return ''

    def typing(self, typing_input):
        accumulate=''
        for pos in typing_input:
            accumulate+=self.press(pos)
            return accumulate
        


#Q4
class TeamMember:
    def __init__(self,operation,prev_member=None):
        self.history=[]
        self.operation=operation
        self.prev_member=prev_member
    def relay_calculate(self,x):
        if not self.prev_member:
            result=self.operation(x)
            self.history=[result]
        else:
            prev_result=self.prev_member.relay_calculate(x)
            result=self.operation(prev_result)
            self.history=self.prev_member.history+[result]
        return result
    def relay_history(self):
        return self.history
    


#Q5
name =owner+"'s Cat'"
return cls(name,owner)