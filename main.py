import json
from difflib import get_close_matches

#loading database to the program
def load_database(file_path:str) -> dict:
    with open(file_path,'r') as file:
        data: dict = json.load(file)
    return data

#save data to the database
def save_database(file_path:str,data) -> dict:
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)

#find best matching ansewer
def find_best_ans(user_question:str,questions:list[str]) -> str | None:
    matches: list = get_close_matches(user_question,questions,n=1,cutoff=0.6) 
    # n=1 (only geting best 1 answer)
    # kind of accuracy, if 0.0 not accurate
    return matches[0] if matches else None

#get answer for each question
def get_ans_for_question(question: str, database:dict) -> str | None:
    for q in database["questions"]:
        if q["questions"] == question:
            return q["answer"]
        
def chatBot():
    database:dict = load_database("database.json")
    while True: 
        user_input: str = input("You : ")

        if user_input.lower() == "quit":
            break
            #when type quit the chatbot stop
        
        best_match: str | None = find_best_ans(user_input, [q["questions"] for q in database ["questions"]])

        if best_match: 
            answer: str = get_ans_for_question(best_match,database)
            print(f'Bot : {answer}')
                
        else: 
            print('Bot : I don\'t know the answer, Teach me ')
            new_answer : str = input(' Type anser or "skip" to skip ')

            if(new_answer.lower() != "skip"):
                database["questions"].append({"questions": user_input, "answer":new_answer})
                save_database("database.json",database)
                print("Bot : Thank you!")

if __name__ == "__main__": 
    chatBot()