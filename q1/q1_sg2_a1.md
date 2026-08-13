<b>Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: 9-Pinatubo                         

Score:____________

C# / Name: (29) Salvador, Beatrice D.       

Date: _____________
</b>

Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

**Step 1: Identify the Big Problem**

Main Problem: The PSHS school canteen gets overcrowded and slows down the process of buying food.

**Step 2: Identify three to four Sub-Problems**
Please list possible sub-problems:

1. There is a larger ratio of students than the concessionaire staff.

2. Cashier has to manually calculate the prices and change.

3. Students take too long to decide what to order.

4. Food items are not tracked for how much is left.

**Step 3: Define Computational Thinking Approaches**
For each sub-problem, apply CT skills:

Sub-Problem

1. Larger ratio of students than concessionaire staff
2. Delay of manual input of prices
3. Indecisiveness of students leading to accumulation of line
4. No tracker for food items

CT Skill

1. Algorithm Design, Data Collection, Data Analysis
2. Automation
3. Automation, Algorithm Design
4. Automation

Example Solution

1. Insert 10-15 minute windows in between grade levels' lunch period dismissals
   so that the canteen line will be regulated.
2. Use Point of Sale Systems (POS) installed in devices to act as a register.
3. Send out weekly/biweekly meal plan through Gmail so that students could determine
   their lunch prior to even entering the canteen. With this could also come pre-paid
   lunches, which could be picked up at a separate area.
5. Point of Sale Systems (POS) could help keep track of the stock and supply of the food.

**Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem**

Identified Sub-Problem: Larger Ratio of Students than Concessionaire Staff

START

WHILE TRUE

   DISPLAY "Enter Grade Level: "
   
   INPUT grade_level

   IF 7 <= grade_level <= 9 THEN
   
      DISPLAY "Your lunch break will be from 11:20 AM to 12:05 PM."
      
      BREAK
      
   ELIF 10 <= grade_level <= 12 THEN
   
      DISPLAY "Your lunch break will be from 12:10 PM to 1:00 PM."
      
      BREAK
      
   ELSE
   
      DISPLAY "Invalid input."
      
   ENDIF
   
ENDWHILE

STOP

   
