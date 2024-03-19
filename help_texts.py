INDENT = "  "

intro_text = f"\n##########################################################################\
    \n\n                            W I T C H - H A Z E L\
    \n\
    \n{INDENT}Welcome to witch-hazel, your simple app for planning and recording\
    \n{INDENT}your production of grafted Hamamelis plants!\
    \n\
    \n{INDENT}For a summary list of the functions of witch-hazel, press Enter.\
    \n\
    \n{INDENT}For an explanation of how the program works, type 'HELP' on the\
    \n{INDENT}command line.\
    \n\
    \n{INDENT}For detailed help on each of the program's options, type 'HELP'\
    \n{INDENT}followed by a space, followed by the number of the option you need\
    \n{INDENT}more information on.\
    \n\
    \n{INDENT}Type 'EXIT' on the command line to close the witch-hazel app.\
    \n\
    \n_____________________________________________________________________________"


help_text1 = f"\n                        WITCH-HAZEL HELP\
    \n\n{INDENT}To run witch-hazel, run the script file that contains its code.\
    \n{INDENT}From within the Heroku App environment, simply on the red 'RUN PROGRAM' button.\
    \n{INDENT}On opening, the app will show you a list of the options available to\
    \n{INDENT}you and ask which of them you would like to perform:\
    \n\n{INDENT}{INDENT}1. Plan grafts for this year\
    \n{INDENT}{INDENT}2. Record grafts taken\
    \n{INDENT}{INDENT}3. Record rooted cuttings potted up\
    \n{INDENT}{INDENT}4. Plan this year's cutting campaign\
    \n{INDENT}{INDENT}5. Record cuttings taken\
    \n{INDENT}{INDENT}6. Record plant losses\
    \n{INDENT}{INDENT}7. Record plant gains\
    \n{INDENT}{INDENT}8. Hold grafted plants over for one year\
    \n{INDENT}{INDENT}9. Bring grafted plants forward one year\
    \n\n{INDENT}{INDENT}0. Close out current year\
    \n"

help_text2 = f"{INDENT}Type in the number of the operation you wish to perform,\
    \n{INDENT}the app will guide the process.\
    \n\n{INDENT}Look at the README.md file for further details on each operation.\
    \n\n{INDENT}The App will tell you the range of numbers you can choose from (0 to 12).\
    \n{INDENT}Any time you enter an invalid number (including a negative number), the app\
    \n{INDENT}will give you another opportunity to enter a valid one.\
    \n\n{INDENT}During some operations the App may ask you a yes or no confirmation\
    \n{INDENT}question. Where this happens you should answer yes by typing a 'y' or 'Y'\
    \n{INDENT}on the command line. Typing in any other symbol will be taken as a 'No',\
    \n{INDENT}and will result in the app returning to the main menu.\
    \n\n{INDENT}To get detailed Help on any specific function, type 'HELP' followed\
    \n{INDENT}by a space and then the number of the function on which\
    \n{INDENT}you want detailed help. You can do this from anywhere in the App.\
    \n"


menu_title = f"\n                            W I T C H - H A Z E L"

menu_text = f"\n{INDENT}What would you like to do?\
    \n{INDENT}Choose from among the following operations:\
    \n\
    \n{INDENT}{INDENT}1. Plan grafts for this year\
    \n{INDENT}{INDENT}2. Record grafts taken\
    \n{INDENT}{INDENT}3. Record rooted cuttings potted up\
    \n{INDENT}{INDENT}4. Plan this year's cutting campaign\
    \n{INDENT}{INDENT}5. Record cuttings taken\
    \n{INDENT}{INDENT}6. Record plant losses\
    \n{INDENT}{INDENT}7. Record plant gains\
    \n{INDENT}{INDENT}8. Hold back grafted plants for one year\
    \n{INDENT}{INDENT}9. Bring grafted plants forward one year\
    \n\n{INDENT}{INDENT}0. Create new year/Close out current year\
    \n"


help_text_option1 = f"\n\n                Option 1 -- PLAN NUMBER OF GRAFTS\
        \n\
        \n{INDENT}Option 1 lets you record the number of grafts you plan to make for each\
        \n{INDENT}cultivar of Hamamelis in the current year. Later, when you use Option 2\
        \n{INDENT}to record the grafts you've actually taken for the chosen cultivar\
        \n{INDENT}(which you can do as often as you like), the App will let you know when\
        \n{INDENT}you've made the number of that cultivar you originally planned to make\
        \n{INDENT}in the current year.\
        \n\n{INDENT}When you choose Option 1, the App will show you the list of cultivars\
        \n{INDENT}recorded in your data and ask you choose the number of the cultivar\
        \n{INDENT}whose grafting program you wish to plan for the year.\
        \n\n{INDENT}If you run Option 1 a second time for the same cultivar, the App will\
        \n{INDENT}tell you how many grafts you planned in the previous session and asks\
        \n{INDENT}you to confirm whether you want to change this number. If you confirm\
        \n{INDENT}and enter a new number, this new entry will REPLACE the previous\
        \n{INDENT}number. It will not be summed together with the old number!\
        \n"


