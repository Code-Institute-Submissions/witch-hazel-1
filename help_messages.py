help_text1 = "\n##########################################################################\
    \n\n                             WITCH-HAZEL HELP\
    \n\nTo run witch-hazel, run the script file that contains its code\
    \nFrom within the Heroku App environment, simply on the red 'RUN PROGRAM' button.\
    \nOn opening, the app will show you a list of the options available to\
    \nyou and ask which of them you would like to perform:\
    \n\n0. Help\
    \n1. Close out current year\
    \n\n2. Plan this year's cutting campaign\
    \n3. Record cuttings taken\
    \n4. Record rooted cuttings potted up\
    \n\n5. Plan grafts for this year\
    \n\n6. Record grafts taken\
    \n\n7. Record plant losses\
    \n8. Record plant gains\
    \n9. Hold plants over for one year\
    \n10. Bring plants forward one year\
    \n\n11. Add new cultivar"

help_text2 = "Type the number of the operation you wish to perform.\
    \nThe app will guide you through the operation you have chosen to perform.\
    \nYou will need to restart the app each time you wish to run an operation.\
    \n\nLook at the README.md file for details on each of these options.\
    \n\nIn most cases you'll be asked to enter a number. It will usually\
    \nindicate the valid range. Negative numbers are always taken as\
    \ninvalid. Any time you enter an invalid number, the app will give you\
    \nanother opportunity to enter a valid one.\
    \n\nFor some operations the App may ask you a yes or no confirmation\
    \nquestion. Where this happens you should answer yes by typing a 'y' or 'Y'\
    \non the command line. Typing in any other symbol will be taken as a 'No',\
    \nand will result in the app returning to the main menu.\
    \n\nThe App will tell you what range of numbers is valid in each case.\
    \n\nTo get detailed Help on any specific function, type 'HELP' followed\
    \nby a space, followed by the number of the function on which you want\
    \ndetailed help.\
    \n\n###############################################################################\
    \n"

intro_text = "\n##########################################################################\
    \n\n                            W I T C H - H A Z E L\
    \n\
    \nWelcome to witch-hazel, your simple app for planning your production of\
    \ngrafted Hamamelis plants!\
    \n\
    \nFor a summary list of the functions of witch-hazel, press Enter\
    \n\
    \nFor a full explanation of each of the program's functions and\
    \ninstructions on how to use them, enter 'help' on the command line\
    \nonce you have finished scrolling through these texts.\
    \nThis will show you the HELP text for the app.\
    \n\
    \nThen follow the instructions to get more detailed Help on each\
    \nindividual function.\
    \n\
    \nType 'EXIT' at any stage to close the witch-hazel app.\
    \n\
    \n_____________________________________________________________________________"

menu_title = "\n\n                            W I T C H - H A Z E L"

menu_text = "\n\
    \nWhat would you like to do?\
    \nChoose from among the following operations:\
    \n\n0. Help\
    \n\n1. Create new year/Close out current year\
    \n\n2. Plan this year's cutting campaign\
    \n3. Record cuttings taken\
    \n4. Record rooted cuttings potted up\
    \n\n5. Plan grafts for this year\
    \n6. Record grafts taken\
    \n\n7. Record plant losses\
    \n8. Record plant gains\
    \n9. Hold over plants for one year\
    \n10. Bring plants forward one year\
    \n\n11. Add new cultivar\
    \n"

help_text_option0 = "\n\n                     Option 0 -- CLOSE CURRENT YEAR/OPEN NEW YEAR\
        \n\
        \nOption 0 tells you what the App's current year is, gives you detailed\
        \nstatistics on the work you've already planned and recorded as completed for that year,\
        \nand asks you if you're sure you want to close out that year and create a new year.\
        \nIf you confirm, it will close out the year and create a new set of records for\
        \nthe new current year, which will be the previous year plus one.\
        \n\nBe very careful all your planning is done and all your work for the current year\
        \nhas been completed and recorded before confirming that you want to create a new year.\
        \n\nYou should run this option only once a year. We recommend doing so either on\
        \n31 December of the old current year or as early as possible in January of the new\
        \ncurrent year."

