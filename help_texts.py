import config, msgs

intro_text = f"\n{config.LINE_OF_POUNDS}\
    \n\n                            W I T C H - H A Z E L\
    \n\
    \n{config.INDENT}Welcome to witch-hazel, your simple app for planning and recording\
    \n{config.INDENT}your production of grafted Hamamelis plants!\
    \n\
    \n{config.INDENT}For a summary list of the functions of witch-hazel, press Enter.\
    \n\
    \n{config.INDENT}For an explanation of how the program works, type 'HELP' on the\
    \n{config.INDENT}command line.\
    \n\
    \n{config.INDENT}For detailed help on each of the program's options, type 'HELP'\
    \n{config.INDENT}followed by a space, followed by the number of the option you need\
    \n{config.INDENT}more information on.\
    \n\
    \n{config.INDENT}Type 'EXIT' on the command line to close the witch-hazel app.\
    \n\
    \n_____________________________________________________________________________"


help_text1 = f"\n                        WITCH-HAZEL HELP\
    \n\n{config.INDENT}To run witch-hazel, run the script file that contains its code.\
    \n{config.INDENT}From within the Heroku App environment, simply on the red 'RUN PROGRAM'\
    \n{config.INDENT}button.\
    \n\n{config.INDENT}On opening, the app will show you a list of the options available to\
    \n{config.INDENT}you and ask which of them you would like to perform.\n\
    \n\
    \n{msgs.LIST_OF_OPTIONS}"

help_text2 =f"\n{config.INDENT}The first group of five options lists the seasonal tasks that you\
    \n{config.INDENT}will have to perform during the course of the calendar year (which the\
    \n{config.INDENT}program lists in seasonal order from January on).\
    \n\n{config.INDENT}You will need to complete all of these actions before you can close\
    \n{config.INDENT}the current year and move on to the next (Using Option 0)\
    \n\n{config.INDENT}The second group of options are there simply to help you record the\
    \n{config.INDENT}maintenance actions you undertake during the course of the year, allowing\
    \n{config.INDENT}you to track changes in your stock of plants as you go.\
    \n\n{config.INDENT}You do not need to complete any or all of these tasks to close out the\
    \n{config.INDENT}and move on to the next.\
    \n\n{config.INDENT}Finally, Option 0 closes out the current year and prepares the data\
    \n{config.INDENT}to allow you to start working on the next year. We recommend running it\
    \n{config.INDENT}as early as possible in the new year, before you start your first task\
    \n{config.INDENT}of the year.\
    \n"

help_text3 = f"{config.INDENT}Type in the number of the operation you wish to perform, the\
    \n{config.INDENT}app will guide you through each process.\
    \n\n{config.INDENT}Look at the README.md file for further details on each operation.\
    \n\n{config.INDENT}The App will tell you the range of numbers you can choose from (0 to 9).\
    \n{config.INDENT}Any time you enter an invalid number (including a negative number), the\
    \n{config.INDENT}app will give you another opportunity to enter a valid one.\
    \n\n{config.INDENT}During some operations the App may ask you a yes or no confirmation\
    \n{config.INDENT}question. Where this happens you should answer yes by typing a 'y' or 'Y'\
    \n{config.INDENT}on the command line or no by typing a 'n' or a 'N'.\
    \n{config.INDENT}Typing any other value will result in an error message followed \
    \n{config.INDENT}by a new request to answer yes or no. \
    \n\n{config.INDENT}To get detailed Help on any specific function, type 'HELP' followed\
    \n{config.INDENT}by a space and then the number of the function on which\
    \n{config.INDENT}you want detailed help. You can do this from anywhere in the App.\
    \n"


menu_title = f"                            W I T C H - H A Z E L"

menu_text = f"\n{config.INDENT}What would you like to do?\
    \n{config.INDENT}Choose from among the following operations:\
    \n\n{msgs.LIST_OF_OPTIONS}"


help_text_option1 = f"\n\n                Option 1 -- PLAN NUMBER OF GRAFTS\
        \n\
        \n{config.INDENT}Option 1 lets you record the number of grafts you plan to make for\
        \n{config.INDENT}each cultivar of Hamamelis in the current year. Later, when you use\
        \n{config.INDENT}Option 2 to record the grafts you've actually taken for the chosen\
        \n{config.INDENT}cultivar (which you can do as often as you like), the App will let\
        \n{config.INDENT}you know when you've made the number of that cultivar you originally\
        \n{config.INDENT}planned to makein the current year.\
        \n\n{config.INDENT}When you choose Option 1, the App will show you the list of cultivars\
        \n{config.INDENT}recorded in your data and ask you choose the number of the cultivar\
        \n{config.INDENT}whose grafting program you wish to plan for the year.\
        \n\n{config.INDENT}If you run Option 1 a second time for the same cultivar, the App will\
        \n{config.INDENT}tell you how many grafts you planned in the previous session and asks\
        \n{config.INDENT}you to confirm whether you want to change this number. If you confirm\
        \n{config.INDENT}and enter a new number, this new entry will REPLACE the previous\
        \n{config.INDENT}number. It will not be summed together with the old number!\
        \n"


