"""HW1 Question 1

Tell us about your interest in computing!

This question is intentionally open-ended. To get full points on this question, 
modify the function below to print a sentence or two about your interests,
goals, or anything that brings you to this course.

You may rename the function, add comments, or make any other modifications.
The file must still work as a valid Python file after your modifications.

Getting your setup ready is the hardest part of the semester.
This question is designed to give you points for getting your GitHub and 
Pawtograder setup working, and making a successful submission."""

def computing_interest(interest:str) -> str:
    """Returns a string about why i became interested in computing"""
    return f"The reason I became interested in Computing is {interest} ."

print(computing_interest("In highschool my magnet was CS programming and i liked it"))
