OPTIONS = ['I', 'E', 'N', 'S', 'T', 'F', 'J', 'F']

answers_to_questions = [20]
questions = [" 1. a. expend energy, enjoy groups or b. conserve energy, enjoy one-on-one",
             "2. a. interpret literally or b. look for meaning and possibilities",
             "3. a. logical, thinking, questioning or b. empathetic, feeling, accommodating",
             "4. a. organized, orderly or b. flexible, adaptable",
             "5. a. more outgoing, think out loud or b. more reserved, think to yourself",
             "6. a. practical, realistic, experiential or b. imaginative, innovative, theoretical",
             "7. a. candid, straight forward, frank or b. tactful, kind, encouraging",
             "8. a. plan, schedule or b. unplanned, spontaneous",
             "9. a. seek many tasks, public activities, interaction with others or b. seek private, solitary "
             "activities with quiet to concentrate",
             "10. a. standard, usual, conventional or b. different, novel, unique",
             "11. a. firm, tend to criticize, hold the line or b. gentle, tend to appreciate, conciliate",
             "12. a. regulated, structured or b. easygoing, “live” and “let live”",
             "13. a. external, communicative, express yourself or b. internal, reticent, keep to yourself",
             "14. a. focus on here-and-now or b. look to the future, global perspective, “big picture”",
             "15. a. tough-minded, just or b. tender-hearted, merciful",
             "16. a. preparation, plan ahead or b. go with the flow, adapt as you go",
             "17. a. active, initiate or b. reflective, deliberate",
             "18. a. facts, things, “what is” or b. ideas, dreams, “what could be,” philosophical",
             "19. a. matter of fact, issue-oriented or b. sensitive, people-oriented, compassionate",
             "20. a. control, govern or b. latitude, freedom"]


def choice():
    global answer
    for i in answers_to_questions:
        print(questions)
        answer = input("Enter your answer")
        if answer == "A":
            answers_to_questions.append(answer)
        else:
            answers_to_questions.append(answer)
        if not answer == "A" or answer == "B":
            raise Exception("Invalid input")


def introvert_extrovert():
    for i in range(0, len(questions), 4):
        if answers_to_questions == "A" or "a":
            E += 1


introvert_extrovert()