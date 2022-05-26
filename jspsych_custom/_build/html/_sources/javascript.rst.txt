An introduction to JavaScript
=============================

As mentioned briefly in the first session, JavaScript is a programming language that can be used
to tell the web browser to react to user input, and change the contents of a web page dynamically
after it has loaded.

jsPsych is written in JavaScript, and builds on it to make common functions easier (like showing
an image, waiting for a keypress, and so on).

Open a new file, and add this text:

.. code:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title>Test1</title>
        </head>
        <body></body>
        <script>

        // code goes here!

        </script>
    </html>

This looks similar to our first experiments with jsPsych. Now you can add more code where the

.. code:: html

    // code goes here!

comment is.

Add the line

.. code:: javascript

    window.alert("hello");

and reload the page. You'll see a message box with ``hello`` (or whatever message you typed).

.. topic:: About this worksheet

    This is a very quick tour of some basic JavaScript. Teaching it all in depth would be
    a whole course to itself! The purpose of this worksheet is to give you an
    understanding of JavaScript to be better able to read jsPsych examples and
    documentation.

    You can work with these examples in a few ways. You could keep them all in the same
    file, though might get confusing (especially when you run them!)

    Alternatively, you can delete the code between the ``<script></script>`` tag each time
    and start again.

    Finally, if you want to keep all the examples, start a new file for every example.

Variables
---------

Try this instead -- change the code and reload the page in your web browser:

.. code:: javascript

    var greeting = "good morning";
    window.alert(greeting);

The variable ``greeting`` stores the value that we want to show. This variable is given to
``window.alert()`` which then shows that value. In JavaScript (and most programming languages)
a variable can be used to store information for later.

Maths
-----

Try this, as before, change the code and reload:

.. code:: javascript

   var result = 123*456;
   window.alert(result);

JavaScript makes a good calculator! It uses ``*`` to multiply numbers. Similarly you can use
``+``, ``-`` and ``/`` for add, subtract and divide.

You can also add text:

.. code:: javascript

    var result = "I wandered lonely "+"as a cloud";
    window.alert(result);

What do you think will happen if you run this code?

.. code:: javascript

   var result = 123+"hi";
   window.alert(result);

Try it and see if you were right.

Conditions
----------

Try this:

.. code:: javascript

   var the_number = 15;

   if (the_number > 10) {
       window.alert("the number is greater than 10");
   }

Now change the ``15`` in the first line to ``5``. If you reload
the page you'll see that no alert appears. Change it back to something
higher than ``10``. Reload again, and this time the message appears.

When you use ``if``, it looks like this:

.. code:: javascript

   if (condition) {
       commands;
   }

(this is just an illustration, no need to type it in!)

This is made up of

#. the word ``if``,
#. in round brackets ``( )`` [#round]_, a condition i.e. something that can be examined to see if it's true or false, and
#. in curly brackets ``{ }`` [#curly]_, a block of code, which is a series of JavaScript commands with ``;`` at the end of each command.

