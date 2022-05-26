The structure of a jsPsych experiment
=====================================

As you know, a jsPsych experiment is a series of nodes.
Usually one node corresponds to one presentation to the
participant. So far in our test experiment, we've only
got one node which says hello (or shows an image, if you
changed it to do that). Let's add some more!

Putting the code in its own file
--------------------------------

First, we're going to give our experiment code its own file. We'll
create a new file just for the JavaScript code, and copy the code into
that file.

Open a new file in the same folder as ``experiment.html``. This will be
called ``experiment.js``. Now in ``experiment.html``, put the following
between ``<head>`` and ``</head>``, *after* all the other lines starting
with ``<script>``:

.. code:: html

    <script src="experiment.js"></script>

This tells the web browser to load code from the file ``experiment.js``.

Now cut all the code you wrote in ``experiment.html`` file between
``<script>`` and ``</script>``, and paste it into ``experiment.js``.
You can now delete the empty ``<script></script>`` in ``experiment.html``.

Adding more images
------------------

Let's add another node to your experiment.
You'll add it just the same way, with another bit of code something
like this:

.. code:: javascript

    var image2_trial = {
        type: 'image-keyboard-response',
        stimulus: 'image2.jpg'
    }

Of course for this you need another image to upload to the server!
There's a test set
of images `linked here <images.zip>`_ (cats, dogs and horses), or of
course you can choose another image for yourself.

Make sure that the name after ``stimulus:`` matches the exact name of
the image on the server.

You can then add this image to the timeline with:

.. code:: javascript

    timeline: [hello_trial, image2_trial]

Your code might not look exactly like this -- the two names between the
``[]`` should match the names you used earlier in the code.

Test this by reloading the experiment page in your web browser.
You should see two images displayed, and each time you can press a key
to move on. Remember
you might need to do a "hard reload", here's a reminder:

| Firefox: ⌘-shift-R on Mac, ctrl-shift-R on Windows or Linux
| Chrome: ⌘-shift-R on Mac, ctrl-F5 on Windows or Linux
| Safari: ⌘-option-E
| Internet Explorer or Edge: ctrl-F5

Results
-------

In a future session we'll look at how to store results on the server.
For now, we'll display them on the screen at the end of the experiment.

You can do this by adding another line to the call to ``jsPsych.init``.
Add the code:

.. code:: javascript

    on_finish: function() {
        jsPsych.data.displayData();
    }

So now, the whole of that part of the code should look like this:

.. code:: javascript

    jsPsych.init({
        timeline: [hello_trial, image2_trial],
        on_finish: function() {
            jsPsych.data.displayData();
        }
    });

Again, test this by reloading the page in your browser.

This time, you should see the two images, then at the end the results.

They look something like this:

