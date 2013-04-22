noun_insp_str = 'Acoustic, Curve, Custard, Hen, Jaw, Bladder, Detail, Output, Polo, Sideboard, Single, Tiger, Fahrenheit, Lettuce, Owner, Parsnip, Path, Resolution, Sardine, Scarecrow, Badger, Butter, Coast, Difference, Jam, Loaf, Methane, Sense, Stew, Apology, Carpenter, Eyeliner, Form, Sister, Handsaw, Save, Softdrink, Study, Tent, Bath, Cast, Creature, Freighter, Nail, Pie, Repair, Request, Throat, Wolf, Ornament, Pan, Supply, Uncle, Wallet'

verb_insp_str = 'Elicit, Save, Solve, Draw, Forecast, Execute, Travel, Research, Assume, Compile, Upheld, Differentiate, Sustain, Code, Fix, Replace, Import, Coordinate, Undertook, Supply, Devote, Secure, Customize, Disseminate, Resolve, Institute, Assist, Intervene, Investigate, Address, Care, Correlate, Model, Enumerate, Discriminate, Outline, Diagnose, Cooperate, Search, Accomplish, Teach, Interpret, Verify, Explore,  Pioneer, Prevent, Visualize, Check, Establish, Distribute, Unify, Foster, Bargain, Renew, Expand, Upgrade, Experiment, Monitor, Moderate'

adj_insp_str = 'Dusty, Superb, Weak, Female, Internal, Nostalgic, Uptight, Habitual, Woozy, Quiet, Thirsty, Fearful, Gleaming, Happy, Vagabond, Ill, Many, Deeply, Luxuriant, Present, Tall, Swanky, Clear, Tired, Fluffy, Blue-eyed, Average, Obscene, Parched, Uninterested, Important, Wooden, Late, Scattered, Materialistic, Alluring, Square, Sweltering, Capable, Gruesome, Maniacal, Periodic, Dashing, Whimsical, Overwrought, Future, Aquatic, Protective, Polite, Undesirable, Orange, Useful, Rich'

adv_insp_str = 'Richly, Honorably, Ably, Magically, Abundantly, Nondescriptly, Hotly, Deafeningly, Viciously, Ferociously, Furiously, Hilariously, Basically, Parsimoniously, Royally, Readily, Strangely, Jokingly, Facetiously, Encouragingly, Enviously, Earsplittingly, Peacefully, Inquisitively, Tastefully, Incredibly, Beneficially, Defiantly, Tensely, Greatly, Firstly, Strongly, Gregariously, Prettily, Interestingly, Simply, Distinctly, Swiftly'

def fix(s):
	slist = s.split(',')
	for i in range(len(slist)):
		if slist[i][0] == ' ':
			slist[i] = slist[i][1:]
	return slist

print(fix(noun_insp_str))
print(fix(verb_insp_str))
print(fix(adj_insp_str))
print(fix(adv_insp_str))


