#iJ

import requests
import time
import os

logo = ("""
          /
      __ /
     /  /\ 
  --|--/--|--
     \/__/ 
     /     Zodiac
    /


""")
print(logo + "Enter data (If you don't know something, leave it blank)\n")


def main():
    name = input("name: ").strip()
    name2 = input("2nd name: ").strip()
    surname = input("surname: ").strip()
    surname2 = input("2nd surname: ").strip()
    nickname = input("nickname: ").strip()

    if (name == "") or (surname == ""):
        print("\nYou must enter name and surname\n")
        main()

    extension = input("\nwebsite extension: ").strip()
    if extension == "":
        extension = ".com"
    if ("." in extension) == False:
        extension = "." + extension

    list = [
        (surname),
        (name + surname),
        (surname + name),
        (name + "-" + surname),
        (surname + "-" + name),    
        (name[0] + surname),
        (surname[0] + name),
        (name + surname[0]),
        (surname + name[0])]
        
    if (name2 != ""):
        list.extend([
            (name + name2 + surname),
            (surname + name + name2),
            (name + "-" +  name2 + "-" +  surname),
            (surname + "-" +  name + "-" +  name2),
            (name + name2 + surname[0]),
            (surname + name[0] + name2),
            (surname + name + name2[0]),
            (name[0] + name2 + surname),
            (surname[0] + name + name2),
            (name[0] + name2[0] + surname),
            (surname + name[0] + name2[0])])

    if (surname2 != ""):
        list.extend([
            (surname + surname2),
            (name + surname + surname2),
            (surname + surname2 + name),
            (surname + "-" + surname2),
            (name + "-" + surname + "-" +  surname2),
            (surname + "-" +  surname2 + "-" +  name),                    
            (name + surname[0] + surname2),
            (surname + surname2 + name[0]),
            (surname + surname2[0] + name),
            (name[0] + surname + surname2),
            (surname[0] + surname2 + name),
            (name + surname[0] + surname2[0]),
            (surname[0] + surname2[0] + name)])

    if (name2 != "") and (surname2 != ""):
        list.extend([
            (name + name2 + surname + surname2),
            (surname + surname2 + name + name2),
            (name + "-" + name2 + "-" + surname + "-" + surname2),
            (surname + "-" + surname2 + "-" + name + "-" + name2),
            (name + name2[0] + surname + surname2[0]),
            (surname + surname2[0] + name + name2[0]),
            (name + name2 + surname[0] + surname2[0]),
            (name[0] + name2[0] + surname + surname2),
            (surname + surname2 + name[0] + name2[0]),
            (surname[0] + surname2[0] + name + name2),
            (name + name2[0] + surname[0] + surname2[0]),
            (surname + surname2[0] + name[0] + name2[0])])
    
    if (nickname != ""):
        list.extend([
            (nickname),
            (nickname + name),
            (nickname + surname),
            (name + nickname),
            (surname + nickname),
            (nickname + name + surname),
            (nickname + surname + name),
            (name + nickname + surname),
            (surname + nickname + name),
            (name + surname + nickname),
            (surname + name + nickname),
            (nickname + "-" + name),
            (nickname + "-" + surname),
            (name + "-" + nickname),
            (surname + "-" + nickname),
            (nickname + "-" + name + "-" + surname),
            (nickname + "-" + surname + "-" + name),
            (name + "-" + nickname + "-" + surname),
            (surname + "-" + nickname + "-" + name),
            (name + "-" + surname + "-" + nickname),
            (surname + "-" + name + "-" + nickname),
            (nickname + name[0]),
            (nickname + surname[0]),
            (name[0] + nickname),
            (surname[0] + nickname),
            (nickname + name[0] + surname),
            (nickname + surname[0] + name), 
            (name[0] + nickname + surname),
            (surname[0] + nickname + name),
            (name[0] + surname + nickname),
            (surname[0] + name + nickname),
            (nickname + name + surname[0]),
            (nickname + surname + name[0]),
            (name + nickname + surname[0]),
            (surname + nickname + name[0]),
            (name + surname[0] + nickname),
            (surname + name[0] + nickname),
            (name[0] + surname[0] + nickname),
            (surname[0] + name[0] + nickname),
            (name[0] + nickname + surname[0]),
            (surname[0] + nickname + name[0]),
            (nickname + name[0] + surname[0]),
            (nickname + surname[0] + name[0])])

    if (nickname != "") and (name2 != ""):
        list.extend([
            (name + name2 + nickname),
            (nickname + name + name2),
            (nickname + name + name2 + surname),
            (nickname + surname + name + name2),
            (name + name2 + nickname + surname),
            (surname + nickname + name + name2),
            (name + name2 + surname + nickname),
            (surname + name + name2 + nickname),
            (name +"-" + name2 +"-" + nickname),
            (nickname +"-" + name +"-" + name2),
            (nickname + "-" + name + "-" + name2 + "-" + surname),
            (nickname + "-" + surname + "-" + name + "-" + name2),
            (name + "-" + name2 + "-" + nickname + "-" + surname),
            (surname + "-" + nickname + "-" + name + "-" + name2),
            (name + "-" + name2 + "-" + surname + "-" + nickname),
            (surname + "-" + name + "-" + name2 + "-" + nickname),
            (nickname + name[0] + name2[0] + surname[0]),
            (nickname + surname[0] + name[0] + name2[0]),
            (name[0] + name2[0] + nickname + surname[0]),
            (surname[0] + nickname + name[0] + name2[0]),
            (name[0] + name2[0] + surname[0] + nickname),
            (surname[0] + name[0] + name2[0] + nickname)])
    
    if (nickname != "") and (surname2 != ""):
        list.extend([
            (surname + surname2 + nickname),
            (nickname + surname + surname2),
            (nickname + name + surname + surname2),
            (nickname + surname + surname2 + name),
            (name + nickname + surname + surname2),
            (surname + surname2 + nickname + name),
            (name + surname + surname2 + nickname),
            (surname + surname2 + name + nickname),
            (surname + "-" + surname2 + "-" + nickname),
            (nickname + "-" + surname + "-" + surname2),
            (nickname + "-" + name + "-" + surname + "-" + surname2),
            (nickname + "-" + surname + "-" + surname2 + "-" + name),
            (name + "-" + nickname + "-" + surname + "-" + surname2),
            (surname + "-" + surname2 + "-" + nickname + "-" + name),
            (name + "-" + surname + "-" + surname2 + "-" + nickname),
            (surname + "-" + surname2 + "-" + name + "-" + nickname),
            (nickname + name[0] + surname[0] + surname2[0]),
            (nickname + surname[0] + surname2[0] + name[0]),
            (name[0] + nickname + surname[0] + surname2[0]),
            (surname[0] + surname2[0] + nickname + name[0]),
            (name[0] + surname[0] + surname2[0] + nickname),
            (surname[0] + surname2[0] + name[0] + nickname)])

    if (nickname != "") and (name2 != "") and (surname2 != ""):
        list.extend([
            (nickname + name + name2 + surname + surname2),
            (nickname + surname + surname2 + name + name2),
            (name + name2 + nickname + surname + surname2),
            (surname + surname2 + nickname + name + name2),
            (name + name2 + surname + surname2 + nickname),
            (surname + surname2 + name + name2 + nickname),
            (nickname + "-" + name + "-" + name2 + "-" + surname + "-" + surname2),
            (nickname + "-" + surname + "-" + surname2 + "-" + name + "-" + name2),
            (name + "-" + name2 + "-" + nickname + "-" + surname + "-" + surname2),
            (surname + "-" + surname2 + "-" + nickname + "-" + name + "-" + name2),
            (name + "-" + name2 + "-" + surname + "-" + surname2 + "-" + nickname),
            (surname + "-" + surname2 + "-" + name + "-" + name2 + "-" + nickname),
            (nickname + name[0] + name2[0] + surname[0] + surname2[0]),
            (nickname + surname[0] + surname2[0] + name[0] + name2[0]),
            (name[0] + name2[0] + nickname + surname[0] + surname2[0]),
            (surname[0] + surname2[0] + nickname + name[0] + name2[0]),
            (name[0] + name2[0] + surname[0] + surname2[0] + nickname),
            (surname[0] + surname2[0] + name[0] + name2[0] + nickname)])

    print()
    websites = []
    
    output = True 
    #change to False if you do not want to create output.txt
    
    if output == True:
        if os.path.exists("output.txt") == True:
            os.remove("output.txt")
    
    for item in list:
        url = ("http://" + item.lower() + extension)
        print(f"Checking : {url}")
        try:
            r = requests.get(url)
            if r.status_code != 404:
                    websites.append(url)

        except requests.exceptions.ConnectionError:
            pass

    os.system("cls||clear")
    print(logo + "Possible owner of these websites:\n")

    for item in websites:
        print(item.lower())
        if output == True:
            file = open("output.txt", "a").write(item + "\n")

main()
input()
