Database saving example
=======================

.. code:: bash

  sudo apt install php-pgsql

  sudo su - postgres
  psql

on the psql prompt:

.. code:: sql

  create database test1;
  \c test1
  create table mydata (
   id serial primary key,
   participant integer not null,
   keypress char(1),
   rt_ms integer
  );

and then exit from psql and the postgres account (ctrl-D for both)

Add the following code to a PHP file, in my example it's in ``/var/www/html/test_pg.php``

.. code:: php

  <?php
  // take in the uploaded data
  $json = file_get_contents('php://input');
  // treat it as json
  $obj = json_decode($json, true);

  // this will be e.g.
  // { participant: 12, response_key: 'c', rt: 210 }
  // as sent from

  // ADD THE RIGHT DB PASSWORD AND NAME
  $connection = pg_connect("user=postgres password=XXXXXXX host=localhost dbname=test1") or die("Couldn't connect to database");

  // ADD THE RIGHT TABLE NAME (instead of mydata)
  $stmt = pg_prepare(
          $connection,
          "add_data",
          "insert into mydata (participant, keypress, rt_ms) values ($1, $2, $3)"
  );

  $result = pg_execute(
          $connection,
          "add_data",
          array($obj["participant"], $obj["response_key"], $obj["rt"])
  ) or die("INSERT failed");

  ?>

In ``/var/www/html/stroop``, add the following to ``stroop.html``:

.. code:: html

  <!DOCTYPE html>
  <html>
      <head>
          <meta charset="UTF-8">
          <title>Stroop task</title>
          <script src="../jspsych-6.1.0/jspsych.js"></script>
          <script src="../jspsych-6.1.0/plugins/jspsych-html-keyboard-response.js"></script>
          <script src="stroop.js"></script>
          <link href="../jspsych-6.1.0/css/jspsych.css" rel="stylesheet" type="text/css"></link>
      </head>
      <body>
      </body>
  </html>

  and this to ``stroop.js``:

.. code:: javascript

  var words = ['blå', 'gul', 'grøn', 'rød'];
  var colours = ["blue", "yellow", "green", "red"];


  var factors = { word: words, colour: colours };

  var factorial_table = jsPsych.randomization.factorial(factors);

  var trial = {
      type: 'html-keyboard-response',
      stimulus: function () {
          // e.g. <span style="color: blue">red</span>
          return (
              '<span style="font-size: xx-large; color:'+jsPsych.timelineVariable("colour", true)+'">'+
              jsPsych.timelineVariable("word", true)+'</span>'
          );
      }
  };

  var timeline_variable_node = {
      timeline: [trial],
      timeline_variables: factorial_table
  }

  function saveTrialData(data){
      // instead of sending text CSV, send the record as JSON
      // e.g. {
      // participant: 1,
      // keypress: 'v',
      // etc.
      // }
      var url = '../test_pg.php'; // THIS MUST MATCH THE DB SAVING SCRIPT
      var data_to_send = data;
      // translate keypress
      data_to_send['response_key'] = jsPsych.pluginAPI.convertKeyCodeToKeyCharacter(data['key_press']);
      // fixed value for now! add the real participant number later elsewhere
      // in the code, and delete this line
      data_to_send['participant'] = 12;
      fetch(url, {
          method: 'POST',
          body: JSON.stringify(data_to_send),
          headers: new Headers({
                  'Content-Type': 'application/json'
          })
      });
  }

  jsPsych.init({
      timeline: [timeline_variable_node],
      on_data_update: function(data) {
          saveTrialData(data);
      }
  });
