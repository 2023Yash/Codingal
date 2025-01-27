def frequency_count(s):
    d = {}
    for i in range(len(s)):
        if(s[i] in d.keys()):
            d[s[i]] += 1
        else:
            d[s[i]] = 1

    return d

def anagram(a_str, b_str):
    if(frequency_count(a_str.lower()) == frequency_count(b_str.lower())):
        print("anagram confermed")
    else:
        print("anagram not confermed")

anagram("listen", "silent")

def word_counter(sentence):
    sentence = sentence.strip()
    ans = 0
    if(len(sentence) != 0):
        ans = 1
        for i in range(len(sentence)):
            if(sentence[i] == " " and sentence[i + 1] != " "):
                ans += 1
    print(ans)

word_counter("   Playing with   frequency")