import csv
import random
def quiz_game():

    def load_csv_file():
       total_list=[]
       with open("quiz.csv") as csv_file:
           csv_reader = csv.reader(csv_file,delimiter=",")
           for row in csv_reader:
               total_list.append(row)
       return total_list

    def shuffle_list(q_a_list):
       random.shuffle(q_a_list)

    def pick_random_quiz(q_a_list, que_amongt):
        picked_quiz = []
        for i in range(que_amongt):
            picked_quiz.append(q_a_list[i])
        return picked_quiz
    
    def get_question_list(picked_list):
        q_list=[]
        for q in picked_list:
            q_list.append(q[0])
        return q_list
    
    def get_answer_list(picked_list):
        a_list=[]
        for q in picked_list:
            a_list.append(q[1:])
        return a_list
    
    def display_questions(picked_list,count):
            print ("Question "+str(count+1)+": "+picked_list[count])

    def shuffle_answer_list(answer):
         for a in answer:
             random.shuffle(a)

    def display_answers(ans_list,count):
        answer_list = ans_list[count]
        optionNo=1
        for a in answer_list:
            if a != "":
              print ("   optionNo "+str(optionNo)+": "+a)
              optionNo+=1

    def get_user_choice(round):
        user_answer=0
        answer_len=len(answer_list[round])
        user_answer=input("Your answer is: ")
        while not user_answer.isdigit() or int(user_answer)<=0 or int(user_answer)>answer_len: 
            user_answer=input("Enter a valid number: ")   
        return int(user_answer)
    
    def check_answer_correct(uers_ans,rounds,correct_answer):
        if answer_list[rounds][uers_ans] == correct_answer:
          return 1
        else:return 0
    
    def check_valid(char):
        if char !="y" and char !="n":
            return False
        return True

     #get ready before play
    quiz_amount=7
    full_list=load_csv_file()
    shuffle_list(full_list)
    picked_quiz_list=pick_random_quiz(full_list,quiz_amount)
    
    #game start
    round_count,right_ans=0,0
    question_list=get_question_list(picked_quiz_list)
    answer_list=get_answer_list(picked_quiz_list)
    #quiz and answer
    while round_count < quiz_amount:
      correct_answer=answer_list[round_count][0]
      shuffle_answer_list(answer_list)
      display_questions(question_list,round_count)
      display_answers(answer_list,round_count)

      user_answer=get_user_choice(round_count)
      right_ans+=check_answer_correct(user_answer-1,round_count,correct_answer)
      
      round_count+=1

    print ("Your score is " + str(right_ans)+"!")
    #how it ends
    is_again=input("Have another go? y/n: ")
    while check_valid(is_again)==False:
        is_again=input("Enter only y or n: ")
    if is_again=="y":
        quiz_game()

    
    

quiz_game()