#!/bin/bash

echo -n "pierre" | md5sum | cut -d " " -f 1
