![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# witch-hazel
A bespoke command-line app developed in Python to manage the Witch Hazel nursery.

Code Institute - Third Milestone Project: Create a user-responsive command-line app to manage a particular domain task, solving a real-world, using a variety of programming constructs.The domain task in this case was the production of high-value garden plants by grafting as practiced by the Witch Hazel nursery.

![Image of a H. x intermedia 'Arnold Promise' in mid-October](assets/readme_assets/hamamelis-autumn.jpg)

*A very common cultivar of H. x intermedia ('Arnold Promise') giving a spectacular show of leaf colour in mid-October*

## The user story

Laura and Donal are joint owners in a specialist horticultural business based in rural Roscommon. Their main business is in growing and selling wholesale high-value shrubs and flowering plants, mostly to garden centres all over Ireland and Europe.



### Specialist growers

Their company, **Witch Hazel**, is named after the beautiful group of plant species (all grouped under the genus name _Hamamelis_) upon which the couple made their reputation soon after leaving agricultural college. This genus, whose English-language common name is the Witch Hazel, is a slow-growing shrub that produces masses of delicate yellow, orange or red flowers in mid to late winter and spectacularly coloured leaves in autumn. Most of the cultivars grown by Laura and Donal are descended from _Hamamelis x intermedia_, a cross between Japanese witch hazel (_H. japonica_) and Chinese witch hazel (_H. mollis_), but they also grow for sale cultivars of both parent species (i.e., _H. mollis_ and _H. japonica_). All the plants they grow for sale are propagated by means of grafting buds onto the root stock of a third Hamamelis species, _H. virginiana_ or the American Witch Hazel, which doesn't produce either such beautiful winter flowers or such rich autumn leaf colours as any of its East Asian relatives, but provides a hardy root upon which the its more spectacular relatives can thrive. Another advantage of the procedure is that grafted plants will begin flowering several years younger than plants grown on their own root. The labour cost of producing such grafts is what drives the high market value of garden varieties of Witch Hazel on the wholesale and retail markets.


### The plant production workflow

The two owners have jointly developed a highly efficient way of producing such grafted plants. They have a plentiful standing stock of _H. virginiana_, which they propagate using soft-wood cuttings over the course of the Roscommon winter (year zero). The following spring (around about April), they pot up all the cuttings that have rooted successfully and grow them on until they become small, one-year-old pot plants. In late winter of year one (usually February or early March), they graft onto those young plants (referred to as 'rootstocks') the carefully selected buds (which they call 'scions') from their lovingly tended stock of mature cultivar specimens. The resulting grafted plants are then cared for for at least five years before being offered on the market as small bushes (about 50 to 60 cm tall) still in their original oblong three-litre pots. Once the graft has sealed successfully (there may be considerable losses during the period before the graft seals), care for the small plants becomes a good deal less labour-intensive; the work mostly involving keeping them watered (and free of waterlogging), controlling weeds, and removing and disposing of any losses. The vast majority of the work is required for production and potting of the rootstocks from cuttings and at the grafting stage, as well as in the early aftercare of the new grafts. For this reason, the profitability of each year's production depends on knowing how many plants to graft to satisfy demand a few years down the road, and making sure at the outset that they have enough healthy, potted-up root stocks available on which they can graft all the plants they want every year just as winter is beginning to turn to spring.

Donal explained the workflow in Hamamelis production as follows:
- Green woody H. virginiana cuttings are taken in October/November and inserted with regular spacing in open ground (in a sheltered spot and well-drained, gritty and nutrient-poor soil). Those of cuttings that successfully produce roots are potted up in April/May of the following year. Donal tells me that most losses at this stage are incurred in the form of cuttings that fail to root. That's why they take many more cuttings than will eventually be needed. Rooted cuttings not needed for grafting almost a year later (in Year Zero &ndash; see below) are disposed of without ever being potted up. The couple always try to avoid such wastage, although after years over which few rooted cuttings die, there will often be a surplus of rootstocks ready for grafting. Such surplus rootstocks are rarely still suitable for grafting a year later, so they are disposed of.
- As compost and pots (the only other critical inputs) can be ordered at short notice, neither input represents a bottleneck risk for the couple. They don't need these variables to be modelled in the program for the moment.
- The production process currently does not involve any repotting; each successfully rooted cutting is potted into its final three-litre pot.
- The rooted, potted-up cuttings of H. virginiana are grown on for a full season and are readied for grafting in February to March of Year One (the precise time of year depends on the weather and the seasonal maturity of the scion buds to be grafted onto them).
- The couple can't recall any year in which there was any shortage of scion buds, though actually selecting, cutting and preparing them correctly is a painstaking and time-intensive job.
- Actually joining the scions onto the rootstocks is also a highly skilled and time-consuming task. But here again, the tools and materials required (a grafting knife, grafting tape and horticultural wax) are easy to obtain at short notice.
- After the hard graft of grafting has been completed, the new baby plants are carefully placed in intensive care in the couple's polyethylene tunnel for about two months, during which time there may be substantial losses (up to 40%) through failure of the graft to fuse.
- Once that period is over, the plants are taken outside to a sheltered spot on open ground. Their three-litre pots are buried to the neck in humus-rich soil to reduce the risk of drying out. They will remain there for several years until they're large enough for sale. The youngest cohort offered for sale are in their fifth year from year zero. All the plants are watered, weeded, cared for and re-spaced where required, and any losses (which are generally much less frequent once they have survived year one) are removed intermittently and disposed of.
- Unsold fifth-year plants may be repotted and grown on for sale as more mature specimens in subsequent years. This part of the production process has not yet been modelled in the witch-hazel app.
- Each year's production is kept together and grouped by cultivar, but particular plants that are growing particularly well or particularly slowly may be promoted or demoted to another year cohort where appropriate.

Both Laura and Donal often referred to "Year Zero", by which they meant the calendar year in which they actually do the biggest job in the whole production process: actually making the grafts. You could say that they make rootstock cuttings in autumn of Year Zero Minus One, pot up the successfully rooted cuttings in the spring of Year Zero and do the grafting work in February to early March of Year One. The plants thus produced are thereafter classified by age, calling newly grafted plants "year-one plants", which become "year-two plants" at grafting time every year, with year-two plants becoming year-three plants and so on. With a few exceptions, the plants are not ready for sale until they reach Year Five. 

- - -

## What the customer wants

Laura and Donal have asked me to provide them with a simple command line program to help them plan their propagation, grafting and crop management activities while the plants are being grown on for sale. They don't need any fancy graphics or sophisticated GUI, but they do want the program to be fairly simple to use and maintain, and to guide them through each step of the workflow. They want it to serve the following purposes:
- maintain a list of the stock of Hamamelis plants destined for sale wholesale to garden centres and the like, grouped according to age/size and cultivar
- plan and keep track of the process of producing the cuttings for rootstocks, potting them up and growing them on
- update and show the number of potted rootstocks available every year for grafting
- plan the numbers of each cultivar to be used as scions on the root stocks, warning the couple when there are not enough rootstocks to execute the plan in full
- record throughout the year any losses incurred by cultivar and age (for whatever reasons) and any acquisitions (whether by purchase from a third party or by any of a number of horticultural tricks that the couple have up their sleeves)
- show the flexibility to allow the couple to hold back particularly slow-growing specimens for another year and to reclassify plants that have grown particularly well in a particular year so that they effectively skip a year. Since they tend to do this sort of work whenever they get time throughout the year, they should be able to do this intermittently at any time of year.

N.B.: They currently grow six different cultivars for sale (but might expand their range in the future if they can find attractive cultivars free of plant breeders' rights fees). The system should be easy to adjust in order to add new cultivars to the workflow.

"That's enough for the moment," said Laura, "once we have a system that can do those things, we'll be able to plan better. And once we've seen the benefits we'll have a look at what might still need doing. The main thing we need right now is something that keeps our records straight, so we can analyse like with like when looking for areas where we can improve our efficiency. We can start looking at what we still need to do upstream and downstream of the actual production process ... maybe even in the sales area ... after we've bedded in our new system. And we can also have a look at applying the system to our rose production business if it looks like it might save us a bit of time and money there too. But let's not get ahead of ourselves."

- - -

## System design

![Some flow charts portraying a selection of important witch-hazel worklflows](assets/readme_assets/hamamelis.gif)

*Some flow charts portraying a selection of important witch-hazel worklflows*



Accordingly, I prepared a series of outline flow charts in consultation with Laura and Donal on the basis of the needs they described to me. Once they'd approved the charts, I began thinking about actually programming the various functionalities.

For simplicity's sake, and because I thought the data was not enormously complex, I decided to store it all on a single google spreadsheet, which I simply named 'hamamelis'. It contains three worksheets.
- rootstock
- grafts-year-zero
- plants

The data should be read as follows.

### The 'rootstock' worksheet 
- The first column (A) is a label to tell the witch-hazel program what year the figures in the corresponding row refer to. The current year is at the top. 
- The top figure in the second column (B) shows the number of cuttings that the couple plan to take in the autumn of the current year minus one. The figures below that represent the number of cuttings that the couple planned to take in each relevant year minus one in the past.
- The third column (C) shows the number of cuttings that they actually took in the relevant year.
- The fourth column (D) shows the number of cuttings that rooted successfully and were potted up during the spring. It is a representation of work done, and does not increase when immature rootstocks are acquired from an outside source, nor does it reduce when such rootstocks are lost through disease or damage, or when they are used up to in the grafting process. Notice the change in nomenclature: successfully rooted _cuttings_ begin to be referred to as _rootstocks_ as soon as they've planted in pots (potted up).
- The fifth column (E) contains at most two non-zero values: one in E1, which represents the figure for rootstocks in stock this year to become available for use as next year as rootstocks. It is equivalent to the value in D1 minus any losses and plus any acquisitions. The value in E2 represents the total number of rootstocks now available for use in this year's grafting. Every time a grafting session is recorded, this value goes down by the number of grafts made. 
Any rootstocks left over after the year's grafting campaign is finished remain in the system until they are set to zero upon creation of a new year. The reason for this is that two-year-old rootstocks will rarely be suitable for grafting when the time comes around again in the new year. They are generally physically disposed of (recycling the pots and compost) when the opportunity arises during the course of the new year.
![The rootstock worksheet the end of a year](assets/readme_assets/rootstock_old_year.png)

*The rootstock worksheet as it might look towards the end of a growing year*

### The 'grafts-year-zero' worksheet
The grafts-year-zero worksheet contains two more columns than the number of cultivars of _Hamamelis_ currently cultivated by the Witch Hazel nursery. 
- The first column identifies the year to which the data in the corresponding row refers.
- The second column tells any human or machine reader whether the figures in the corresponding row refer to numbers of grafted plants that the couple originally planned ('planned'), that they actually made ('grafted') and that they currently have in stock ('stock'). The 'stock' figure for the current year refers to the number of plants of the given category currently in stock (i.e., the number of grafts originally made of the relevant cultivar in the current year minus any losses recorded since then, plus any gains since then). When a new year is created, the relevant numbers are passed into the 'plants' worksheet, three new rows are created for the current year and the figures for 'planned' and 'grafted' for previous years can no longer be edited. 
- Each subsequent column gives the figures described above for the cultivar labelled in the topmost cell.
![The grafts-year-zero worksheet the end of a year](assets/readme_assets/grafts-year-zero_old_year.png)

*The grafts-year-zero worksheet as it might look towards the end of a growing year*

### The 'plants' worksheet
The plants worksheet is a little simpler. It shows the current stocks of each cultivar of each age group &ndash; i.e.: the total number of grafts of that age currently in stock, adjusted according to the losses and gains subsequently recorded by the couple in the witch-hazel program using the record_loss, record_gain, hold_back and bring_forward functions (see below).
![The plants worksheet towards the end of a year](assets/readme_assets/plants_old_year.png)

*The plants worksheet as it might look towards the end of a growing year*


- - - 

## The program's original workflow and the technical issues with the technology used

At the outset of programming, I wanted the app to call a run.py file in the usual way but to attach an argument after a blank space on the command line, depending on the task that the user wished to do at that time. Unfortunately, the Heroku pseudo terminal on which the app is destined to run does not allow the use of command-line arguments (or at least I have been unable to find a way of implementing such a command-line-argument-based design). Due to some issues with my implementation of the Heroku architecture, I discovered this limitation rather late in the day. As a result I was forced redesign the app at the last-minuteto follow a different (and in my opinion much less elegant) logic. Originally, the user would have typed the run.py file name on the terminal, followed by a space and then a short string indicating what they wanted the app to do.

For example, they would have typed ``run.py plan_cuttings`` to plan their campaign of taking and preparing cuttings. But the Heroku pseudo-terminal automatically runs the ``run.py`` file without any arguments immediately upon opening, so everything must be based on an argument-free initial call. The description of the workflow below is based on my last-minute changes due to this difficulty. It should be understood, however, that workflow described below was not my first choice.

The time used dealing with this problem at the last minute may have affected some of the finishing work on the program. For example, it was my original intention to connect each task to the next in their logical order, asking the user if they wished to go on to the next task. Sadly, the user now needs to restart the program every time they wish to complete a new task. 

- - - 

## The program's workflow:

### Seasonal tasks in order
Typically towards the autumn of every year, the owners will want to close out the figures they have entered over the previous year, begin a new year and start work on planning their campaign of taking H. Virginiana cuttings. They begin this task by running the app and choosing option ``1`` (``Create new year/Close out current year``). This function adds the required new lines for the new current year on each worksheet, and copies the data on graft stocks for the old current year to date from the ``grafts-year-zero`` worksheet to the ``plants`` worksheet. This has the effect of putting the data for the previous year out of reach of the seasonal tasks.

Also within the ``Create new year/Close out current year`` function, users can choose either to enter the figure for cuttings that they anticipate taking this year or opt to leave that job for later.

![The rootstock worksheet straight after the user executes the ``Create new year/Close out current year`` function](assets/readme_assets/rootstock_new_year.png)

*The rootstock worksheet straight after the user executes the ``Create new year/Close out current year`` function. Note that the user has chosen to enter a value for planned cuttings of 2800. That value can be changed at any time during the year by running Option 2 ``Plan this year's cutting campaign``.*

- - -

![The grafts-year-zero worksheet straight after the user executes the ``Create new year/Close out current year`` function](assets/readme_assets/grafts-year-zero_new_year.png)

*The grafts-year-zero worksheet straight after the user executes the ``Create new year/Close out current year`` function.*

- - -

![The plants worksheet straight after the user executes the ``Create new year/Close out current year`` function](assets/readme_assets/plants_new_year.png)

*The plants worksheet straight after the user executes the ``Create new year/Close out current year`` function.*

Then, whether or not they have entered a figure for planned cuttings, they can run app option ``2`` ``Plan this year's cutting campaign`` to revise that figure. If they have already recorded a figure for cuttings actually made, they are given a warning to tell them that the cutting campaign has already started and asked to confirm whether they want to replace the planned figure with a new total. The new figure is not added to the old one; it simply replaced it. This is the case with all planning functions.

When they run app option ``3`` (``Record cuttings taken``), they are asked to enter a number of cuttings actually taken. They are given the already existing figure for cuttings taken and warned not to enter a number for cuttings unless that number has already been physically taken, prepared and inserted in the cuttings bed. It tells the user when the number of cuttings taken exceeds the number of cuttings planned.

The new figure entered by the user is added to the already existing number. In the nursery, the cuttings campaign takes several days, the owners typically entering the day's figure for cutting production in the evening of the relevant day. The user receives a message on the command line when the figure exceeds the planned figure. The logic behind the difference between planned figures (each of which simply replaces the previous one) and the actually taken figures is that the latter are usually totted up for each day in the cutting/grafting campaigns, and the user should expect the app to remember the numbers recorded from previous days.

Option ``4`` (``Record rooted cuttings potted up``) instructs the user to enter a figure for the number of successfully rooted cuttings actually potted up. As another figure indicating for work actually done (usually daily), it functions in a similar cumulative way to option ``3`` (``Record cuttings taken``, as do all functions designed to record work actually done). It informs the user when the total number of potted cuttings recorded has reached or exceeded the total number of cuttings taken.

Option ``5`` (``Plan grafts for this year``) displays the number of rootstocks (i.e. the figure for cuttings successfully potted up in the previous year, minus losses, plus gains) asks the user what cultivar they want to graft and how many grafts they want to make of that cultivar. The function keeps a running total of the rootstocks required and issues a notification/warning if and when the total number of planned cuttings exceeds the number of rootstocks available. As the function is about planning numbers, new numbers simply overwrite old ones the second and subsequent time the user runs the option for a particular cultivar.

Option ``6`` (``Record grafts taken``) argument asks the user which cultivar they want to record grafts for. The owners typically enter the day's figure for graft production separately for each cultivar in the evening of the relevant day. The user receives a message on the command line if and when any figure exceeds the associated planned figure. As for other options recording work actually done, new figures are added to old figures creating a new total. Each time a grafting session is recorded in this way, the current stock of rootstocks is reduced by the corresponding amount.

_N.B.: In order to record total work done separately from current stocks (i.e., total work done minus losses plus gains) all the following numbers are recorded separately:_
- _cuttings taken vs total rootstocks_
- _grafts taken vs total plants in stock (recorded for each cultivar separately)_

### ad-hoc tasks
Option ``7`` (``Record plant losses``) asks the user the cultivar and age of the plants they want to record as lost (including year-zero rooted cuttings), showing them the current figure for that cultivar and age. The user is prevented from entering a number greater than that figure. It gives a confirmation message before writing the data entered by the user to the spreadsheet.

Option ``8`` (``Record plant gains``) works similarly, adding instead of subtracting. It does not impose any restriction on the number added.

Option ``9`` (``Hold over plants for one year``) asks the user to identify the cultivar and age of the plants they want to hold back, shows the user the current number of those plants and subtracts the number given by the user from the current age category, adding the same number to the category one year younger. As with ``record_loss``, the user can't move more plants than the recorded number for the relevant category in any direction. The system also prevents the user from entering a value less than two, as it is impossible to hold year-one plants over to year-zero. The year zero values are not recorded in the ``plants`` worksheet at all. They have ther own worksheet (``grafts-year-zero``)

Option ``10`` (``Bring plants forward one year``) does the same in the opposite direction. Again, the appropriate restriction on numbers moved applies. In contrast to the previous option, the user can choose the value ``1`` for year cohort, as the same problem doesn't apply here.

In exceptional cases where the user wishes to hold back or bring forward a number of plants by more than a year, they must run the relevant process twice.

Unfortunately, due to the time restraints, I was unable to implement option ``11`` (``Add new cultivar``). I have, however prepared much of the groundwork to introducing it in the future. For example, I have implemented a system by which the functions that involve cultivars identify those cultivars dynamically.

Reductions in plant stocks through _sales_ are not recorded in this app. The couple tell me that this may be the next step once they have this work planning system bedded in.

The same can be said of a number of other parts of the nursery workflow.

##

### Numerical vs string entries
Aside from the restrictions on user entries mentioned above, the user is not allowed to enter either a negative number or an entry that cannot be rendered as an integer.

---
## Programming philosophy

Being an app generally modelling a procedural series of steps, little use was made of the concepts of OOP in its design. Few custom classes were specifically designed for the app. This was deliberate and should not be taken for any absence of understanding of the basic concepts of OOP.  It may, however, be useful to look at other programs created for a similar purpose when the time comes to refactor this code, and to use the advantages of OOD/OOP to make the code more efficient and more comprehensible.

##

Todo
logging
reasons for loss/gain
disposing of excess rooted cuttings
wipeouts
stuff that's more than zero
loss/acquisition of year-zero grafted plants
storage and committing
reporting
refactoring
adding new cultivars
program continuity
escape errors due to badly formatted spreadsheets
authentication for access to spreadsheets
heroku setup
heroku problems