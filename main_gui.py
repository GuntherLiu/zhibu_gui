#encoding=utf-8
from wx import App,Frame,Panel, Button, Font, GridSizer, TextCtrl, Image, StaticBitmap
from wx import ROMAN, NORMAL, BITMAP_TYPE_PNG, EVT_LEFT_DOWN, EVT_CHAR, EVT_SET_FOCUS, EVT_KILL_FOCUS, EVT_CHILD_FOCUS
from login_event import LoginEvent

class Main_gui(App):
    def __init__(self):
        self._frame = None
        self._panel = None
        self._button_login = None
        self._input_username = None
        self._input_pwd = None
        self._input_captcha = None
        self._panel_login = None
        self._login_event = LoginEvent()

        App.__init__(self)
        print "Main GUI"


    def OnInit(self):
        print "overwrite on init"
        self._frame = Frame(parent=None, title="支部工作，一键刷单", pos=(150, 50), size=(1000, 600))
        # self.Frame.SetMaxSize((1000, 800))
        self.SetTopWindow(self._frame)
        self._panel = Panel(self._frame, -1)
        self._panel_login = Panel(self._panel, -1, pos=(100, 20), size=(420, 340))
        self.login_button()
        self.login_input()
        self.login_captcha()
        # self.sizer()


        self._frame.Show()
        return True

    def sizer(self):
        sizer = GridSizer(rows=4, cols=4, hgap=5, vgap=5)
        sizer.Add(self._button_login)
        sizer.Add(self._input_username)
        sizer.Add(self._input_pwd)
        sizer.Add(self._input_capcha)

    def login_button(self):
        print "login button"

        self._button_login = Button(self._panel_login, -1, "登录", pos=(100, 150), size=(80, 30))
        font = Font(18, ROMAN, NORMAL, NORMAL)
        self._button_login.SetFont(font)

    def login_input(self):
        print "login msg"
        self._input_username = TextCtrl(self._panel_login, 1, "请输入用户名：",  pos=(100, 20), size=(200, 40))
        self._input_pwd = TextCtrl(self._panel_login, 2, "请输入密码：", pos=(100,60), size=(200, 40))
        self._input_captcha = TextCtrl(self._panel_login, 3,  "请输入验证码：", pos=(100, 100), size=(200, 40))
        self._input_username.Bind(EVT_CHILD_FOCUS, self._login_event.get_login_msg)



    def login_captcha(self):
        print "login captcha"
        captcha_image = Image('captcha.png', BITMAP_TYPE_PNG).ConvertToBitmap()
        StaticBitmap(self._panel_login, bitmap=captcha_image, pos=(305, 105))




if __name__ == '__main__':
    Main_gui().MainLoop()