# author: rithea cheng
# date: 9/11/19
# random select 5 question out of 20 maori language.

import random;

questions = ["ngutu","tamariki","kirikiri","pī","poraka","tī","aihikirīmi","kūmara","rīwai","rererangi","moenga","niho","pere","pōro","rorohiko","kura","huruhuru","pea","tapuwae","kurī"];
answers = ["lip","children","sand","bee","frog","tea","ice cream","sweet potato","potato","airplane","bed","tooth","bell","ball","computer","school","feather","pair","footprint","dog"];



# generate 5 random number into the list Num5
def gen5():
    while(len(Num5)<5):
        mynum = random.randint(0,19);
        while(mynum in Num5):
            mynum = random.randint(0,19);
        Num5.append(mynum);

#print(Num5);

#questions and answers
mycon = 'y'
while(mycon != 'n'):
    score = [];
    Num5 = [];
    gen5()
    print("\nThis is the quiz to test your understanding of maori language.\n")
    for i in range(0,5):
        myindex = int(Num5[i]);
        print("Question "+str(i+1)+":");
        print('what is the word "'+questions[myindex]+'" mean?');
        user_ans = input("ans: ");
        if user_ans.lower() == answers[myindex]:
            print("Correct answer.\n");
            score.append(1);
        else:
            print("Wrong answer.\n");
            score.append(0);

    # results
    myscore = 0;
    for k in score:
        myscore += k;
    print("Result:");
    print("your score is: "+str(myscore*20)+"%");
    mycon = input("do you want to start again?(y/n) ")
    
        

    
    
