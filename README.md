In the project we  used vaderSentiment python library functions to rate a sentence and compare it with rating in uploaded file the invalid ratings are displayed.
The django site is made to accept a file submission frome home page
which in return displays the invalid ratings after processing through backend logic.

Logic involves

1.Reading the file from user.

2.Extracting reviews and corresponding ratings.

3.Identifying the rating using vandersentiment library functions.

4.Comparing output rating with original and adding it to invalid rating category(incas rating is differred).

the live link is http://sriramanush.pythonanywhere.com/ 