help_text_option2 = f"\n\n                Option 2 -- RECORD GRAFTS MADE\
        \n\n{config.INDENT}Option 2 lets you record the number of grafts of your chosen cultivar\
        \n{config.INDENT}you have taken since you last ran that option for that cultivar (or,\
        \n{config.INDENT}if you are running the option for the first time in the current year,\
        \n{config.INDENT}the number of grafts you have taken so far of that graft in the\
        \n{config.INDENT}current year).\
        \n\n{config.INDENT}When you choose Option 2, the App will output the list of cultivars\
        \n{config.INDENT}recorded in your data and ask you choose the number of the cultivar\
        \n{config.INDENT}for which you want to record new grafts.\
        \n\n{config.INDENT}You can run Option 2 as often as you like for any cultivar, though\
        \n{config.INDENT}we recommend running it every time you've completed a session of\
        \n{config.INDENT}grafting, while the number of grafts you've taken in that session is\
        \n{config.INDENT}still fresh in your mind.\
        \n\n{config.INDENT}Each time you record a number of grafts made for a particular\
        \n{config.INDENT}cultivar, that number is added to the previous total for that\
        \n{config.INDENT}cultivar.\
        \n\n{config.INDENT}The App will tell you when you've reached (or exceeded) the number\
        \n{config.INDENT}of grafts you planned to make for that cultivar (using Option 1).\
        \n"


help_text_option3 = f"\n\n                Option 3 -- RECORD CUTTINGS POTTED UP\
        \n\n{config.INDENT}Option 3 lets you record the number of rooted cuttings you have potted\
        \n{config.INDENT}up since you last ran that Option (or, if you are running the Option\
        \n{config.INDENT}for the first time in the current year, the number of rooted cuttings\
        \n{config.INDENT}you have potted up so far in the current year).\
        \n\n{config.INDENT}You can run Option 3 as often as you like, though we recommend running\
        \n{config.INDENT}it every time you've completed a session of potting up rooted\
        \n{config.INDENT}cuttings, while the number you've potted up in that session is still\
        \n{config.INDENT} fresh in your mind.\
        \n\n{config.INDENT}Each time you record some rooted cuttings being potted up, that number\
        \n{config.INDENT}is added to the previous total.\
        \n\n{config.INDENT}The App will warn you when you've reached (or exceeded) the number of\
        \n{config.INDENT}cuttings you have recorded as being available for potting up (i.e. the\
        \n{config.INDENT}number of cuttings made, minus any losses you have recorded since then).\
        \n"


help_text_option4 = f"\n\n                Option 4 -- PLAN NUMBER OF CUTTINGS\
        \n\
        \n{config.INDENT}Option 1 lets you record the number of cuttings for future rootstocks\
        \n{config.INDENT}that you plan to make for the current year. Later, when you use Option\
        \n{config.INDENT}2 to record the cuttings you've actually taken (which you can do as\
        \n{config.INDENT}oftenas you like), the App will let you know when you've reached the\
        \n{config.INDENT}number of cuttings you originally planned for the current year.\
        \n\n{config.INDENT}If you run Option 1 a second time, the App will tell how many cuttings\
        \n{config.INDENT}you planned in the previous session and asks you to confirm whether\
        \n{config.INDENT}you want to change this number. If you confirm and enter a new number,\
        \n{config.INDENT}this new entry will REPLACE the previous number. It will not be\
        \n{config.INDENT}summed together with the old number!\
        \n"


help_text_option5 = f"\n\n                Option 5 -- RECORD CUTTINGS TAKEN\
        \n\n{config.INDENT}Option 2 lets you record the number of cuttings you have taken since\
        \n{config.INDENT}you last ran that Option (or, if you are running the Option for the\
        \n{config.INDENT}first time in the current year, the number of cuttings you have taken\
        \n{config.INDENT} so far in the current year).\
        \n\n{config.INDENT}You can run Option 2 as often as you like, though we recommend running\
        \n{config.INDENT}it every time you've completed a session of cutting taking, while the\
        \n{config.INDENT}number of cuttings you've taken in that session is still fresh in your\
        \n{config.INDENT}mind.\
        \n\n{config.INDENT}Each time you record a number of cuttings made, that number is added\
        \n{config.INDENT}to the previous total.\
        \n\n{config.INDENT}The App will tell you when you've reached (or exceeded) the number of\
        \n{config.INDENT}cuttings you planned to make (using Option 1).\
        \n"


help_text_option6 = f"\n\n                Option 6 -- RECORD GRAFTS LOST\
        \n\n{config.INDENT}Option 6 lets you record any losses of grafted plants you may suffer.\
        \n{config.INDENT}It first asks you to identify the cultivar that has suffered losses\
        \n{config.INDENT}and the age of that cultivar (1 for year-one plants, 2 for year-two\
        \n{config.INDENT}plants and so on).\
        \n\n{config.INDENT}The number you enter will then be subtracted from the numbers of\
        \n{config.INDENT}plants recorded as being in stock for that cultivar and that age.\
        \n\n{config.INDENT}We recommend running this option as soon as you can after noting and\
        \n{config.INDENT}disposing of dead or irreversibly damaged plants.\
        \n\n{config.INDENT}The App will not allow you to record losses greater than the total\
        \n{config.INDENT}stock of the affected cultivar and age. It will let you know when\
        \n{config.INDENT}stocks of the affected plants reach zero.\
        \n"


