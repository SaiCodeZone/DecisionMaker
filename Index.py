from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER so we can use it later
sentimentAnalyser = SentimentIntensityAnalyzer()

#input choices
choices =  input("Enter your choices: ").split()

print(choices)
Strengths=list()
highStrength=0
suggestedchoice=""
ChoicesList={}
for choice in choices:
    print("Enter atleast two pros why you want "+ choice+", type quit to stop:")
    #pros=list()
    #cons=list()
    scores=list()
    
    i=1
    Strength=0
    while True:
        pro = input(i)
        if(pro=="quit"):
            if(i<=2):
                print("please enter atleast 2 pros to make better choice")
                continue
            else:
                break
        #pros.append(pro)
        i=i+1
        score=sentimentAnalyser.polarity_scores(pro)
        Strength=Strength+score['compound']
        scores.append(score)

    #print(pros)
    print("Enter some cons why you dont want "+choice+", type quit to stop:")
    i=1
    while True:
        con=input(i)
        if(con=="quit"):
            break
        #cons.append(con)
        i=i+1
        score=sentimentAnalyser.polarity_scores(con)
        Strength=Strength+score['compound']
        scores.append(score)
    #print(cons)
    #Details=list()
    ##Details.append(cons)
    #print("compound score of "+choice+" is:",compoundscore)
    if(highStrength<Strength):
        highStrength=Strength
        suggestedchoice=choice
    Strengths.append(Strength)
    #print(compoundscores)
    ChoicesList[choice]=scores


print(ChoicesList)
print(Strengths)

print("Suggested better choice",suggestedchoice)

