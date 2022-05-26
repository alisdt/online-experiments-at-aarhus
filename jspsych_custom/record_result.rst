PHP code to receive data on the server
======================================

Note that:

* You **must** replace ``UUN`` with your username.
* Throughout all the examples, this file is given the name ``record_result.php``.
* The line ``$outfile = fopen($path, "a");`` opens the file in "append" mode, which means results will always be appended to the file. If you want this code to always write a new file (possibly replacing the old one), change the ``"a"`` to ``"w"``.

.. code:: php

    <?php
    $json = file_get_contents('php://input');
    $obj = json_decode($json, true);
    $server_data = '/home/UUN/server_data';
    $path = $server_data."/".$obj["filename"];
    if (substr(realpath(dirname($path)), 0, strlen($server_data))!=$server_data) {
        error_log("attempt to write to bad path: ".$path);
    } else {
        $outfile = fopen($path, "a");
        fwrite(
            $outfile,
            sprintf($obj["filedata"])
        );
        fclose($outfile);
    }
    ?>