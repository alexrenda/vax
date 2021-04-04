# Rite Aid covid scanner usage

First, check availability and find nearby locations at https://www.riteaid.com/pharmacy/apt-scheduler. You'll need to keep this tab open since this is where you'll actually schedule the appointment. You should get to a screen that looks like this:

![Step 1](/images/step1.png)

The, run the script with `python riteaid.py`, which will scan for Rite Aid locations within 50 miles of 95070 (the zip code and radius are configured in `riteaid.py`)

When an available slot is found, the script will print something like:

`23:25:42 available: #5976 at 2620 El Camino Real, Santa Clara CA 95051`

which means that there is *possibly* a slot available at store #5976. 
I haven't figured out how to find whether the slot is for Pfizer, Moderna, or J&J, but the Rite Aid website says.
On a mac, the script will also say "available" out loud.

When the script says that a slot is available, go to the open tab with the Rite Aid pharmacies, select the store number that the script was available, then click Next. 

Occasionally at this you will be able to select a time and schedule an appointment, looking like this:

![Step 2](/images/step2.png)

In this case, click the time and click next as soon as possible to get the slot.

Sometimes you will get a screen that looks like this, with no time slots:

![Step 3](/images/step3.png)

To fix this, click on the date on the left. The slot should then pop up:

![Step 3](/images/step3.png)
![Step 4](/images/step4.png)

However, more often than not, when you click "Next" the website will end up saying:

`Apologies, due to high demand, there are currently no appointment times available at this Rite Aid. Please select a different store or check again another day.`

If that happens, then just wait for a different appointment slot to be available (or just keep clicking "Next", which does actually check every time you click it, though probably someone has already taken the slot).

