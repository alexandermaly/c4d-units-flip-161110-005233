import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    wc=c4d.GetWorldContainer()
    #wc2=c4d.GetWorldContainerInstance()
    #oldPasteAt = wc[c4d.WPREF_PASTEAT] # Get the current Paste setting
    #u1=wc[c4d.PREF_UNITS_BASIC] # get units pref
    v1=wc[c4d.WPREF_UNITS_BASIC]
    #wc[c4d.PREF_UNITS_BASIC]=5
    wc[c4d.WPREF_UNITS_BASIC]=1
    #u2=wc[c4d.PREF_UNITS_BASIC] # get units pref
    v2=wc[c4d.WPREF_UNITS_BASIC]
    #c4d.gui.UpdateMenus()
    #c4d.gui.GeUpdateUI()
    c4d.SetWorldContainer(wc)
    print v1,v2#u1,u2#,v1,u2,v2
    print wc
    c4d.EventAdd()
if __name__=='__main__':
    main()
