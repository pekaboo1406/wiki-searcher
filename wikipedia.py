import lxml
import bs4
import requests
import webbrowser

weblink = ""


def get_input():
    s = input("WHAT DO YOU WANT TO SEARCH FOR TODAY ? ")
    search(s)


def search(s):
    globals()['web_link'] = "https://en.wikipedia.org/wiki/" + s

    re = requests.get(globals()['web_link'])
    soup = bs4.BeautifulSoup(re.text, "lxml")
    soup.select(".toctext")
    print()

    print(s.upper() + " : ")

    print("TABLE OF CONTENTS : ")
    print()
    ctr = 1
    for i in soup.select(".toctext"):
        print(ctr, end=". ")
        print(i.getText())
        ctr += 1

    print()
    print()


def redirect(n):
    re = requests.get(globals()['web_link'])
    soup = bs4.BeautifulSoup(re.text, "lxml")
    soup.select(".toctext")

    l = (soup.select(".toctext")[n - 1].getText()).replace(" ", "_")

    open_link = globals()['web_link'] + "#" + l
    webbrowser.open(open_link)


def main():
    get_input()
    n = int(input("ENTER THE NUMBER OF THE REQUIRED TOPIC : "))
    print()
    r = int(
        input("OKAY.DO YOU WISH TO BE REDIRECTED TO THE WEB-PAGE CONTAINING YOUR INFORMATION? PRESS 1 FOR YES AND 0 "
              "FOR "
              "NO AND 9 IF YOU WANT TO SEARCH FOR SOMETHING ELSE. : "))

    if r == 1:
        print()
        print("YOU ARE NOW BEING REDIRECTED TO YOUR BROWSER.")
        redirect(n)

    elif r == 9:
        print()
        print()
        main()

    elif r == 0:
        print("THANK YOU.")


if __name__ == "__main__":

        main()



