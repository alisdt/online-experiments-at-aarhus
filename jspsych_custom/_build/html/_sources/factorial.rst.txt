.. _factorial:

Factorial code example
======================

.. code:: javascript

    var factors = {
        stimulus: ['Dog1.jpg', 'Dog2.jpg', 'Dog3.jpg'],
        stimulus_duration: [400, 800, 1200]
    };

    var factorial_values = jsPsych.randomization.factorial(factors);

    var trial = {
        type: 'image-keyboard-response',
        prompt: '<p>Press a key!</p>',
        stimulus: jsPsych.timelineVariable('stimulus'),
        stimulus_duration: jsPsych.timelineVariable('stimulus_duration')
    };

    var trials_with_variables = {
        timeline: [trial],
        timeline_variables: factorial_values
    };

    jsPsych.init({
        timeline: [trials_with_variables],
        on_finish: function() {
            jsPsych.data.displayData();
        }
    });
