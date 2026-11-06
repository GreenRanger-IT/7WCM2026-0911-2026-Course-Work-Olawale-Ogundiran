# Ask: write a function using recursion

def follow_instructions(instructions: list[str]) -> list[int]:
  # let our index be i and stop if index does not exist
  def checker(i, checked):
    if i < 0 or i >= len(instructions):
      return checked
    checked.append(i)

    current_element = instructions[i]

    if current_element == "green":
      next_i = i + 1
    
    elif current_element == "red":
      next_i = (2 * i) + 1
    
    elif current_element == "blue":
       # find next occurrence of blue
       next_blue = -1

       for i in range(i + 1, len(instructions)):
         if instructions[i] == "blue":
           next_blue =  i
           # exit loop if blue is found
           break
         if next_blue == -1:
         
          return checked
         next_i = next_blue + 1
       
    else:
      return checked
    return checker(next_i, checked)

  return checker(0,[])

# Tests: given 2 instructions: inst_1 and inst_2
inst_1=["green", "red", "red", "blue","green", "blue", "green"]
inst_2=["red", "red", "blue", "green", "green", "red"]

# call the follow instruction function

outcome_1 = follow_instructions(inst_1)
print(outcome_1)

outcome_2 = follow_instructions(inst_2)
print(outcome_2)