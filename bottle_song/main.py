def sing_ten_green_bottles():
    for i in range(10, 0, -1):
        print(f"{i} green bottles hanging on the wall,")
        print(f"{i} green bottles hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There'll be {i-1} green bottles hanging on the wall.")
        print()

    print("No green bottles hanging on the wall,")
    print("No green bottles hanging on the wall,")
    print("And if all the green bottles should accidentally fall,")
    print("There'll be 10 green bottles hanging on the wall.")


sing_ten_green_bottles()
