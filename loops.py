start = int(input("starting number:" ))
end = int(input("ending number:" ))
while start < end : 
    start += 1 
    print(f"{start}")




            
            

        

forbidden_text = "Practical uses for the Necromoicon"
counter = 0
while counter < len(forbidden_text):
    # print out every other letters, but leave out spaces
    if (counter % 2) == 0 and forbidden_text[counter] != " ":
        print(forbidden_text[counter])
    counter = counter + 1
