.. _stroop_timeline_variables:

Stroop with timeline variables
==============================

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

    var stroop_variables = [
        { colour: "blue", text: "blue", condition: "congruent" },
        { colour: "red", text: "red", condition: "congruent" },
        { colour: "yellow", text: "yellow", condition: "congruent" },
        { colour: "green", text: "green", condition: "congruent" },
        { colour: "blue", text: "yellow", condition: "incongruent" },
        { colour: "red", text: "green", condition: "incongruent" },
        { colour: "yellow", text: "blue", condition: "incongruent" },
        { colour: "green", text: "red", condition: "incongruent" }
    ];

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

    var trial = {
        type: 'html-keyboard-response',
        stimulus: function () {
            // note: the outer parentheses are only here so we can break the line
            return (
                 '<p style="color: '+jsPsych.timelineVariable("colour", true)+'">'
                 +jsPsych.timelineVariable("text", true)
                 +'</p>'
            );
        },
        // 'choices' restricts the available responses for the participant
        choices: ['r','g','b','y'],
        data: {
          colour: jsPsych.timelineVariable('colour'),
          text: jsPsych.timelineVariable('text'),
          condition: jsPsych.timelineVariable('condition')
        }
    };

    var trials_with_variables = {
        timeline: [iti, fixation, trial],
        timeline_variables: stroop_variables
    };

    jsPsych.init({
        timeline: [instructions, trials_with_variables],
        on_finish: function() {
            jsPsych.data.displayData('csv');
        }
    });
