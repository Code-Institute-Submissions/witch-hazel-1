intro_text = "\n##########################################################################\
    \n\n                            W I T C H - H A Z E L\
    \n\
    \n  Welcome to witch-hazel, your simple app for planning and recording\
    \n  your production of grafted Hamamelis plants!\
    \n\
    \n  For a summary list of the functions of witch-hazel, press Enter.\
    \n\
    \n  For an explanation of how the program works, type 'HELP' on the\
    \n  command line.\
    \n\
    \n  For detailed help on each of the program's options, type 'HELP'\
    \n  followed by a space, followed by the number of the option you need\
    \n  more information on.\
    \n\
    \n  Type 'EXIT' on the command line to close the witch-hazel app.\
    \n\
    \n_____________________________________________________________________________"


help_text1 = "\n                               WITCH-HAZEL HELP\
    \n\n  To run witch-hazel, run the script file that contains its code.\
    \n  From within the Heroku App environment, simply on the red 'RUN PROGRAM' button.\
    \n  On opening, the app will show you a list of the options available to\
    \n  you and ask which of them you would like to perform:\
    \n\n    1. Plan grafts for this year\
    \n    2. Record grafts taken\
    \n    3. Record rooted cuttings potted up\
    \n    4. Plan this year's cutting campaign\
    \n    5. Record cuttings taken\
    \n    6. Record plant losses\
    \n    7. Record plant gains\
    \n    8. Hold grafted plants over for one year\
    \n    9. Bring grafted plants forward one year\
    \n\n    0. Close out current year\
    \n"

help_text2 = "  Type in the number of the operation you wish to perform,\
    \n  the app will guide the process.\
    \n\n  Look at the README.md file for further details on each operation.\
    \n\n  The App will tell you the range of numbers you can choose from (0 to 12).\
    \n  Any time you enter an invalid number (including a negative number), the app\
    \n  will give you another opportunity to enter a valid one.\
    \n\n  During some operations the App may ask you a yes or no confirmation\
    \nquestion. Where this happens you should answer yes by typing a 'y' or 'Y'\
    \non the command line. Typing in any other symbol will be taken as a 'No',\
    \nand will result in the app returning to the main menu.\
    \n\nTo get detailed Help on any specific function, type 'HELP' followed\
    \nby a space and then the number of the function on which\
    \n you want detailed help. You can do this from anywhere in the App.\
    \n"


menu_title = "\n                            W I T C H - H A Z E L"

menu_text = "\n  What would you like to do?\
    \n  Choose from among the following operations:\
    \n\
    \n    1. Plan grafts for this year\
    \n    2. Record grafts taken\
    \n    3. Record rooted cuttings potted up\
    \n    4. Plan this year's cutting campaign\
    \n    5. Record cuttings taken\
    \n    6. Record plant losses\
    \n    7. Record plant gains\
    \n    8. Hold back grafted plants for one year\
    \n    9. Bring grafted plants forward one year\
    \n\n    0. Create new year/Close out current year\
    \n"


help_text_option1 = "\n\n                     Option 1 -- PLAN NUMBER OF GRAFTS\
        \n\
        \n  Option 1 lets you record the number of grafts you plan to make for each\
        \n  cultivar of Hamamelis in the current year. Later, when you use Option 2\
        \n  to record the grafts you've actually taken for the chosen cultivar\
        \n  (which you can do as often as you like), the App will let you know when\
        \n  you've made the number of that cultivar you originally planned to make\
        \n  in the current year.\
        \n\n  When you choose Option 1, the App will show you the list of cultivars\
        \n  recorded in your data and ask you choose the number of the cultivar\
        \n  whose grafting program you wish to plan for the year.\
        \n\n  If you run Option 1 a second time for the same cultivar, the App will\
        \n  tell you how many grafts you planned in the previous session and asks\
        \n  you to confirm whether you want to change this number. If you confirm\
        \n  and enter a new number, this new entry will REPLACE the previous\
        \n  number. It will not be summed together with the old number!\
        \n"


