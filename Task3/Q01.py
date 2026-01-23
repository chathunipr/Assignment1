len = float(input("Enter the length(cm) of the zander: "))

sizeLimit = 42

dif = sizeLimit - len

if len >= sizeLimit:
    print("Size meets the requirements. You can keep the fish")
else:
    print("Size meets the requirements. Size difference is ",dif)
    print("Please release the fish to the lake")

        