from .name2idx import C, V

def diffeq(y, t, *x):

	v = [0] * 114
	
	#1 ∅ −→ EGFR
	v[1] = 2*x[C.EGFR_basal_activation]*(x[C.init_EGFR]**2) *x[C.pEGFR_degradation] \
            /(x[C.pEGFR_degradation] + x[C.init_RTKph]*x[C.pEGFR_phosphatase_binding]) + x[C.EGFR_ErbB2_basal_act]  \
            *x[C.init_EGFR]*x[C.pErbB12_degradation]/(x[C.pErbB12_degradation] + x[C.init_RTKph] \
            *x[C.pErbB12i_phosphatase])+ x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR]*x[C.init_ErbB3] \
            *x[C.pErbB13_degradation]/(x[C.pErbB13_degradation] + x[C.init_RTKph]*x[C.pErbB13i_phosphatase]) \
            + x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]*x[C.pMetEGFR_degradation] \
            /(x[C.pMetEGFR_degradation] + x[C.init_RTKph]*x[C.pMetEGFRi_phosphatase])
	#2 ∅ −→ ErbB2
	v[2] = 2*x[C.ErbB2_dimerize]*(x[C.init_ErbB2]**2) *x[C.pErbB2_degradation] \
            /(x[C.pErbB2_degradation] + x[C.init_RTKph]*x[C.pErbB2i_phosphatase]) + x[C.EGFR_ErbB2_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB2]*x[C.pErbB12_degradation]/(x[C.pErbB12_degradation] \
            + x[C.init_RTKph]*x[C.pErbB12i_phosphatase]) + x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2] \
            *x[C.init_ErbB3]*x[C.pErbB32_degradation]/(x[C.pErbB32_degradation] + x[C.init_RTKph] \
            *x[C.pErbB32i_phosphatase])
	#3 ∅ −→ ErbB3
	v[3] = 2*x[C.ErbB3_basal_activation]*(x[C.init_ErbB3]**2) *x[C.pErbB3_degradation] \
            /(x[C.pErbB3_degradation] + x[C.init_RTKph]*x[C.pErbB3i_phosphatase]) + x[C.EGFR_ErbB3_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB3]*x[C.pErbB13_degradation]/(x[C.pErbB13_degradation] + x[C.init_RTKph] \
            *x[C.pErbB13i_phosphatase]) + x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2]*x[C.init_ErbB3] \
            *x[C.pErbB32_degradation]/(x[C.pErbB32_degradation] + x[C.init_RTKph]*x[C.pErbB32i_phosphatase]) \
            + x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]*x[C.pMetErbB3_degradation] \
            /(x[C.pMetErbB3_degradation] + x[C.init_RTKph]*x[C.pMetErbB3i_phosphatase])
	#4 ∅ −→ IGF1R
	v[4] = 2*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2) *x[C.pIGF1R_degradation] \
            /(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase])
	#5 ∅ −→ Met
	v[5] = 2*x[C.Met_basal_act]*(x[C.init_Met]**2) *x[C.pMet_degradation]/(x[C.pMet_degradation] \
            + x[C.init_RTKph]*x[C.pMeti_phosphatase]) + x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met] \
            *x[C.pMetEGFR_degradation]/(x[C.pMetEGFR_degradation] + x[C.init_RTKph]*x[C.pMetEGFRi_phosphatase]) \
            + x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]*x[C.pMetErbB3_degradation] \
            /(x[C.pMetErbB3_degradation] + x[C.init_RTKph]*x[C.pMetErbB3i_phosphatase])
	#6 dose EGF + EGFR −→ EGFR EGF
	v[6] = x[C.EGFR_lig_binding]*y[V.dose_EGF]*y[V.EGFR]
	#7 EGFR EGF −→ dose EGF + EGFR
	v[7] = x[C.EGF_kD]*y[V.EGFR_EGF]*x[C.EGFR_lig_binding]
	#test8 dose BTC + EGFR −→ EGFR BTC
	v[8] = y[V.EGFR]*x[C.EGFR_BTC_binding]*y[V.dose_BTC]
	#test9 EGFR BTC −→ dose BTC + EGFR
	v[9] = y[V.EGFR_BTC]*x[C.EGFR_BTC_binding]*x[C.EGF_kD]
	#10 dose HRG + ErbB3 −→ ErbB3 HRG
	v[10] = x[C.ErbB3_lig_binding]*y[V.dose_HRG]*y[V.ErbB3]
	#11 ErbB3 HRG −→ dose HRG + ErbB3
	v[11] = y[V.ErbB3_HRG]*x[C.ErbB3_lig_binding]*x[C.HRG_kD]
	#12 dose IGF1 + IGF1R −→ IGF1R IGF1
	v[12] = x[C.IGF1R_lig_binding]*y[V.dose_IGF1]*y[V.IGF1R]
	#13 IGF1R IGF1 −→ dose IGF1 + IGF1R
	v[13] = x[C.IGF1_kD]*y[V.IGF1R_IGF1]*x[C.IGF1R_lig_binding]
	#14 dose HGF + Met −→ Met HGF
	v[14] = x[C.Met_lig_binding]*y[V.dose_HGF]*y[V.Met]
	#15 Met HGF −→ dose HGF + Met
	v[15] = x[C.HGF_kD]*y[V.Met_HGF]*x[C.Met_lig_binding]
	#16 2·EGFR EGF −→ pEGFRd
	v[16] = x[C.EGFR_dimerize]*(y[V.EGFR_EGF]**2)
	#test17 2·EGFR BTC −→ pEGFRd
	v[17] = (y[V.EGFR_BTC]**2)*x[C.EGFR_BTC_dimerize]
	#18 2·ErbB2 −→ pErbB2
	v[18] = x[C.ErbB2_dimerize]*(y[V.ErbB2]**2)
	#19 2·ErbB3 HRG −→ pErbB3d
	v[19] = x[C.ErbB3_dimerize]*(y[V.ErbB3_HRG]**2)
	#20 2·IGF1R IGF1 −→ pIGF1Rd
	v[20] = x[C.IGF1R_dimerize]*(y[V.IGF1R_IGF1]**2)
	#21 EGFR EGF + ErbB2 −→ pErbB12
	v[21] = x[C.EGFR_ErbB2_dimerize]*y[V.EGFR_EGF]*y[V.ErbB2]
	#test22 EGFR BTC + ErbB2 −→ pErbB12
	v[22] = y[V.EGFR_BTC]*x[C.EGFR_ErbB2_BTC_dimerize]*y[V.ErbB2]
	#23 EGFR EGF + ErbB3 HRG −→ pErbB13
	v[23] = x[C.EGFR_ErbB3_dimerize]*y[V.EGFR_EGF]*y[V.ErbB3_HRG]
	#test24 EGFR BTC + ErbB3 HRG −→ pErbB13
	v[24] = y[V.EGFR_BTC]*x[C.EGFR_ErbB3_BTC_dimerize]*y[V.ErbB3_HRG]
	#test25 EGFR BTC + ErbB3 −→ pErbB13
	v[25] = y[V.EGFR_BTC]*x[C.EGFR_ErbB3_dimerize_noHRG]*y[V.ErbB3]
	#26 ErbB2 + ErbB3 HRG −→ pErbB32
	v[26] = x[C.ErbB2_ErbB3_dimerize]*y[V.ErbB2]*y[V.ErbB3_HRG]
	#27 2·Met HGF −→ pMetd
	v[27] = x[C.Met_dimerize]*(y[V.Met_HGF]**2)
	#28 ErbB3 HRG + Met −→ pMetErbB3
	v[28] = x[C.Met_ErbB3_dimerize]*y[V.ErbB3_HRG]*y[V.Met]
	#29 ErbB3 HRG + Met HGF −→ pMetErbB3
	v[29] = x[C.Met_lig_ErbB3_dimerize]*y[V.ErbB3_HRG]*y[V.Met_HGF]
	#30 EGFR EGF + Met HGF −→ pMetEGFR
	v[30] = x[C.Met_EGFR_dimerize]*y[V.EGFR_EGF]*y[V.Met_HGF]
	#test31 EGFR BTC + Met HGF −→ pMetEGFR
	v[31] = y[V.EGFR_BTC]*x[C.Met_EGFR_BTC_dimerize]*y[V.Met_HGF]
	#32 2·EGFR −→ pEGFRd
	v[32] = x[C.EGFR_basal_activation]*(y[V.EGFR]**2)
	#33 2·ErbB3 −→ pErbB3d
	v[33] = x[C.ErbB3_basal_activation]*(y[V.ErbB3]**2)
	#34 2·IGF1R −→ pIGF1Rd
	v[34] = x[C.IGF1R_basal_activation]*(y[V.IGF1R]**2)
	#35 EGFR + ErbB2 −→ pErbB12
	v[35] = x[C.EGFR_ErbB2_basal_act]*y[V.EGFR]*y[V.ErbB2]
	#36 EGFR + ErbB3 −→ pErbB13
	v[36] = x[C.EGFR_ErbB3_basal_act]*y[V.EGFR]*y[V.ErbB3]
	#37 ErbB2 + ErbB3 −→ pErbB32
	v[37] = x[C.ErbB3_ErbB2_basal_act]*y[V.ErbB2]*y[V.ErbB3]
	#38 ErbB3 + Met −→ pMetErbB3
	v[38] = x[C.Met_ErbB3_basal_act]*y[V.ErbB3]*y[V.Met]
	#39 2·Met −→ pMetd
	v[39] = x[C.Met_basal_act]*(y[V.Met]**2)
	#40 EGFR + Met −→ pMetEGFR
	v[40] = x[C.Met_EGFR_basal_act]*y[V.EGFR]*y[V.Met]
	#41 pEGFRd −→ pEGFRi
	v[41] = x[C.pEGFR_internalize]*y[V.pEGFRd]
	#42 pEGFRi −→ ∅
	v[42] = x[C.pEGFR_degradation]*y[V.pEGFRi]
	#43 RTKph + pEGFRi −→ pEGFRi ph
	v[43] = x[C.pEGFR_phosphatase_binding]*y[V.RTKph]*y[V.pEGFRi]
	#44 pEGFRi ph −→ RTKph + 2·EGFRi
	v[44] = x[C.pEGFRi_dephosph]*y[V.pEGFRi_ph]
	#45 EGFRi −→ EGFR
	v[45] = x[C.EGFR_basal_recycle]*y[V.EGFRi]
	#46 pErbB2 −→ pErbB2i
	v[46] = x[C.pErbB2_internalize]*y[V.pErbB2]
	#47 RTKph + pErbB2i −→ pErbB2i ph
	v[47] = x[C.pErbB2i_phosphatase]*y[V.RTKph]*y[V.pErbB2i]
	#48 pErbB2i ph −→ RTKph + 2·ErbB2i
	v[48] = x[C.pErbB2i_dephosph]*y[V.pErbB2i_ph]
	#49 pErbB2i −→ ∅
	v[49] = x[C.pErbB2_degradation]*y[V.pErbB2i]
	#50 ErbB2i −→ ErbB2
	v[50] = x[C.ErbB2_recycle]*y[V.ErbB2i]
	#51 pErbB3d −→ pErbB3i
	v[51] = x[C.pErbB3_internalize]*y[V.pErbB3d]
	#52 pErbB3i −→ ∅
	v[52] = x[C.pErbB3_degradation]*y[V.pErbB3i]
	#53 RTKph + pErbB3i −→ pErbB3i ph
	v[53] = x[C.pErbB3i_phosphatase]*y[V.RTKph]*y[V.pErbB3i]
	#54 pErbB3i ph −→ RTKph + 2·ErbB3i
	v[54] = x[C.pErbB3i_dephosph]*y[V.pErbB3i_ph]
	#55 ErbB3i −→ ErbB3
	v[55] = x[C.ErbB3_basal_recycle]*y[V.ErbB3i]
	#56 pIGF1Rd −→ pIGF1Ri
	v[56] = x[C.pIGF1R_internalize]*y[V.pIGF1Rd]
	#57 pIGF1Ri −→ ∅
	v[57] = x[C.pIGF1R_degradation]*y[V.pIGF1Ri]
	#58 RTKph + pIGF1Ri −→ pIGF1Ri ph
	v[58] = x[C.pIGF1Ri_phosphatase]*y[V.RTKph]*y[V.pIGF1Ri]
	#59 pIGF1Ri ph −→ RTKph + 2·IGF1Ri
	v[59] = x[C.pIGF1Ri_dephosph]*y[V.pIGF1Ri_ph]
	#60 IGF1Ri −→ IGF1R
	v[60] = x[C.IGF1R_basal_recycle]*y[V.IGF1Ri]
	#61 pErbB12 −→ pErbB12i
	v[61] = x[C.pErbB12_internalize]*y[V.pErbB12]
	#62 pErbB12i −→ ∅
	v[62] = x[C.pErbB12_degradation]*y[V.pErbB12i]
	#63 RTKph + pErbB12i −→ pErbB12i ph
	v[63] = x[C.pErbB12i_phosphatase]*y[V.RTKph]*y[V.pErbB12i]
	#64 pErbB12i ph −→ RTKph + EGFRi + ErbB2i
	v[64] = x[C.pErbB12i_dephosph]*y[V.pErbB12i_ph]
	#65 pErbB32 −→ pErbB32i
	v[65] = x[C.pErbB32_internalize]*y[V.pErbB32]
	#66 pErbB32i −→ ∅
	v[66] = x[C.pErbB32_degradation]*y[V.pErbB32i]
	#67 RTKph + pErbB32i −→ pErbB32i ph
	v[67] = x[C.pErbB32i_phosphatase]*y[V.RTKph]*y[V.pErbB32i]
	#68 pErbB32i ph −→ RTKph + ErbB2i + ErbB3i
	v[68] = x[C.pErbB32i_dephosph]*y[V.pErbB32i_ph]
	#69 pErbB13 −→ pErbB13i
	v[69] = x[C.pErbB13_internalize]*y[V.pErbB13]
	#70 pErbB13i −→ ∅
	v[70] = x[C.pErbB13_degradation]*y[V.pErbB13i]
	#71 RTKph + pErbB13i −→ pErbB13i ph
	v[71] = x[C.pErbB13i_phosphatase]*y[V.RTKph]*y[V.pErbB13i]
	#72 pErbB13i ph −→ RTKph + EGFRi + ErbB3i
	v[72] = x[C.pErbB13i_dephosph]*y[V.pErbB13i_ph]
	#73 pMetd −→ pMeti
	v[73] = x[C.pMet_internalize]*y[V.pMetd]
	#74 pMeti −→ ∅
	v[74] = x[C.pMet_degradation]*y[V.pMeti]
	#75 RTKph + pMeti −→ pMeti ph
	v[75] = x[C.pMeti_phosphatase]*y[V.RTKph]*y[V.pMeti]
	#76 pMeti ph −→ RTKph + 2·Meti
	v[76] = x[C.pMeti_dephosph]*y[V.pMeti_ph]
	#77 Meti −→ Met
	v[77] = x[C.Met_recycle]*y[V.Meti]
	#78 pMetErbB3 −→ pMetErbB3i
	v[78] = x[C.pMetErbB3_internalize]*y[V.pMetErbB3]
	#79 pMetErbB3i −→ ∅
	v[79] = x[C.pMetErbB3_degradation]*y[V.pMetErbB3i]
	#80 RTKph + pMetErbB3i −→ pMetErbB3i ph
	v[80] = x[C.pMetErbB3i_phosphatase]*y[V.RTKph]*y[V.pMetErbB3i]
	#81 pMetErbB3i ph −→ RTKph + ErbB3i + Meti
	v[81] = x[C.pMetErbB3i_dephosph]*y[V.pMetErbB3i_ph]
	#82 pMetEGFR −→ pMetEGFRi
	v[82] = x[C.pMetEGFR_internalize]*y[V.pMetEGFR]
	#83 pMetEGFRi −→ ∅
	v[83] = x[C.pMetEGFR_degradation]*y[V.pMetEGFRi]
	#84 RTKph + pMetEGFRi −→ pMetEGFRi ph
	v[84] = x[C.pMetEGFRi_phosphatase]*y[V.RTKph]*y[V.pMetEGFRi]
	#85 pMetEGFRi ph −→ RTKph + EGFRi + Meti
	v[85] = x[C.pMetEGFRi_dephosph]*y[V.pMetEGFRi_ph]
	#86 MEK -pEGFRd,pERK→ pMEK
	v[86] = y[V.MEK]*x[C.MEK_phosphorylation_pEGFR]*y[V.pEGFRd]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3] \
            *x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#87 MEK -pErbB12,pERK→  pMEK
	v[87] = y[V.MEK]*x[C.MEK_phosphorylation_pErbB12]*y[V.pErbB12]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase])  \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3] \
            *x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#88 MEK -pErbB13,pERK→  pMEK
	v[88] = y[V.MEK]*x[C.MEK_phosphorylation_pErbB13]*y[V.pErbB13]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize]  \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#89 MEK -pErbB32,pERK→ pMEK
	v[89] = y[V.MEK]*x[C.MEK_phosphorylation_pErbB32]*y[V.pErbB32]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
             *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
             *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
             *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#90 MEK -pMetd,pERK→ pMEK
	v[90] = y[V.MEK]*x[C.MEK_phosphorylation_pMetd]*y[V.pMetd]/(x[C.feedback_pERK]*y[V.pERK] \
            + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation]*(x[C.init_EGFR]**2) \
            /x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2) \
            /x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2)/x[C.pMet_internalize] \
            + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2) \
            /(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) + x[C.AKT_activation_pErbB12] \
            *x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2]/x[C.pErbB12_internalize] \
            + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR]*x[C.init_ErbB3] \
            /x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2] \
            *x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR]*x[C.Met_EGFR_basal_act] \
            *x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3] \
            *x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#91 MEK -pMetEGFR,pERK→ pMEK
	v[91] = y[V.MEK]*x[C.MEK_phosphorylation_pMetEGFR]*y[V.pMetEGFR]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase])  \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#92 MEK -pIGF1Rd,pERK→ pMEK
	v[92] = y[V.MEK]*x[C.MEK_phosphorylation_pIGF1R]*y[V.pIGF1Rd]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR] \
            *x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act] \
            *x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR] \
            *x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met]/x[C.pMetEGFR_internalize] \
            + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act]*x[C.init_Met]*x[C.init_ErbB3] \
            /x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1]*x[C.init_pS6K1] \
            + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#93 MEK -pMetErbB3,pERK→ pMEK
	v[93] = y[V.MEK]*x[C.MEK_phosphorylation_pMetErbB3]*y[V.pMetErbB3]/(x[C.feedback_pERK] \
            *y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR]*x[C.EGFR_basal_activation] \
            *(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd]*x[C.Met_basal_act]*(x[C.init_Met]**2) \
            /x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation] \
            *(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) \
            + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act]*x[C.init_EGFR]*x[C.init_ErbB2] \
            /x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13]*x[C.EGFR_ErbB3_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB3]/x[C.pErbB13_internalize] + x[C.AKT_activation_pErbB32] \
            *x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2]*x[C.init_ErbB3]/x[C.pErbB32_internalize] \
            + x[C.AKT_activation_pMetEGFR]*x[C.Met_EGFR_basal_act]*x[C.init_EGFR]*x[C.init_Met] \
            /x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act] \
            *x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation] \
            *(x[C.feedback_pS6K1]*x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#94 MEK -pIGF1Ri,pERK→ pMEK
	v[94] = y[V.MEK]*x[C.MEK_internIGF1R_effect]*x[C.MEK_phosphorylation_pIGF1R] \
            *y[V.pIGF1Ri]/(x[C.feedback_pERK]*y[V.pERK] + x[C.feedback_pAKT]*x[C.init_AKT]*(x[C.AKT_activation_pEGFR] \
            *x[C.EGFR_basal_activation]*(x[C.init_EGFR]**2)/x[C.pEGFR_internalize] + x[C.AKT_activation_pIGF1R] \
            *x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2)/x[C.pIGF1R_internalize] + x[C.AKT_activation_pMetd] \
            *x[C.Met_basal_act]*(x[C.init_Met]**2)/x[C.pMet_internalize] + x[C.AKT_activation_pIGF1R] \
            *x[C.AKT_internIGF1R_effect]*x[C.IGF1R_basal_activation]*(x[C.init_IGF1R]**2)/(x[C.pIGF1R_degradation] \
            + x[C.init_RTKph]*x[C.pIGF1Ri_phosphatase]) + x[C.AKT_activation_pErbB12]*x[C.EGFR_ErbB2_basal_act] \
            *x[C.init_EGFR]*x[C.init_ErbB2]/x[C.pErbB12_internalize] + x[C.AKT_activation_pErbB13] \
            *x[C.EGFR_ErbB3_basal_act]*x[C.init_EGFR]*x[C.init_ErbB3]/x[C.pErbB13_internalize] \
            + x[C.AKT_activation_pErbB32]*x[C.ErbB3_ErbB2_basal_act]*x[C.init_ErbB2]*x[C.init_ErbB3] \
            /x[C.pErbB32_internalize] + x[C.AKT_activation_pMetEGFR]*x[C.Met_EGFR_basal_act]*x[C.init_EGFR] \
            *x[C.init_Met]/x[C.pMetEGFR_internalize] + x[C.AKT_activation_pMetErbB3]*x[C.Met_ErbB3_basal_act] \
            *x[C.init_Met]*x[C.init_ErbB3]/x[C.pMetErbB3_internalize])/(x[C.pAKT_deactivation]*(x[C.feedback_pS6K1] \
            *x[C.init_pS6K1] + x[C.feedback_pERK_on_AKT]*x[C.init_pERK] + 1)) + 1)
	#95 pMEK −→ MEK
	v[95] = x[C.pMEK_dephosphorylation]*y[V.pMEK]
	#96 ERK -pMEK→ pERK
	v[96] = y[V.ERK]*x[C.ERK_phosphorylation_pMEK]*y[V.pMEK]
	#97 pERK −→ ERK
	v[97] = x[C.pERK_dephosphorylation]*y[V.pERK]
	#98 AKT -pEGFRd,pERK,pS6K1→ pAKT
	v[98] = y[V.AKT]*x[C.AKT_activation_pEGFR]*y[V.pEGFRd]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#99 AKT -pErbB12,pERK,pS6K1→ pAKT
	v[99] = y[V.AKT]*x[C.AKT_activation_pErbB12]*y[V.pErbB12]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#100 AKT -pErbB13,pERK,pS6K1→ pAKT
	v[100] = y[V.AKT]*x[C.AKT_activation_pErbB13]*y[V.pErbB13]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#101 AKT -pErbB32, pERK,pS6K1→ pAKT
	v[101] = y[V.AKT]*x[C.AKT_activation_pErbB32]*y[V.pErbB32]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#102 AKT -pMetEGFR,pERK,pS6K1→ pAKT
	v[102] = y[V.AKT]*x[C.AKT_activation_pMetEGFR]*y[V.pMetEGFR]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#103 AKT -pMetd,pERK,pS6K1→ pAKT
	v[103] = y[V.AKT]*x[C.AKT_activation_pMetd]*y[V.pMetd]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#104 AKT -pIGF1Rd,pERK,pS6K1→ pAKT
	v[104] = y[V.AKT]*x[C.AKT_activation_pIGF1R]*y[V.pIGF1Rd]/(x[C.feedback_pERK_on_AKT]*y[V.pERK] \
            + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#105 AKT -pMetErbB3,pERK,pS6K1→ pAKT
	v[105] = y[V.AKT]*x[C.AKT_activation_pMetErbB3]*y[V.pMetErbB3]/(x[C.feedback_pERK_on_AKT] \
            *y[V.pERK] + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#106 AKT −pIGF1Ri,pERK,pS6K1→ pAKT
	v[106] = y[V.AKT]*x[C.AKT_activation_pIGF1R]*x[C.AKT_internIGF1R_effect]*y[V.pIGF1Ri] \
            /(x[C.feedback_pERK_on_AKT]*y[V.pERK] + x[C.feedback_pS6K1]*y[V.pS6K1] + 1)
	#107 pAKT −→ AKT
	v[107] = x[C.pAKT_deactivation]*y[V.pAKT]
	#108 -S6K1-pAKT→ pS6K1
	v[108] = y[V.S6K1]*x[C.S6K1_phosphorylation_pAKT]*y[V.pAKT]
	#109 S6K1-pERK→ pS6K1
	v[109] = y[V.S6K1]*x[C.S6K1_phosphorylation_pERK]*y[V.pERK]
	#109 pS6K1 −→ S6K1
	v[110] = x[C.pS6K1_dephosphorylation]*y[V.pS6K1]
	#111 S6 -pS6K1→ pS6
	v[111] = y[V.S6]*x[C.S6_phosphorylation_pS6K1]*y[V.pS6K1]
	#112 S6 pERK→ pS6
	v[112] = y[V.S6]*x[C.S6_phosphorylation_pERK]*y[V.pERK]
	#113 pS6 −→ S6
	v[113] = x[C.pS6_dephosphorylation]*y[V.pS6]

	dydt = [0] * V.NUM

	dydt[V.dose_EGF] = - v[6] + v[7]
	dydt[V.dose_HGF] = - v[14] + v[15]
	dydt[V.RTKph] = - v[43] + v[44] - v[47] + v[48] - v[53] + v[54] - v[58] + v[59] \
					- v[63] + v[64] - v[67] + v[68] - v[71] + v[72] - v[75] + v[76] \
					- v[80] + v[81] - v[84] + v[85]
	dydt[V.dose_IGF1] = - v[12] + v[13]
	dydt[V.dose_HRG] = - v[10] + v[11]
	dydt[V.dose_BTC] = -v[8] + v[9]
	dydt[V.EGFR] = v[1] - v[6] + v[7] - 2.0*v[32] - v[35] - v[36] - v[40] + v[45]
	dydt[V.EGFR_EGF] = v[6] - v[7] - 2.0*v[16] - v[21] - v[23] - v[30]
	dydt[V.EGFR_BTC] = v[8] - v[9] - 2.0*v[17] - v[22] - v[24] - v[25] - v[31]
	dydt[V.pEGFRd] = v[16] + v[32] - v[41]
	dydt[V.pEGFRi] = v[41] - v[42] - v[43]
	dydt[V.pEGFRi_ph] = v[43] - v[44]
	dydt[V.EGFRi] = 2.0*v[44] - v[45] + v[64] + v[72] + v[85]
	dydt[V.ErbB2] = v[2] - 2.0*v[18] - v[21] - v[26] - v[35] - v[37] + v[50]
	dydt[V.pErbB2] = v[18] - v[46]
	dydt[V.pErbB2i] = v[46] - v[47] - v[49]
	dydt[V.ErbB2i] = 2.0*v[48] - v[50] + v[64] + v[68]
	dydt[V.pErbB2i_ph] = v[47] - v[48]
	dydt[V.pErbB12] = v[21] + v[35] - v[61]
	dydt[V.pErbB12i] = v[61] - v[62] - v[63]
	dydt[V.pErbB12i_ph] = v[63] - v[64]
	dydt[V.ErbB3] = v[3] - v[10] + v[11] - 2.0*v[33] - v[36] - v[37] - v[38] + v[55]
	dydt[V.ErbB3_HRG] = v[10] - v[11] - 2.0*v[19] - v[23] - v[26] - v[28] - v[29]
	dydt[V.pErbB3d] = v[19] + v[33] - v[51]
	dydt[V.pErbB3i] = v[51] - v[52] - v[53]
	dydt[V.pErbB3i_ph] = v[53] - v[54]
	dydt[V.ErbB3i] = 2.0*v[54] - v[55] + v[68] + v[72] + v[81]
	dydt[V.pErbB13] = v[23] + v[36] - v[69]
	dydt[V.pErbB13i] = v[69] - v[70] - v[71]
	dydt[V.pErbB13i_ph] = v[71] - v[72]
	dydt[V.pErbB32] = v[26] + v[37] - v[65]
	dydt[V.pErbB32i] = v[65] - v[66] - v[67]
	dydt[V.pErbB32i_ph] = v[67] - v[68]
	dydt[V.IGF1R] = v[4] - v[12] + v[13] - 2.0*v[34] + v[60]
	dydt[V.IGF1R_IGF1] = v[12] - v[13] - 2.0*v[20]
	dydt[V.pIGF1Rd] = v[20] + v[34] - v[56]
	dydt[V.pIGF1Ri] = v[56] - v[57] - v[58]
	dydt[V.pIGF1Ri_ph] = v[58] - v[59]
	dydt[V.IGF1Ri] = 2.0*v[59] - v[60]
	dydt[V.Met] = v[5] - v[14] + v[15] - v[28] - v[38] - 2.0*v[39] - v[40] + v[77]
	dydt[V.Met_HGF] = v[14] - v[15] - 2.0*v[27] - v[29] - v[30]
	dydt[V.pMetd] = v[27] + v[39] - v[73]
	dydt[V.pMeti] = v[73] - v[74] - v[75]
	dydt[V.pMeti_ph] = v[75] - v[76]
	dydt[V.Meti] = 2.0*v[76] - v[77] + v[81] + v[85]
	dydt[V.pMetErbB3] = v[28] + v[29] + v[38] - v[78]
	dydt[V.pMetErbB3i] = v[78] - v[79] - v[80]
	dydt[V.pMetErbB3i_ph] = v[80] - v[81]
	dydt[V.pMetEGFR] = v[30] + v[40] - v[82]
	dydt[V.pMetEGFRi] = v[82] - v[83] - v[84]
	dydt[V.pMetEGFRi_ph] = v[84] - v[85]
	dydt[V.MEK] = - v[86] - v[87] - v[88] - v[89] - v[90] - v[91] - v[92] - v[93] - v[94] + v[95]
	dydt[V.pMEK] = v[86] + v[87] + v[88] + v[89] + v[90] + v[91] + v[92] + v[93] + v[94] - v[95]
	dydt[V.ERK] = - v[96] + v[97]
	dydt[V.pERK] = v[96] - v[97]
	dydt[V.AKT] = - v[98] - v[99] - v[100] - v[101] - v[102] - v[103] - v[104] - v[105] - v[106] + v[107]
	dydt[V.pAKT] = v[98] + v[99] + v[100] + v[101] + v[102] + v[103] + v[104] + v[105] + v[106] - v[107]
	dydt[V.S6K1] = - v[108] - v[109] + v[110]
	dydt[V.pS6K1] = v[108] + v[109] - v[110]
	dydt[V.S6] = - v[111] - v[112] + v[113]
	dydt[V.pS6] = v[111] + v[112] - v[113]

	return dydt


def param_values():

	x = [0] * C.NUM
	
	x[C.AKT_activation_pEGFR] = 1.00000000000008E-5
	x[C.AKT_activation_pErbB12] = 0.0639758596193363
	x[C.AKT_activation_pErbB13] = 13.114480220736
	x[C.AKT_activation_pErbB32] = 0.560696624171667
	x[C.AKT_activation_pIGF1R] = 0.685272879413749
	x[C.AKT_activation_pMetEGFR] = 1.00000000000016E-5
	x[C.AKT_activation_pMetErbB3] = 0.0369784304561464
	x[C.AKT_activation_pMetd] = 0.895634029510145
	x[C.AKT_internIGF1R_effect] = 1.02158595529249E-5
	x[C.EGFR_BTC_binding] = 2.24E-5
	x[C.EGFR_BTC_dimerize] = 1.00E3
	x[C.EGFR_ErbB2_BTC_dimerize] = 1.61E0
	x[C.EGFR_ErbB2_basal_act] = 1.00000055393187E-5
	x[C.EGFR_ErbB2_dimerize] = 0.0156992626983121
	x[C.EGFR_ErbB3_BTC_dimerize] = 3.52E-2
	x[C.EGFR_ErbB3_basal_act] = 7.51086344216133E-4
	x[C.EGFR_ErbB3_dimerize] = 0.00118163147147325
	x[C.EGFR_ErbB3_dimerize_noHRG] = 1.00E-5
	x[C.EGFR_basal_activation] = 1.00000000000013E-5
	x[C.EGFR_basal_recycle] = 519022.804648067
	x[C.EGFR_dimerize] = 0.0630202348036973
	x[C.EGFR_lig_binding] = 1.89365431456425E-5
	x[C.EGF_kD] = 1.0
	x[C.ERK_phosphorylation_pMEK] = 2.58273728135596E-4
	x[C.ErbB2_ErbB3_dimerize] = 0.0302521519982926
	x[C.ErbB2_dimerize] = 0.00679233180470311
	x[C.ErbB2_recycle] = 0.00657059769157574
	x[C.ErbB3_ErbB2_basal_act] = 1.00000000000009E-5
	x[C.ErbB3_basal_activation] = 0.0292989708706365
	x[C.ErbB3_basal_recycle] = 0.736644857921333
	x[C.ErbB3_dimerize] = 0.0445825815551282
	x[C.ErbB3_lig_binding] = 5.7141588472601E-5
	x[C.HGF_kD] = 0.3
	x[C.HRG_kD] = 0.05
	x[C.IGF1R_basal_activation] = 0.00117036535223592
	x[C.IGF1R_basal_recycle] = 999.999999999949
	x[C.IGF1R_dimerize] = 17.128618175105
	x[C.IGF1R_lig_binding] = 0.00152919451073767
	x[C.IGF1_kD] = 0.3
	x[C.MEK_internIGF1R_effect] = 1.00008963405935E-5
	x[C.MEK_phosphorylation_pEGFR] = 1.00000000000534E-5
	x[C.MEK_phosphorylation_pErbB12] = 0.273831131210384
	x[C.MEK_phosphorylation_pErbB13] = 1.00000000000005E-5
	x[C.MEK_phosphorylation_pErbB32] = 0.0605666784423666
	x[C.MEK_phosphorylation_pIGF1R] = 0.0299477004480249
	x[C.MEK_phosphorylation_pMetEGFR] = 1.00000000000305E-5
	x[C.MEK_phosphorylation_pMetErbB3] = 0.0383373232331984
	x[C.MEK_phosphorylation_pMetd] = 1.87982658293355
	x[C.Met_EGFR_BTC_dimerize] = 1.11E-2
	x[C.Met_EGFR_basal_act] = 1.74545892225427E-5
	x[C.Met_EGFR_dimerize] = 5.13154978177414E-4
	x[C.Met_ErbB3_basal_act] = 3.29370803896943
	x[C.Met_ErbB3_dimerize] = 0.0370817212557079
	x[C.Met_basal_act] = 1.0000000000001E-5
	x[C.Met_dimerize] = 0.00916578895965068
	x[C.Met_lig_ErbB3_dimerize] = 567.027453817882
	x[C.Met_lig_binding] = 0.00451627458718536
	x[C.Met_recycle] = 0.542441478615171
	x[C.S6K1_phosphorylation_pAKT] = 0.249792927251245
	x[C.S6K1_phosphorylation_pERK] = 1.06710979945488E-5
	x[C.S6_phosphorylation_pERK] = 1.00288673965446E-5
	x[C.S6_phosphorylation_pS6K1] = 0.00856925565136242
	x[C.feedback_pAKT] = 1.05838913850398E-5
	x[C.feedback_pERK] = 999.999999999924
	x[C.feedback_pERK_on_AKT] = 1.00256433454385E-5
	x[C.feedback_pS6K1] = 2.09124432361637E-5
	x[C.init_AKT] = 2.70857345464684
	x[C.init_EGFR] = 17.8621933083143
	x[C.init_EGFR_EGF] = 0.0
	x[C.init_ErbB2] = 5.70185166249099
	x[C.init_ErbB3] = 2.47992342696256
	x[C.init_ErbB3_HRG] = 0.0
	x[C.init_IGF1R] = 4.73494621402554
	x[C.init_IGF1R_IGF1] = 0.0
	x[C.init_MEK] = 4.2412663925898
	x[C.init_Met] = 7.90290414461229
	x[C.init_Met_HGF] = 0.0
	x[C.init_RTKph] = 0.618911491797731
	x[C.init_S6] = 145.50079875804
	x[C.init_pERK] = 0.334274838149849
	x[C.init_pS6K1] = 0.00124327830478657
	x[C.pAKT_deactivation] = 0.302953254180854
	x[C.pEGFR_degradation] = 1.00000000000008E-5
	x[C.pEGFR_internalize] = 6.23146511697858
	x[C.pEGFR_phosphatase_binding] = 184.624220936499
	x[C.pEGFRi_dephosph] = 21.7225651446297
	x[C.pERK_dephosphorylation] = 0.542612023876822
	x[C.pErbB12_degradation] = 0.181829581884234
	x[C.pErbB12_internalize] = 1.89552080394473
	x[C.pErbB12i_dephosph] = 999.999999999899
	x[C.pErbB12i_phosphatase] = 0.845257575353603
	x[C.pErbB13_degradation] = 49.7215215909086
	x[C.pErbB13_internalize] = 999.985836443242
	x[C.pErbB13i_dephosph] = 58.4184341302768
	x[C.pErbB13i_phosphatase] = 1.59502117687145E-5
	x[C.pErbB2_degradation] = 318.736400510241
	x[C.pErbB2_internalize] = 999.999999999921
	x[C.pErbB2i_dephosph] = 8.24400865276562
	x[C.pErbB2i_phosphatase] = 999.996393349007
	x[C.pErbB32_degradation] = 0.573545291738867
	x[C.pErbB32_internalize] = 1.08720273664406
	x[C.pErbB32i_dephosph] = 0.0119215988587425
	x[C.pErbB32i_phosphatase] = 0.048790203127517
	x[C.pErbB3_degradation] = 0.908458608626761
	x[C.pErbB3_internalize] = 999.999999999923
	x[C.pErbB3i_dephosph] = 16.313728223184
	x[C.pErbB3i_phosphatase] = 82.1863566077617
	x[C.pIGF1R_degradation] = 1.00000000000006E-5
	x[C.pIGF1R_internalize] = 999.999999999947
	x[C.pIGF1Ri_dephosph] = 331.686853643139
	x[C.pIGF1Ri_phosphatase] = 999.999999999777
	x[C.pMEK_dephosphorylation] = 0.328146453777363
	x[C.pMetEGFR_degradation] = 1.42534860283419
	x[C.pMetEGFR_internalize] = 1.32700039711088
	x[C.pMetEGFRi_dephosph] = 0.503783534367803
	x[C.pMetEGFRi_phosphatase] = 3.57308236526967E-5
	x[C.pMetErbB3_degradation] = 983.696417689528
	x[C.pMetErbB3_internalize] = 999.999999999785
	x[C.pMetErbB3i_dephosph] = 999.999999999949
	x[C.pMetErbB3i_phosphatase] = 999.999999999868
	x[C.pMet_degradation] = 1.9065412889509
	x[C.pMet_internalize] = 999.997342974877
	x[C.pMeti_dephosph] = 12.9849936165651
	x[C.pMeti_phosphatase] = 999.999999999902
	x[C.pS6K1_dephosphorylation] = 0.0103304388732084
	x[C.pS6_dephosphorylation] = 0.118806824178018

	x[C.offset_pAKT_CelllineA431] = 4.52E0
	x[C.offset_pAKT_CelllineACHN_197] = 2.33E3
	x[C.offset_pAKT_CelllineACHN_200] = 1.64E-3
	x[C.offset_pAKT_CelllineACHN_218] = 5.88E2
	x[C.offset_pAKT_CelllineACHN_DM] = 3.92E3
	x[C.offset_pAKT_CelllineADRr] = 4.60E0
	x[C.offset_pAKT_CelllineADRr_B] = 1.00E2
	x[C.offset_pAKT_CelllineADRr_B2] = 1.00E0
	x[C.offset_pAKT_CelllineBT20] = 1.30E1
	x[C.offset_pAKT_CelllineBxPc3] = 1.38E-1
	x[C.offset_pAKT_CelllineH322M] = 1.87E-1
	x[C.offset_pAKT_CelllineIGROV1] = 1.49E1
	x[C.offset_pEGFR_CelllineA431] = 3.39E3
	x[C.offset_pEGFR_CelllineACHN_197] = 2.53E2
	x[C.offset_pEGFR_CelllineACHN_200] = 6.94E2
	x[C.offset_pEGFR_CelllineACHN_218] = 8.60E-2
	x[C.offset_pEGFR_CelllineACHN_DM] = 1.00E5
	x[C.offset_pEGFR_CelllineADRr] = 5.08E2
	x[C.offset_pEGFR_CelllineADRr_B] = 1.80E1
	x[C.offset_pEGFR_CelllineADRr_B2] = 1.00E2
	x[C.offset_pEGFR_CelllineBT20] = 2.86E2
	x[C.offset_pEGFR_CelllineBxPc3] = 2.28E0
	x[C.offset_pEGFR_CelllineH322M] = 4.90E0
	x[C.offset_pEGFR_CelllineIGROV1] = 5.69E2
	x[C.offset_pERK_CelllineA431] = 1.00E-7
	x[C.offset_pERK_CelllineACHN_197] = 1.00E-7
	x[C.offset_pERK_CelllineACHN_200] = 1.00E-7
	x[C.offset_pERK_CelllineACHN_218] = 1.00E-7
	x[C.offset_pERK_CelllineACHN_DM] = 1.00E-7
	x[C.offset_pERK_CelllineADRr] = 1.00E-7
	x[C.offset_pERK_CelllineADRr_B] = 1.00E-7
	x[C.offset_pERK_CelllineADRr_B2] =  1.00E-7
	x[C.offset_pERK_CelllineBT20] = 1.00E-7
	x[C.offset_pERK_CelllineBxPc3] = 1.00E-7
	x[C.offset_pERK_CelllineH322M] = 1.00E-7
	x[C.offset_pERK_CelllineIGROV1] = 1.00E-7
	x[C.offset_pErbB2_CelllineA431] = 5.28E-2
	x[C.offset_pErbB2_CelllineACHN_197] = 1.62E-4
	x[C.offset_pErbB2_CelllineACHN_200] = 1.16E-5
	x[C.offset_pErbB2_CelllineACHN_218] = 8.66E4
	x[C.offset_pErbB2_CelllineACHN_DM] = 2.15E-1
	x[C.offset_pErbB2_CelllineADRr] = 1.61E2
	x[C.offset_pErbB2_CelllineADRr_B] = 2.48E3
	x[C.offset_pErbB2_CelllineADRr_B2] =  3.80E1
	x[C.offset_pErbB2_CelllineBT20] = 2.39E2
	x[C.offset_pErbB2_CelllineBxPc3] = 1.81E0
	x[C.offset_pErbB2_CelllineH322M] = 1.09E0
	x[C.offset_pErbB2_CelllineIGROV1] = 3.43E-4
	x[C.offset_pErbB3_CelllineA431] = 3.20E2
	x[C.offset_pErbB3_CelllineACHN_197] = 5.80E-2
	x[C.offset_pErbB3_CelllineACHN_200] = 1.49E-2
	x[C.offset_pErbB3_CelllineACHN_218] = 4.58E1
	x[C.offset_pErbB3_CelllineACHN_DM] = 3.88E4
	x[C.offset_pErbB3_CelllineADRr] = 2.67E1
	x[C.offset_pErbB3_CelllineADRr_B] = 4.01E-4
	x[C.offset_pErbB3_CelllineADRr_B2] =  5.00E1
	x[C.offset_pErbB3_CelllineBT20] = 1.53E-4
	x[C.offset_pErbB3_CelllineBxPc3] = 8.28E-2
	x[C.offset_pErbB3_CelllineH322M] = 1.00E-5
	x[C.offset_pErbB3_CelllineIGROV1] = 1.07E2
	x[C.offset_pIGF1R_CelllineA431] = 1.49E2
	x[C.offset_pIGF1R_CelllineACHN_197] = 8.32E-3
	x[C.offset_pIGF1R_CelllineACHN_200] = 5.25E-2
	x[C.offset_pIGF1R_CelllineACHN_218] = 6.20E3
	x[C.offset_pIGF1R_CelllineACHN_DM] = 4.92E-3
	x[C.offset_pIGF1R_CelllineADRr] = 9.90E1
	x[C.offset_pIGF1R_CelllineADRr_B] = 1.79E3
	x[C.offset_pIGF1R_CelllineADRr_B2] = 6.51E4
	x[C.offset_pIGF1R_CelllineBT20] = 9.85E1
	x[C.offset_pIGF1R_CelllineBxPc3] = 8.08E1
	x[C.offset_pIGF1R_CelllineH322M] = 4.07E2
	x[C.offset_pIGF1R_CelllineIGROV1] = 2.20E2
	x[C.offset_pMEK_CelllineA431] = 5.80E0
	x[C.offset_pMEK_CelllineACHN_197] = 3.23E4
	x[C.offset_pMEK_CelllineACHN_200] = 1.28E-2
	x[C.offset_pMEK_CelllineACHN_218] = 5.25E2
	x[C.offset_pMEK_CelllineACHN_DM] = 3.99E-1
	x[C.offset_pMEK_CelllineADRr] = 7.01E0
	x[C.offset_pMEK_CelllineADRr_B] = 7.08E-1
	x[C.offset_pMEK_CelllineADRr_B2] = 4.70E3
	x[C.offset_pMEK_CelllineBT20] = 6.82E0
	x[C.offset_pMEK_CelllineBxPc3] = 2.83E-1
	x[C.offset_pMEK_CelllineH322M] = 1.37E-1
	x[C.offset_pMEK_CelllineIGROV1] = 5.66E0
	x[C.offset_pMet_CelllineA431] = 3.78E4
	x[C.offset_pMet_CelllineACHN_197] = 5.70E3
	x[C.offset_pMet_CelllineACHN_200] = 1.74E3
	x[C.offset_pMet_CelllineACHN_218] = 9.89E2
	x[C.offset_pMet_CelllineACHN_DM] = 1.98E4
	x[C.offset_pMet_CelllineADRr] = 2.04E-2
	x[C.offset_pMet_CelllineADRr_B] = 7.31E3
	x[C.offset_pMet_CelllineADRr_B2] = 3.19E3
	x[C.offset_pMet_CelllineBT20] = 4.98E-4
	x[C.offset_pMet_CelllineBxPc3] = 3.45E0
	x[C.offset_pMet_CelllineH322M] = 3.14E-2
	x[C.offset_pMet_CelllineIGROV1] = 2.67E3
	x[C.offset_pS6K1_CelllineA431] = 1.00E-7
	x[C.offset_pS6K1_CelllineACHN_197] = 1.00E-7
	x[C.offset_pS6K1_CelllineACHN_200] = 1.00E-7
	x[C.offset_pS6K1_CelllineACHN_218] = 1.00E-7
	x[C.offset_pS6K1_CelllineACHN_DM] = 1.00E-7
	x[C.offset_pS6K1_CelllineADRr] = 1.00E-7
	x[C.offset_pS6K1_CelllineADRr_B] = 1.00E-7
	x[C.offset_pS6K1_CelllineADRr_B2] = 1.00E-7
	x[C.offset_pS6K1_CelllineBT20] = 1.00E-7
	x[C.offset_pS6K1_CelllineBxPc3] = 1.00E-7
	x[C.offset_pS6K1_CelllineH322M] = 1.00E-7
	x[C.offset_pS6K1_CelllineIGROV1] = 1.00E-7
	x[C.offset_pS6_CelllineA431] = 1.00E-7
	x[C.offset_pS6_CelllineACHN_197] = 1.00E-7
	x[C.offset_pS6_CelllineACHN_200] = 1.00E-7
	x[C.offset_pS6_CelllineACHN_218] = 1.00E-7
	x[C.offset_pS6_CelllineACHN_DM] = 1.00E-7
	x[C.offset_pS6_CelllineADRr] = 1.00E-7
	x[C.offset_pS6_CelllineADRr_B] = 1.00E-7
	x[C.offset_pS6_CelllineADRr_B2] = 1.00E-7
	x[C.offset_pS6_CelllineBT20] = 1.00E-7
	x[C.offset_pS6_CelllineBxPc3] = 1.00E-7
	x[C.offset_pS6_CelllineH322M] = 1.00E-7
	x[C.offset_pS6_CelllineIGROV1] = 1.00E-7
	x[C.offset_tEGFR_CelllineA431] = 4.19E-2
	x[C.offset_tEGFR_CelllineACHN_197] = 1.70E2
	x[C.offset_tEGFR_CelllineACHN_200] = 1.46E2
	x[C.offset_tEGFR_CelllineACHN_218] = 3.91E-2
	x[C.offset_tEGFR_CelllineACHN_DM] = 5.74E3
	x[C.offset_tEGFR_CelllineADRr] = 1.38E3
	x[C.offset_tEGFR_CelllineADRr_B] = 2.42E-1
	x[C.offset_tEGFR_CelllineADRr_B2] = 1.35E1
	x[C.offset_tEGFR_CelllineBT20] = 3.70E3
	x[C.offset_tEGFR_CelllineBxPc3] = 6.50E-4
	x[C.offset_tEGFR_CelllineH322M] = 1.46E0
	x[C.offset_tEGFR_CelllineIGROV1] = 1.17E2
	x[C.offset_tErbB2_CelllineA431] = 1.00E2
	x[C.offset_tErbB2_CelllineACHN_197] = 1.30E-1
	x[C.offset_tErbB2_CelllineACHN_200] = 3.56E3
	x[C.offset_tErbB2_CelllineACHN_218] = 8.68E4
	x[C.offset_tErbB2_CelllineACHN_DM] = 2.45E-3
	x[C.offset_tErbB2_CelllineADRr] = 1.24E2
	x[C.offset_tErbB2_CelllineADRr_B] = 1.98E0
	x[C.offset_tErbB2_CelllineADRr_B2] = 1.86E-4
	x[C.offset_tErbB2_CelllineBT20] = 1.51E1
	x[C.offset_tErbB2_CelllineBxPc3] = 2.70E0
	x[C.offset_tErbB2_CelllineH322M] = 7.91E0
	x[C.offset_tErbB2_CelllineIGROV1] = 7.19E-2
	x[C.offset_tErbB3_CelllineA431] = 1.54E2
	x[C.offset_tErbB3_CelllineACHN_197] = 2.20E-1
	x[C.offset_tErbB3_CelllineACHN_200] = 5.18E-1
	x[C.offset_tErbB3_CelllineACHN_218] = 1.93E-3
	x[C.offset_tErbB3_CelllineACHN_DM] = 8.44E-5
	x[C.offset_tErbB3_CelllineADRr] = 1.17E2
	x[C.offset_tErbB3_CelllineADRr_B] = 3.83E2
	x[C.offset_tErbB3_CelllineADRr_B2] = 1.07E4
	x[C.offset_tErbB3_CelllineBT20] = 6.46E1
	x[C.offset_tErbB3_CelllineBxPc3] = 4.88E-1
	x[C.offset_tErbB3_CelllineH322M] = 7.86E-1
	x[C.offset_tErbB3_CelllineIGROV1] = 5.93E-5
	x[C.offset_tIGF1R_CelllineA431] = 2.81E-1
	x[C.offset_tIGF1R_CelllineACHN_197] = 1.06E1
	x[C.offset_tIGF1R_CelllineACHN_200] = 2.38E1
	x[C.offset_tIGF1R_CelllineACHN_218] = 5.94E-1
	x[C.offset_tIGF1R_CelllineACHN_DM] = 7.67E-3
	x[C.offset_tIGF1R_CelllineADRr] = 2.06E-3
	x[C.offset_tIGF1R_CelllineADRr_B] = 1.36E2
	x[C.offset_tIGF1R_CelllineADRr_B2] = 5.31E-4
	x[C.offset_tIGF1R_CelllineBT20] = 2.86E-1
	x[C.offset_tIGF1R_CelllineBxPc3] = 2.20E0
	x[C.offset_tIGF1R_CelllineH322M] = 4.21E-2
	x[C.offset_tIGF1R_CelllineIGROV1] = 2.51E-4

	x[C.scale_Ligand] = 37810.0
	x[C.scale_pAKT_CelllineA431] = 7.83E0
	x[C.scale_pAKT_CelllineACHN_197] = 3.44E4
	x[C.scale_pAKT_CelllineACHN_200] = 5.18E5
	x[C.scale_pAKT_CelllineACHN_218] = 1.35E3
	x[C.scale_pAKT_CelllineACHN_DM] = 1.62E5
	x[C.scale_pAKT_CelllineADRr] = 1.31E1
	x[C.scale_pAKT_CelllineADRr_B] = 5.65E3
	x[C.scale_pAKT_CelllineADRr_B2] = 4.18E2
	x[C.scale_pAKT_CelllineBT20] = 4.38E0
	x[C.scale_pAKT_CelllineBxPc3] = 9.87E-1
	x[C.scale_pAKT_CelllineH322M] = 7.14E-1
	x[C.scale_pAKT_CelllineIGROV1] = 1.24E1
	x[C.scale_pEGFR_CelllineA431] = 7.89E2
	x[C.scale_pEGFR_CelllineACHN_197] = 9.71E4
	x[C.scale_pEGFR_CelllineACHN_200] = 3.13E-1
	x[C.scale_pEGFR_CelllineACHN_218] = 1.72E-4
	x[C.scale_pEGFR_CelllineACHN_DM] = 1.43E4
	x[C.scale_pEGFR_CelllineADRr] = 7.54E-1
	x[C.scale_pEGFR_CelllineADRr_B] = 1.41E3
	x[C.scale_pEGFR_CelllineADRr_B2] = 1.90E2
	x[C.scale_pEGFR_CelllineBT20] = 1.39E3
	x[C.scale_pEGFR_CelllineBxPc3] = 2.45E1
	x[C.scale_pEGFR_CelllineH322M] = 3.30E1
	x[C.scale_pEGFR_CelllineIGROV1] = 5.01E3
	x[C.scale_pERK_CelllineA431] = 4.18E-1
	x[C.scale_pERK_CelllineACHN_197] = 3.40E4
	x[C.scale_pERK_CelllineACHN_200] = 9.02E4
	x[C.scale_pERK_CelllineACHN_218] = 3.33E4
	x[C.scale_pERK_CelllineACHN_DM] = 4.58E4
	x[C.scale_pERK_CelllineADRr] = 8.92E-1
	x[C.scale_pERK_CelllineADRr_B] = 5.76E3
	x[C.scale_pERK_CelllineADRr_B2] = 2.26E2
	x[C.scale_pERK_CelllineBT20] = 5.72E-1
	x[C.scale_pERK_CelllineBxPc3] = 9.12E-1
	x[C.scale_pERK_CelllineH322M] = 3.85E-1
	x[C.scale_pERK_CelllineIGROV1] = 5.80E-1
	x[C.scale_pErbB2_CelllineA431] = 8.48E2
	x[C.scale_pErbB2_CelllineACHN_197] = 3.89E5
	x[C.scale_pErbB2_CelllineACHN_200] = 3.97E-2
	x[C.scale_pErbB2_CelllineACHN_218] = 2.82E5
	x[C.scale_pErbB2_CelllineACHN_DM] = 2.11E3
	x[C.scale_pErbB2_CelllineADRr] = 6.91E2
	x[C.scale_pErbB2_CelllineADRr_B] = 2.08E3
	x[C.scale_pErbB2_CelllineADRr_B2] = 8.00E1
	x[C.scale_pErbB2_CelllineBT20] = 2.97E2
	x[C.scale_pErbB2_CelllineBxPc3] = 3.79E0
	x[C.scale_pErbB2_CelllineH322M] = 5.27E0
	x[C.scale_pErbB2_CelllineIGROV1] = 6.37E2
	x[C.scale_pErbB3_CelllineA431] = 1.54E3
	x[C.scale_pErbB3_CelllineACHN_197] = 1.71E3
	x[C.scale_pErbB3_CelllineACHN_200] = 5.63E-1
	x[C.scale_pErbB3_CelllineACHN_218] = 3.95E5
	x[C.scale_pErbB3_CelllineACHN_DM] = 1.75E-3
	x[C.scale_pErbB3_CelllineADRr] = 1.02E3
	x[C.scale_pErbB3_CelllineADRr_B] = 6.75E2
	x[C.scale_pErbB3_CelllineADRr_B2] = 1.31E-4
	x[C.scale_pErbB3_CelllineBT20] = 5.42E2
	x[C.scale_pErbB3_CelllineBxPc3] = 2.76E-1
	x[C.scale_pErbB3_CelllineH322M] = 2.71E0
	x[C.scale_pErbB3_CelllineIGROV1] = 1.82E1
	x[C.scale_pIGF1R_CelllineA431] = 1.10E3
	x[C.scale_pIGF1R_CelllineACHN_197] = 6.62E2
	x[C.scale_pIGF1R_CelllineACHN_200] = 4.54E2
	x[C.scale_pIGF1R_CelllineACHN_218] = 2.31E-4
	x[C.scale_pIGF1R_CelllineACHN_DM] = 1.05E1
	x[C.scale_pIGF1R_CelllineADRr] = 1.97E2
	x[C.scale_pIGF1R_CelllineADRr_B] = 1.44E-2
	x[C.scale_pIGF1R_CelllineADRr_B2] = 2.17E5
	x[C.scale_pIGF1R_CelllineBT20] = 9.08E1
	x[C.scale_pIGF1R_CelllineBxPc3] = 3.43E2
	x[C.scale_pIGF1R_CelllineH322M] = 1.19E4
	x[C.scale_pIGF1R_CelllineIGROV1] = 2.35E3
	x[C.scale_pMEK_CelllineA431] = 2.20E3
	x[C.scale_pMEK_CelllineACHN_197] = 2.14E-4
	x[C.scale_pMEK_CelllineACHN_200] = 6.79E-4
	x[C.scale_pMEK_CelllineACHN_218] = 2.06E1
	x[C.scale_pMEK_CelllineACHN_DM] = 6.92E0
	x[C.scale_pMEK_CelllineADRr] = 6.76E-4
	x[C.scale_pMEK_CelllineADRr_B] = 4.70E2
	x[C.scale_pMEK_CelllineADRr_B2] = 2.51E3
	x[C.scale_pMEK_CelllineBT20] = 3.66E3
	x[C.scale_pMEK_CelllineBxPc3] = 1.34E3
	x[C.scale_pMEK_CelllineH322M] = 3.51E2
	x[C.scale_pMEK_CelllineIGROV1] = 7.66E3
	x[C.scale_pMet_CelllineA431] = 6.41E-3
	x[C.scale_pMet_CelllineACHN_197] = 2.83E3
	x[C.scale_pMet_CelllineACHN_200] = 2.52E3
	x[C.scale_pMet_CelllineACHN_218] = 1.24E3
	x[C.scale_pMet_CelllineACHN_DM] = 8.92E3
	x[C.scale_pMet_CelllineADRr] = 9.16E0
	x[C.scale_pMet_CelllineADRr_B] = 1.52E-2
	x[C.scale_pMet_CelllineADRr_B2] = 6.40E-2
	x[C.scale_pMet_CelllineBT20] = 9.33E-4
	x[C.scale_pMet_CelllineBxPc3] = 4.84E3
	x[C.scale_pMet_CelllineH322M] = 6.53E-3
	x[C.scale_pMet_CelllineIGROV1] = 3.61E-4
	x[C.scale_pS6K1_CelllineA431] = 5.92E-1
	x[C.scale_pS6K1_CelllineACHN_197] = 4.40E5
	x[C.scale_pS6K1_CelllineACHN_200] = 3.76E-4
	x[C.scale_pS6K1_CelllineACHN_218] = 1.71E4
	x[C.scale_pS6K1_CelllineACHN_DM] = 1.63E-1
	x[C.scale_pS6K1_CelllineADRr] = 1.39E1
	x[C.scale_pS6K1_CelllineADRr_B] = 4.00E5
	x[C.scale_pS6K1_CelllineADRr_B2] = 1.14E0
	x[C.scale_pS6K1_CelllineBT20] = 6.97E4
	x[C.scale_pS6K1_CelllineBxPc3] = 4.69E2
	x[C.scale_pS6K1_CelllineH322M] = 3.22E2
	x[C.scale_pS6K1_CelllineIGROV1] = 6.14E4
	x[C.scale_pS6_CelllineA431] = 5.45E2
	x[C.scale_pS6_CelllineACHN_197] = 2.75E2
	x[C.scale_pS6_CelllineACHN_200] = 4.86E3
	x[C.scale_pS6_CelllineACHN_218] = 2.30E5
	x[C.scale_pS6_CelllineACHN_DM] = 6.14E4
	x[C.scale_pS6_CelllineADRr] = 3.48E2
	x[C.scale_pS6_CelllineADRr_B] = 5.72E4
	x[C.scale_pS6_CelllineADRr_B2] = 1.70E0
	x[C.scale_pS6_CelllineBT20] = 2.40E2
	x[C.scale_pS6_CelllineBxPc3] = 4.10E1
	x[C.scale_pS6_CelllineH322M] = 2.65E1
	x[C.scale_pS6_CelllineIGROV1] = 2.33E2
	x[C.scale_tEGFR_CelllineA431] = 1.16E2
	x[C.scale_tEGFR_CelllineACHN_197] = 1.64E-2
	x[C.scale_tEGFR_CelllineACHN_200] = 3.71E-2
	x[C.scale_tEGFR_CelllineACHN_218] = 2.02E5
	x[C.scale_tEGFR_CelllineACHN_DM] = 2.42E3
	x[C.scale_tEGFR_CelllineADRr] = 8.24E-4
	x[C.scale_tEGFR_CelllineADRr_B] = 2.74E5
	x[C.scale_tEGFR_CelllineADRr_B2] = 2.04E4
	x[C.scale_tEGFR_CelllineBT20] = 8.20E0
	x[C.scale_tEGFR_CelllineBxPc3] = 8.62E-1
	x[C.scale_tEGFR_CelllineH322M] = 7.91E-1
	x[C.scale_tEGFR_CelllineIGROV1] = 2.57E1
	x[C.scale_tErbB2_CelllineA431] = 1.67E1
	x[C.scale_tErbB2_CelllineACHN_197] = 1.70E5
	x[C.scale_tErbB2_CelllineACHN_200] = 4.55E3
	x[C.scale_tErbB2_CelllineACHN_218] = 2.84E-4
	x[C.scale_tErbB2_CelllineACHN_DM] = 3.45E1
	x[C.scale_tErbB2_CelllineADRr] = 2.00E0
	x[C.scale_tErbB2_CelllineADRr_B] = 7.73E3
	x[C.scale_tErbB2_CelllineADRr_B2] = 3.40E4
	x[C.scale_tErbB2_CelllineBT20] = 7.52E0
	x[C.scale_tErbB2_CelllineBxPc3] = 1.00E-4
	x[C.scale_tErbB2_CelllineH322M] = 1.00E-4
	x[C.scale_tErbB2_CelllineIGROV1] = 9.41E-1
	x[C.scale_tErbB3_CelllineA431] = 4.57E1
	x[C.scale_tErbB3_CelllineACHN_197] = 3.67E3
	x[C.scale_tErbB3_CelllineACHN_200] = 4.08E0
	x[C.scale_tErbB3_CelllineACHN_218] = 9.14E-2
	x[C.scale_tErbB3_CelllineACHN_DM] = 9.27E1
	x[C.scale_tErbB3_CelllineADRr] = 1.25E0
	x[C.scale_tErbB3_CelllineADRr_B] = 6.25E1
	x[C.scale_tErbB3_CelllineADRr_B2] = 1.15E-2
	x[C.scale_tErbB3_CelllineBT20] = 9.93E-2
	x[C.scale_tErbB3_CelllineBxPc3] = 5.74E-4
	x[C.scale_tErbB3_CelllineH322M] = 3.69E-4
	x[C.scale_tErbB3_CelllineIGROV1] = 4.18E-1
	x[C.scale_tIGF1R_CelllineA431] = 2.26E1
	x[C.scale_tIGF1R_CelllineACHN_197] = 3.70E5
	x[C.scale_tIGF1R_CelllineACHN_200] = 6.73E0
	x[C.scale_tIGF1R_CelllineACHN_218] = 2.35E3
	x[C.scale_tIGF1R_CelllineACHN_DM] = 2.39E3
	x[C.scale_tIGF1R_CelllineADRr] = 2.03E1
	x[C.scale_tIGF1R_CelllineADRr_B] = 1.63E1
	x[C.scale_tIGF1R_CelllineADRr_B2] = 2.51E0
	x[C.scale_tIGF1R_CelllineBT20] = 1.08E1
	x[C.scale_tIGF1R_CelllineBxPc3] = 1.70E-5
	x[C.scale_tIGF1R_CelllineH322M] = 2.17E0
	x[C.scale_tIGF1R_CelllineIGROV1] = 1.45E1

	return x


def initial_values():

    y0 = [0] * V.NUM

    y0[V.dose_EGF] = 0.0
    y0[V.dose_HGF] = 0.0
    y0[V.RTKph] = 0.618911491797731
    y0[V.dose_IGF1] = 0.0
    y0[V.dose_HRG] = 0.0
    y0[V.dose_BTC] = 0.0
    y0[V.EGFR] = 17.8621933083143
    y0[V.EGFR_EGF] = 0.0
    y0[V.EGFR_BTC] = 0.0
    y0[V.pEGFRd] = 5.12011130278668E-4
    y0[V.pEGFRi] = 2.79223720669219E-5
    y0[V.pEGFRi_ph] = 1.4687856601509E-4
    y0[V.EGFRi] = 1.37508187561569E-8
    y0[V.ErbB2] = 5.70185166249099
    y0[V.pErbB2] = 2.20826262632109E-4
    y0[V.pErbB2i] = 2.35511421879916E-4
    y0[V.ErbB2i] = 44.4835113645705
    y0[V.pErbB2i_ph] = 0.0176807431775487
    y0[V.pErbB12] = 5.37306859494303E-4
    y0[V.pErbB12i] = 0.00144471037537624
    y0[V.pErbB12i_ph] = 7.55785246775258E-7
    y0[V.ErbB3] = 2.47992342696256
    y0[V.ErbB3_HRG] = 0.0
    y0[V.pErbB3d] = 1.8018926279905E-4
    y0[V.pErbB3i] = 0.00348026782363202
    y0[V.pErbB3i_ph] = 0.0108514486150842
    y0[V.ErbB3i] = 34.3224209878038
    y0[V.pErbB13] = 3.32712466211581E-5
    y0[V.pErbB13i] = 6.69142208681604E-4
    y0[V.pErbB13i_ph] = 1.13074197411592E-10
    y0[V.pErbB32] = 1.30059969850016E-4
    y0[V.pErbB32i] = 2.34208535412277E-4
    y0[V.pErbB32i_ph] = 5.93238579976826E-4
    y0[V.IGF1R] = 4.73494621402554
    y0[V.IGF1R_IGF1] = 0.0
    y0[V.pIGF1Rd] = 2.6239258403409E-5
    y0[V.pIGF1Ri] = 4.2395816408642E-5
    y0[V.pIGF1Ri_ph] = 7.91085256809129E-5
    y0[V.IGF1Ri] = 5.24785159589016E-5
    y0[V.Met] = 7.90290414461229
    y0[V.Met_HGF] = 0.0
    y0[V.pMetd] = 6.24560598662565E-7
    y0[V.pMeti] = 1.0060257690714E-6
    y0[V.pMeti_ph] = 4.79508059771836E-5
    y0[V.Meti] = 45.960014100956
    y0[V.pMetErbB3] = 0.0645520569171923
    y0[V.pMetErbB3i] = 0.0402793824584546
    y0[V.pMetErbB3i_ph] = 0.0249293726860515
    y0[V.pMetEGFR] = 0.00185677841647765
    y0[V.pMetEGFRi] = 0.00172863499055847
    y0[V.pMetEGFRi_ph] = 7.58806259570584E-8
    y0[V.MEK] = 4.2412663925898
    y0[V.pMEK] = 1.014543757693E-4
    y0[V.ERK] = 6922167.20947519
    y0[V.pERK] = 0.334274838149849
    y0[V.AKT] = 2.70857345464684
    y0[V.pAKT] = 0.0263677143207646
    y0[V.S6K1] = 0.00194894402116983
    y0[V.pS6K1] = 0.00124327830478657
    y0[V.S6] = 145.50079875804
    y0[V.pS6] = 0.0171533722671392
    
    return y0