help_text_option1 = "\n\n                     Option 1 -- PLAN NUMBER OF CUTTINGS\
        \n\
        \nOption 1 lets you record the number of cuttings for future rootstocks that\
        \nyou plan to make for the current year. Later, when you use Option 2 to record\
        \nthe cuttings you've actually taken (which you can do as often as you like), the App\
        \nwill let you know when you've reached the number of cuttings you originally planned\
        \nfor the current year.\
        \n\nIf you run Option 1 a second time, the App will tell how many cuttings you planned\
        \nin the previous session and asks you to confirm whether you want to change this number.\
        \nIf you confirm and enter a new number, this new entry will REPLACE the previous number.\
        \nIt will not be summed together with the old number!"

help_text_option2 = "\n\n                     Option 2 -- RECORD CUTTINGS TAKEN\
        \n\
        \nOption 2 lets you record the number of cuttings you have taken since you last ran\
        \nthat Option (or, if you are running the Option for the first time in the current year,\
        \nthe number of cuttings you have taken so far in the current year).\
        \n\nYou can run Option 2 as often as you like, though we recommend running it every time\
        \nyou've completed a session of cutting taking, while the number of cuttings you've taken\
        \nin that session is still fresh in your mind.\
        \n\nEach time you record a number of cuttings made, that number is added to the previous\
        \ntotal.\
        \n\nThe App will tell you when you've reached (or exceeded) the number of cuttings you\
        \nplanned to make (using Option 1)."

help_text_option3 = "\n\n                     Option 3 -- RECORD CUTTINGS POTTED UP\
        \n\
        \nOption 3 lets you record the number of rooted cuttings you have potted up\
        \nsince you last ran that Option (or, if you are running the Option for the first time\
        \nin the current year, the number of rooted cuttings you have potted up so far\
        \nin the current year).\
        \n\nYou can run Option 3 as often as you like, though we recommend running it every time\
        \nyou've completed a session of potting up rooted cuttings, while the number you've potted\
        \nup in that session is still fresh in your mind.\
        \n\nEach time you record some rooted cuttings being potted up, that number is added to\
        \nthe previous total.\
        \n\nThe App will warn you when you've reached (or exceeded) the number of cuttings you\
        \nhave recorded as being available for potting up (i.e. the number of cuttings made,\
        \nminus any losses you have recorded since then)."

help_text_option4 = "\n\n                     Option $ -- PLAN NUMBER OF GRAFTS\
        \n\
        \nOption 4 lets you record the number of grafts you plan to make for each cultivar\
        \nof Hamamelis in the current year. Later, when you use Option 5 to record\
        \nthe grafts you've actually taken for the chosen cultivar (which you can do as often\
        \nas you like), the App will let you know when you've reached the number of grafts\
        \nof that cultivar you originally planned for the current year.\
        \n\nWhen you choose Option 4, the App will output the list of cultivars recorded in\
        \nyour data and ask you choose the number of the cultivar whose grafting program you\
        \nwish to plan for the year.\
        \n\nIf you run Option 4 a second time for the same cultivar, the App will tell how\
        \nmany grafts you planned in the previous session and asks you to confirm whether\
        \nyou want to change this number. If you confirm and enter a new number, this new\
        \nentry will REPLACE the previous number. It will not be summed together with the\
        \nold number!"

help_text_option5 = "\n\n                     Option 5 -- RECORD GRAFTS MADE\
        \n\
        \nOption 5 lets you record the number of grafts of your chosen cultivar you have\
        \ntaken since you last ran that Option for that cultivar (or, if you are running\
        \nthe option for the first time in the current year, the number of grafts you have\
        \ntaken so far of that graft in the current year).\
        \n\nWhen you choose Option 5, the App will output the list of cultivars recorded in\
        \nyour data and ask you choose the number of the cultivar for which you want to\
        \nrecord new grafts.\
        \n\nYou can run Option 5 as often as you like for any cultivar, though we recommend\
        \nrunning it every time you've completed a session of grafting , while the number\
        \nof grafts you've taken in that session is still fresh in your mind.\
        \n\nEach time you record a number of grafts made for a particular cultivar, that\
        \nnumber is added to the previous total for that cultivar.\
        \n\nThe App will tell you when you've reached (or exceeded) the number of grafts you\
        \nplanned to make for that cultivar (using Option 4)."

