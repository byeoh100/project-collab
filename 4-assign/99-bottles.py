def bottle_song():
    bottle_count = 99
    while bottle_count > 1:
        print(f"{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer.")
        print(f"Take one down and pass it around, {bottle_count - 1} bottles of beer on the wall.")
        bottle_count -= 1
    print(f"{bottle_count} bottle of beer on the wall, {bottle_count} bottle of beer.")
    print(f"Take one down and pass it around, no more bottles of beer on the wall.")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
bottle_song()