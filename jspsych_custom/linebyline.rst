.. _linebyline:

Line-by-line data saving example
================================

.. warning:: Make sure that your HTML file loads two plugins:
   ``jspsych-html-keyboard-response`` and ``jspsych-image-keyboard-response``.

You should have ``record_result.php`` on the server to receive the data. See :doc:`this page <record_result>`.

.. code:: javascript

    var factors = {
        stimulus: ['Dog1.jpg', 'Dog2.jpg', 'Dog3.jpg'],
        stimulus_duration: [400, 800, 1200],
        fixation_duration: [500, 1000, 1500]
    };

    var factorial_values = jsPsych.randomization.factorial(factors);

    // adding a 'data' field gives us extra values which:
    // - are saved automatically if we save the whole dataset at the end
    // - are accessible in saveDataLine if we save line-by-line
    var fixation = {
        type: 'html-keyboard-response',
        stimulus: '+',
        trial_duration: jsPsych.timelineVariable('fixation_duration'),
        response_ends_trial: false,
        data: {
            type: 'fixation'
        }
    };

    // fixation_duration is put into the 'data' field for this node as this
    // is the one we report at the end -- fixation nodes are filtered out
    var trial = {
        type: 'image-keyboard-response',
        prompt: '<p>Press a key!</p>',
        stimulus: jsPsych.timelineVariable('stimulus'),
        stimulus_duration: jsPsych.timelineVariable('stimulus_duration'),
        data: {
            type: 'trial',
            stimulus_duration: jsPsych.timelineVariable('stimulus_duration'),
            fixation_duration: jsPsych.timelineVariable('fixation_duration')
        }
    };

    var trials_with_variables = {
        timeline: [fixation, trial],
        timeline_variables: factorial_values
    };

    function saveData(name, data_in){
        // this is exactly the same as in the previous example
        // (all it does is send data to the server!)
        var url = 'record_result.php';
        var data_to_send = {filename: name, filedata: data_in};
        fetch(url, {
            method: 'POST',
            body: JSON.stringify(data_to_send),
            headers: new Headers({
                    'Content-Type': 'application/json'
            })
        });
    }

    function saveDataLine(data) {
        // if this isn't a trial node, return from the function (i.e. no action)
        if (data.type != 'trial') {
            return;
        }
        // choose the data we want to save
        var data_to_save = [
            data.type, data.stimulus, data.stimulus_duration, data.fixation_duration, data.rt
        ];
        // join these with commas and add a newline
        var line = data_to_save.join(',')+"\n";
        saveData("test.csv", line);
    }

    jsPsych.init({
        timeline: [trials_with_variables],
        on_data_update: saveDataLine
    });
