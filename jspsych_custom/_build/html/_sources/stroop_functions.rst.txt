.. _stroop_functions:

Stroop with functions
=====================

Example ``experiment.html``. You may have to change this slightly
depending on the location of your copy of jsPsych on the server.

It contains some extra style information to make the background grey,
and make the text of the stimulus bigger and boldface.

.. code:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>My experiment</title>
        <script src="jspsych-6.0/jspsych.js"></script>
        <script src="jspsych-6.0/plugins/jspsych-html-keyboard-response.js"></script>
        <script src="jspsych-6.0/plugins/jspsych-instructions.js"></script>
        <link href="jspsych-6.0/css/jspsych.css" rel="stylesheet" type="text/css"></link>
        <script src="experiment.js"></script>
        <style>
          body {
            background-color: #777777;
          }
          .jspsych-display-element {
             font-size: xx-large;
             font-family: sans;
             font-weight: bold
          }
        </style>
    </head>
    <body></body>
    </html>

And ``experiment.js``:

.. code:: javascript

    // the colours are also the words ....
    var colours = ['red', 'green', 'blue', 'yellow'];

    var n_trials = 30;

    // returns a JavaScript object with { text: ...., colour: .... }
    // using a random colour (text is the same as colour)
    function congruent() {
        // pick a colour ....
        // (when we're only picking one, with/without replacement doesn't matter)
        var colour_list = jsPsych.randomization.sampleWithReplacement(colours,1);
        // this returns a list with one item, so we select the first (only) item
        return { text: colour_list[0], colour: colour_list[0], condition: 'congruent' };
    }

    // returns a JavaScript object with { text: ...., colour: .... }
    // using a random colour (text is different to colour)
    function incongruent() {
        // pick two colours without replacement (i.e. they will be different)
        var colour_list = jsPsych.randomization.sampleWithoutReplacement(colours,2);
        // this returns a list with two item, we select these out
        return { text: colour_list[0], colour: colour_list[1], condition: 'incongruent' };
    }

    // these are in HTML, so <br> means "line break"
    var instructions = {
        type: 'instructions',
        pages: [
          "Welcome to the experiment.<br>Press Space to continue.",
          "In this experiment you will be presented with the words blue, red, yellow and green.<br>Press Space to continue.",
          "As soon as you see a new word, press its first letter.<br>For example, press the B key for blue.<br>Press Space to continue.",
          "Try to answer as quickly as you can!<br>Press Space to start the experiment.",
        ],
        key_forward: ' '
    }

    var fixation = {
        type: 'html-keyboard-response',
        stimulus: '+',
        trial_duration: 500,
        response_ends_trial: false
    };

    // blank (ITI stands for "inter trial interval")
    var iti = {
      type: 'html-keyboard-response',
      stimulus: '',
      trial_duration: 250,
      response_ends_trial: false
    }

    var trials = [instructions];
    // repeat this code n_trials times
    for (var i=0; i<n_trials; i++) {
        var values;
        // Math.random returns a random number between 0 and 1. Use this to decide
        // whether the current trial is congruent or incongruent.
        if (Math.random() < 0.5) {
            values = congruent();
        } else {
            values = incongruent();
        }
        var trial = {
            type: 'html-keyboard-response',
            stimulus: '<p style="color: '+values.colour+'">'+values.text+'</p>',
            // 'choices' restricts the available responses for the participant
            choices: ['r','g','b','y'],
            data: values
        };
        trials.push(iti);
        trials.push(fixation);
        trials.push(trial);
    }

    jsPsych.init({
        timeline: trials,
        on_finish: function() {
            jsPsych.data.displayData('csv');
        }
    });
