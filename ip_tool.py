#!/usr/bin/env python3

import argparse
import ipaddress
import json
import os
import socket

def get_container_ip_network():
    """Retrieve the container's IP address and subnet."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    subnet_mask = "255.255.255.0"  # Assuming a /24 subnet for simplicity
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    return str(network)

def check_ip_collisions(file_path):
    """Check for IP range collisions from a given file containing IP networks."""
    try:
        with open(file_path, "r") as file:
            ip_networks = [ipaddress.IPv4Network(line.strip()) for line in file.readlines()]

        collisions = set()
        for i, net1 in enumerate(ip_networks):
            for j, net2 in enumerate(ip_networks):
                if i != j and net1.overlaps(net2):
                    collisions.add(str(net1))

        if collisions:
            print(f"Colliding Networks: {json.dumps(list(collisions), indent=2)}")
        else:
            print("No IP collisions detected.")
    except Exception as e:
        print(f"Error reading file or processing networks: {e}")

def main():
    parser = argparse.ArgumentParser(description="IP Tool for checking network configurations and collisions")
    parser.add_argument("--check-collision", type=str, help="Check for IP collisions from the given file")
    args = parser.parse_args()

    if args.check_collision:
        check_ip_collisions(args.check_collision)
    else:
        print(get_container_ip_network())

if __name__ == "__main__":
    main()
