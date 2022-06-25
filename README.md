# QA-DevOps-Core-Practical-Project



Bug fix - ended up wit a bug becuase the beholder array only had 5 items not 6, this lead to trying to write more tests to check this, this led me to discovering that python does not like multiple or statements, or atleast the way i had written them in the if statements meant that the new tests werent passing, as such the conditional for these was changed from 

    if x == (a or b or c) 
    to 
    if x in (a, b,c)
