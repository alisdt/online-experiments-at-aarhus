.. _data:

Getting data from your experiment
=================================

Of course, for your experiment to be useful you'll need to record the results!
Here we'll take a look at different ways of getting results out of a jsPsych
experiment.

Testing
-------

As we've seen before, if you're just testing your experiment you can show the
results after the experiment with something like this:

.. code:: javascript

    jsPsych.init({
      timeline: timeline,
      on_finish: function() {
        jsPsych.data.displayData('csv');
      }
    });

Sending the data to the server
------------------------------

``record_result.php`` is a small program that runs on the server when a particular page is accessed.
This receives the data and saves it to disk.

.. topic:: ``server_data`` and security

    You'll have noticed that on the server there's a folder called ``server_data``. This is where
    the results will be stored.

    For security reasons, it would be bad for your experiment to be
    able to add files to the ``public_html`` area. Anything there could then be seen by the outside
    world, and could then be used to spread viruses or for other malicious purposes.
    It may seem far-fetched, but institutions like universities are often targeted for this purpose
    as people are more likely to trust a link on a university website.

This small program is in a different programming language called PHP. I won't go into the details
of this -- if you're interested, PHP has a lot in common with Javascript.

As I said before, this code will receive the data. Now we need to write some code to *send* the data. Remember
that the experiment is running entirely in the participant's web browser. We'll write some code that sends all
of the data from the experiment to the server. This will happen right at the end of the experiment.

In the your experiment's JavaScript file, add a new function:

