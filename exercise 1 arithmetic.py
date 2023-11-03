#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:27:39 2023

@author: LuisFlacke
"""

def arithmetic_arranger(problems, optional_solution=False):
        
    problems_split = []

    num_of_max_num_digits = []
    added_spaces_first_row = []
    added_spaces_second_row = []
    seperators_list = []
    added_spaces_solution_row = []
    space = " "
    separator = "-"
    between_spacer = "    "
    formatted_output = ""

    for i in range(len(problems)): # fill the list with sublists containing the integers and their corresponding operators in one list
        
        if i > 4:
            formatted_output = "Error: Too many problems."
            return formatted_output
        problems[i] = problems[i].replace(" ", "")
        problems_split.append(problems[i].replace("+", "op").replace("-", "op").split("op"))
        
        if len(problems_split[i]) == 1:
            formatted_output = "Error: Operator must be '+' or '-'."
            return formatted_output
        
        problems_split[i] = [problems_split[i][j] for j in range(len(problems_split[i])) ]
        
        #check whether first number is negaitve
        if problems_split[i][0] == "":
            problems_split[i].pop(0)
            problems_split[i][0] = "-" + problems_split[i][0]
                        
        #create operand1 as integer - check for digits only
        try:
            operand1 = int(problems_split[i][0])
        except:
            formatted_output = "Error: Numbers must only contain digits."
            return formatted_output
        
        #create operand2 as integer - check for digits only
        try:
            operand2 = int(problems_split[i][1])
        except:
            formatted_output = "Error: Numbers must only contain digits."
            return formatted_output        
        
        #check for numbers with maximum 4 digits
        if operand1 > 9999 or operand1 < -9999 or operand2 > 9999 or operand2 < -9999:
            formatted_output = "Error: Numbers cannot be more than four digits."
            return formatted_output        
        
        #create the solution of the task
        if "+" in problems[i]:
            problems_split[i].append("+")
            solution = operand1 + operand2
            
        elif "-" in problems[i]:
            problems_split[i].append("-")
            solution = operand1 - operand2
            
        problems_split[i].append(solution)

        # prepare the spacing for the formatted output            
        num1_length = len(str(operand1))
        num2_length = len(str(operand2))
        numS_length = len(str(solution))
        num_of_max_num_digits.append(max(num1_length, num2_length)) # determine the max digits in the task
        
        added_spaces_first_row.append((max(num2_length, num1_length) - num1_length) * space)
        added_spaces_second_row.append((max(num1_length, num2_length) - num2_length) * space)
        added_spaces_solution_row.append((max(num1_length, num2_length) - numS_length) * space)
        seperators_list.append(((num_of_max_num_digits[-1] + 2) * separator))

    # Add the first line to the formatted output
    for i in range(len(problems_split)):
        formatted_output += "  "
        formatted_output += added_spaces_first_row[i]
        formatted_output += str(problems_split[i][0])
        if i < len(problems_split) - 1:
            formatted_output += between_spacer
        else:
            formatted_output += "\n"

    # Add the second line to the formatted output
    for i in range(len(problems_split)):
        formatted_output += problems_split[i][2] + " "
        formatted_output += added_spaces_second_row[i]
        formatted_output += str(problems_split[i][1])
        if i < len(problems_split) - 1:
            formatted_output += between_spacer
        else:
            formatted_output += "\n"

    # Add separators to the formatted output
    for i in range(len(problems_split)):
        formatted_output += seperators_list[i]
        if i < len(problems_split) - 1:
            formatted_output += between_spacer
        elif optional_solution:
            formatted_output += "\n"

    # Add solutions to the formatted output
    if optional_solution:
        for i in range(len(problems_split)):
            solution_spaces = " " * (num_of_max_num_digits[i] + 2 - len(str(problems_split[i][3])))
            formatted_output += solution_spaces + str(problems_split[i][3])
            if i < len(problems_split) - 1:
                formatted_output += between_spacer
            #else:
             #   formatted_output += "\n"
    return formatted_output

print(arithmetic_arranger(["32 + 698", "3801 - 2", "41 - 43", "99 - 99", "342 - 341"], True))

