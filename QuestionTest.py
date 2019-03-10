from Question import Question
questions_prompts =[
    "What color are apples? \n(a) Red/Green \n(b)Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Teal \n(b) Yellow\n(c)Red\n\n",
    "What color are strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n"
    ]


test = [
    Question(questions_prompts[0],"a"),
    Question(questions_prompts[1],"b"),
    Question(questions_prompts[2],"b")
    ]
def run_test(test):
    score=0
    for item in test:
        guess = input(item.prompt)
        if guess== item.answer:
            score=score+1
    print("You got: " +str(score) + "/"+str(len(test))+" correct.")
    
run_test(test)    
