#encoding=utf-8
from wx import App,Frame,Panel


class Main_gui(App):
    def __init__(self):
        App.__init__(self)
        print "Main GUI"


    def OnInit(self):
        print "overwrite on init"

        self.Frame = Frame(parent=None, title="支部工作，一键刷单", pos=(150, 50), size=(1000, 600))
        self.Frame.SetMaxSize((1000, 800))
        self.SetTopWindow(self.Frame)
        self.panel = Panel(self.Frame, -1)

        self.Frame.Show()
        return True

    


if __name__ == '__main__':
    Main_gui().MainLoop()