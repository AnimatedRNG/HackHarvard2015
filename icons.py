import win32ui
import win32gui
import win32con
import win32api


def loadFile(filename):
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    large, small = win32gui.ExtractIconEx(filename, 0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_x )
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject( hbmp )
    hdc.DrawIcon( (0,0), large[0] )
    hbmp.SaveBitmapFile( hdc, "cache/save.bmp" )

loadFile("")