help_text_option2 = "\n\n                     Option 2 -- RECORD GRAFTS MADE\
        \n\n  Option 2 lets you record the number of grafts of your chosen cultivar\
        \n  you have taken since you last ran that option for that cultivar (or, if\
        \n  you are running the option for the first time in the current year, the\
        \n  number of grafts you have taken so far of that graft in the current\
        \n  year).\
        \n\n  When you choose Option 2, the App will output the list of cultivars\
        \n  recorded in your data and ask you choose the number of the cultivar for\
        \n  which you want to record new grafts.\
        \n\n  You can run Option 2 as often as you like for any cultivar, though we\
        \n  recommend running it every time you've completed a session of grafting,\
        \n  while the number of grafts you've taken in that session is still fresh\
        \n  in your mind.\
        \n\n  Each time you record a number of grafts made for a particular cultivar,\
        \n  that number is added to the previous total for that cultivar.\
        \n\n  The App will tell you when you've reached (or exceeded) the number of\
        \n  grafts you planned to make for that cultivar (using Option 1).\
        \n"


help_text_option3 = "\n\n                     Option 3 -- RECORD CUTTINGS POTTED UP\
        \n\n  Option 3 lets you record the number of rooted cuttings you have potted\
        \n  up since you last ran that Option (or, if you are running the Option for\
        \n  the first time in the current year, the number of rooted cuttings you\
        \n  have potted up so far in the current year).\
        \n\n  You can run Option 3 as often as you like, though we recommend running\
        \n  it every time you've completed a session of potting up rooted cuttings,\
        \n  while the number you've potted up in that session is still fresh in your\
        \n  mind.\
        \n\n  Each time you record some rooted cuttings being potted up, that number\
        \n  is added to the previous total.\
        \n\n  The App will warn you when you've reached (or exceeded) the number of\
        \n  cuttings you have recorded as being available for potting up (i.e. the\
        \n  number of cuttings made, minus any losses you have recorded since then).\
        \n"


help_text_option4 = "\n\n                     Option 4 -- PLAN NUMBER OF CUTTINGS\
        \n\
        \n  Option 1 lets you record the number of cuttings for future rootstocks\
        \n  that you plan to make for the current year. Later, when you use Option 2\
        \n  to record the cuttings you've actually taken (which you can do as often\
        \n  as you like), the App will let you know when you've reached the number\
        \n  of cuttings you originally planned for the current year.\
        \n\n  If you run Option 1 a second time, the App will tell how many cuttings\
        \n  you planned in the previous session and asks you to confirm whether you\
        \n  want to change this number. If you confirm and enter a new number, this\
        \n  new entry will REPLACE the previous number. It will not be summed\
        \n  together with the old number!\
        \n"


help_text_option5 = "\n\n                     Option 5 -- RECORD CUTTINGS TAKEN\
        \n\n  Option 2 lets you record the number of cuttings you have taken since you\
        \n  last ran that Option (or, if you are running the Option for the first\
        \n  time in the current year, the number of cuttings you have taken so far\
        \n  in the current year).\
        \n\n  You can run Option 2 as often as you like, though we recommend running\
        \n  it every time you've completed a session of cutting taking, while the\
        \n  number of cuttings you've taken in that session is still fresh in your\
        \n  mind.\
        \n\n  Each time you record a number of cuttings made, that number is added to\
        \n  the previous total.\
        \n\n  The App will tell you when you've reached (or exceeded) the number of\
        \n  cuttings you planned to make (using Option 1).\
        \n"


help_text_option6 = "\n\n                     Option 6 -- RECORD GRAFTS LOST\
        \n\n  Option 6 lets you record any losses of grafted plants you may suffer.\
        \n  It first asks you to identify the cultivar that has suffered losses and\
        \n  the age of that cultivar (1 for year-one plants, 2 for year-two plants\
        \n  and so on).\
        \n\n  The number you enter will then be subtracted from the numbers of plants\
        \n  recorded as being in stock for that cultivar and that age.\
        \n\n  We recommend running this option as soon as you can after noting and\
        \n  disposing of dead or irreversibly damaged plants.\
        \n\n  The App will not allow you to record losses greater than the total stock\
        \n  of the affected cultivar and age. It will let you know when stocks of\
        \n  the affected plants reach zero.\
        \n"


