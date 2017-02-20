#!/bin/bash

echo "May I ask you a about your birthdate?"
select option in "Ok" "Never"
do
    case $option in
        #IF THE USER DOES WANT TO PLAY
        Ok)echo "ok";

        echo "What year?";
        read year;

        echo "What month?";
        read month;

        echo "What day?";
        read day;

        echo "So that was >> $day/$month/$year";
        break;;

        #IF THE USER DOES NOT WANT TO PLAY
        Never)echo "Maybe another day...";break;;

    esac
    #IF THE USER DOES NOT PICK OPTIONS 1, 2 OR 3
    echo "Thas was not an option..."
    break
done
