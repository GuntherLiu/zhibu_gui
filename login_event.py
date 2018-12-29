#encoding=utf-8

class LoginEvent():
    def __init__(self):
        self._username = None
        self._pwd = None
        self._captcha = None

        print "login event"


    def get_login_msg(self, event):
        print "get login msg"

        # EventObject 这个对象，就是 组件对象的封装， 内部封装了组件的所有信息
        event_obj = event.EventObject
        event_obj.SetValue("")

        # print value

        id = event_obj.Id

        # username
        if id == 1:
            self._username = event_obj.Value

        # pwd
        elif id == 2:
            self._pwd = event_obj.Value

        # captcha
        else:
            self._captcha = event_obj.Value







