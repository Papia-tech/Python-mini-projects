import pyttsx3
engine = pyttsx3.init()

engine.say("Enter your birth date and press enter")
engine.runAndWait()
A= int(input("Enter your birth date(in form of dd): "))# 8 as int

engine.say("Enter your birth month and press enter")
engine.runAndWait()
B= int(input("Enter your birth month(in form of mm): "))# 8 as int

engine.say("Enter your birth year and press enter")
engine.runAndWait()
Y= int(input("Enter your birth year(in form of yy): "))# 2006 as int

print(" ")
print(" ")
C=Y//100# 20 as int
D=Y%100# 6 as int

a=f"{A:02}"#08 as string
b=f"{B:02}"#08 as string
c=f"{C:02}"#08 as string
d=f"{D:02}"#08 as string

E=D+1
F=C-1
G=B-3
H=A+3

e=f"{E:02}" 
f=f"{F:02}"
g=f"{G:02}" 
h=f"{H:02}"

I=B-2
J=A+2
K=D+2
L=C-2

i=f"{I:02}" 
j=f"{J:02}"
k=f"{K:02}" 
l=f"{L:02}"

M=C+1
N=D-1
O=A+1
P=B-1

m=f"{M:02}" 
n=f"{N:02}"
o=f"{O:02}"
p=f"{P:02}"

engine.say("The magic square of your date of birth is")
engine.runAndWait()
print(f"The magic square of {a}/{b}/{Y} is: ")
print("---------------")
print(":",a, b, c, d, ":")
print(":",e, f, g, h, ":")
print(":",i, j, k, l, ":")
print(":",m, n, o, p, ":")
print("---------------")
print(" ")
print(" ")

engine.say("Press enter to know more details about this magic square")
engine.runAndWait()
z=input("Press enter")

engine.say("Summation of first row numbers")
engine.runAndWait()
print("sum of first row numbers(08+08+20+06)= 42")
print(a, b, c, d)
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of second row numbers")
engine.runAndWait()
print("sum of second row numbers(07+19+05+11)= 42")
print("--", "--", "--", "--")
print(e, f, g, h)
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of third row numbers")
engine.runAndWait()
print("sum of third row numbers(06+10+08+18)= 42")
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print(i, j, k, l)
print("--", "--", "--", "--")
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of fourth row numbers")
engine.runAndWait()
print("sum of fourth row numbers(21+05+09+7)= 42")
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print(m, n, o, p)
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of first diagonal numbers")
engine.runAndWait()
print("sum of diagonal numbers(08+19+08+07)= 42")
print(a, "--", "--", "--")
print("--", f, "--", "--")
print("--", "--", k, "--")
print("--", "--", "--", p)
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of second diagonal numbers")
engine.runAndWait()
print("sum of diagonal numbers(06+05+10+21)= 42")
print("--", "--", "--", d)
print("--", "--", g, "--")
print("--", j, "--", "--")
print(m, "--", "--", "--")
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of corner numbers")
engine.runAndWait()
print("sum of corner numbers(08+06+07+21)= 42")
print(a, "--", "--", d)
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print(m, "--", "--", p)
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of up middle and down middle numbers")
engine.runAndWait()
print("sum of up middle and down middle numbers(08+06+07+21)= 42")
print("--", b, c, "--")
print("--", "--", "--", "--")
print("--", "--", "--", "--")
print("--", n, o, "--")
print(" ")
print(" ")

engine.say("Press enter to know more")
engine.runAndWait()
z=input("Press enter")
engine.say("Summation of left middle and right middle numbers")
engine.runAndWait()
print("sum of left middle and right middle numbers(08+06+07+21)= 42")
print("--", "--", "--", "--")
print(e, "--", "--", h)
print(i, "--", "--", l)
print("--", "--", "--", "--")