.. code:: javascript

    function saveData(name, data_in){
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

.. topic:: fetch

    This uses a relatively new function called ``fetch``. While this is the best way to send data, it's not
    supported by all web browsers. Notably, it doesn't work on Internet Explorer. If you need the experiment
    to be available on IE, you can either use a different method to send the data (see
    `the jsPsych documentation <http://www.jspsych.org/overview/data/#storing-data-permanently-as-a-file>`_ )
    or use the `fetch polyfill <https://github.com/github/fetch>`_ [#polyfills]_ .

Now finally, we need to change the experiment to send the data. Change the function
given in ``on_finish`` to call ``saveData``. Remember that the first thing you
give it should be the filename for the data file, and the second thing should
be the data as CSV (see hints below).

This should replace any previous ``on_finish`` that was in the call.


Hint
....

* You can get the data from your experiment as CSV with jsPsych.data.get().csv()

How it works
------------

The protocol used for the web, HTTP, has two different ways of getting web pages. [#http]_ These are called GET and POST.

To use GET, a web browser sends a request with a URL [#url]_ and gets back a page. Any extra information
in a GET must be included in the URL. It will look something like this:

.. code::

    http://example.com/page?colour=red&size=3

Here after the location of the page, there are two values -- "colour" is "red" and "size" is "3".

Instead of sending data this way, for larger amounts of data, a POST is used. This might
be used to send data from a web form, for example. The data are not sent in the URL -- instead, the browser sends them
attached to the request, in a way that isn't visible to the user.

The data that we send is:

.. code:: json

    { filename: "test.csv", filedata: "\"rt\",\"stimulus\",\"key_press\",\"trial_type\",\"trial_index\", .... " }

where ``filedata`` contains the whole contents of the CSV file. The PHP program at the other end receives this data
in the POST.
It opens a file corresponding to the given filename, and saves the data in it.

Adding new data fields
----------------------

You will almost certainly want to store more data than jsPsych gives you by default.

Some data will remain the same for the whole test for each participant, such as
participant number or demographics. Other data will change for each trial. Let's look at both of these.

.. _addproperties:

Data that doesn't change
........................

You can add this using ``jspsych.data.addProperties()``. For example, let's add the date and time of the start of
the experiment.

Before your ``jsPsych.init``, add the code:

.. code:: javascript

    jsPsych.data.addProperties({ start_time: (new Date()).toISOString() });

This adds a new column with the time at the start of the experiment. (Of course, you have to be cautious with this
information, as it will give the time on the participant's computer!)

Data that does change
.....................

You can add extra information that varies for each trial. If you haven't already, add a fixation node to your
current copy of the ``factorial`` experiment. (You can see how this is done
:ref:`here <factorial_with_fixation>` ). The fixation uses the ``jspsych-html-keyboard-response`` plugin so
remember to add this to your ``experiment.html`` file.

Now run the experiment again. You'll see that the fixation node also generates a line in the output.

.. code::

    "rt","stimulus","key_press","trial_type","trial_index","time_elapsed","internal_node_id"
    "null","+","null","html-keyboard-response","0","753","0.0-0.0-0.0"
    "1010","Dog1.jpg","32","image-keyboard-response","1","1777","0.0-0.0-1.0"
    "null","+","null","html-keyboard-response","2","2283","0.0-0.0-0.1"

We might want to filter these (or other nodes) out. To add this to the nodes, we use the ``data`` field.

In the ``fixation`` node, add:

.. code::

    data: { type: 'fixation' }

Remember that you'll need to add a comma to the line before, so something like:

.. code::

    var fixation = {
        ....
        response_ends_trial: false,
        data: { type: 'fixation' }
    };

Now do the same for the ``trial`` node, but add:

.. code::

    data: { type: 'trial' }

Run your experiment again. There should be a new column, with "trial" or "fixation". This will make it easier
to filter out fixations.

.. topic:: Filters

    If you want to try this out using jsPsych's built in filters, make sure you have data saving implemented
    as in the previous section.

    Replace ``jsPsych.data.get()`` with

    .. code:: javascript

        jsPsych.data.get().filter({ type: 'trial' });

    That should return just the data from the nodes with "type" equal to "trial".

    While this is good for testing, it's always safer to save *all* the raw data, and filter it in analysis.

    If you get filtering wrong in analysis, you can run it again. If you get filtering wrong when saving the
    data, anything which was filtered out is gone forever!

We can also add new fields which change every time. In the ``trial`` node, change ``data`` part to read:

.. code:: javascript

    data: {
        type: "trial",
        stimulus_duration: jsPsych.timelineVariable('stimulus_duration'),
        fixation_duration: jsPsych.timelineVariable('fixation_duration')
    }

This will tell jsPsych to copy these values into the data. Reload the experiment and you should see two
new columns for these values.

Extra Exercise
--------------

In online experiments it's quite common to have the participant type in an ID number,
for example their Prolific ID or Amazon MTurk number, that will allow you to
verify their participation and pay them.

Add a node at the beginning of your code which allows the user to input an ID, using
`the survey-text plugin <http://www.jspsych.org/plugins/jspsych-survey-text/>`_ . (Remember you'll also have to add a ``<script>`` tag
to your ``experiment.html`` file to load the plugin). Add this node to your experiment
at the beginning. This works a little differently to the plugins we've seen before,
so be sure to read the documentation before you start.

Before you go any further, run the experiment and check that this new node only appears
once at the beginning of the experiment. Check the console to make sure there are no
errors.

In your new node, add a new item ``on_finish``. This specifies a function to call
when the trial is finished. Create an *anonymous function* (see
:ref:`this section <functions>`), and inside it use ``jsPsych.data.addProperties``
(see :ref:`this section <addproperties>`) to add a new column to the data which includes
the ID. The function you pass to ``on_finish`` receives the data from the trial as an
argument -- take a look at the documentation
`here <http://www.jspsych.org/overview/callbacks/#on_finish-trial>`_ .

**Hint:** to get the response out of the ``survey-text`` trial, use

.. code:: javascript

    JSON.parse(data.responses).Q0

(If you gave your question a name, you'll need to use this instead of "Q0").

This is quite involved so don't be too worried if you don't get it straight away --
take some time to look in the documentation, use the Developer Tools, and feel free
to ask questions!

Answers
-------

* :ref:`Example experiment <datasaving>` which demonstrates saving data at the end
  of the experiment.
* :ref:`Example experiment <linebyline>` which demonstrates saving data line-by-line.
* :ref:`Solution to exercise <surveytext>` which takes the result of a ``survey-text``
  node and adds it as a new column.

.. rubric:: Footnotes

.. [#missing] The ``stimulus_duration`` field is missing -- we'll see how to add this to the output later on.

.. [#polyfills] In JavaScript programming, a *polyfill* is a piece of code which implements a particular function,
    usually for browsers that don't have that function.

.. [#http] .... and a few other methods for things like changing and deleting pages, but these are seldom used.

.. [#url] In case you've ever wondered, **U** niform **R** esource **L** ocator.
