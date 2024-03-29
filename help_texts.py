import config, msgs

intro_text = f"\n##########################################################################\
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
    \n{config.INDENT}From within the Heroku App environment, simply on the red 'RUN PROGRAM' button.\
    \n{config.INDENT}On opening, the app will show you a list of the options available to\
    \n{config.INDENT}you and ask which of them you would like to perform:\
    \n{msgs.LIST_OF_OPTIONS}"

help_text2 = f"{config.INDENT}Type in the number of the operation you wish to perform,\
    \n{config.INDENT}the app will guide the process.\
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


menu_title = f"\n                            W I T C H - H A Z E L"

menu_text = f"\n{config.INDENT}What would you like to do?\
    \n{config.INDENT}Choose from among the following operations:\
    \n\n{msgs.LIST_OF_OPTIONS}"


help_text_option1 = f"\n\n                Option 1 -- PLAN NUMBER OF GRAFTS\
        \n\
        \n{config.INDENT}Option 1 lets you record the number of grafts you plan to make for each\
        \n{config.INDENT}cultivar of Hamamelis in the current year. Later, when you use Option 2\
        \n{config.INDENT}to record the grafts you've actually taken for the chosen cultivar\
        \n{config.INDENT}(which you can do as often as you like), the App will let you know when\
        \n{config.INDENT}you've made the number of that cultivar you originally planned to make\
        \n{config.INDENT}in the current year.\
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
        \n{config.INDENT}you have taken since you last ran that option for that cultivar (or, if\
        \n{config.INDENT}you are running the option for the first time in the current year, the\
        \n{config.INDENT}number of grafts you have taken so far of that graft in the current\
        \n{config.INDENT}year).\
        \n\n{config.INDENT}When you choose Option 2, the App will output the list of cultivars\
        \n{config.INDENT}recorded in your data and ask you choose the number of the cultivar for\
        \n{config.INDENT}which you want to record new grafts.\
        \n\n{config.INDENT}You can run Option 2 as often as you like for any cultivar, though we\
        \n{config.INDENT}recommend running it every time you've completed a session of grafting,\
        \n{config.INDENT}while the number of grafts you've taken in that session is still fresh\
        \n{config.INDENT}in your mind.\
        \n\n{config.INDENT}Each time you record a number of grafts made for a particular cultivar,\
        \n{config.INDENT}that number is added to the previous total for that cultivar.\
        \n\n{config.INDENT}The App will tell you when you've reached (or exceeded) the number of\
        \n{config.INDENT}grafts you planned to make for that cultivar (using Option 1).\
        \n"


help_text_option3 = f"\n\n                Option 3 -- RECORD CUTTINGS POTTED UP\
        \n\n{config.INDENT}Option 3 lets you record the number of rooted cuttings you have potted\
        \n{config.INDENT}up since you last ran that Option (or, if you are running the Option for\
        \n{config.INDENT}the first time in the current year, the number of rooted cuttings you\
        \n{config.INDENT}have potted up so far in the current year).\
        \n\n{config.INDENT}You can run Option 3 as often as you like, though we recommend running\
        \n{config.INDENT}it every time you've completed a session of potting up rooted cuttings,\
        \n{config.INDENT}while the number you've potted up in that session is still fresh in your\
        \n{config.INDENT}mind.\
        \n\n{config.INDENT}Each time you record some rooted cuttings being potted up, that number\
        \n{config.INDENT}is added to the previous total.\
        \n\n{config.INDENT}The App will warn you when you've reached (or exceeded) the number of\
        \n{config.INDENT}cuttings you have recorded as being available for potting up (i.e. the\
        \n{config.INDENT}number of cuttings made, minus any losses you have recorded since then).\
        \n"


help_text_option4 = f"\n\n                Option 4 -- PLAN NUMBER OF CUTTINGS\
        \n\
        \n{config.INDENT}Option 1 lets you record the number of cuttings for future rootstocks\
        \n{config.INDENT}that you plan to make for the current year. Later, when you use Option 2\
        \n{config.INDENT}to record the cuttings you've actually taken (which you can do as often\
        \n{config.INDENT}as you like), the App will let you know when you've reached the number\
        \n{config.INDENT}of cuttings you originally planned for the current year.\
        \n\n{config.INDENT}If you run Option 1 a second time, the App will tell how many cuttings\
        \n{config.INDENT}you planned in the previous session and asks you to confirm whether you\
        \n{config.INDENT}want to change this number. If you confirm and enter a new number, this\
        \n{config.INDENT}new entry will REPLACE the previous number. It will not be summed\
        \n{config.INDENT}together with the old number!\
        \n"


help_text_option5 = f"\n\n                Option 5 -- RECORD CUTTINGS TAKEN\
        \n\n{config.INDENT}Option 2 lets you record the number of cuttings you have taken since you\
        \n{config.INDENT}last ran that Option (or, if you are running the Option for the first\
        \n{config.INDENT}time in the current year, the number of cuttings you have taken so far\
        \n{config.INDENT}in the current year).\
        \n\n{config.INDENT}You can run Option 2 as often as you like, though we recommend running\
        \n{config.INDENT}it every time you've completed a session of cutting taking, while the\
        \n{config.INDENT}number of cuttings you've taken in that session is still fresh in your\
        \n{config.INDENT}mind.\
        \n\n{config.INDENT}Each time you record a number of cuttings made, that number is added to\
        \n{config.INDENT}the previous total.\
        \n\n{config.INDENT}The App will tell you when you've reached (or exceeded) the number of\
        \n{config.INDENT}cuttings you planned to make (using Option 1).\
        \n"


