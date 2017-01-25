# Cat-box
Raspberry Pi controlled cat litter box

I developed this project because I wanted to finish a basement and turn it into a comfortable living space.
Unfortunately, the dust from the litter pan covered everything in the room. 

I cut a tunnel in a wall large enough for a cat to walk through and built a large plywood box which I placed on the other 
side of the wall.  I incorporated a 200CFM fan to exhaust the litter dust to the outside of the house via a 4" dryer vent.
The box contains a PIR sensorand white LEDs to provide light inside the box.  A Raspberry Pi monitors the PIR sensor
and triggers the fan motor and lights while a cat is inside the box.  The top of the box is hinged for easy cleaning.

A PWM was used to ramp the LEDs up so they wouldn't startle the cats.

# Future expansion
Report "events" to a cloud service so usage can be monitored and a cleaning schedule can be set up.
