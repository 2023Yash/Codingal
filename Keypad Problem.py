keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def keypad_combination(combination, curr, output, n):
    if (curr == n):
        print(*output, sep=",")
        return
    
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        keypad_combination(combination, curr + 1, output, n)
        output.pop()

        if(combination[curr] == 0 or combination[curr] == 1):
            return
        
combination = [4, 3, 4]
n = len(combination)
keypad_combination(combination, 0, [], n)