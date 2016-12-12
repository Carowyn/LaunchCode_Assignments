# LaunchCode_Assignments
This project houses the chapter assignments that I did as I progressed through the Python class. There are 14 chapters in the online book that we used.

<i>Chapters 1 and 2 did not have chapter assignments</i>

<b><u>Chapter 3: </u></b> <i> Submitted on 10/25/2016</i>

You have a thermostat that allows you to set the room to any temperature between 40 and 90 degrees.

The thermostat can be adjusted by turning a circular dial. If you turn the dial all the way to the left, you will set the temperature to 40 degrees. If you turn to the right by one click, you will get 41 degrees. As you continue to turn to the right, the temperature goes up, and the temperature gets closer and closer to 90 degrees. But as soon as you complete one full rotation (50 clicks), the temperature cycles back around to 40 and starts over.

Write a program that calculates the temperature based on how much the dial has been turned. You should prompt the user for a number of clicks-to-the-right (from the starting point of 40 degrees). Then you should print the current temperature.


<b><u>Chapter 4: </u><b/> <i> Submitted on 10/30/2016</i>

Assume you have a list of numbers nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
  a. Write a loop that prints each of the numbers on a new line, like this:
     12
     10
     ...etc

  b. Write a second loop that prints each number and its square on a new line, like this:
     The square of 12 is 144
     The square of 10 is 100
     ...etc


<b><u>Chapter 5: </u></b> <i> Submitted on 11/3/2016</i>

Write a function areaOfCircle(r) which returns the area of a circle of radius r

As a refresher, the area of any circle is equal to the radius squared, multiplied by pi (where pi is 3.14159....).
Don’t forget to include the math module, where pi is defined.

<b><u>Chapter 6: </u></b> <i> Submitted on 11/5/2016</i>

A year is a leap year if it is divisible by 4, unless it is a century that is not divisible by 400.

For example:
  - 1956 is a leap year because 1956 is divisible by 4.
  - 1957 is not a leap year, because it is not divisible by 4.
  - 1900 is not a leap year, despite the fact that it is divisible by 4, because 1900 is a century and 1900 is not divisible by 400.
  - 1600 is a leap year, because 1600 is divisible by 4 and 1600 is divisible by 400

Write a function isLeap that takes a year as a parameter and returns True if the year is a leap year, False otherwise.

<b><u>Chapter 7: </u></b> <i> Submitted on 11/10/2016</i>

Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime number and False otherwise.

As a refresher, a number is prime if it is not divisible by any other number (other than itself and 1).

For example:
  - 2 is prime
  - 3 is prime
  - 4 is not prime because is is divisible by 2
  - 5 is prime
  - 6 is not prime because it is divisible by 2 and 3
  - 7 is prime
  - 8 is not prime because it is divisible by 2 and 4
  - 9 is not prime because it is divisible by 3
Also remember that you can use the modulo operator (%) to check whether one number is divisible by another.

For example, here are a bunch of modulo operations on 12:
  - 12 % 2 is 0
  - 12 % 3 is 0
  - 12 % 4 is 0
  - 12 % 5 is 2
  - 12 % 6 is 0
  - 12 % 7 is 5
  - 12 % 8 is 4
  - 12 % 9 is 3
Notice that 2, 3, 4, and 6, all the factors of 12, yield 0. This makes sense because modulo returns the remainder after division, and these numbers divide 12 perfectly, so there is no remainder left over.

Anyway, 12 is definitely not prime since it is divisible by a bunch of numbers: 2, 3, 4, and 6.

<b><u>Chapter 8: </u></b> <i> Submitted on 11/19/2016</i>

Write a function analyze_text that receives a string as input. Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text, something like this:
The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.

You will need to make use of the isalpha function, which can be used like this:
    "a".isalpha() # => evaluates to True
    "3".isalpha() # => evaluates to False
    "&".isalpha() # => False
    " ".isalpha() # => False

    mystr = "Q"
    mystr.isalpha() # => True

<b><u>Chapter 9: </u></b> <i> Submitted on 11/20/2016</i>

Write a function that mirrors its argument. For example, mirror('good') should return a string holding the value gooddoog. (Hint: Make use of the reverse function that you wrote in the previous exercise

<b><u>Chapter 10: </u></b> <i> Submitted on 11/20/2016</i>

Write a function to find the sum of all the even numbers in a list.

Normally we start you off by providing the function definition statement, e.g.:
def launch_rockets(destination, num_passengers):
      # your code here
      
But in this case we will leave that to you! In other words, you will need to write that def line yourself. Make sure you give your function the name sum_evens, so that the tests work. Your function should accept one argument, the list of numbers to be summed.

<b><u>Chapter 11: </u></b> <i> Submitted on 11/27/2016</i>

Write a function that will sum up all the elements in a list up to but not including the first even number.

<b><u>Chapter 12</u></b>

*****<i>THERE WAS NO CHAPTER 12 ASSIGNMENT, THOUGH WE WERE WORKING ON OUR CRYPTO ASSIGNMENT AT THIS TIME</i>*****

<b><u>Chapter 13: </u></b> <i> Submitted on 12/7/2016</i>

The starter code below contains a Point class. Add a method slopeFromOrigin, which returns the slope of the line joining the origin to the point. For example,

>>> Point(4, 10).slopeFromOrigin()
2.5
>>> Point(12, -3).slopeFromOrigin()
-0.25
>>> Point(-6, 0).slopeFromOrigin()
0

The equation for calculating slope between any two points is slope = (Y2 - Y1) / (X2 - X1). Remember that dividing by 0 is not allowed, so there are some inputs that will cause your method to fail. Return None when that happens.

<b><u>Chapter 14: </u></b> <i> Submitted on 12/11/2016</i>

The code below contains a Chatbot class. A Chatbot is an object that can engage in rudimentary conversation with a human. You will be asked to define a subclass that inherits from this Chatbot superclass.

First, run the code below to talk to the chatbot. Then look over the code to make sure you understand it.
****************************************************************************************************************************
class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


sally = Chatbot("Sally")

human_message = input(sally.greeting())

print(sally.response(human_message))

****************************************************************************************************************************

>>>A DIALOG APPEARS THAT SAYS "Hello, my name is Sally"
>>>>>ENTER IN A PHRASE (HUMAN_MESSAGE)
>>>>>>>OUTPUT OF "It is very interesting that you say: HUMAN_MESSAGE"

****************************************************************************************************************************

Your job is to make a subclass called BoredChatbot that inherits from Chatbot, but acts a little differently, in the following way:

A bored chatbot has a short attention span. When the human says something that is longer than 20 characters, it should respond by saying:

“zzz... Oh excuse me, I dozed off reading your essay.”
If, on the other hand, the human says something with a length of 20 characters or less, then the bored chatbot should respond just like a normal chatbot would.

Note that we are requiring you to use inheritence. Your new BoredChatbot class must be a subclass of the Chatbot class, and your subclass should only implement the things that make it distinct. (See the Inheritence chapter for a review of how this works.)
