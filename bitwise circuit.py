def circuit(A, B, C):
    output1 = A & B
    output2 = A & C
    output3 = B & C
    output4 = output1 | output2 | output3
    output = output4 & (output1 | output2 | output3)

    return output

A = 1
B = 0
C = 1

output = circuit(A, B, C)

print(f"A = {A} B = {B} C = {C} and output is {output}")