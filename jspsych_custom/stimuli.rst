More interesting stimuli
========================

So far the experiments we've created have only used simple text and static images.

In this section we'll take a look at other stimulus types.

The exercises in this section give you fewer hints to make things a bit more challenging.
If you need more clues, take a look at the previous pages and past examples.

Multiple images using HTML
--------------------------

Using a HTML stimulus you can show text in different sizes, different colours, different fonts -- you can
do anything with a HTML stimulus that can be done on a web page! For example, you could use a HTML stimulus
to show two images side-by-side:

.. code:: javascript

    var two_images = {
        type: 'html-keyboard-response',
        stimulus: '<img src="Dog1.jpg"> <img src="Dog2.jpg">'
    }

Optional Exercise - multiple images
...................................

Copy the ``factorial`` experiment to make a new experiment. Modify ``experiment.js`` to show two images in the
full-factorial design -- in other words, your list of factors will have two lists of images in it. When you add
these to the node above, it will look something like this:

.. code:: javascript

    var two_images = {
        type: 'html-keyboard-response',
        stimulus: function() {
             return (
                 '<img src="'+jsPsych.timelineVariable("image1", true)+'">'
                 +'<img src="'+jsPsych.timelineVariable("image2", true)+'">'
             );
        }
    }

Some notes on this:

* The parentheses inside the function are just to allow us to break the line
  by adding two strings using ``+``. If we didn't do this it would be a really
  long line (which is absolutely allowed in JavaScript, but really hard to read!)
* When using a single timeline variable with no modification, one can just use
  the ``timelineVariable`` function directly:

.. code:: javascript

  stimulus: timelineVariable('myvariable');

* When using more than one timeline variable, or combining a timeline variable
  with other information, one must wrap it in ``function() { .... }`` and also
  give ``timelineVariable`` an extra argument, ``true``, as in the example above.
* There is another way to do this which doesn't involve timeline variables.
  Instead, create a loop over the result of the factorial function to create
  a list of nodes. This may be easier to understand, and it's good to know this
  approach as some experiment structures will require you to do this.

Solution
........

Here is an :ref:`example solution <multiple_images>` using the first approach
(timeline variables).

Here is an :ref:`example solution <multiple_images_loop>` using the second approach.

Text changes using HTML
-----------------------

Normally, information about text size, colour, font etc. would go into the CSS file. In the web page there would
be something like this:

.. code:: html

    <p class="positivefeedback">Well done!</p>

and in the CSS file, something like this:

.. code:: css

    .positivefeedback {
        color: green;
    }


In experiments it's often more expedient to put this directly into the HTML. You can do this using the ``style``
attribute:

.. code:: html

    <p style="color: green">Well done!</p>

.. important::

    CSS uses the American spelling for "color". If you write "colour" it will be ignored!

Optional Exercise -- Stroop, list approach
..........................................

The `Stroop effect <https://en.wikipedia.org/wiki/Stroop_effect>`_ works as follows. In a *congruent* Stroop trial
the name of a colour is printed in that colour, e.g.

.. raw:: html

   <p style="color: red; font-size: x-large; font-family: sans; font-weight: bold;">red</p>

In an *incongruent* trial, the name of a colour is printed in a different colour:

.. raw:: html

   <p style="color: red; font-size: x-large; font-family: sans; font-weight: bold;">blue</p>

The Stroop effect means that, on average, participants take longer to name the colour of the
text in an incongruent trial than a congruent one.

You could (as above) write another full-factorial experiment to implement a Stroop test.
If you did this with four colours (for example) then a quarter of the trials would be congruent
and three-quarters would be incongruent:

====== ====== ===========
Colour Text   Condition
====== ====== ===========
red    red    congruent
red    green  incongruent
red    blue   incongruent
red    yellow incongruent
green  red    congruent
green  green  incongruent
green  blue   incongruent
green  yellow incongruent
etc.   etc.   etc.
====== ====== ===========

In a real experiment you'd want to statistically compare the congruent and
incongruent conditions -- and for this it would be better to have half of each.

The most straightforward way to do this would be to write a list yourself,
with half congruent and half incongruent trials:

.. code:: javascript

    var stroop_variables = [
        { colour: "blue", text: "blue", condition: "congruent" },
        { colour: "red", text: "blue", condition: "incongruent" },
        ....
    ];

You can use this the same way you use the output from the ``factorial`` function. Define a
fixation node and a Stroop test node, using one of the approaches above, either:

* Use ``jsPsych.timelineVariable`` where you need the ``colour`` and ``text`` values.
* Use a loop to accumulate a list of nodes.

``condition`` can go in to the ``data`` field of the node, so you will see "congruent"
and "incongruent" in the results.

Once you've got this working, see if you can use ``jsPsych.randomization.repeat`` to
show the trials in a random order.

Solution
........

Here is an :ref:`example solution <stroop_timeline_variables>` using timeline variables.

Here is an :ref:`example solution <stroop_loop>` using a loop.

Optional Exercise -- Stroop, automated approach
...............................................

Rather than having a fixed list of trials, you could generate an equal number of
congruent and incongruent trials. First, write a function that generates a random congruent
trial, and one that generates a random incongruent trial [#random]_. Then, write a loop that
adds one congruent and one incongruent trial to the timeline for each time around the loop.
This will ensure that there are equal numbers of congruent and incongruent trials.

Solution
........

Here is an :ref:`example solution <stroop_functions>` using functions.

.. rubric:: Footnotes

.. [#random] You can use ``jsPsych.randomization.sampleWithoutReplacement`` and
   ``jsPsych.randomization.sampleWithReplacement`` to choose colours and words.