help_text_option7 = "\n\n                     Option 7 -- RECORD GRAFTS ACQUIRED\
        \n\n  Option 7 lets you record any acquisitions of grafted plants you may\
        \n  make. It first asks you to identify the cultivar you have purchased\
        \n  or otherwise acquired and then the age of that cultivar (1 for year-one\
        \n  plants, 2 for year-two and so on).\
        \n\n  The number you enter will then be added to the numbers of plants\
        \n  recorded as being in stock for that cultivar and that age.\
        \n\n  We recommend running this option as soon as you can after acquiring new\
        \n plants.\
        \n\n  The App will let you know when stocks of the affected plants reach the\
        \n  originally planned number.\
        \n"


help_text_option8 = "\n\n                     Option 8 -- HOLD PLANTS BACK\
        \n\n  A grafted plant assigned a particular age is not necessarily of that age.\
        \n  The best way of putting it would be to say that Year-Two plants are\
        \n  plants of the size and quality typical of plants in their second year of\
        \n  growth after grafting. Any plants that have grown more slowly or faster\
        \n  during the year may need to be reclassified to reflect their progress.\
        \n  Options 8 and 9 allow you to do this.\
        \n\n  Option 8 allows you to hold back slower plants for a year, so that a\
        \n  number of Year-Three plants, for example, are held back to Year Two.\
        \n\n  It first asks you to identify the cultivar you want to hold back and\
        \n  then the age of that cultivar (1 for Year-One grafted plants, 2 for\
        \n  Year-Two plants and so on).\
        \n\n  The number you indicate of affected plants will be held back by one\
        \n  year.\
        \n\n  The App will not let you know hold back more of the affected plants than\
        \n  there are in stock.\
        \n\n  We recommend recording such changes as soon as you have physically moved\
        \n  the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option9 = "\n\n                     Option 9 -- BRING PLANTS FORWARD\
        \n\n  A grafted plant assigned a particular age is not necessarily of that age.\
        \n  The best way of putting it would be to say that Year-Two plants are\
        \n  plants of the size and quality typical of plants in their second year\
        \n  of growth after grafting. Any plants that have grown more slowly or faster\
        \n  during the year may need to be reclassified to reflect their progress.\
        \n  Options 8 and 9 allow you to do this.\
        \n\n  Option 9 allows you to bring faster-growing plants forward by a year,\
        \n  so that a number of Year-Three plants, for example, are brought forward\
        \n  to Year Four.\
        \n\n  It first asks you to identify the cultivar you want to bring forward and\
        \n  then the age of that cultivar (1 for Year-One grafted plants, 2 for\
        \n  Year-Two plants and so on).\
        \n\n  The affected plants will be brought forward by one year.\
        \n\n  The App will not let you know hold back more of the affected plants than\
        \n  there are in stock.\
        \n\n  We recommend recording such changes as soon as you have physically moved\
        \n  the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option0 = "\n\n             Option 0 -- CLOSE CURRENT YEAR/OPEN NEW YEAR\
        \n\n  Option 0 tells you what the App's current year is, gives you detailed\
        \n  statistics on the work you've already planned and recorded as completed\
        \n  for that year, and asks you if you're sure you want to close out that\
        \n  year and create a new year.\
        \n\n  If you confirm, it will close out the year and create a new set of\
        \n  records for the new current year, which will be the previous year plus\
        \n  one.\
        \n\n  Be very careful all your planning is done and all your work for the\
        \n  current year has been completed and recorded before confirming that you\
        \n  want to create a new year.\
        \n\n  You should run this option only once a year. We recommend doing so\
        \n  either on 31 December of the old current year or as early as possible\
        \n  in January of the new current year.\
        \n"
        