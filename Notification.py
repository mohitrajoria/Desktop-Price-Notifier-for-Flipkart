import time
import notify2
import scrap
from re import sub
from decimal import Decimal




def noti(product_address,freq,t):
    start = time.time()
    last_price=0
    new_price=0
    elapsed=0
    notify2.init("Notifier")
    last_price = new_price
    new_price = scrap.get_price(product_address)

    sum = new_price+" -> Price"+"\n"+"Further Notifications Will Appear on given Frequency"
    n = notify2.Notification(sum, icon = '/home/mohit/Desktop/app folder/home.jpg')

    n.set_urgency(notify2.URGENCY_NORMAL)

    n.set_timeout(10)

    n.show()

    time.sleep(int(float(freq)))
    elapsed=time.time() - start
    while(elapsed < int(float(t))):
        print(elapsed)

        notify2.init("Notifier")
        last_price = new_price
        new_price = scrap.get_price(product_address)
        diff = int(Decimal(sub(r'[^\d.]', '', new_price))) - int(Decimal(sub(r'[^\d.]', '', last_price)))
        sum = "Price-> "+new_price+" Change-> "+str(diff)
        n = notify2.Notification(sum, icon = '/home/mohit/Desktop/app folder/home.jpg')

        n.set_urgency(notify2.URGENCY_NORMAL)

        n.set_timeout(10)

        n.show()

        time.sleep(int(float(freq)))
        elapsed=time.time() - start
