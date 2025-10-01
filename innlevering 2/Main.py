filnavn = input("Vennligst legg ved din fil:\n")

with open(filnavn+"_merge.out", "w") as file:
    # Write content to the file
    file.write("This is the first line.\n")
    file.write("This is the second line.")

print("Content written to my_file.txt (overwriting if it existed).")
  
