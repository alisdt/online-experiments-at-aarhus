#!/bin/bash

make html
make latexpdf
cp images.zip _build/html
cd _build/html
scp -r * root@tullo.co.uk:/var/www/html/au/
#rsync -av . root@softdev.ppls.ed.ac.uk:/var/www/deploy/online_experiments
#lftp -f
