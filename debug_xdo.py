import xdo


xdo = xdo.Xdo()
win = xdo.search_windows(winname=b'farm')
for i in win:
    winsize = xdo.get_window_size(i)
    winloc = xdo.get_window_location(i)
    winreg = (winloc.x, winloc.y, winsize.width, winsize.height)
    print(winsize)
    print(winloc)
    print(winreg)


print("done")
