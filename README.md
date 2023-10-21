![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The user story

Laura and Donal are joint owners in a specialist horticultural business based in rural Roscommon. Their main business is in growing and selling wholesale high-value shrubs and flowering plants, mostly to garden centres all over Ireland and Europe.

- - -
## Specialist growers

Their company, "Witch Hazel", is named after the beautiful group of plant species (all grouped under the genus name Hamamelis) upon which the couple made their reputation soon after leaving agricultural college: the witch hazel, a slow-growing shrub that produces beautiful yellow, orange or red flowers in mid to late winter and spectacularly coloured leaves in autumn. Most of the cultivars grown by Laura and Donal are descended from Hamamelis x intermedia, a cross between Japanese witch hazel (Hamamelis Japonica) and Chinese witch hazel (Hamamelis Mollis), but they also grow for sale both parent species (H. mollis and H. Japonica). All the plants they grow for sale are propagated by means of grafting buds onto the root stock of a third Hamamelis species, **H. Virginiana** or American witch hazel, which doesn't produce either such beautiful winter flowers or such rich autumn leaf colours as any of its East Asian relatives, but provides a hardy root upon which the its more spectacular relatives can thrive. Another advantage of the procedure is that grafted plants will begin flowering several years younger than plants grown on their own root. The labour cost of producing such grafts is what drives the high market value of garden varieties of witch hazel on the wholesale and retail markets.

- - -

## The plant production workflow

The two owners have jointly developed a highly efficient way of producing such grafted plants. They have a plentiful standing stock of Hamamelis Virginiana, which they propagate using soft-wood cuttings over the course of the Roscommon winter (year zero) and grow on until they become small, one-year-old pot plants. In late winter of year one, they graft onto those plants (referred to as 'root stocks') carefully selected buds (which they call 'scions') from their lovingly tended stock of mature cultivar specimens. The plants are then cared for for up to five years before being offered on the market as small bushes (about 50 to 60 cm tall) in oblong three-litre pots. Once the graft has sealed successfully (there are considerable losses during the period before the graft seals), care for the small plants becomes a good deal less labour-intensive; the work mostly involving keeping them watered (and free of waterlogging), controlling weeds, and removing and disposing of any losses. The vast majority of the work is required for production and potting of the root-stocks from cuttings and at the grafting stage, as well as in the early aftercare of the new grafts. For this reason, the profitability of each year's production depends on knowing how many plants to graft, and making sure they have enough healthy, potted-up root stocks available on which they can graft all the plants they want to produce every late winter.

Donal explained the workflow in Hamamelis production as follows:
- Green woody H. virginiana cuttings are taken in October/November and inserted with regular spacing in open ground (in a sheltered spot and well-drained, nutrient-poor soil). The cuttings that successfully produce roots are potted up in April/May of the following year. Donal tells me that most losses at this stage are incurred in the form of cuttings that fail to root. That's why they take many more cuttings than will eventually be needed. Rooted cuttings not needed for grafting almost a year later (in Year Zero &ndash; see below) are disposed of without being potted up.
- As compost and pots (the only other critical inputs) can be ordered at short notice, neither represent a bottleneck risk for the couple. They don't need these variables to be modelled in the program.
- The production process does not involve any repotting; each successfully rooted cutting is potted into its final three-litre pot.
- The rooted, potted-up cuttings of H. virginiana are grown on for a full season and are readied for grafting in February to March of Year One (the precise time of year depends on the weather and the seasonal maturity of the scion buds to be grafted onto them).
- The couple can't recall any year in which there was any shortage of scion buds, though actually selecting, cutting and preparing them is a painstaking and time-intensive job.
- Actually joining the scions onto the rootstocks is also a highly skilled and time-consuming task. But here again, the tools and materials required (a grafting knife, grafting tape and horticultural wax) are easy to obtain at short notice.
- After the hard graft of grafting has been completed, the new baby plants are carefully placed in intensive care in the couple's polyethylene tunnel for about two months, during which time there may be substantial losses (up to 40%) through failure of the graft to fuse.
- Once that period is over, the plants are taken outside to a sheltered spot on open ground, in their three-litre pots are buried to the neck in humus-rich soil to reduce the risk of them drying out. They will remain here for several years until they're large enough for sale. They're watered, weeded, cared for and re-spaced where required, and any losses (which are generally much less frequent at this stage) are removed intermittently and disposed of.
- Each year's production is kept together and grouped by cultivar, but plants that are growing particularly well or particularly slowly may be promoted or demoted to another year cohort.

I noticed that both Laura and Donal often referred to "Year Zero", by which they meant the calendar year in which they actually do the biggest job in the whole production process: actually making the grafts. You could say that they make rootstock cuttings in autumn of Year Zero minus two, pot up the successfully rooted cuttings in the spring of Year Zero minus one and do the grafting work in February to early March of Year Zero. The plants thus produced are thereafter classified by age, calling newly grafted plants "year-zero grafts", which become "year-one plants" at grafting time every year, with year-one plants becoming year-two plants and so on. With few exceptions, the plants are not ready for sale until they reach Year Four. 

- - -

## What the customer wants

So Laura and Donal have asked me to provide them with a simple command line program to help them plan their propagation and grafting activities in the wet Roscommon winter. They don't need any fancy graphics or sophisticated GUI, but they do want the program to be fairly simple to use and maintain, and to guide them through each step of the workflow. They want it to serve the following purposes:
- maintain a list of the stock of Hamamelis plants destined for sale wholesale to garden centres and the like, grouped according to age/size and cultivar
- plan and keep track of the process of producing the cuttings for rootstocks, potting them up and growing them on
- update and show the number of potted rootstocks available every year for grafting
- plan the numbers of each cultivar to be used as scions on the root stocks, warning the couple when there are not enough rootstocks to execute the plan in full
- record throughout the year any losses incurred by cultivar and age (for any number of reasons) and any gains (whether by purchase from a third party or by any of a number of horticultural tricks that the couple have up their sleeves)
- show the flexibility to allow the couple to hold back particularly slow-growing specimens for another year and to reclassify plants that have grown particularly well in a particular year so that they effectively skip a year. Since they tend to do this sort of work whenever they get time throughout the year, they should be able to do this intermittently at any time of year

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
The plants worksheet is a little simpler. It shows the current stocks of each cultivar of each age group &ndash; i.e.: the total number of grafts of that age currently in stock, adjusted according to the losses and gains subsequently recorded by the couple in the Witch-Hazel program using the record_loss, record_gain, hold_back and bring_forward functions (see below).


## The program's workflow:

### Seasonal tasks in order
When the owners want to begin planning their campaign of taking H. Virginiana cuttings in the autumn of each year, they create a new year; ordinarily the following year.  You might think of it as buying a calendar for 2024 in the autumn of 2023. They do so by running the program with the argument ``new_year`` (i.e., by typing ``run.py new_year`` and pressing enter), which adds the required new lines for the new current on each worksheet, copying the data on graft stocks for the old current year to date from the ``grafts-year-zero`` worksheet to the ``plants`` worksheet.

They can then choose either to enter the figure for cuttings that they anticipate taking this year or to leave that job for later.

Then, whether or not they have entered a figure for planned cuttings, they can run the program at any time with the ``plan_cuttings`` argument to revise that figure. If they have already recorded a figure for cuttings actually made, they are given a warning to tell them that the cutting campaign has already started and asked to confirm whether they want to add to the planned figure or simply to replace it with a new total.

When they run the program with the ``take_cuttings`` argument they are asked to enter a number of cuttings actually taken. They are given the already existing figure for cuttings taken and warned not to enter a number for cuttings unless that number has already been physically taken and inserted in the cuttings bed.

The new figure entered by the user is added to the already existing number. The cuttings campaign takes several days, the owners typically entering the day's figure for cutting production in the evening of the relevant day. The user receives a message on the command line when the figure exceeds the planned figure.

The ``pot_cuttings`` argument instructs the user to enter a figure for the number of successfully rooted cuttings actually potted up. It works in a similar cumulative way to the ``take_cuttings`` argument. It informs the user if the total number of potted cuttings recorded exceeds the total number of cuttings taken.

The ``plan_grafting`` argument displays the number of rootstocks (i.e. the figure for cuttings successfully potted up in the previous year, minus losses, plus gains) asks the user how many grafts they want to make of each cultivar in turn. The function keeps a running total of the rootstocks required and issues a warning if the total number of planned cuttings exceeds the number of rootstocks available. The planned numbers are only written to the ``grafts-year-0`` worksheet when the numbers for all cultivars have been entered and the user has confirmed the figures entered.

The ``record_grafts`` argument asks the user which cultivar they want to record grafts for. The owners typically enter the day's figure for graft production separately for each cultivar in the evening of the relevant day. The user receives a message on the command line when any figure exceeds the associated planned figure.

### ad-hoc tasks
The ``record_loss`` argument asks the user the cultivar and age of the plants they want to record as lost (including year-zero rooted cuttings) and gives them the current figure for that cultivar and age. The user is prevented from entering a number greater than that figure. It gives a confirmation message before writing the data entered by the user to the spreadsheet.

The ``record_gain`` argument works similarly, adding instead of subtracting, but it does not impose any restriction on the number added.

The ``hold_back`` argument asks the user to identify the cultivar and age of the plants they want to hold back, shows the user the current number of those plants and subtracts the number given by the user from the current age category, adding the same number to the category one year younger.

The ``bring_forward`` argument does the same in the opposite direction. In neither case is the user allowed to enter a number greater than the total number of plants recorded as existing for that age.

In exceptional cases where the user wishes to hold back or bring forward a number of plants by more than a year, they must run the relevant process twice.
