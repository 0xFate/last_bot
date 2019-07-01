import xdo


xdo = xdo.Xdo()
win = xdo.search_windows(winname=b'farm')
for i in win:
    winsize = xdo.get_window_size(win[0])
    winloc = xdo.get_window_location(win[0])
    print(winsize)
    print(winloc)


print("done")
