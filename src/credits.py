from colored import fg, attr

creditcolor = fg('#009900')
pinkcolor = fg('#C71585')
whitecolor = fg('#FFFFFF')
res = attr('reset')

def credits():
    print("")
    print((pinkcolor + "   [*]   " + res) + (whitecolor + "Created by " + res) + (creditcolor + "TigerNetv [Ariel Shabaev] " + res) + (whitecolor + "for " + res) + (pinkcolor + "GitHub.com" + res))
    print((pinkcolor + "   [*]   " + res) + (whitecolor + "Contact me on Discord " + res) + (creditcolor + "Ariel#8422" + res))
    print("")