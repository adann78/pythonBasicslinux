import requests
from os import path
import argparse
import sys

parser= argparse.ArgumentParser(description="Subdominios")
parser.add_argument("-t","--target", help="Dominio a escanear", required=True)
parser=parser.parse_args()
def main():
    if parser.target:
        if path.isfile("subdominios.txt"):
            with open("subdominios.txt","r") as f:
                subdominios=f.read().splitlines()
                for sub in subdominios:
                    url=f"http://{sub}.{parser.target}"
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        print(f"[+] Subdominio encontrado: {url}")
        else:
            print("[!] No se encontró el archivo subdominios.txt")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Saliendo...")
        sys.exit(0)