help_text_option6 = "\n\n                     Option 6 -- RECORD GRAFTS LOST\
        \n\
        \nOption 6 lets you record any losses of grafted plants you may suffer. It first\
        \nasks you to identify the cultivar that has suffered losses and the age of that cultivar\
        \n(1 for year-one plants, 2 for year-two plants and so on).\
        \n\nThe number you enter will then be subtracted from the numbers of plants recorded as\
        \nbeing in stock for that cultivar and that age.\
        \n\nWe recommend running this option as soon as you can after noting and disposing of\
        \ndead or irreversibly damaged plants.\
        \n\nThe App will not allow you to record losses greater than the total stock of the\
        \naffected cultivar and age. It will let you know when stocks of the affected plants\
        \nreach zero."

help_text_option7 = "\n\n                     Option 7 -- RECORD GRAFTS ACQUIRED\
        \n\
        \nOption 7 lets you record any acquisitions of grafted plants you may make. It first\
        \nasks you to identify the cultivar you have purchased or otherwise acquired and then the age\
        \nof that cultivar (1 for year-one plants, 2 for year-two and so on).\
        \n\nThe number you enter will then be added to the numbers of plants recorded as\
        \nbeing in stock for that cultivar and that age.\
        \n\nWe recommend running this option as soon as you can after acquiring new plants.\
        \n\nThe App will let you know when stocks of the affected plants reach the originally\
        \nplanned number."

help_text_option8 = "\n\n                     Option 8 -- HOLD PLANTS BACK\
        \n\
        \nA grafted plant assugned a particular age, is not necessarily of that age. The best way\
        \nof putting it would be to say that Year-Two plants are plants of the size and quality\
        \ntypical of plants in their second year of growth after grafting. Any plants that have\
        \ngrown more slowly or faster during the year may need to be reclassified to reflect their\
        \nprogress. Options 8 and 9 allow you to do this.\
        \n\nOption 8 allows you to hold back slower plants for a year, so that a number of Year-Three\
        \nplants, for example, are held back to Year Two.\
        \n\nIt first asks you to identify the cultivar you want to hold back and then the age\
        \nof that cultivar (1 for Year-One grafted plants, 2 for Year-Two plants and so on).\
        \n\nThe number you indicate of affected plants will be held back by one year.\
        \n\nThe App will not let you know hold back more of the affected plants than there are in\
        \nstock.\
        \n\nWe recommend recording such changes as soon as you have physically moved the affected\
        \nplants to the appropriate section of the nursery."

help_text_option9 = "\n\n                     Option 9 -- BRING PLANTS FORWARD\
        \n\
        \nA grafted plant assugned a particular age, is not necessarily of that age. The best way\
        \nof putting it would be to say that Year-Two plants are plants of the size and quality\
        \ntypical of plants in their second year of growth after grafting. Any plants that have\
        \ngrown more slowly or faster during the year may need to be reclassified to reflect their\
        \nprogress. Options 8 and 9 allow you to do this.\
        \n\nOption 9 allows you to bring slower plants forward by a year, so that a number of Year-Three\
        \nplants, for example, are brought forward to Year Four.\
        \n\nIt first asks you to identify the cultivar you want to bring forward and then the age\
        \nof that cultivar (1 for Year-One grafted plants, 2 for Year-Two plants and so on).\
        \n\nThe affected plants will be brought forward by one year.\
        \n\nThe App will not let you know hold back more of the affected plants than there are in\
        \nstock.\
        \n\nWe recommend recording such changes as soon as you have physically moved the affected\
        \nplants to the appropriate section of the nursery."

help_text_option10 = "\n\n                     Option 10 -- ADD NEW CULTIVAR\
        \n\
        \n"

help_text_option11 = "\n\n                     Option 11 -- REMOVE CULTIVAR\
        \n\
        \n"

help_text_option12 = "\n\n                     Option 12 -- SHOW TABLES ON SCREEN\
        \n\
        \n"
