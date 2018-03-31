#!/usr/local/bin/bash

echo $(/usr/local/bin/bash --version)

for i in {2000..3000};
do
  echo -e "${i}: \u${i}"
#  printf "\u${i} "
done
