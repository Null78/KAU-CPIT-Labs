# Table header
print("--------------------------------------------------------")
# print kilograms to the left with width 10 and type string
print(format("kilograms", "<10s"),
      # print pounds to the right with width 10 and type string
      format("pounds", ">10s"),
      # spcae between columns
      "     |     ",
      # print pounds to the left with width 10 and type string
      format("pounds", "<10s"),
      # print kilograms to the right with width 10 and type string
      format("kilograms", ">10s"))
print("--------------------------------------------------------")

# Defain counting variables
kg = 1
pnd = 20

while kg <= 199:
    # Calculate
    kg_to_pnd = kg * 2.2
    pnd_to_kg = pnd * 0.45

    # Display the resault
    # print kg to the left with width 10 and type integer
    print(format(kg, "<10d"),
    # print kg_to_pnd to the right with width 10 rounded by 1 and type float
    format(kg_to_pnd, ">10.1f"),
    # spcae between columns
    "     |     ",
    # print pnd to the left with width 10 and type integer
    format(pnd, "<10d"),
    # print pnd_to_kg to the right with width 10 rounded by 2 and type float
    format(pnd_to_kg, ">10.2f"))

    # Add 2 to kg and 5 to pnd
    kg += 2
    pnd += 5
