# packtpub-claimer
Simple, lightweight free e-book claimer from Packtpub

# step by step usage
1. Change ${PP_USER} and ${PP_PASS} to yours Packtpub user and password
2. In folder with docker-compose.yml run command:
```
docker-compose build
```
3. After build have been finished run command:
```
docker-compose up -d
```
4. Once a day there will be new e-book saved on your Packtpub account. 

# additional informations
* In filter.txt you can add new line with unwanted books (words)
* File claimed.txt will have list of saved titles
* To make it work on Raspberry Pi or other devices with **ARM architecture** change content of Dockerfile to Dockerfile.rpi
