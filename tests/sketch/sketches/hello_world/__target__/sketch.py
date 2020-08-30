import math

def log(iterations):
        node = document.getElementById("sketch-holder")
        for _ in iterations:
            textnode = document.createTextNode("Hello World")
            node.appendChild(textnode)
            br = document.createElement("br")
            node.appendChild(br)

def main(iterations):
    log(range(iterations))

main(6)