help_text_option2 = f"\n\n                Option 2 -- RECORD GRAFTS MADE\
        \n\n{INDENT}Option 2 lets you record the number of grafts of your chosen cultivar\
        \n{INDENT}you have taken since you last ran that option for that cultivar (or, if\
        \n{INDENT}you are running the option for the first time in the current year, the\
        \n{INDENT}number of grafts you have taken so far of that graft in the current\
        \n{INDENT}year).\
        \n\n{INDENT}When you choose Option 2, the App will output the list of cultivars\
        \n{INDENT}recorded in your data and ask you choose the number of the cultivar for\
        \n{INDENT}which you want to record new grafts.\
        \n\n{INDENT}You can run Option 2 as often as you like for any cultivar, though we\
        \n{INDENT}recommend running it every time you've completed a session of grafting,\
        \n{INDENT}while the number of grafts you've taken in that session is still fresh\
        \n{INDENT}in your mind.\
        \n\n{INDENT}Each time you record a number of grafts made for a particular cultivar,\
        \n{INDENT}that number is added to the previous total for that cultivar.\
        \n\n{INDENT}The App will tell you when you've reached (or exceeded) the number of\
        \n{INDENT}grafts you planned to make for that cultivar (using Option 1).\
        \n"


help_text_option3 = f"\n\n                Option 3 -- RECORD CUTTINGS POTTED UP\
        \n\n{INDENT}Option 3 lets you record the number of rooted cuttings you have potted\
        \n{INDENT}up since you last ran that Option (or, if you are running the Option for\
        \n{INDENT}the first time in the current year, the number of rooted cuttings you\
        \n{INDENT}have potted up so far in the current year).\
        \n\n{INDENT}You can run Option 3 as often as you like, though we recommend running\
        \n{INDENT}it every time you've completed a session of potting up rooted cuttings,\
        \n{INDENT}while the number you've potted up in that session is still fresh in your\
        \n{INDENT}mind.\
        \n\n{INDENT}Each time you record some rooted cuttings being potted up, that number\
        \n{INDENT}is added to the previous total.\
        \n\n{INDENT}The App will warn you when you've reached (or exceeded) the number of\
        \n{INDENT}cuttings you have recorded as being available for potting up (i.e. the\
        \n{INDENT}number of cuttings made, minus any losses you have recorded since then).\
        \n"


help_text_option4 = f"\n\n                Option 4 -- PLAN NUMBER OF CUTTINGS\
        \n\
        \n{INDENT}Option 1 lets you record the number of cuttings for future rootstocks\
        \n{INDENT}that you plan to make for the current year. Later, when you use Option 2\
        \n{INDENT}to record the cuttings you've actually taken (which you can do as often\
        \n{INDENT}as you like), the App will let you know when you've reached the number\
        \n{INDENT}of cuttings you originally planned for the current year.\
        \n\n{INDENT}If you run Option 1 a second time, the App will tell how many cuttings\
        \n{INDENT}you planned in the previous session and asks you to confirm whether you\
        \n{INDENT}want to change this number. If you confirm and enter a new number, this\
        \n{INDENT}new entry will REPLACE the previous number. It will not be summed\
        \n{INDENT}together with the old number!\
        \n"


help_text_option5 = f"\n\n                Option 5 -- RECORD CUTTINGS TAKEN\
        \n\n{INDENT}Option 2 lets you record the number of cuttings you have taken since you\
        \n{INDENT}last ran that Option (or, if you are running the Option for the first\
        \n{INDENT}time in the current year, the number of cuttings you have taken so far\
        \n{INDENT}in the current year).\
        \n\n{INDENT}You can run Option 2 as often as you like, though we recommend running\
        \n{INDENT}it every time you've completed a session of cutting taking, while the\
        \n{INDENT}number of cuttings you've taken in that session is still fresh in your\
        \n{INDENT}mind.\
        \n\n{INDENT}Each time you record a number of cuttings made, that number is added to\
        \n{INDENT}the previous total.\
        \n\n{INDENT}The App will tell you when you've reached (or exceeded) the number of\
        \n{INDENT}cuttings you planned to make (using Option 1).\
        \n"


help_text_option6 = f"\n\n                Option 6 -- RECORD GRAFTS LOST\
        \n\n{INDENT}Option 6 lets you record any losses of grafted plants you may suffer.\
        \n{INDENT}It first asks you to identify the cultivar that has suffered losses and\
        \n{INDENT}the age of that cultivar (1 for year-one plants, 2 for year-two plants\
        \n{INDENT}and so on).\
        \n\n{INDENT}The number you enter will then be subtracted from the numbers of plants\
        \n{INDENT}recorded as being in stock for that cultivar and that age.\
        \n\n{INDENT}We recommend running this option as soon as you can after noting and\
        \n{INDENT}disposing of dead or irreversibly damaged plants.\
        \n\n{INDENT}The App will not allow you to record losses greater than the total stock\
        \n{INDENT}of the affected cultivar and age. It will let you know when stocks of\
        \n{INDENT}the affected plants reach zero.\
        \n"


