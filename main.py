notes = []
x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

'#Start of remove one'
n = str(input("Would you like to delete something from the list? : "))
if n == 'yes':
    y = str(input("Which element would you like to remove? Use index : "))
    if y == '0':
        del notes[0]
        print(notes)
    if y == '1':
        del notes[1]
        print(notes)

if n == 'no':
    x = str(input("Enter a note here: "))
    notes.append(x)
    for note in notes:
        print("\t", note)
'#End of remove one'

x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

'#Start of remove two'
n = str(input("Would you like to delete something from the list? : "))
if n == 'yes':
    y = str(input("Which element would you like to remove? Use index : "))
    if y == '0':
        del notes[0]
        print(note)
    if y == '1':
        del notes[1]
        print(note)
    if y == '2':
        del notes[2]
        print(note)

if n == 'no':
    x = str(input("Enter a note here: "))
    notes.append(x)
    for note in notes:
        print("\t", note)
'#End of remove two'
x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

'#Start of remove three'
n = str(input("Would you like to delete something from the list? : "))
if n == 'yes':
    y = str(input("Which element would you like to remove? Use index : "))
    if y == '0':
        del notes[0]
        print(note)
    if y == '1':
        del notes[1]
        print(note)
    if y == '2':
        del notes[2]
        print(note)

if n == 'no':
    x = str(input("Enter a note here: "))
    notes.append(x)
    for note in notes:
        print("\t", note)
'#End of remove three'

x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

'#Start of remove four'
n = str(input("Would you like to delete something from the list? : "))
if n == 'yes':
    y = str(input("Which element would you like to remove? Use index : "))
    if y == '0':
        del notes[0]
        print(note)
    if y == '1':
        del notes[1]
        print(note)
    if y == '2':
        del notes[2]
        print(note)

if n == 'no':
    x = str(input("Enter a note here: "))
    notes.append(x)
    for note in notes:
        print("\t", note)
'#End of remove four'

x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

'#Start of remove five'
n = str(input("Would you like to delete something from the list? : "))
if n == 'yes':
    y = str(input("Which element would you like to remove? Use index : "))
    if y == '0':
        del notes[0]
        print(note)
    if y == '1':
        del notes[1]
        print(note)
    if y == '2':
        del notes[2]
        print(note)

if n == 'no':
    x = str(input("Enter a note here: "))
    notes.append(x)
    for note in notes:
        print("\t", note)
'#End of remove five'

x = str(input("Enter a note here: "))
notes.append(x)
for note in notes:
    print("\t", note)

'#Start of remove six'
n = str(input("Would you like to delete something from the list? : "))
if n == 'yes':
    y = str(input("Which element would you like to remove? Use index : "))
    if y == '0':
        del notes[0]
        print(note)
    if y == '1':
        del notes[1]
        print(note)
    if y == '2':
        del notes[2]
        print(note)


if n == 'no':
    x = str(input("Enter a note here: "))
    notes.append(x)
    for note in notes:
        print("\t", note)
'#End of remove six'

if y == 'no':
    print("You chose to not delete any notes.")
    x = str(input("Enter a note here: "))
    notes.append(x)
    print("\t", notes)
