from user import User,Driver,Rider
from ride import Ride,RideMatching,RideRequest,RideSharing
from vehicle import Vehicle,Car,Bike

niye_jao = RideSharing('Niye Jao')
rahim = Rider('Rahim Khan','rahim@gmail.com',94384013434,'Taltola',2000000)
niye_jao.add_rider(rahim)
kolimia = Driver('Koli Mia','fulkoli@gmail.com',9848593054,'Onk dhur',0)
niye_jao.add_driver(kolimia)

