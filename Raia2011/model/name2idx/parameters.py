NAMES = [
    'Kon_IL13Rec',
    'Rec_phosphorylation',
    'pRec_intern',
    'pRec_degradation',
    'Rec_intern',
    'Rec_recycle',
    'JAK2_phosphorylation',
    'pJAK2_dephosphorylation',
    'STAT5_phosphorylation',
    'pSTAT5_dephosphorylation',
    'SOCS3mRNA_production',
    'DecoyR_binding',
    'JAK2_p_inhibition',
    'SOCS3_translation',
    'SOCS3_accumulation',
    'SOCS3_degradation',
    'CD274mRNA_production',
]

for idx, name in enumerate(NAMES):
    exec(
        '{} = {:d}'.format(
            name, idx
        )
    )

NUM = len(NAMES)