
import models

def testZoneInitWorks():
	myZone = models.Zone('Test Zone', 12)
	assert myZone != None

testZoneInitWorks()