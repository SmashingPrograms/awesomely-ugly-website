import sys
import random

randletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
randletterssym = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()!~.,[]{};:-=+-*^$@!?&%'|"
lettergen = len(randletters) - 1
lettergensym = len(randletterssym) - 1
randcolor = "abcdef0123456789"

htmlbeginning = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Public Domain Insanity, Part 1</title>
    <link rel="stylesheet" href="https://pagecdn.io/lib/normalize/8.0.1/normalize.min.css" />
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body onclick="openInNewTab('https://en.wikisource.org/wiki/The_Fighting_Coward')">
    <script src="./main.js"></script>
    <section>
      <h1>09dsagojdsj09g09dsg9009u0w93i9t0909ksdkafdsopjfdsjopfASDFPSDFwoerqr0231)@!R!(@)$(@!DASO)</h1>
"""

# bodytofooter = """
#     </section>
#   </body>
#   <footer>
# """

htmlending = """      </section>\n    </body>\n    <footer>\n      <button onclick="swapImage()">Click me to swap out an image!</button>\n    </footer>\n</html>"""

filename_list = """Night Of The Living Dead trailer screenshot.jpg
Nightofthelivingdead screenshot.jpg
Romero zombie.jpg
Russell Streiner as Johnny in Night of the Living Dead.png
StateTheatreAnnArborMarquee.jpg
Zombie dead live.png
Zombies NightoftheLivingDead.jpg
Night of the Living Dead (1968) - Zombies.JPG
Ben giving Barbra slippers in Night of the Living Dead bw.jpg
Bill Hinzman.png
CooperFamily.jpg
Duane Jones as Ben in Night of the Living Dead bw.jpg
Duane Jones as Ben in Night of the Living Dead shadowed bw.jpg
EvansCityCemetery PA.jpg
Flickr - Sasoriza - Night of the Living Dead at Yonge-Dundas Square (1).jpg
Flickr - Sasoriza - Night of the Living Dead at Yonge-Dundas Square (2).jpg
Flickr - Sasoriza - Night of the Living Dead at Yonge-Dundas Square.jpg
FSK-Karte.jpg
Girl zombie eating her victim Night of the Living Dead bw - cropped.jpg
Girl zombie eating her victim Night of the Living Dead bw.jpg
John A. Russo (cropped).JPG
John A. Russo and Ryota Nakanishi.JPG
John A. Russo as zombie in Night of the Living Dead.JPG
Judith O'Dea clutching grave in Night of the Living Dead bw.jpg
Judith Ridley as Judy in Night of the Living Dead.png
JudithRidley.jpg
Karl Hardman as Harry Cooper in Night of the Living Dead.png
Keith Wayne as Tom in Night of the Living Dead.png
Kyra Schon as Karen Cooper in Night of the Living Dead.png
Lipton can prop, Night of the Living Dead (1968).png
Livingdead.jpg
Marilyn Eastman as Helen Cooper in Night of the Living Dead.png
Marilyn Eastman as Helen Cooper in Night of the Living Dead.png
Little Annie Rooney (1925) Poster.jpg
Pickfordannierooney.jpg
Cullen Landis, silent film actor (SAYRE 5548).jpg
The Fighting Coward (1924) - 7.jpg
The Fighting Coward (SAYRE 14435).jpg
The Fighting Coward official still 1.png
The Fighting Coward official still 3.png
The Fighting Coward poster 1.jpg
The Fighting Coward poster 2.jpg
The Fighting Coward poster 3.jpg
The Fighting Coward poster 4.jpg
The Fighting Coward poster 5.jpg
The Fighting Coward poster 6.jpg
The Fighting Coward scene poster 2.jpg
The Fighting Coward scene poster 3.jpg
The Fighting Coward scene poster 4.jpg
The Fighting Coward official still 2.png
The Fighting Coward official still 4.png
The Fighting Coward official still 5.png"""

filename_list = filename_list.split("\n")

img = """<img src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file&wpvalue=Cullen Landis, silent film actor (SAYRE 5548).jpg" alt="KADSFGokasdgkdoko320495r23095ir23tiekopfgokpsaddfkop" />"""

# x = x.split("\n")
# y = []

# for l in x:
#     if l != "":
#         y.append(l)

link_list = []

for f in filename_list:
    # if (y.index(ultimate_list)) % 2 == 0:
    f = f.replace(" ", "_")
    link_list.append("https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file&wpvalue" + f)

# print(link_list)

css = """body {
  background-color: red;
  opacity: 0.3;

}

footer {
    font-weight: bold;
    font-style: italic;
    font-size: x-small;
    letter-spacing: 7em;
    line-height: normal;
    font-variant: common-ligatures tabular-nums;
}

img {
  width: 1000%;
}

"""
css2 = []

def randomColor(num):
    return f"#{hex(num)[2:]}"

def classMake():
    list = []
    for prog in range(random.randint(30, 50)):
        list.append(randletters[random.randint(0, lettergen)])
    list = "".join(list)
    css2.append(f".{list} {{\n  color: {randomColor(random.randint(0, 16777215))};\n  background-color: {randomColor(random.randint(0, 16777215))};\n}}")
    return list

def lettersMake(element):
    list = []
    for l in range(random.randint(50, 1000)):
        for prog in range(random.randint(3, 10)):
            original = randletterssym[random.randint(0, lettergensym)]
            new = f"<span class=\"{classMake()}\">" + original + "</span>"
            list.append(new)
        list.append(" ")
    list = "".join(list)
    if element == "h1":
        newElement = "        <h1>" + list + "</h1>"
    else:
        newElement = f"            <{element}>" + list + f"</{element}>"
    return list

def altMake():
    list = []
    for l in range(random.randint(50, 1000)):
        for prog in range(random.randint(3, 10)):
            new = randletterssym[random.randint(0, lettergensym)]
            list.append(new)
        list.append(" ")
    list = "".join(list)
    return list

print(lettersMake("p"))

# print(randomColor(16777215))

def randomImage():
    return f"        <img src=\"https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file&wpvalue={filename_list[random.randint(0, len(filename_list)-1)]}\" alt=\"{altMake()}\" />"

bodyelements = []
footer = ""

ideas = ["img", "p", "div", "section"]

for i in range(50):
    print(i)
    shuffle = random.randint(1, 3)
    if random.randint(1, 50) == 45:
        bodyelements.append("    </section>\n    <section>\n" + lettersMake("h1"))
    elif shuffle == 1:
        bodyelements.append(randomImage())
    elif shuffle == 2:
        bodyelements.append(lettersMake("p"))
    elif shuffle == 3:
        bodyelements.append(lettersMake("div"))
    bodyelements.append("<br />")

body = "\n".join(bodyelements)
css = css + "\n\n".join(css2)

fh = open("index.html", "w+")
fh.write(htmlbeginning + body + htmlending)
fh.close()
print("written")

cssh = open("styles.css", "w+")
cssh.write(css)
cssh.close()
print("written css")

fh = open("index.html", "r")
fh = fh.readlines()
# print(fh)
