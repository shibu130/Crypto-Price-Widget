from tkinter import Tk,Label
import requests
from sys import exit
from time import perf_counter,ctime


btc_price="starting!"
eth_price="starting!"


def main():
    
    root=Tk()
    Bitcoin=Label(root,text="bitcoin")
    Ethereum=Label(root,text="etherum")
    Btc_Price=Label(root,text=btc_price)
    Eth_Price=Label(root,text=eth_price)

    Bitcoin.grid(row=0,column=0)
    Btc_Price.grid(row=0,column=1)
    Ethereum.grid(row=1,column=0)
    Eth_Price.grid(row=1,column=1)

    def Price():
        a=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd%2Cusd").json()
        Btc_Price.configure(text=str(a['bitcoin']['usd'])+"$")
        Eth_Price.configure(text=str(a['ethereum']['usd'])+"$")
        root.after(15000,Price)
        print("refreshed at {}  ".format(str(ctime())))
    
    Price()
    root.title("crypto prices")
    root.iconbitmap(None)
    root.resizable(0,0)
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Crtl C pressed exiting")
        exit()
