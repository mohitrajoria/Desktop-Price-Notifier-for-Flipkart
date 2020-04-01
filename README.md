# Desktop-Price-Notifier-for-Flipkart
Recieve price alerts at a desired frequency and  a desired time duration


This desltop notifier is build on python.
The libraries and modules used are requests, beautifulsoup4,notify2,tkinter and time.
The main control is in notifier.py.
When notifier.py is run, a gui appears through the user can control the frequency and time duration of the notification.
And the user is also asked to enter the flipkart page url of the product.
The page is reached is using webscrapping tool requests. It returns the html data of the page.
This data is then extracted using a parsing tool called beautifullsoup.
And the notification is set up using the notify2 tool.
