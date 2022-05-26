.. _repetition:

Repetition code example
=======================

Make sure you either have these images uploaded to the server, or change the filenames to match your own images!

.. code:: javascript

    var dog1_trial = {
        type: 'image-keyboard-response',
        stimulus: 'Dog1.jpg'
    };

    var dog2_trial = {
        type: 'image-keyboard-response',
        stimulus: 'Dog2.jpg'
    };

    var trials = [dog1_trial, dog2_trial];
    var repeated_trials = jsPsych.randomization.repeat(trials,5);

    jsPsych.init({
        timeline: repeated_trials,
        on_finish: function() {
            jsPsych.data.displayData();
        }
    });
