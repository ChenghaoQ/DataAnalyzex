

airliner = [('CRJ', 'CRJ', 'CANADAIR RIGIONAL JET', 'JET', '86'),
 ('M11', 'MD-11', 'MCDONNELD DOUGLAS MD-11', 'JET', '409'),
 ('M82', 'MD-82', 'MCDONNELD DOUGLAS MD-82', 'JET', '165'),
 ('M90', 'MD-90', 'MCDONNELD DOUGLAS MD-90', 'JET', '187'),
 ('TU5', '154', 'TUPOLEV 154', 'JET', '180'),
 ('YK2', '42', 'YAKOVLEV YAK 42', 'JET', '120'),
 ('YN7', 'Yun-7', 'YUN-7', 'TURB', '48'),
 ('143', '146-300', 'BRITISH AEROSPACE 146-300', 'JET', '112'),
 ('146', '146', 'BRITISH AEROSPACE 146', 'JET', '112'),
 ('310', 'A310', 'AIRBUS INDUSTRIE A310', 'JET', '246'),
 ('312', 'A310-200', 'AIRBUS INDUSTRIE A310-200', 'JET', '246'),
 ('AB3', 'A300', 'AIRBUS INDUSTRIE A300', 'JET', '317'),
 ('AB6', 'A300-600', 'AIRBUS INDUSTRIE A300-600', 'JET', '317'),
 ('313', 'A310-300', 'AIRBUS INDUSTRIE A310-300', 'JET', '222'),
 ('319', 'A319', 'AIRBUS INDUSTRIE A319', 'JET', '134'),
 ('320', 'A320', 'AIRBUS INDUSTRIE A320', 'JET', '180'),
 ('321', 'A321', 'AIRBUS INDUSTRIE A321', 'JET', '220'),
 ('332', 'A330-200', 'AIRBUS INDUSTRIE A330-200', 'JET', '412'),
 ('340', 'A340', 'AIRBUS INDUSTRIE A340', 'JET', '420'),
 ('343', 'A340-300', 'AIRBUS INDUSTRIE A340-300', 'JET', '420'),
 ('73G', '737-700', 'BOEING 737-700', 'JET', '137'),
 ('73M',
  '737-200',
  'BOEING 737-200(mixed configuration)',
  'JET',
  '79'),
 ('73S', '737-200', 'BOEING 737-200 passenger', 'JET', '130'),
 ('732', '737-200', 'BOEING 737-200', 'JET', '189'),
 ('733', '737-300', 'BOEING 737-300', 'JET', '145'),
 ('734', '737-400', 'BOEING 737-400', 'JET', '171'),
 ('735', '737-500', 'BOEING 737-500', 'JET', '132'),
 ('736', '737-600', 'BOEING 737-600', 'JET', '119'),
 ('737', '737', 'BOEING 737 all series', 'JET', '189'),
 ('738', '737-800', 'BOEING 737-800', 'JET', '189'),
 ('74E',
  '747-400',
  'BOEING 747-400(mixed configuration)',
  'JET',
  '420'),
 ('74L', '747 SP', 'BOEING 747 SP', 'JET', '440'),
 ('74M',
  '747-200',
  'BOEING 747-200 (mixed configuration)',
  'JET',
  '400'),
 ('744', '747-400', 'BOEING 747-400 passenger', 'JET', '569'),
 ('747', '747', 'BOEING 747 all series', 'JET', '569'),
 ('757', '757', 'BOEING 757 all series', 'JET', '239'),
 ('763', '767-300', 'BOEING 767-300', 'JET', '290'),
 ('767', '767-200', 'BOEING 767-200', 'JET', '290'),
 ('772', '777-200', 'BOEING 777-200', 'JET', '440'),
 ('777', '777', 'Boeing 777 all series', 'JET', '440')]

lines = []
for each in airliner:
        seat = int(each[4])
        pilot = 2
        if seat >= 100:
                pilot = 2+ (seat-100)/100+1
        elif seat < 51:
                pilot = 1
        att = seat//50+1
        print('Insert Into Equipment values("%s",%d,%d,%d,"%s","%s");'%(each[0],seat,att,pilot,each[2],each[1]))
        lines.append(each[1])

print(lines)
