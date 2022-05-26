.. _pptcondition:

Example
=======

This example demonstrates gathering a participant number
from the URL, calculating a condition number, and adding the participant number
and the date to the data filename.

``record_result.php`` as given :ref:`here <record_result>`.

In ``experiment.js``:

.. code:: javascript

    // e.g. with three conditions
    var participant_id = jsPsych.data.getURLVariable('participant');
    var condition_number = participant_id % 3;
    if (condition_number == 0) {
        condition_number = 3;
    }
    jsPsych.data.addProperties({
        participant: participant_id,
        condition: condition_number
    });

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

    function saveData(name, data_in){
        var url = 'record_result.php';
        var data_in = {filename: name, filedata: data_to_send};
        fetch(url, {
            method: 'POST',
            body: JSON.stringify(data_to_send),
            headers: new Headers({
                    'Content-Type': 'application/json'
            })
        });
    }

    jsPsych.init({
        timeline: [trials_with_variables],
        on_finish: function() {
            var experiment_data = jsPsych.data.get();
            saveData(participant_id+"_data.csv", experiment_data.csv());
        }
    });
