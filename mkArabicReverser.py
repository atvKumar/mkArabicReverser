import wx
import arabic_reshaper
from bidi.algorithm import get_display
from wx.lib.wordwrap import wordwrap

class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(500, 500))

        # Now create the Panel to put the other controls on.
#        panel = wx.Panel(self)
#        menuBar = wx.MenuBar()
#        menu = wx.Menu()
#        menu.Append(wx.ID_EXIT, "About")
#        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_EXIT)
#        menuBar.Append(menu, "&About")
#        self.SetMenuBar(menuBar)
        
        l1 = wx.StaticText(self, -1, "Enter your Source Arabic Text")
        t1 = wx.TextCtrl(self, -1, "Enter your Arabic Text Here",
                         size=(300, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        b = wx.Button(self, -1, "Convert")
        l2 = wx.StaticText(self, -1, "Your Converted Text")
        t2 = wx.TextCtrl(self, -1, "Click Convert!",
                         size=(300, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_BUTTON, self.OnConvert, b)
        b2 = wx.Button(self, -1, "About mkArabicReverser 1.0", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnAbout, b2)
        
        wx.CallAfter(t1.SetInsertionPoint, 0)
        self.tc1 = t1
        self.tc2 = t2

        bsizer = wx.BoxSizer(wx.VERTICAL)
        bsizer.Add(l1, 0, wx.GROW|wx.ALL, 10)
        bsizer.Add(t1, 0, wx.GROW|wx.ALL, 10)
        bsizer.Add(b, 0, wx.GROW|wx.ALL, 10)
        bsizer.Add(l2, 0, wx.GROW|wx.ALL, 10)
        bsizer.Add(t2, 0, wx.GROW|wx.ALL, 10)
        bsizer.Add(b2, 0, wx.GROW|wx.ALL, 10)

        self.SetAutoLayout(True)
        self.SetSizer(bsizer)
        self.Layout()

    def OnAbout(self, evt):
        licenseText = """This work is licensed under the GNU Public License (GPL).
        To view a copy of this license,
        visit http://www.gnu.org/copyleft/gpl.html
        """
        info = wx.AboutDialogInfo()
        info.Name = "mkArabicReverser"
        info.Version = "1.0.1"
        info.Copyright = "(C) 2013 Kumaran S/O Murugun"
        info.Description = wordwrap(
            "mkArabicReverser is an Arabic text reverser "
            "It takes your Arabic text from your source "
            "example: Word Processor, Web Browser, etc "
            "And it converts it into a format that is "
            "ready for your media applications "
            "\nexample: Photoshop, Illustrator, etc"
            "\nUTF-8,Unicode Support",
            350, wx.ClientDC(self))
        info.WebSite = ("http://github.com/atvkumar", "mkArabicReverser")
        info.Developers = [ "Kumaran",
                            "atv.kumar@gmail.com",
                            "Abd Allah Diab",
                            "mpcabd@gmail.com" ]

        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)
        
    def OnClose(self, evt):
        print "See ya later!"
        self.Close()

    def OnConvert(self, evt):
        self.tc2.Clear()
        reshaped_text = arabic_reshaper.reshape(self.tc1.GetValue())
        bidi_text = get_display(reshaped_text)
        self.tc2.WriteText(bidi_text)

class MyApp(wx.App):
    def OnInit(self):
        frame = Frame(None, "mkArabicReverser 1.0")
        self.SetTopWindow(frame)

        #print "Print statements go to this stdout window by default."
        frame.Centre()
        frame.Show(True)
        return True
        
app = MyApp(redirect=True)
app.MainLoop()
