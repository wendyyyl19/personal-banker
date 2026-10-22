**personal-banker**


Hi. This is my personal banker project Github.

The purpose of this project is to help me record my money expense. As an international student, I struggle a lot in recording my money. Here are my few reasons:
1. In a new environment, it is hard to pay focus to my money expense without a proper system
2. There is exchange rate between the money I used here and RMB, which is the currency I used at home. I need to calculate this often, which I don't remember. 
3. I used to track my money in a paper but I always lost it.

This Github repository has my coding journey here, so that, I can use this personal banker to track my money, summarize in categories easily and calculate into RMB with ease.

# Files

- personalbankerfinal_v4.py is the final version of the python file.
- draft/ has the older versions showing my progress. 
- progress-images/ has screenshots and the progress graph that I shared in the class with tutors.
- REFERENCES.md has all the references I used and checked for this project.
- requirements.txt lists the library to install.
- GENAIDecalration.md is my GenAI declaration.

# How to run this program

First you need to open your terminal, find directory of this folder. Then, you will need to install openpyxl, then run the file:

Run:
python3 -m pip install -r requirements.txt

Then run:
python3 personalbankerfinal_v4.py


Then you will see a menu. Choose a number from the menu. For the amount and date, you need to follow the instruction in the terminal. 

It saves the records in `expenses.xlsx` in the same folder. When you run it again, it should load that file.

Also in the end we will have the RMB amount, which uses 1 AUD = 5 RMB. It is not a real and live calculation. In the future I may be able to learn how to add live currency rate to the program but not now. Also, I used While loop to avoid invalid input for the menu.  
