A=[11,12,13,14,11]

def peakfinder(Array):
    mid=(len(Array)-1)//2
    print(f"{Array[mid]}")

    #deal with the case when there is just one element and it's the peak
    if len(Array)==1:
        return Array[mid]

    # Deal with the case when two elements and edge element is the peak
    elif len(Array)==2:
        return max(Array[0], Array[1])

    else:
        if Array[mid]<=Array[mid-1]:
            print(Array[:mid])
            return peakfinder(Array[:mid])
        elif Array[mid]<=Array[mid+1]:
            print(Array[mid:])
            return peakfinder(Array[mid:])
        else:
            return Array[mid]

def main():
    peak=peakfinder(A)
    print(f"Element order")
    print("-----------------")
    print(f"One peak in the array is {peak}")


if __name__ == '__main__':
    main()
