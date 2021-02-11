Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import pandas as pd
>>> import os
>>> os.chdir(r"C:\Users\jakes\Documents\Python")
>>> table = pd.read_csv("Colchester.csv")
>>> table
                       Name  Age  Minutes StillAtClub Loan
0                Josh Bohui   21      123           Y    N
1             Shamal George   23      165           Y    N
2          Junior Tchamadeu   17      168           Y    N
3           Miquel Scarlett   20      202           N    N
4              Ryan Clampin   22      226           N    N
5               Tom Lapsile   25      293           Y    N
6            Michael Folivi   22      510           Y    N
7              Omar Sowunmi   25      516           Y    N
8               Luke Gambin   27      570           Y    Y
9               Luke Norris   27      786           N    N
10               Harry Pell   29      928           Y    N
11          Courtney Senior   23     1486           Y    N
12           Callum Harriot   26     1652           Y    N
13            Ben Stevenson   23     1692           Y    N
14               Kwame Poku   19     1695           Y    N
15        Miles Welsh Hayes   24     1704           Y    N
16             Jevani Brown   26     1814           Y    N
17            Noah Chilvers   19     2040           Y    N
18              Dean Gerken   35     2175           Y    N
19              Tom Eastmon   29     2250           Y    N
20              Tommy Smith   30     2250           Y    N
21             Frank Nouble   29       90           Y    Y
22   Brendan Sarpong Wiredu   21       90           Y    N
23             Josh Doherty   24       72           Y    Y
24             Aramide Oteh   22       72           Y    Y
25         Paris Cowen Hall   30       69           Y    N
26            Sammie McLeod   20        8           N    N
27  Marley Marshall Miranda   18        1           Y    N
>>> fig, ax = plt.subplots()
>>> plt.plot(table["Age"], table["Minutes"], "o")
[<matplotlib.lines.Line2D object at 0x0000026245DDEFA0>]
>>> x_ticks = np.arange(17,36,1)
>>> plt.xticks(x_ticks)
([<matplotlib.axis.XTick object at 0x0000026245DB5940>, <matplotlib.axis.XTick object at 0x0000026245DB5910>, <matplotlib.axis.XTick object at 0x00000262455BB460>, <matplotlib.axis.XTick object at 0x0000026248305760>, <matplotlib.axis.XTick object at 0x0000026248305C70>, <matplotlib.axis.XTick object at 0x000002624830A1C0>, <matplotlib.axis.XTick object at 0x00000262483057C0>, <matplotlib.axis.XTick object at 0x000002624830A6D0>, <matplotlib.axis.XTick object at 0x000002624830ABE0>, <matplotlib.axis.XTick object at 0x0000026248313130>, <matplotlib.axis.XTick object at 0x0000026248313640>, <matplotlib.axis.XTick object at 0x0000026248313B50>, <matplotlib.axis.XTick object at 0x00000262483190A0>, <matplotlib.axis.XTick object at 0x00000262483195B0>, <matplotlib.axis.XTick object at 0x0000026248319AC0>, <matplotlib.axis.XTick object at 0x0000026248313280>, <matplotlib.axis.XTick object at 0x00000262483053D0>, <matplotlib.axis.XTick object at 0x0000026248319C70>, <matplotlib.axis.XTick object at 0x00000262483201C0>], [Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, '')])
>>> for i, txt in enumerate(table["Name"]):
    ax.annotate(txt, (table["Age"][i], table["Minutes"][i]))

    
Text(21, 123, 'Josh Bohui')
Text(23, 165, 'Shamal George')
Text(17, 168, 'Junior Tchamadeu')
Text(20, 202, 'Miquel Scarlett')
Text(22, 226, 'Ryan Clampin')
Text(25, 293, 'Tom Lapsile')
Text(22, 510, 'Michael Folivi')
Text(25, 516, 'Omar Sowunmi')
Text(27, 570, 'Luke Gambin')
Text(27, 786, 'Luke Norris')
Text(29, 928, 'Harry Pell')
Text(23, 1486, 'Courtney Senior')
Text(26, 1652, 'Callum Harriot')
Text(23, 1692, 'Ben Stevenson')
Text(19, 1695, 'Kwame Poku')
Text(24, 1704, 'Miles Welsh Hayes')
Text(26, 1814, 'Jevani Brown')
Text(19, 2040, 'Noah Chilvers')
Text(35, 2175, 'Dean Gerken')
Text(29, 2250, 'Tom Eastmon')
Text(30, 2250, 'Tommy Smith')
Text(29, 90, 'Frank Nouble')
Text(21, 90, 'Brendan Sarpong Wiredu')
Text(24, 72, 'Josh Doherty')
Text(22, 72, 'Aramide Oteh')
Text(30, 69, 'Paris Cowen Hall')
Text(20, 8, 'Sammie McLeod')
Text(18, 1, 'Marley Marshall Miranda')
>>> a = 24
>>> b = 28
>>> plt.axvspan(a,b,color="y", alpha = 0.35, lw = 0)
<matplotlib.patches.Polygon object at 0x00000262483207F0>
>>> c = 17
>>> d = 24
>>> plt.axvspan(c,d,color="r",alpha = 0.5, lw=0)
<matplotlib.patches.Polygon object at 0x0000026248319B20>
>>> e = 28
>>> f = 36
>>> plt.axvspan(e,f,color="g", alpha = 0.5, lw=0)
<matplotlib.patches.Polygon object at 0x000002624830AC40>
>>> ax.text(21, 2500, "Young")
Text(21, 2500, 'Young')
>>> ax.text(26,2500,"Peak")
Text(26, 2500, 'Peak')
>>> ax.text(32,2500,"Experienced")
Text(32, 2500, 'Experienced')
>>> ax.set_title("Colchester United Age Minutes Plot 2020/2021")
Text(0.5, 1.0, 'Colchester United Age Minutes Plot 2020/2021')
>>> ax.set_xlabel("Age")
Text(0.5, 0, 'Age')
>>> ax.set_ylabel("Minutes")
Text(0, 0.5, 'Minutes')
>>> plt.show()
