import easygui
arv1 = easygui.integerbox("Esimene arv: ", lowerbound = 1, upperbound = 10)
arv2 = easygui.integerbox("Teine arv: ", lowerbound = 1, upperbound = 10)
tehted = ["+", "-", "*"]
valik = easygui.buttonbox("Vali üks kolmest", choices = tehted)
if valik == "+":
    easygui.msgbox(arv1+arv2)
elif valik == "-":
    easygui.msgbox(arv1-arv2)
else:
    easygui.msgbox(arv1*arv2)