help_text_option7 = f"\n\n                Option 7 -- RECORD GRAFTS ACQUIRED\
        \n\n{INDENT}Option 7 lets you record any acquisitions of grafted plants you may\
        \n{INDENT}make. It first asks you to identify the cultivar you have purchased\
        \n{INDENT}or otherwise acquired and then the age of that cultivar (1 for year-one\
        \n{INDENT}plants, 2 for year-two and so on).\
        \n\n{INDENT}The number you enter will then be added to the numbers of plants\
        \n{INDENT}recorded as being in stock for that cultivar and that age.\
        \n\n{INDENT}We recommend running this option as soon as you can after acquiring new\
        \n{INDENT}plants.\
        \n\n{INDENT}The App will let you know when stocks of the affected plants reach the\
        \n{INDENT}originally planned number.\
        \n"


help_text_option8 = f"\n\n                Option 8 -- HOLD PLANTS BACK\
        \n\n{INDENT}A grafted plant assigned a particular age is not necessarily of that age.\
        \n{INDENT}The best way of putting it would be to say that Year-Two plants are\
        \n{INDENT}plants of the size and quality typical of plants in their second year of\
        \n{INDENT}growth after grafting. Any plants that have grown more slowly or faster\
        \n{INDENT}during the year may need to be reclassified to reflect their progress.\
        \n{INDENT}Options 8 and 9 allow you to do this.\
        \n\n{INDENT}Option 8 allows you to hold back slower plants for a year, so that a\
        \n{INDENT}number of Year-Three plants, for example, are held back to Year Two.\
        \n\n{INDENT}It first asks you to identify the cultivar you want to hold back and\
        \n{INDENT}then the age of that cultivar (1 for Year-One grafted plants, 2 for\
        \n{INDENT}Year-Two plants and so on).\
        \n\n{INDENT}The number you indicate of affected plants will be held back by one\
        \n{INDENT}year.\
        \n\n{INDENT}The App will not let you know hold back more of the affected plants than\
        \n{INDENT}there are in stock.\
        \n\n{INDENT}We recommend recording such changes as soon as you have physically moved\
        \n{INDENT}the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option9 = f"\n\n                Option 9 -- BRING PLANTS FORWARD\
        \n\n{INDENT}A grafted plant assigned a particular age is not necessarily of that age.\
        \n{INDENT}The best way of putting it would be to say that Year-Two plants are\
        \n{INDENT}plants of the size and quality typical of plants in their second year\
        \n{INDENT}of growth after grafting. Any plants that have grown more slowly or faster\
        \n{INDENT}during the year may need to be reclassified to reflect their progress.\
        \n{INDENT}Options 8 and 9 allow you to do this.\
        \n\n{INDENT}Option 9 allows you to bring faster-growing plants forward by a year,\
        \n{INDENT}so that a number of Year-Three plants, for example, are brought forward\
        \n{INDENT}to Year Four.\
        \n\n{INDENT}It first asks you to identify the cultivar you want to bring forward and\
        \n{INDENT}then the age of that cultivar (1 for Year-One grafted plants, 2 for\
        \n{INDENT}Year-Two plants and so on).\
        \n\n{INDENT}The affected plants will be brought forward by one year.\
        \n\n{INDENT}The App will not let you know hold back more of the affected plants than\
        \n{INDENT}there are in stock.\
        \n\n{INDENT}We recommend recording such changes as soon as you have physically moved\
        \n{INDENT}the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option0 = f"\n\n          Option 0 -- CLOSE CURRENT YEAR/OPEN NEW YEAR\
        \n\n{INDENT}Option 0 tells you what the App's current year is, gives you detailed\
        \n{INDENT}statistics on the work you've already planned and recorded as completed\
        \n{INDENT}for that year, and asks you if you're sure you want to close out that\
        \n{INDENT}year and create a new year.\
        \n\n{INDENT}If you confirm, it will close out the year and create a new set of\
        \n{INDENT}records for the new current year, which will be the previous year plus\
        \n{INDENT}one.\
        \n\n{INDENT}Be very careful all your planning is done and all your work for the\
        \n{INDENT}current year has been completed and recorded before confirming that you\
        \n{INDENT}want to create a new year.\
        \n\n{INDENT}You should run this option only once a year. We recommend doing so\
        \n{INDENT}either on 31 December of the old current year or as early as possible\
        \n{INDENT}in January of the new current year.\
        \n"
        