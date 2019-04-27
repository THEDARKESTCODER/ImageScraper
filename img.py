

import string, random, os, sys, _thread, urllib, time, requests




if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python3 " + sys.argv[0] + " (Number of threads)")
THREAD_AMOUNT = int(sys.argv[1])

print ("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\nThis script is for educational purposes only! Use on your own responsibility!\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
input("Press ENTER if you have read and accept that you are fully responsible for using this script!\n")

INVALID = [0, 503, 5082, 4939, 4940, 4941, 12003, 5556]

def scrape_pictures(thread):
    while True:
        #url = 'http://img.prntscr.com/img?url=http://i.imgur.com/'
        url = 'http://i.imgur.com/'
        length = random.choice((5, 6))
        if length == 5:
            url += ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(5))
        else:
            
            url += ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(6))
            url += '.jpg'
            # print (url)


            filename = url.rsplit('/', 1)[-1]
            # print (filename)

            r = requests.get (url, allow_redirects=True)
            open(filename , 'wb').write(r.content)

           
            file_size = os.path.getsize(filename)
            if file_size in INVALID:
                print("[-] Invalid: " + url)
                os.remove(filename)
            else:
                print("[+] Valid: " + url)

for thread in range(1, THREAD_AMOUNT + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(scrape_pictures, (thread,))
    except:
        print('Error starting thread ' + thread)
print('Succesfully started ' + thread + ' threads.')

while True:
    time.sleep(1)