help_text_option7 = f"\n\n                Option 7 -- RECORD GRAFTS ACQUIRED\
        \n\n{config.INDENT}Option 7 lets you record any acquisitions of grafted plants you may\
        \n{config.INDENT}make. It first asks you to identify the cultivar you have purchased\
        \n{config.INDENT}or otherwise acquired and then the age of that cultivar (1 for\
        \n{config.INDENT}year-one plants, 2 for year-two and so on).\
        \n\n{config.INDENT}The number you enter will then be added to the numbers of plants\
        \n{config.INDENT}recorded as being in stock for that cultivar and that age.\
        \n\n{config.INDENT}We recommend running this option as soon as you can after acquiring\
        \n{config.INDENT}new plants.\
        \n\n{config.INDENT}The App will let you know when stocks of the affected plants reach the\
        \n{config.INDENT}originally planned number.\
        \n"


help_text_option8 = f"\n\n                Option 8 -- HOLD PLANTS BACK\
        \n\n{config.INDENT}A grafted plant assigned a particular age is not necessarily of that\
        \n{config.INDENT}age. The best way of putting it would be to say that Year-Two plants\
        \n{config.INDENT}are plants of the size and quality typical of plants in their second\
        \n{config.INDENT}year of growth after grafting. Any plants that have grown more slowly\
        \n{config.INDENT}or faster during the year may need to be reclassified to reflect their\
        \n{config.INDENT}progress. Options 8 and 9 allow you to do this.\
        \n\n{config.INDENT}Option 8 allows you to hold back slower plants for a year, so that a\
        \n{config.INDENT}number of Year-Three plants, for example, are held back to Year Two.\
        \n\n{config.INDENT}It first asks you to identify the cultivar you want to hold back and\
        \n{config.INDENT}then the age of that cultivar ('1' for Year-One grafted plants, '2'\
        \n{config.INDENT}for Year-Two plants and so on).\
        \n\n{config.INDENT}The number you indicate of affected plants will be held back by one\
        \n{config.INDENT}year.\
        \n\n{config.INDENT}The App will not let you  hold back more of the affected plants than\
        \n{config.INDENT}there are in stock.\
        \n\n{config.INDENT}We recommend recording such changes as soon as you have physically\
        \n{config.INDENT}moved the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option9 = f"\n\n                Option 9 -- BRING PLANTS FORWARD\
        \n\n{config.INDENT}A grafted plant assigned a particular age is not necessarily of that\
        \n{config.INDENT}age. The best way of putting it would be to say that Year-Two plants\
        \n{config.INDENT}are plants of the size and quality typical of plants in their second\
        \n{config.INDENT}year of growth after grafting. Any plants that have grown more slowly\
        \n{config.INDENT}or faster during the year may need to be reclassified to reflect their\
        \n{config.INDENT}progress. Options 8 and 9 allow you to do this.\
        \n\n{config.INDENT}Option 9 allows you to bring faster-growing plants forward by a year,\
        \n{config.INDENT}so that a number of Year-Three plants, for example, are brought\
        \n{config.INDENT}forward to Year Four.\
        \n\n{config.INDENT}It first asks you to identify the cultivar you want to bring forward\
        \n{config.INDENT}and then the age of that cultivar ('1' for Year-One grafted plants,\
        \n{config.INDENT}'2' for Year-Two plants and so on).\
        \n\n{config.INDENT}The affected plants will be brought forward by one year.\
        \n\n{config.INDENT}The App will not let you hold back more of the affected plants than\
        \n{config.INDENT}there are in stock.\
        \n\n{config.INDENT}We recommend recording such changes as soon as you have physically\
        \n{config.INDENT}moved the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option0 = f"\n\n          Option 0 -- CLOSE CURRENT YEAR/OPEN NEW YEAR\
        \n\n{config.INDENT}Option 0 tells you what the App's current year is, gives you some\
        \n{config.INDENT}statistics on the work you've already planned and recorded as\
        \n{config.INDENT}completed for that year, and asks you if you're sure you want to\
        \n{config.INDENT}close out that year and create a new year.\
        \n\n{config.INDENT}If you confirm, it will close out the year and create a new set of\
        \n{config.INDENT}records for the new current year, which will be the previous year plus\
        \n{config.INDENT}one.\
        \n\n{config.INDENT}Be very careful all your planning is done and all your work for the\
        \n{config.INDENT}current year has been completed and recorded before confirming that\
        \n{config.INDENT}you want to create a new year.\
        \n\n{config.INDENT}You should run this option only once a year. We recommend doing so\
        \n{config.INDENT}either on 31 December of the old current year or as early as possible\
        \n{config.INDENT}in January of the new current year.\
        \n"
        