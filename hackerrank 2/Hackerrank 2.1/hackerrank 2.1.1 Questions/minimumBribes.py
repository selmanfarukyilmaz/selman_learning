def minimumBribes(q):
    n = len(q)
    result = ""
    counter = 0
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for ii in range(i + 1):
            if q[ii] > q[i]:
                counter += 1

    print(counter)


minimumBribes([1, 5, 2, 3, 4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])


# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def minimumBribess(q):
    n = len(q)
    result = ""
    counter = 0
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for ii in range(i + 1):
            if q[ii] > q[i]:
                counter += 1

    print(counter)


minimumBribess([1, 5, 2, 3, 4])
minimumBribess([1, 2, 5, 3, 7, 8, 6, 4])
minimumBribess([1, 2, 5, 3, 7, 8, 6, 4])
