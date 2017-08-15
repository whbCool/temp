import math
import time
tst = open("CashierMlog.txt", 'w+')

def addit(bal, adnum):
    x = bal + adnum
    print "%d + %d = %d" % (bal, adnum, x)
    return "%d + %d = %d" % (bal, adnum, x)
    addlog("%d + %d = %d" % (bal, adnum, x))


#def subtr(bal, subnum):
#    x = bal - subnum
#    print "%d - %d = %d" % (bal, subnum, x)
#    return "%d - %d = %d" % (bal, subnum, x)
#    addlog("%d - %d = %d" % (bal, subnum, x))


def change(total, paid):
    x = bal - subnum
    print "Change: %s" % x
    cf = open("CashierMlog.txt", 'a')
    cf.write("Change given during transaction: %s\n") % x


def addlog(history):
    print "Added to log."
    cf = open("CashierMlog.txt", 'a')
    cf.seek(0)
    cf.write("\n"), cf.write(time.strftime("%d/%m/%Y\n"))
    cf.write(history), cf.write("\n")
    cf.close

def intro():
    introprompt = float(raw_input("What is the total starting balance?\n> "))
    roundint = math.ceil(introprompt*100)/100)
    while True:
        prompt = int(raw_input("How many items is the person buying (Whole numbers only)?\n> "))
        if prompt == 1:
            prompt = prompt + 1
            w = prompt - 1
            print "What are the prices of each of the %d item(s)?" % w
        else:
            print "What are the prices of each of the %d item(s)?" % prompt

        itemslist = []


        for i in range(1, prompt):
            price = float(raw_input(">"))
            roundprice = math.ceil(price*100)/100)
            itemslist.append(price)
            print "%d" % price

        ttl = sum(itemslist)
        print "Total owed: %d" % ttl
        print "How much money are they paying with?"
        paidwt = float(raw_input("> "))
        roundpaidwt = math.ceil(paidwt*100)/100)

        if paidwt > ttl:
            admon = change(roundpaidwt, ttl)
            addit(roundint, admon)
            introprompt = roundint + addit(roundint, admon)
        elif paidwt < ttl:
            print "Insufficient funds."
        elif paidwt == ttl:
            addit(roundint, ttl)
            introprompt = roundint + addit(roundint, ttl)


def setup():
    print "Welcome to CashierMate v0.0.1. Type CTRL-C to quit at any time."
    while True:
        if "Transaction History" in open("CashierMlog.txt").read():
            intro()
        else:
            target = open("CashierMlog.txt", 'w+')
            target.write("Transaction History")
            target.close

setup()