.. code:: javascript

    [
        {
            "rt": 1239,
            "stimulus": "Dog1.jpg",
            "key_press": 32,
            "trial_type": "image-keyboard-response",
            "trial_index": 0,
            "time_elapsed": 1241,
            "internal_node_id": "0.0-0.0"
        },
        ....

We'll go through this in more detail later on, but you can already see
a couple of familiar features there. Firstly, the information in the node
(the type and stimulus) are there. Secondly, the reaction time (``rt``) is
there. Finally, ``key_press`` tells you what key was pressed.

Key codes
.........

This is not
straightforward as JavaScript gives key codes rather than just showing the
letter on the key. There are plenty of web pages that will tell you which
code corresponds to which key, for example
`this one <https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes>`_.

You can also ask jsPsych to give you the
`code corresponding to a character <http://www.jspsych.org/core_library/jspsych-pluginAPI/#jspsychpluginapiconvertkeycharactertokeycode>`_,
or the `character corresponding to a code <http://www.jspsych.org/core_library/jspsych-pluginAPI/#jspsychpluginapiconvertkeycodetokeycharacter>`_.

It's always wise to test with the layout of keyboard and input language that
your participants will use, so bear this in mind.

Repetition
----------

What if you want to repeat a set of trials several times? jsPsych allows
you to do this without having to type out all the repetitions. After your
node definitions (``var hello_trial = { ....``) add a line:

.. code:: javascript

    var trials = [hello_trial, image2_trial];

Again, if you gave the two nodes different names, use those names instead.

This puts your two nodes into a list, called ``trials``. Now add a line:

.. code:: javascript

    var repeated_trials = jsPsych.randomization.repeat(trials,5);

This repeats the list ``trials`` five times, randomises it, and puts the
result in a new list called ``repeated_trials``.

Finally, we use this new list as our timeline. Change the ``jsPsych.init``
call to this:

.. code:: javascript

    jsPsych.init({
        timeline: repeated_trials,
        on_finish: function() {
            jsPsych.data.displayData();
        }
    });

Now reload and run your experiment again. You should see ten trials in total,
with five of each image.

Once you've finished, your code should look like :ref:`this <repetition>`. (Don't look at
this until you've taken a look at the console errors and tried to fix it, though!)

Factorial design
----------------

jsPsych also has a function which will create a full-factorial design for you. A
full-factorial design is one which
tests all possible combinations of a set of parameters.

Create a new experiment by copying the "hello" folder and its contents. Rename this
new folder ``factorial``.

This means that your new experiment will appear in a different place. Take the link
for the first experiment and replace ``hello`` with ``factorial``.

Let's create a factorial design over a set of images and a set of stimulus durations.

Look at the
`documentation for the image-keyboard-response plugin <http://www.jspsych.org/plugins/jspsych-image-keyboard-response/>`_.
There is a ``stimulus_duration`` parameter which controls the duration of the stimulus.

So, we can make a full-factorial design with:

.. code:: javascript

    var factors = {
        stimulus: ['Dog1.jpg', 'Dog2.jpg', 'Dog3.jpg'],
        stimulus_duration: [400, 800, 1200]
    };

Start off by deleting the contents of ``experiment.js`` in your new folder, and add this code.
Now add:

.. code:: javascript

    var factorial_values = jsPsych.randomization.factorial(factors);
    console.log(JSON.stringify(factorial_values));

This won't show anything in the main window of the browser. Instead,
``console.log`` sends text to the console that we saw earlier.
Open up the console in Developer Tools and reload the page.
You can see that it's generated all possible combinations of stimulus and duration, as we wanted.
These are not fully-formed jsPsych nodes though, as they need some extra information. At the
very least they need a ``type``. Usually there's also a ``prompt`` parameter, giving some
explanatory text telling the participant what they need to do. We can use timeline variables to
use the ``stimulus`` and ``stimulus_duration`` values that we generated.

Timeline variables
------------------

You can think of timeline variables like a table that jsPsych reads from to generate a set of repetitions.
As a table, ``factorial_values`` would look like this:

======== =================
stimulus stimulus_duration
======== =================
Dog2.jpg 400
Dog1.jpg 1200
Dog1.jpg 800
Dog3.jpg 800
etc.     etc.
======== =================

Let's write a node which uses these variables. Instead of giving numbers or text
for ``stimulus`` and ``stimulus_duration``, we'll use jsPsych timeline variables,
which will substitute values from the table.

.. code:: javascript

    var trial = {
        type: 'image-keyboard-response',
        prompt: '<p>Press a key!</p>',
        stimulus: jsPsych.timelineVariable('stimulus'),
        stimulus_duration: jsPsych.timelineVariable('stimulus_duration')
    };

Now we can link the table up to this using the ``timeline_variables`` property:

.. code:: javascript

    var trials_with_variables = {
        timeline: [trial],
        timeline_variables: factorial_values
    };

This bit says to jsPsych, "please use the node ``trial``, and use ``factorial_values``
to supply the values".

Finally, as before, we must use ``jsPsych.init`` to start the experiment:

.. code:: javascript

    jsPsych.init({
        timeline: [trials_with_variables],
        on_finish: function() {
            jsPsych.data.displayData();
        }
    });

Once you've finished the code should look like :ref:`this <factorial>`. As before,
try your best to finish this on your own first, solving any problems by asking for help,
looking at the code, or using Developer Tools.

Exercise: Instructions
----------------------

Add a node to the start of the experiment which shows some instructions.
This should go in the main timeline (in jsPsych.init).

You can use the ``html-keyboard-response`` plugin, which you saw in the "Hello World!"
example right at the start, or you can use the ``instructions`` plugin
(`documented here <https://www.jspsych.org/plugins/jspsych-instructions/>`_). Remember that
when you add a plugin to an experiment, there must be a corresponding ``<script src="...."></script>``
in ``experiment.html``.

Exercise: Fixation cross
------------------------

Add a fixation cross before each trial. This should go in the timeline in ``trials_with_variables``.

So that code will change to look like this:

.. code:: javascript

    var trials_with_variables = {
        timeline: [fixation, trial],
        timeline_variables: factorial_values
    };

You then need to define a new node, ``fixation``, somewhere above that in the code.

Extra exercise: variable fixation duration
------------------------------------------

Add a new variable to the factorial design, giving two different fixation durations.

Change the definition of your fixation node to use this new variable.