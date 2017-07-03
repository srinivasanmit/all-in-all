continue_search="y"
 while [ $continue_search = 'y' ]
     do echo
     echo "Enter file to search on : "
     read filename
     echo "Enter word to search for: "
     read word
     word_count=`grep $word $filename | wc -w`
     if [ $word_count -gt 0 ]
     then echo "Word found on file $word_count times"
     else
         echo "Word could not be found"
     fi
     echo "Do you want to continue searching? (y/n)"
     read continue_search
 done

