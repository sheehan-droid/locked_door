get 5 cards, random order
1 card played at a time, 1v1 with  enemy
randomize who goes first (may implement a speed rating 1-5 system later on to determine turn order)

at the start of a turn, player chooses to attack atk, df, or hp

if player chooses to attack hp, then player deals dmg == (playeratk) - (enemydf) = (newenemyhp)

if player chooses to attack df, then player deals dmg to (enemydf) == (playeratk/2)
	rollover dmg (before reduction) is dealt to hp

if player chooses to attack atk, 

	then player deals dmg to (enemyatk) == (playeratk/2)
	if enemyatk > playeratk, enemy instantly counters to hp enemyatk - playeratk BEFORE reduction
	if playeratk > enemyatk, rollover dmg is dealt to hp == rolloveratk - enemydf
		if rollover (before reduction) does not exceed enemydf, no dmg is dealt to hp

example battles:

player atk 4, df 3, hp 13
enemy atk 3, df 4, hp 13

player goes first

player attacks hp, deals 0 dmg
enemy attacks hp, deals 0 dmg

player attacks enemydf, deals 2 dmg, enemy df now 2
enemy attacks playeratk, deals 1 dmg, player atk now 3

current stats: player atk 3, df 3, hp 13
				enemy atk 3, df 2, hp 13

player attacks enemydf, deals 1 dmg to enemydf, 1 dmg to enemyhp
enemy now atk 3, df 1, hp 12

enemy attacks playeratk, deasl 1 dmg to playeratk,
player now atk 2, df 3, hp 13
 
current stats player atk 2, df 3, hp 13
			enemy atk 3, df 1, hp 12

player atk enemydf deals 1 dmg to df and hp
enemy atks player atk, deals 1 dmg

current player atk 1, df 3, hp 13



