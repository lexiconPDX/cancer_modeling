param_names = [
    'Bg',
    'kSyE2f',
    'kSyE2fE2f',
    'jSyE2f',
    'kAsRbE2f',
    'kDsRbE2f',
    'kDeE2f',
    'kPhRbCd',
    'kPhRbCe',
    'kPhRbCa',
    'kDpRb',
    'kSyE1',
    'kDeE1C1',
    'kDeE1',
    'kPhC1',
    'kPhC1Ce',
    'kPhC1Ca',
    'kDpC1',
    'kAsE1C1',
    'kDsE1C1',
    'kSyP21',
    'kSyP21P53',
    'kDeP21',
    'kDeP21Cy',
    'kDeP21aRc',
    'kSyCe',
    'kSyCa',
    'kAsCyP21',
    'kDsCyP21',
    'kDeCe',
    'kDeCa',
    'kDeCeCa',
    'kDeCaC1',
    'kImPc',
    'kExPc',
    'kPhRc',
    'kDpRc',
    'jCy',
    'n',
    'kAsRcPc',
    'kDsRcPc',
    'kAsPcP21',
    'kDsPcP21',
    'kSyDna',
    'kSyP53',
    'kDeP53',
    'jP53',
    'kGeDam',
    'kGeDamArc',
    'kReDam',
    'kReDamP53',
    'jDam',
    'kSyPr',
    'kDePr',
    #
    'len_f_params'\
]

for idx,name in enumerate(param_names):
  exec('%s=%d'%(name,idx))