help_text_option6 = f"\n\n                Option 6 -- RECORD GRAFTS LOST\
        \n\n{config.INDENT}Option 6 lets you record any losses of grafted plants you may suffer.\
        \n{config.INDENT}It first asks you to identify the cultivar that has suffered losses and\
        \n{config.INDENT}the age of that cultivar (1 for year-one plants, 2 for year-two plants\
        \n{config.INDENT}and so on).\
        \n\n{config.INDENT}The number you enter will then be subtracted from the numbers of plants\
        \n{config.INDENT}recorded as being in stock for that cultivar and that age.\
        \n\n{config.INDENT}We recommend running this option as soon as you can after noting and\
        \n{config.INDENT}disposing of dead or irreversibly damaged plants.\
        \n\n{config.INDENT}The App will not allow you to record losses greater than the total stock\
        \n{config.INDENT}of the affected cultivar and age. It will let you know when stocks of\
        \n{config.INDENT}the affected plants reach zero.\
        \n"


help_text_option7 = f"\n\n                Option 7 -- RECORD GRAFTS ACQUIRED\
        \n\n{config.INDENT}Option 7 lets you record any acquisitions of grafted plants you may\
        \n{config.INDENT}make. It first asks you to identify the cultivar you have purchased\
        \n{config.INDENT}or otherwise acquired and then the age of that cultivar (1 for year-one\
        \n{config.INDENT}plants, 2 for year-two and so on).\
        \n\n{config.INDENT}The number you enter will then be added to the numbers of plants\
        \n{config.INDENT}recorded as being in stock for that cultivar and that age.\
        \n\n{config.INDENT}We recommend running this option as soon as you can after acquiring new\
        \n{config.INDENT}plants.\
        \n\n{config.INDENT}The App will let you know when stocks of the affected plants reach the\
        \n{config.INDENT}originally planned number.\
        \n"


help_text_option8 = f"\n\n                Option 8 -- HOLD PLANTS BACK\
        \n\n{config.INDENT}A grafted plant assigned a particular age is not necessarily of that age.\
        \n{config.INDENT}The best way of putting it would be to say that Year-Two plants are\
        \n{config.INDENT}plants of the size and quality typical of plants in their second year of\
        \n{config.INDENT}growth after grafting. Any plants that have grown more slowly or faster\
        \n{config.INDENT}during the year may need to be reclassified to reflect their progress.\
        \n{config.INDENT}Options 8 and 9 allow you to do this.\
        \n\n{config.INDENT}Option 8 allows you to hold back slower plants for a year, so that a\
        \n{config.INDENT}number of Year-Three plants, for example, are held back to Year Two.\
        \n\n{config.INDENT}It first asks you to identify the cultivar you want to hold back and\
        \n{config.INDENT}then the age of that cultivar (1 for Year-One grafted plants, 2 for\
        \n{config.INDENT}Year-Two plants and so on).\
        \n\n{config.INDENT}The number you indicate of affected plants will be held back by one\
        \n{config.INDENT}year.\
        \n\n{config.INDENT}The App will not let you know hold back more of the affected plants than\
        \n{config.INDENT}there are in stock.\
        \n\n{config.INDENT}We recommend recording such changes as soon as you have physically moved\
        \n{config.INDENT}the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option9 = f"\n\n                Option 9 -- BRING PLANTS FORWARD\
        \n\n{config.INDENT}A grafted plant assigned a particular age is not necessarily of that age.\
        \n{config.INDENT}The best way of putting it would be to say that Year-Two plants are\
        \n{config.INDENT}plants of the size and quality typical of plants in their second year\
        \n{config.INDENT}of growth after grafting. Any plants that have grown more slowly or faster\
        \n{config.INDENT}during the year may need to be reclassified to reflect their progress.\
        \n{config.INDENT}Options 8 and 9 allow you to do this.\
        \n\n{config.INDENT}Option 9 allows you to bring faster-growing plants forward by a year,\
        \n{config.INDENT}so that a number of Year-Three plants, for example, are brought forward\
        \n{config.INDENT}to Year Four.\
        \n\n{config.INDENT}It first asks you to identify the cultivar you want to bring forward and\
        \n{config.INDENT}then the age of that cultivar (1 for Year-One grafted plants, 2 for\
        \n{config.INDENT}Year-Two plants and so on).\
        \n\n{config.INDENT}The affected plants will be brought forward by one year.\
        \n\n{config.INDENT}The App will not let you know hold back more of the affected plants than\
        \n{config.INDENT}there are in stock.\
        \n\n{config.INDENT}We recommend recording such changes as soon as you have physically moved\
        \n{config.INDENT}the affected plants to the appropriate section of the nursery.\
        \n"


help_text_option0 = f"\n\n          Option 0 -- CLOSE CURRENT YEAR/OPEN NEW YEAR\
        \n\n{config.INDENT}Option 0 tells you what the App's current year is, gives you detailed\
        \n{config.INDENT}statistics on the work you've already planned and recorded as completed\
        \n{config.INDENT}for that year, and asks you if you're sure you want to close out that\
        \n{config.INDENT}year and create a new year.\
        \n\n{config.INDENT}If you confirm, it will close out the year and create a new set of\
        \n{config.INDENT}records for the new current year, which will be the previous year plus\
        \n{config.INDENT}one.\
        \n\n{config.INDENT}Be very careful all your planning is done and all your work for the\
        \n{config.INDENT}current year has been completed and recorded before confirming that you\
        \n{config.INDENT}want to create a new year.\
        \n\n{config.INDENT}You should run this option only once a year. We recommend doing so\
        \n{config.INDENT}either on 31 December of the old current year or as early as possible\
        \n{config.INDENT}in January of the new current year.\
        \n"
        