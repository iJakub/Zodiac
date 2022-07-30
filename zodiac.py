#iJ

import requests
import time
import os

logo = ("""
      |
     _|_ Zodiac
 ___/_|_\___
    \_|_/
      |
      |


""")
print(logo + "Enter data (If you don't know something, leave it empty)\n")


def main():
    name = input("name: ")
    name2 = input("2nd name: ")
    surname = input("surname: ")
    surname2 = input("2nd surname: ")

    if (name == "") or (surname == ""):
        print("\nYou must enter name and surname\n")
        main()

    ns = [
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
        n2 = [
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
            (surname + name[0] + name2[0])] 
        ns.extend(n2)

    if (surname2 != ""):
        s2 = [
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
            (surname[0] + surname2[0] + name)]
        ns.extend(s2)

    if (name2 != "") or (surname2 != ""):
        ns2 = [
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
            (surname + surname2[0] + name[0] + name2[0])]
        ns.extend(ns2)


    print()
    websites = []

    for item in ns:
        url = ("http://" + item.lower() + ".com")
        print(f"Checking : {url}")
        try:
            requests.get(url)
            websites.append(url)
        except requests.exceptions.ConnectionError:
            pass
    os.system('cls||clear')
    print(logo + "Possible owner of these websites:\n")

    for item in websites:
        print(item.lower())     

main()
input()