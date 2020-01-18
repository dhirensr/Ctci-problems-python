def uniqueMorseRepresentations(words):
    result=set()
    encoding=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i in words:
        temp=""
        for j in i:
            temp+=encoding[ord(j)-97]
        result.add(temp)
    return len(result)

print(uniqueMorseRepresentations(["rwjje","aittjje","auyyn","lqtktn","lmjwn"]))
