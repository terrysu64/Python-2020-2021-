#Name: Terry Su
#Date: December 27, 2020
#Purpose:
# - Create a 'hypothetical' program that can determine the number of moles given a compound and a mass
# - Class suggestion
# - just something I thought of trying during the winter break

Elements = {'H':1,'He':3,'C':12,'O':16,'Ca':40,'Fe':55}
Elements_key = ['H','He','C','O','Ca','Fe']

Formula = str(input('enter element formula with subscripts as normal numbers ex:H2O :'))
Mass = int(input('enter mass in grams :'))

compound_elements = []
compound_elements_mass = []
molar_mass = 0

count = 1
ele_count = 1

for x in Elements_key:
    Elements_index = Formula.find(x)

    if Elements_index != -1 and (Formula[Elements_index + len(x): Elements_index + 1 + len(x)].islower() == False or type(Formula[Elements_index + len(x): Elements_index + 1 + len(x)]) == int):
        compound_elements.append(x)

        if type(Formula[Elements_index + len(x): Elements_index + 1 + len(x)]) == int:
                
            while type(Formula[Elements_index + len(x): Elements_index + count + len(x)]) == int:
                ele_count = type(Formula[Elements_index + len(x): Elements_index + count + len(x)])
                count += 1
                    
            for y in range(0,ele_count - 1):
                compound_elements.append(x)

for x in compound_elements:
    compound_elements_mass.append(Elements[x])

for x in compound_elements_mass:
    molar_mass += x

print('there are ' + str(Mass / molar_mass) + ' moles')
    
#split element cases
#one capital, capital + lowercase, frm both options also no subscript or subscript
