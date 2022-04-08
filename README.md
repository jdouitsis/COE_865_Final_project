# COE 865 - Final Project

## About

This is the final project for the computer engineering course COE 865. The purpose is to create a network topology from configuration files and then map out the shortest path between different nodes.

## How to run the program

Steps to run the program

1. All of the config files for each router need to be placed in the [configs](configs) directory with the format below:

```
1 100 10.2.2.1	; RCID ASN IP Address (local rc info)
2	            ; No. of RC connected
2 200 10.1.1.2	; RCID ASN IP Address
3 300 11.1.1.2	; RCID ASN IP Address
4	            ; No. of ASN connected
10 2 5 	        ; ASN Mbps(link capacity) cost
20 5 5	        ; ASN Mbps(link capacity) cost
200 10 5        ; ASN Mbps(link capacity) cost
300 10 5        ; ASN Mbps(link capacity) cost
```

2. Run the following commands below

```sh
python3 -m venv venv            # Setup virtual environment
. venv/bin/activate             # Enter the virtual environment
pip install -r requirements.txt # Install dependencies
python app.py                   # Run the program
```

Once running, the program will prompt the user for the source and receiver, then it will map out the shortest path and display it to the user.
