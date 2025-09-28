# 2 input int | +,_*,/%

x = int(input("Entwr Number 1:\n"))
y = int(input("Entwr Number 2:\n"))
print("""1 or Add or + for Addition" \n2 or Sub or - traction \n3 or Mult or * for Multipication \n4 or Divid or / for Division \n5 or Mod or % for Modulas """)
z = (input("The Optration:\n"))
if ("1") in z or "add" in z or "+" in z:
    sum = x + y
    print(f"The sum the numbers is:\n{sum}")
elif ("2") in z or "sub" in z or "-" in z:
    sum = x - y
    print(f"The sum the numbers is:\n{sum}")
elif ("3") in z or "mult" in z or "*" in z:
    sum = x * y
    print(f"The sum the numbers is:\n{sum}")
elif ("4") in z or "divid" in z or "/" in z:
    sum = x / y
    print(f"The sum the numbers is:\n{sum}")
elif ("5") in z or "mod" in z or "%" in z:
    sum = x % y
    print(f"The sum the numbers is:\n{sum}")
else:
    print("Plz Enter valid number betweeen 1 to 5")


