students={
 
    "Jisna":35,
    "Nabeel":55,
    "Dilawar":90
}
for mark in students:
    marks=students[mark]
    if(marks>40):
        print(mark, ":",marks,"Pass")
    else:
        print(mark, ":",marks,"Fail")
