#how to create a dictionary in python:
#{key:value}

programming_concepts={"bug":"error code",
                      "function":"piece of code that does a specific task ",
                      "python":"a programming language"
                      }

#retreiving data from a dictionary
print(programming_concepts["bug"]) #notice the sq brackets and the data type in "" since it's a string 
print(programming_concepts["function"])
print(programming_concepts["python"])

#adding data to a dictionary 
programming_concepts["loop"]="loop thanne. pokan para.alland ippo nth parayana."
print(programming_concepts)

#to delete the contents of the dictionary entirely
programming_concepts={}


#to create a dictionary in python 
dict={}
#then add data
dict["apple"]="a fruit"
dict["banana"]="another fruit"
dict["cat"]="an animal"
dict["duck"]="a bird "
print(dict)
#print individual data athokke pattum sir
print(dict["duck"])
#wipe out data pattum
dict={}
#how to loop through a dictionary
for key in dict:
    print(key)    #prints only key mone. nth peru venelm kodutho.
    print(dict[key]) #ippo value kitm 
