![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The user story

Laura and Donal are joint owners in a specialist horticultural business based in rural Roscommon. Their main business is in growing and selling wholesale high-value shrubs and flowering plants, mostly to garden centres all over Ireland and Europe.

- - -
## Specialist growers

Their company, "Witch Hazel", is named after the beautiful group of plant species (all grouped under the genus name Hamamelis) upon which the couple made their reputation soon after leaving agricultural college: the witch hazel, a slow-growing shrub that produces beautiful yellow, orange or red flowers in mid to late winter and spectacularly coloured leaves in autumn. Most of the cultivars grown by Laura and Donal are descended from Hamamelis x intermedia, a cross between Japanese witch hazel (Hamamelis Japonica) and Chinese witch hazel (Hamamelis Mollis), but they also grow for sale both parent species (H. mollis and H. Japonica). All the plants they grow for sale are propagated by means of grafting of their buds onto the root stock of a third Hamamelis species, H. Virginiana or American witch hazel, which doesn't produced either such beautiful flowers as any of its East Asian relatives, but provide a hardy root upon which the its more spectacular relatives will thrive. Another advantage of the procedure is that grafted plants will begin flowering several years younger than plants grown on their own root. The labour cost of producing such grafts is what drives the high market value of witch hazel in the garden centre industry.

- - -

## The production workflow

The two owners have jointly developed a highly efficient way of producing such grafted plants. They have a plentiful standing stock of Hamamelis Virginiana, which they propagate using soft-wood cuttings over the course of the Roscommon winter (year zero) and grow on until they become small, one-year-old pot plants. In late winter of year one, they graft onto those root stocks carefully selected buds (which they call "scions") from their lovingly tended stock of mature cultivar specimens. The plants are then cared for for up to five years before being offered on the market as small bushes (about 50 to 60 cm tall) in oblong three-litre pots. Once the graft has sealed successfully (there are considerable losses during period before the graft seals), care for the small plants is not very labour-intensive, the work mostly involving keeping them watered (and free of waterlogging), keeping down weeds, and removing and disposing of any losses. The vast majority of the work is needed at the grafting stage and the early care thereafter. For this reason, the profitability of each year's production depends on knowing how many plants to graft, and making sure they have enough potted root stocks available for all the plants they want to produce each year.

Donal explained the workflow in Hamamelis production as follows:
- Green woody H. virginiana cuttings are taken in October/November of year zero minus one in open ground (in a sheltered spot). The cuttings that have rooted are potted up in April of year zero. Donal tells me that most losses are incurred in the form of cuttings that fail to root. That's why they take many more cuttings than will eventually be needed. Rooted cuttings not needed for grafting in Year One are disposed of without being potted up.
- As compost and pots (the only other critical inputs) can be ordered at short notice, neither represent a bottleneck risk for the couple.
- There is no need for repotting, each rooted cutting is potted into its final pot.
- The rooted, potted-up cuttings of H. virginiana are grown on for a full season and are readied for grafting in February to March (depending on the weather and the maturity of the scion buds).
- They can't recall any year in which there was any shortage of scion buds, though actually cutting and preparing them is a painstaking and time-intensive job.
- Actually fusing the scions onto the rootstock is also a highly skilled and time-consuming tasks. Again, the tools and materials required (grafting tape and horticultural wax) are easy to obtain at short notice.
- After the hard graft of grafting has been completed, the new babies are put into intensive care in the couple's polyethylene tunnel for about two months, during which time losses may be substantial (up to 40%).
- Once that period is over, the plants are taken outside to a sheltered spot on open ground, in their original three-litre pots buried to the neck in humus-rich soil to reduce the risk of drying out, where they remain for several years until they're ready for sale. They're watered, weeded and cared for, and any losses (which are generally much less frequent at this stage) are renoved intermittently.
- Each year's production is kept together and grouped by cultivar, but plants that are growing particularly well or particularly slowly may be promoted or demoted to another year.


## What the customer wants

So Laura and Donal have asked me to provide them with a simple command line program to help them plan their propagation and grafting activities in the wet Roscommon winter. They don't need any fancy graphics or sophisticated GUI, but they do want the program to be fairly simple to use and maintain, and to guide them through each step of the program's task. They want it to do the following:
- maintain a list of the stock of grafted plants destined for sale in the nursery, grouped according to age/size and cultivar
- show the number of root-stock plants available every year for grafting
- plan the numbers of each cultivar to be used as scions on the root stocks, warning the couple when potted root stocks are insufficient
- they currently grow six different cultivars for sale (but might expand their range if they can find good cultivars free of plant breeders' rights)
- record throughout the year losses incurred by cultivar and age (for any number of reasons) and any gains (usually by purchase from a third party)
- show the flexibility to allow the couple to hold back particularly slow-growing specimens for another year and to reclassify plants that have grown particularly well in a particular year so that they effectively skip a year. Since they do this sort of work whenever they get time throughout the year, they should be able to do this intermittently at any time of the year.

"That's enough for the moment," said Laura, "once we have a system that can do those things, we'll be able to plan better. And then we'll have a look at what might still need doing. The main thing we need is something that keeps our records straight, so we can analyse like with like when looking for spots where we can improve our efficiency. We can start looking at what we still need to do upstream and downstream of the actual production process after we've bedded in your new system."


## System design

So I prepared a series of outline flow charts in consultation with Laura and Donal on the basis of the needs they described to me. Once they'd approved the charts, I began thinking about the actual programming of the functionality.

For simplicity's sake, and because the data was not hugely complex, I decided to store it all on a single google spreadsheet, opting to include one page for each growing year (from zero to four).
The year zero records the number of ready rooted and potted cuttings available towards February and March of year zero.






This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
