# QA-DevOps-Core-Practical-Project



Bug fix - ended up wit a bug becuase the beholder array only had 5 items not 6, this lead to trying to write more tests to check this, this led me to discovering that python does not like multiple or statements, or atleast the way i had written them in the if statements meant that the new tests werent passing, as such the conditional for these was changed from 

    if x == (a or b or c) 
    to 
    if x in (a, b,c)

GCP seems to have issues with running more than 1 instance of each service, using replicas caused issues, currently uncertain how to solve. Also even though the swarm-worker is running services, when I attempt to visit the app on the swarm-worker, i end up with This site can’t be reached The connection was reset. 
