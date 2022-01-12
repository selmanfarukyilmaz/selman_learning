def countingValleys(steps, path):
    kot = 0
    valley = 0
    for i in path:
        if i == "U":
            kot +=1
            if kot == 0:
                valley += 1
        else:
            kot -= 1

    return valley

#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup