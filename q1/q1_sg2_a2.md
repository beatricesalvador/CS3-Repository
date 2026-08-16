<h1 = align = "center">Annex C </h1>
<h2 = align = "center">Code Quality Assessment Worksheet </h2>

<table width="100%">
<tr>
  <td align = "left"><b>Section:</b> Pinatubo</td>
  <td align = "right"><b>Score:</b>________________</td>
</tr>
<tr>
  <td align = "left"><b>C# / Name:</b> (#29) Salvador, Beatrice D.</td>
  <td align = "right"><b>Date:</b>_________________</td>
</tr>
</table>


**Instructions:**
The problem: Finding the highest (Maximum) number from a given list of numbers.

<h3 = align = "left">PseudoCode 1</h3>

~~~
Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm
~~~

<h3 = align = "right">PseudoCode 2</h3>

~~~
Algorithm FindMax2(numbers)

  For i from 0 to length (numbers)-1bigger ← true

    For j from 0 to length(numbers)-1

      If numbers[j] > numbers[i] Then

        bigger ← false

      EndIf

    EndFor

    If bigger = true Then

      Return numbers[i]

    EndIf

  EndFor

EndAlgorithm
~~~

**Questions with Checklist**

<b>1. Efficiency </b>  \
Which algorithm is faster when the list of numbers is very large? Why?
__________________________________


**Checklist to guide your answer:**
<table width = "100%">
<tr>
  <td align = "left"><b>PseudoCode 1</b></td>
  <td align = "right"><b>PseudoCode 2</b></td>
</tr>
<tr>
  <td align = "left">- [ ] Does the algorithm use one loop or two nested loops?</td>
  <td align = "right">- [ ] Does the algorithm use one loop or two nested loops?</td>
</tr>
  
<tr>
  <td align = "left">- [ ] Does the algorithm repeat work unnecessarily?</td>
  <td align = "right">- [ ] Does the algorithm repeat work unnecessarily?</td>
</tr>

<tr>
  <td align = "left">- [ ] Which algorithm finishes in fewer steps?</td>
  <td align = "right">- [ ] Which algorithm finishes in fewer steps?</td>
</tr>
</table>

<b>2. Readability </b>  \
Which algorithm is easier to understand at first glance? What makes it clearer?
___________________________________


**Checklist to guide your answer:**
<table width = "100%">
  <tr>
    <td align = "left"><b>PseudoCode 1</b></td>
    <td align = "right"><b>Pseudocode 2</b></td>
  </tr>
  <tr>
    <td align = "left">- [ ] Are variable names meaningful (e.g., max vs. bigger?</td>
    <td align = "right">- [ ] Are variable names meaningful (e.g., max vs. bigger?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Is the logic simple or complicated?</td>
    <td align = "right">- [ ] Is the logic simple or complicated?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Are there fewer lines of code?</td>
    <td align = "right">- [ ] Are there fewer lines of code?</td>
  </tr>
</table>

<b>3. Maintainability </b>  \
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
________________________


**Checklist to guide your answer:**
<table width = "100%">
  <tr>
    <td align = "left"><b>PseudoCode 1</b></td>
    <td align = "right"><b>PseudoCode 2</b></td>
  </tr>

  <tr>
    <td align = "left">- [ ] Is the structure straightforward?</td>
    <td align = "right">- [ ] Is the structure straightforward?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Would adding new steps break the code easily?</td>
    <td align = "right">- [ ] Would adding new steps break the code easily?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Is there less chance of errors when updating?</td>
    <td align = "right">- [ ] Is there less chance of errors when updating?</td>
  </tr>
</table>

<b>4. Testability </b>  \
Which algorithm is easier to tezt with different inputs? Why?
______________________


**Checklist to guide your answer:**
<table width = "100%">
  <tr>
    <td align = "left"><b>PseudoCode 1</b></td>
    <td align = "right"><b>PseudoCode 2</b></td>
  </tr>

  <tr>
    <td align = "left">- [ ] Can you test with small lists easily?</td>
    <td align = "right">- [ ] Can you test with small lists easily?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Does the algorithm have fewer conditions to check?</td>
    <td align = "right">- [ ] Does the algorithm have fewer conditions to check?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Is the output predictable and clear?</td>
    <td align = "right">- [ ] Is the output predictable and clear?</td>
  </tr>
</table>

<b>5. Security </b>  \
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
_____________________________


**Checklist to guide your answer:**
<table width = "100%">
  <tr>
    <td align = "left"><b>PseudoCode 1</b></td>
    <td align = "right"><b>PseudoCode 2</b></td>
  </tr>

  <tr>
    <td align = "left">- [ ] Does the algorithm check if the list is empty?</td>
    <td align = "right">- [ ] Does the algorithm check if the list is empty?</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Does it handle invalid inputs (like letters instead of numbers?)</td>
    <td align = "right">- [ ] Does it handle invalid inputs (like letters instead of numbers?)</td>
  </tr>

  <tr>
    <td align = "left">- [ ] Does it avoid crashing when inputs are unusual?</td>
    <td align = "right">- [ ] Does it avoid crashing when inputs are unusual?</td>
  </tr>
</table>

<b>6. Final Answer </b>  \
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer.
______________________

