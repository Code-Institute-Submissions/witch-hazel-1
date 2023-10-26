![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The user story

Laura and Donal are joint owners in a specialist horticultural business based in rural Roscommon. Their main business is in growing and selling wholesale high-value shrubs and flowering plants, mostly to garden centres all over Ireland and Europe.

- - -

## Specialist growers

Their company, "Witch Hazel", is named after the beautiful group of plant species (all grouped under the genus name Hamamelis) upon which the couple made their reputation soon after leaving agricultural college: the Witch Hazel, a slow-growing shrub that produces masses of delicate yellow, orange or red flowers in mid to late winter and spectacularly coloured leaves in autumn. Most of the cultivars grown by Laura and Donal are descended from Hamamelis x intermedia, a cross between Japanese witch hazel (Hamamelis Japonica) and Chinese witch hazel (Hamamelis Mollis), but they also grow for sale both parent species (i.e., H. mollis and H. Japonica). All the plants they grow for sale are propagated by means of grafting buds onto the root stock of a third Hamamelis species, **H. Virginiana** or American Witch Hazel, which doesn't produce either such beautiful winter flowers or such rich autumn leaf colours as any of its East Asian relatives, but provides a hardy root upon which the its more spectacular relatives can thrive. Another advantage of the procedure is that grafted plants will begin flowering several years younger than plants grown on their own root. The labour cost of producing such grafts is what drives the high market value of garden varieties of witch hazel on the wholesale and retail markets.

- - -

## The plant production workflow

The two owners have jointly developed a highly efficient way of producing such grafted plants. They have a plentiful standing stock of Hamamelis Virginiana, which they propagate using soft-wood cuttings over the course of the Roscommon winter (year zero). The following spring (around about April), they pot up the successfully rooted cuttings and grow them on until they become small, one-year-old pot plants. In late winter of year one (usually February or early March), they graft onto those young plants (referred to as 'root stocks') carefully selected buds (which they call 'scions') from their lovingly tended stock of mature cultivar specimens. The resulting grafted plants are then cared for for up to five years before being offered on the market as small bushes (about 50 to 60 cm tall) still in their original oblong three-litre pots. Once the graft has sealed successfully (there may be considerable losses during the period before the graft seals), care for the small plants becomes a good deal less labour-intensive; the work mostly involving keeping them watered (and free of waterlogging), controlling weeds, and removing and disposing of any losses. The vast majority of the work is required for production and potting of the root-stocks from cuttings and at the grafting stage, as well as in the early aftercare of the new grafts. For this reason, the profitability of each year's production depends on knowing how many plants to graft to satisfy demand a few years down the road, and making sure at the outset that they have enough healthy, potted-up root stocks available on which they can graft all the plants they want to produce every late winter.

Donal explained the workflow in Hamamelis production as follows:
- Green woody H. virginiana cuttings are taken in October/November and inserted with regular spacing in open ground (in a sheltered spot and well-drained, nutrient-poor soil). The cuttings that successfully produce roots are potted up in April/May of the following year. Donal tells me that most losses at this stage are incurred in the form of cuttings that fail to root. That's why they take many more cuttings than will eventually be needed. Rooted cuttings not needed for grafting almost a year later (in Year Zero &ndash; see below) are disposed of without ever being potted up. The couple always try to avoid such wastage, although after years over which few rooted cuttings die, there will often be a surplus of mature rootstocks.
- As compost and pots (the only other critical inputs) can be ordered at short notice, neither represent a bottleneck risk for the couple. They don't need these variables to be modelled in the program.
- The production process does not involve any repotting; each successfully rooted cutting is potted into its final three-litre pot.
- The rooted, potted-up cuttings of H. virginiana are grown on for a full season and are readied for grafting in February to March of Year One (the precise time of year depends on the weather and the seasonal maturity of the scion buds to be grafted onto them).
- The couple can't recall any year in which there was any shortage of scion buds, though actually selecting, cutting and preparing them is a painstaking and time-intensive job.
- Actually joining the scions onto the rootstocks is also a highly skilled and time-consuming task. But here again, the tools and materials required (a grafting knife, grafting tape and horticultural wax) are easy to obtain at short notice.
- After the hard graft of grafting has been completed, the new baby plants are carefully placed in intensive care in the couple's polyethylene tunnel for about two months, during which time there may be substantial losses (up to 40%) through failure of the graft to fuse.
- Once that period is over, the plants are taken outside to a sheltered spot on open ground, in their three-litre pots are buried to the neck in humus-rich soil to reduce the risk of them drying out. They will remain there for several years until they're large enough for sale. The youngest cohort offered for sale are in their fifth year from year zero. All the plants are watered, weeded, cared for and re-spaced where required, and any losses (which are generally much less frequent at this stage) are removed intermittently and disposed of.
- unsold fifth year plants may be repotted and grown on for sale as more mature specimens in subsequent years. This part of the production process is not yet modelled in the witch-hazel app.
- Each year's production is kept together and grouped by cultivar, but plants that are growing particularly well or particularly slowly may be promoted or demoted to another year cohort.

Both Laura and Donal often referred to "Year Zero", by which they meant the calendar year in which they actually do the biggest job in the whole production process: actually making the grafts. You could say that they make rootstock cuttings in autumn of Year Zero Minus One, pot up the successfully rooted cuttings in the spring of Year Zero  and do the grafting work in February to early March of Year One. The plants thus produced are thereafter classified by age, calling newly grafted plants "year-one grafts", which become "year-two plants" at grafting time every year, with year-two plants becoming year-three plants and so on. With a few exceptions, the plants are not ready for sale until they reach Year Five. 

- - -

## What the customer wants

So Laura and Donal have asked me to provide them with a simple command line program to help them plan their propagation and grafting activities in the wet Roscommon winter. They don't need any fancy graphics or sophisticated GUI, but they do want the program to be fairly simple to use and maintain, and to guide them through each step of the workflow. They want it to serve the following purposes:
- maintain a list of the stock of Hamamelis plants destined for sale wholesale to garden centres and the like, grouped according to age/size and cultivar
- plan and keep track of the process of producing the cuttings for rootstocks, potting them up and growing them on
- update and show the number of potted rootstocks available every year for grafting
- plan the numbers of each cultivar to be used as scions on the root stocks, warning the couple when there are not enough rootstocks to execute the plan in full
- record throughout the year any losses incurred by cultivar and age (for any number of reasons) and any gains (whether by purchase from a third party or by any of a number of horticultural tricks that the couple have up their sleeves)
- show the flexibility to allow the couple to hold back particularly slow-growing specimens for another year and to reclassify plants that have grown particularly well in a particular year so that they effectively skip a year. Since they tend to do this sort of work whenever they get time throughout the year, they should be able to do this intermittently at any time of year.

N.B.: They currently grow six different cultivars for sale (but might expand their range in the future if they can find attractive cultivars free of plant breeders' rights fees). The system should be easy to adjust in order to add new cultivars to the workflow.

"That's enough for the moment," said Laura, "once we have a system that can do those things, we'll be able to plan better. Once we've seen the benefits we'll have a look at what might still need doing. The main thing we need right now is something that keeps our records straight, so we can analyse like with like when looking for areas where we can improve our efficiency. We can start looking at what we still need to do upstream and downstream of the actual production process ... maybe in sales ... after we've bedded in your new system. And we can also have a look at applying the system to our rose production business if it looks like it might save us a bit of time and money there too. But let's not get ahead of ourselves."

- - -

## System design

Accordingly, I prepared a series of outline flow charts in consultation with Laura and Donal on the basis of the needs they described to me. Once they'd approved the charts, I began thinking about the actual programming of the functionalities.

For simplicity's sake, and because the data was not hugely complex, I decided to store it all on a single google spreadsheet, which I simply named 'hamamelis'. It contains three pages.

The data should be read as follows.

### The 'rootstock' worksheet 
- The first column (A) is a label to tell the witch-hazel program what year the figures in the corresponding row refer to. The current year is at the top. 
- The top figure in the second column (B) shows the number of cuttings that the couple plan to take in the autumn of the current year minus one. The figures below that represent the number of cuttings that the couple planned to take in each relevant year minus one in the past.
- The third column (C) shows the number of cuttings that they actually took in the relevant year.
- The fourth column (D) shows the number of cuttings were rooted successfully and potted up during the spring. This figure minus (any losses in the meantime) represents the maximum number of grafts that can be made in February or March of the following year unless the owner can source rooted cuttings of the right quality from a third party in the meantime.
N.B.: Please note that the rootstocks (i.e. successfully rooted cuttings) recorded for, say, the year 2023 are started from cuttings taken in Autumn 2022. The relevant year for rootstocks refers to the year in which they were potted up (i.e. when became rootstocks), not the year in which the cuttings were taken.  Grafts for, say, the year 2024 were grafted onto rootstocks for the year 2023 (i.e. rootstocks that were potted up in the previous year).

### The 'grafts-year-zero' worksheet
The grafts-year-0 worksheet contains two more columns than the number of cultivars of Hamamelis currently cultivated by the Witch Hazel nursery. 
- The first column identifies the year to which the data in the corresponding row refers.
- The second column tells any human or machine reader whether the figures in the corresponding row refer to numbers of grafted plants that the couple originally planned ('planned'), that they actually made ('grafted'), and that they had in stock **at the end of the relevant year** ('stock'), respectively. The 'stock' figure for the current year refers to the number of plants of the given category currently in stock (i.e., the number of grafts originally made of the relevant cultivar in the current year minus any losses recorded since then, plus any gains since then). When a new year is created, the relevant numbers are passed into the 'plants' worksheet, three new rows are created for the current year and the figures for previous years are no longer edited.
- Each subsequent column gives the figures described above for the cultivar labelled in the topmost cell.

### The 'plants' worksheet
The plants worksheet is a little simpler. It shows the current stocks of each cultivar of each age group &ndash; i.e.: the total number of grafts of that age currently in stock, adjusted according to the losses and gains subsequently recorded by the couple in the witch-hazel program using the record_loss, record_gain, hold_back and bring_forward functions (see below).

- - - 

## The program's original workflow and the technical issues with the technology used

At the outset of programming, I wanted the app to call a run.py file in the usual way but to attach an argument after a blank space on the command line, depending on the task that the user wished to do at that time. Unfortunately, the Heroku pseudo terminal on which the app is destined to run does not allow the use of command-line arguments (or at least I have been unable to find a way of implementing such a command-line-argument-based design). Due to some issues with my implementation of the Heroku architecture, I discovered this limitation rather late in the day. As a result I was forced redesign the app at the last-minuteto follow a different (and in my opinion much less elegant) logic. Originally, the user would have typed the run.py file name on the terminal, followed by a space and then a short string indicating what they wanted the app to do.

For example, they would have typed ``run.py plan_cuttings`` to plan their campaign of taking and preparing cuttings. But the Heroku pseudo-terminal automatically runs the ``run.py`` file without any arguments immediately upon opening, so everything must be based on an initial argument-free initial call. The description of the workflow below is based on my last-minute changes due to this difficulty. It should be understood, however, that workflow described below was not my first choice.

## The program's workflow:

### Seasonal tasks in order
Typically towards the autumn of every year, the owners will want to close out the figures they have entered over the previous year, begin a new year and start work on planning their campaign of taking H. Virginiana cuttings. They begin this task by running the app and choosing option ``1`` (``Close out current year``). They then run the app again, this time choosing option ``2`` (``Create new year``), which adds the required new lines for the new current year on each worksheet, and copies the data on graft stocks for the old current year to date from the ``grafts-year-zero`` worksheet to the ``plants`` worksheet. ``2`` cannot be run without first running ``1``.

Within the ``Create new year`` function they can choose either to enter the figure for cuttings that they anticipate taking this year or opt to leave that job for later.

Then, whether or not they have entered a figure for planned cuttings, they can run app option ``3`` argument to revise that figure. If they have already recorded a figure for cuttings actually made, they are given a warning to tell them that the cutting campaign has already started and asked to confirm whether they want to replace the planned figure with a new total. The new figure replaces the old figure. The two are not added together.

When they run app option ``4`` (``take_cuttings``), they are asked to enter a number of cuttings actually taken. They are given the already existing figure for cuttings taken and warned not to enter a number for cuttings unless that number has already been physically taken, prepared and inserted in the cuttings bed. It tells the user when the number of cuttings taken exceeds the number of cuttings planned.

The new figure entered by the user is added to the already existing number. The cuttings campaign takes several days, the owners typically entering the day's figure for cutting production in the evening of the relevant day. The user receives a message on the command line when the figure exceeds the planned figure. The logic behind the difference between planned figures (each of which simply replaces the previous one) and the actually taken figures is that the latter are usually totted up for each day in the cutting/grafting campaigns, and the user should expect the app to remember the numbers recorded from previous days.

Option ``5`` (``pot_cuttings``) instructs the user to enter a figure for the number of successfully rooted cuttings actually potted up. As another figure indicating for work actually done (usually daily), it functions in a similar cumulative way to option ``4`` (``take_cuttings``). It informs the user when the total number of potted cuttings recorded has reached or exceeded the total number of cuttings taken.

Option ``6`` (``plan_grafting``) displays the number of rootstocks (i.e. the figure for cuttings successfully potted up in the previous year, minus losses, plus gains) asks the user what cultivar they want to graft and how many grafts they want to make of that cultivar. The function keeps a running total of the rootstocks required and issues a notification/warning if and when the total number of planned cuttings exceeds the number of rootstocks available. As the function is about planning numbers, new numbers simply overwrite old ones the second and subsequent time the user runs the option for a particular cultivar.

Option ``7`` (``record_grafts``) argument asks the user which cultivar they want to record grafts for. The owners typically enter the day's figure for graft production separately for each cultivar in the evening of the relevant day. The user receives a message on the command line if and when any figure exceeds the associated planned figure. As for other options recording work actually done, new figures are added to old figures creating a new total.

In order to record total work done separately from current stocks (i.e., total work done minus losses plus gains) all the following numbers are recorded separately:
- cuttings taken vs total rootstocks
- grafts taken vs total plants in stock (recorded for each cultivar separately)

### ad-hoc tasks
Option ``8`` (``record_loss``) asks the user the cultivar and age of the plants they want to record as lost (including year-zero rooted cuttings), showing them the current figure for that cultivar and age. The user is prevented from entering a number greater than that figure. It gives a confirmation message before writing the data entered by the user to the spreadsheet.

Option ``9`` (``record_gain``) works similarly, adding instead of subtracting. It does not impose any restriction on the number added.

Option ``10`` (``hold_back``) asks the user to identify the cultivar and age of the plants they want to hold back, shows the user the current number of those plants and subtracts the number given by the user from the current age category, adding the same number to the category one year younger. As with ``record_loss``, the user can't move more plants than the recorded number for the relevant category in any direction.

Option ``11`` (``bring_forward``) does the same in the opposite direction. Again, the appropriate restriction on numbers moved applies.

In exceptional cases where the user wishes to hold back or bring forward a number of plants by more than a year, they must run the relevant process twice.

Reductions in plant stocks through _sales_ are not recorded in this app. The couple tell me that this is the next step once they have this work planning system bedded in.

### Numerical vs string entries
Aside from the restrictions on user entries already mentioned, the user is never allowed to enter either a negative number or an entry that cannot be rendered as an integer.

---
## Programming philosophy

Being an app generally modelling a procedural series of steps, little use was made of the concepts of OOP in its design. Few custom classes were specifically designed for the app. This was deliberate and should not be taken for any absence of understanding of the basic concepts of OOP.  It may, however, be useful to look at other programs created for a similar purpose when the time comes to refactor this code, and to use the advantages of OOD/OOP to make the code more efficient and more comprehensible.

##

Todo
logging
reasons for loss/gain
wipeouts
storage and committing
reporting
refactoring
program continuity
escape errors due to badly formatted spreadsheets
heroku setup
heroku problems