.. topic:: Conditions

    As you saw in the example, ``if`` decides whether
    to run some code or not depending on a condition.

    It's important to note that when comparing two values to see if they are equal,
    you must use two equals signs ``==``. A single equals sign ``=`` sets a variable.

    For example, this code:

    .. code:: javascript

        if (x == 3) {

    is testing if the value of the variable ``x`` is ``3``. This code:

    .. code:: javascript

        var x = 3;

    is creating a new variable ``x``, and using it to store the value ``3``.

You can also provide
alternative code to run if the condition is not true. Change your code
to look like this:

.. code:: javascript

   var the_number = 15;

   if (the_number > 10) {
       window.alert("the number is greater than 10");
   } else {
       window.alert("the number is less than or equal to 10");
   }

Now change the number a few times. Each time, hit reload and see what
happens. You'll see that now, you *always* get a message. If you use
``if`` with ``else``, exactly one of the two blocks of code will run.

.. topic:: Code blocks vs. objects

    The curly brackets are often used to enclose
    blocks of code, when using ``if`` and in other contexts.
    But they are also used to write nodes in jsPsych:

    .. code:: javascript

        var my_node = {
            type: "image-keyboard-response",
            stimulus: "fluffydog.jpg"
        };

    This is a completely different use of curly brackets! The easiest
    way to tell the difference is that the items in a code block will
    end with a ``;`` (semicolon).

    In a *JavaScript object* like a node, they will end with a ``,`` (comma).

Loops
-----

Try this:

.. code:: javascript

    for (var i=1; i<6; i++) {
        window.alert("The number is "+i);
    }

You'll see five alerts, with the numbers from 1 to 5. The code above is a loop, it runs the
code in the code block several times.

Taking a closer look at the code:

* ``for`` tells the program to expect a loop
* ``( )`` then there are round brackets, with some instructions on how to run the loop

  * ``var i=1`` runs once at the start of the loop -- create ``i`` and make it equal to 1
  * ``i < 6`` means "keep running the loop while ``i`` is less than 6"
  * ``i++`` runs after the code every time round the loop. It means "add 1 to ``i``".
    (Similarly, ``i--`` means "subtract 1 from ``i``")

* ``{ }`` then there are curly brackets with a code block

Exercise
........

Can you change the loop so that it counts down from 5 to 1?

Arrays
------

An array in JavaScript is a list of items.

For example, try:

.. code:: javascript

    var vegetables = ["Carrot", "Cabbage", "Parsnip", "Potato"];
    window.alert(vegetables[2]);

What happened here? ``vegetables[2]`` selects an item from the array. It's not
the second one though. This is because JavaScript (like many programming languages)
starts counting from zero! Try changing the code to read ``vegetables[0]`` reload --
does this do what you expect?

.. _for-of:

Looping through an array
........................

What if we want to use a loop to go through these items, running some code for each item?

One way is this:

.. code:: javascript

    var vegetables = ["Carrot", "Cabbage", "Parsnip", "Potato"];
    for (var veg of vegetables) {
        window.alert("I'm eating a "+veg);
    }

This is a different kind of ``for`` loop, where we run the code for each item in a list.
Unfortunately some older browsers (notably Internet Explorer) don't support this.
A more universal method, which will work on older browsers is this:

.. code:: javascript

    var vegetables = ["Carrot", "Cabbage", "Parsnip", "Potato"];
    for (var i=0; i<vegetables.length; i++) {
        window.alert("I'm eating a "+vegetables[i]);
    }

This is using a numerical loop, like the first one you saw above, to go through
the list.

Using a loop in jsPsych
-----------------------

Copy one of your existing experiments -- we'll use this as a template for a new one.
Take a look in ``experiment.html`` and make sure it loads the ``jspsych-html-keyboard-response``
plugin.

Here's a quick example of how you might use a loop in a jsPsych program. Copy the code below
into ``experiment.js``:

.. code:: javascript

    var nodes = []
    for (var i=1; i<11; i++) {
        var node = {
            type: 'html-keyboard-response',
            stimulus: i,
            trial_duration: 500,
            response_ends_trial: false
        }
        nodes.push(node);
    }
    jsPsych.init({
        timeline: nodes
    });

Note that the ``push()`` method inside the loop is used to add something on to the end of
a list -- this is quite a common way of building up a timeline in jsPsych.

Exercise
........

Instead of the code above which displays a number, create an experiment which loops through
an array of strings, showing each one in turn. So if you start with:

.. code:: javascript

    var sentence = ["I", "wandered", "lonely", "as", "a", "cloud"];

the experiment should show each of these words in order. (Hint: see the use of ``for`` .... ``of``
:ref:`above <for-of>`).


Functions
---------

One of the most fundamental building blocks in JavaScript is the function. A function is a
block of code that is stored to be used later. Once you have stored some code, you can run
it as many times as you like.

Try this:

.. code:: javascript

    function greeting() {
        window.alert("hello!");
    }

This code *defines* a function, in other words, it stores the code for
later use, but doesn't run it. Now after that, add:

.. code:: javascript

    greeting();

This *calls* the function. That means it runs the code that was stored earlier.

Think of a function like a recipe for a cake. Defining the function
is like writing the recipe. Calling the function is like baking the
cake!

You can write a recipe once, and then follow it many times. In the same way,
in JavaScript you define a function once, but call it many times.

Add a few more calls to your function:

.. code:: javascript

    greeting();
    greeting();
    greeting();

The action in the function is repeated as many times as the function is called.

Now change your function to look like this:

.. code:: javascript

    function greeting(person) {
        window.alert("hello "+person+"!");
    }

Now the function takes a *parameter*, a piece of information that you pass to it.

Change the calls to the function to give it this information:

.. code:: javascript

    greeting('Hendrick');
    greeting('Arran');
    greeting('Priyangi');

A function that takes multiple parameters separates them with commas:

.. code:: javascript

    function example_function(a,b,c) {

Exercise
........

Given a list of names:

.. code:: javascript

    var names = ['Hendrick', 'Arran', 'Kalvyn', 'Priyangi', 'Ted'];

how would you call the ``greeting()`` function for each item in the list?

Return value
............

Functions can also return a value. Try this:

.. code:: javascript

    function square(x) {
        return x*x;
    }

    window.alert(square(3));
    window.alert(square(5));

Here the word *return* means "give this value back to where the function is called".

.. _functions:

Use of functions in jsPsych
---------------------------

Let's look at an example we've already seen.

.. code:: javascript

    jsPsych.init({
        timeline: [trials_with_variables],
        on_finish: function() {
            jsPsych.data.displayData('csv');
        }
    });

Here the ``on_finish`` field specifies an action to occur when the experiment ends.

Why does this say:

.. code:: javascript

        on_finish: function() {
            jsPsych.data.displayData('csv');
        }

and not just this:

.. code:: javascript

        on_finish: jsPsych.data.displayData('csv');

The answer is that putting the call inside a function delays its action.
If the code was written the second way, it would run before ``jsPsych.init`` ran.
Written the first way, in runs when ``on_finish`` is *used*, at the end of the
experiment.

If this seems confusing, don't worry -- just remember that the form above (using
``function() { .... }``) is used to delay the action of some code.

.. topic:: Different ways of defining functions

    The examples in this section are just for illustration, so
    don't type them in!

    A function in JavaScript can be defined like this:

    .. code:: javascript

        function myfunc(x,y) {
            return "The input was "+x+" and "+2*y;
        }

    and called like this:

    .. code:: javascript

        var result = myfunc(4,10);

    or this:

    .. code:: javascript

        console.log(myfunc(4,10));

    In this case the function has a name. If we want to
    define a function and immediately use it, we can define it
    like this:

    .. code:: javascript

        function(x, y) { return "The input was "+x+" and "+2*y; }

    Newer versions of JavaScript have another way to define functions:

    .. code::

        (x, y) => "The input was "+x+" and "+2*y;

    This new way isn't used as widely, as it's not supported on some older browsers and browser versions.

.. rubric:: Footnotes

.. [#round] .... also called "parentheses".
.. [#curly] .... also called "braces".