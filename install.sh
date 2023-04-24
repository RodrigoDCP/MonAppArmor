#!/bin/bash

# Instalación de Python, Python3 y pip3 si no están instalados
if ! command -v python3 &> /dev/null
then
    echo "Python3 no se encuentra instalado"
    sudo apt-get update
    sudo apt-get install python3 -y
else
    echo "Python3 ya está instalado"
fi

if ! command -v python &> /dev/null
then
    echo "Python no se encuentra instalado"
    sudo apt-get update
    sudo apt-get install python -y
else
    echo "Python ya está instalado"
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 no se encuentra instalado"
    sudo apt-get update
    sudo apt-get install python3-pip -y
else
    echo "pip3 ya está instalado"
fi

# Instalación de librerías necesarias
echo "Instalando librerías necesarias..."
sudo pip3 install colorama
sudo pip3 install termcolor

echo "¡Instalación de librerías completada!"
