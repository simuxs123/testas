# 1.
labas="labas";
skaicius=5;
tiesa=True;
kitasSkaicius=5.5;

# 2.
skaiciai=[6,3,9,1,1,2,2,2,3,4,5];
vaikas={
    "name":"petras",
    "age":15
}
# 3

manoKintamasis="bla"

# 4
skaiciusFloat=float(4.5);

# 5
def my_function(arr):
    for el in arr:
        print(el);

print(my_function(skaiciai));

# 6
kintamasis = "IlgasSakinys"
x = kintamasis[2:5]
y = kintamasis[7:9]

x="gas";
y="ki";

# 7
# kintamas ar nekintamas tipas ar struktura
# tarkim string nekintamas, array kintamas
# skaiciai=[6,3,9,1,1,2,2,2,3,4,5];
# skaiciai[0]=5; kintamas
# labas="labas";
# labas[0]="b"; nekintamas

# 8. Jeigu norėtumėm patobulinti mūsų funkcija kuri išspauzdina sarašo įrašus žinant,
# kad type(kintamasis) gražina kintamojo data tipą parašyti funkcija kuri patikrina ar
# parametras funkcijoje yra list ar dictionary ir išspauzdinti jų reikšmes.
def my_function(data):
    if type(data) is list:
        print("your data is a list")
        for el in data:
            print(el);
    elif type(data) is dict:
        print("your data is Dictionary")
        for key,value in data.items():
            print(key," ",value);

print(my_function(skaiciai));
print(my_function(vaikas));
