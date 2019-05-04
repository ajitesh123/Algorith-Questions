A=[1,1,1,2,4,5,6,7,8,9,0]

def peakfinder(Array):
    mid=len(Array)//2
    print(f"{Array[mid]}")
    if Array[mid]<=Array[mid-1]:
        return peakfinder(Array[:mid])
    elif Array[mid]<=Array[mid+1]:
        return peakfinder(Array[mid:])
    else:
        return Array[mid]

def main():
    peak=peakfinder(A)
    print(f"Element order")
    print("-------------")
    print(f"One peak in the array is {peak}")


if __name__ == '__main__':
    main()
