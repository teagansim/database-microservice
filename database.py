import time

locationData = {
    "seattle": [5, 3, 0, 6, 8, 0],
    "portland": [0, 0, 3, 0, 4, 10, 7],
    "reno": [0, 1, 0, 2, 2],
    "burns": [1, 9, 3, 28, 1, 0, 0]
}

def main():
    loops = 0
    while True:
        time.sleep(1)
        f = open("branch-booking.txt", "r")
        n = f.read()
        if n == "valid" or n == "invalid":
            continue
        if n == "":
            continue
        try:
            int(n)
            continue
        except ValueError:
            pass
        request = n.split(',')
        response = "invalid"
        try:
            location = locationData[request[0]]
        except KeyError:
            f.close()
            f = open("branch-booking.txt", "w")
            f.write(str(response))
            f.close()
            continue
        try:
            branch = int(request[1])
        except IndexError:
            pass
        if len(request) == 1:
            for i in range(len(location)):
                if location[i] != 0:
                    response = i
                    break
        else:
            vacancy = 0
            try:
                vacancy = location[branch]
            except IndexError:
                pass

            if vacancy != 0:
                location[branch] -= 1
                response = "valid"
        f.close()
        f = open("branch-booking.txt", "w")
        f.write(str(response))
        f.close()
            
if __name__ == "__main__":
    main()
