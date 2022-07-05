# QA-DevOps-Core-Practical-Project
## Encounter Generator
### By Ahsan Rasul

The objective of this project is to create and deploy a containerised app using microservices

## ISSUES and BUGS
Bug fix - ended up with a bug becuase the beholder array only had 5 items not 6, this lead to trying to write more tests to check this, this led me to discovering that python does not like multiple or statements, or atleast the way i had written them in the if statements meant that the new tests werent passing, as such the conditional for these was changed from 

    if x == (a or b or c) 
    to 
    if x in (a, b,c)

GCP seems to have issues with running more than 1 instance of each service, using replicas caused issues, currently uncertain how to solve. Also even though the swarm-worker is running services, when I attempt to visit the app on the swarm-worker, i end up with This site can’t be reached The connection was reset. Upon further inspection it turns out that if service1 is on the worker then it fails to return data to the nginx on the manager, all other traffic between the app is bi-directional. This is the case even with the network explictly set to an overlay network, which allows containers on different hosts to communicate with each other, as per the diagram below.  Even with support no solution or reason has been found as of 05/07/22.



Version 1.0



References : https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-install-and-set-up-docker-on-ubuntu-20-04 and https://medium.com/@pierangelo1982/install-docker-with-ansible-d078ad7b0a54 for how to get ansible to install docker.

https://blog.networktocode.com/post/Accessing-other-host-variables-in-Ansible/ for how to access variables from on host and use them in another host
