
maxsum([HA|[]],HA).
maxsum([HA|TA],B):- HA>0,
	B1 is B+HA,
	maxsum(TA, B1).
