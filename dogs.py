# Name: Zac Huffman
# Purpose: This program demonstrates how to manipulate a list, including:
# finding number of items in the list, sorting the list, adding/removing items,
# copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle",
        "Gonzo", "Sweetie-Pie", "Diego"]
dogs2 = []

def main():
    how_many = len(dogs)
    print("\nNumber of dogs in the list, using len(): " + str(how_many))
    print("\nOriginal list of dog names:")
    print(dogs)
    input("\nPress ENTER to continue...")

    dogs.reverse()
    print("\nList from last to first, using reverse():")
    print(dogs)
    input("\nPress ENTER to continue...")

    dogs.sort()
    print("\nAlphabetized list, using sort():")
    print(dogs)
    input("\nPress ENTER to continue...")

    dogs.sort(reverse=True)
    print("\nList in reverse alphabetized order, using sort(reverse=True):")
    print(dogs)
    input("\nPress ENTER to continue...")

    dogs.append("Ranger")
    print("\nAdd a dog to the end of a list, using append():")
    print(dogs)
    input("\nPress ENTER to continue...")

    doggy = dogs.pop(0)
    print("\nRemove a dog off from the front of the list, using pop():")
    print(doggy + " was removed from the front of the list.")
    print(dogs)
    input("\nPress ENTER to continue...")

    another_dog = dogs.pop(3)
    print("\nRemove a dog from position 3 (the 4th dog) in the list, using pop(index-here):")
    print(another_dog + " was removed from position 3 of the list.")
    print(dogs)
    input("\nPress ENTER to continue...")

    dogs.remove("AnnaBelle")
    print("\nRemove a dog by name rather than position in the list, using remove(name-here):")
    print(dogs)
    input("\nPress ENTER to continue...")

    dogs2 = dogs
    print("\nA list can be copied into another list by setting one equal to the other:")
    print("Dogs: ")
    print(dogs)
    print("Dogs2: ")
    print(dogs2)
    input("\nPress ENTER to continue...")

    print("\nUse a FOR loop to give each dog in the list the same last name, using the for loop:")
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Huffman"  
    print(dogs)

    input("\nPress ENTER to continue...")

main()
