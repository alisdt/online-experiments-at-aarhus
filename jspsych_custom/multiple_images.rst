.. _multiple_images:

Multiple images
===============

This code uses ``jspsych-html-keyboard-response``, so make sure it's included in your
``experiment.html``.

.. code:: javascript

    // create a list of all images so we can tell jsPsych to
    // preload them for speed (see jsPsych.init below)
    var cats = ['Cat1.jpg', 'Cat2.jpg', 'Cat3.jpg'];
    var dogs = ['Dog1.jpg', 'Dog2.jpg', 'Dog3.jpg'];
    var all_images = cats.concat(dogs);

    // this example uses fewer durations (just to make the number
    // of trials sensible).
    var factors = {
        image1: cats,
        image2: dogs,
        stimulus_duration: [750, 1500],
        fixation_duration: [250, 500]
    };

    var factorial_values = jsPsych.randomization.factorial(factors);

    var fixation = {
        type: 'html-keyboard-response',
        stimulus: '+',
        trial_duration: jsPsych.timelineVariable('fixation_duration'),
        response_ends_trial: false
    };

    // add all of the relevant variables to the data field so they
    // will appear in the results
    var trial = {
        type: 'html-keyboard-response',
        prompt: '<p>Press a key!</p>',
        stimulus: function () {
            // note: the outer parentheses are only here so we can break the line
            return (
               '<img src="'+jsPsych.timelineVariable("image1", true)+'">'
               +'<img src="'+jsPsych.timelineVariable("image2", true)+'">'
            );
        },
        stimulus_duration: jsPsych.timelineVariable('stimulus_duration'),
        data: {
          fixation_duration: jsPsych.timelineVariable('fixation_duration'),
          stimulus_duration: jsPsych.timelineVariable('stimulus_duration'),
          image1: jsPsych.timelineVariable('image1'),
          image2: jsPsych.timelineVariable('image2')
        }
    };

    var trials_with_variables = {
        timeline: [fixation, trial],
        timeline_variables: factorial_values
    };

    // add a list of all images, these will be loaded right at the start
    // to avoid delays
    jsPsych.init({
        timeline: [trials_with_variables],
        on_finish: function() {
            jsPsych.data.displayData('csv');
        },
        preload_images: all_images
    });
