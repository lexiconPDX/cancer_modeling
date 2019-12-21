from .name2idx import parameters as C
from .name2idx import variables as V

def diffeq(y,t,*x):

    v=[0]*26

    v[1]  = x[C.k1f]*y[V.R]*y[V.EGF] - x[C.k1b]*y[V.Ra]
    v[2]  = x[C.k2f]*y[V.Ra]*y[V.Ra] - x[C.k2b]*y[V.R2]
    v[3]  = x[C.k3f]*y[V.R2] - x[C.k3b]*y[V.RP]
    v[4]  = x[C.V4]*y[V.RP]/(x[C.K4]+y[V.RP])
    v[5]  = x[C.k5f]*y[V.RP]*y[V.PLCg] - x[C.k5b]*y[V.R_PL]
    v[6]  = x[C.k6f]*y[V.R_PL] - x[C.k6b]*y[V.R_PLP]
    v[7]  = x[C.k7f]*y[V.R_PLP] - x[C.k7b]*y[V.RP]*y[V.PLCgP]
    v[8]  = x[C.V8]*y[V.PLCgP]/(x[C.K8]+y[V.PLCgP])
    v[9]  = x[C.k9f]*y[V.RP]*y[V.Grb2]- x[C.k9b]*y[V.R_G]
    v[10] = x[C.k10f]*y[V.R_G]*y[V.SOS] - x[C.k10b]*y[V.R_G_S]
    v[11] = x[C.k11f]*y[V.R_G_S] - x[C.k11b]*y[V.RP]*y[V.G_S]
    v[12] = x[C.k12f]*y[V.G_S] - x[C.k12b]*y[V.Grb2]*y[V.SOS]
    v[13] = x[C.k13f]*y[V.RP]*y[V.Shc] - x[C.k13b]*y[V.R_Sh]
    v[14] = x[C.k14f]*y[V.R_Sh] - x[C.k14b]*y[V.R_ShP]
    v[15] = x[C.k15f]*y[V.R_ShP] - x[C.k15b]*y[V.ShP]*y[V.RP]
    v[16] = x[C.V16]*y[V.ShP]/(x[C.K16]+y[V.ShP])
    v[17] = x[C.k17f]*y[V.R_ShP]*y[V.Grb2] - x[C.k17b]*y[V.R_Sh_G]
    v[18] = x[C.k18f]*y[V.R_Sh_G] - x[C.k18b]*y[V.RP]*y[V.Sh_G]
    v[19] = x[C.k19f]*y[V.R_Sh_G]*y[V.SOS] - x[C.k19b]*y[V.R_Sh_G_S]
    v[20] = x[C.k20f]*y[V.R_Sh_G_S] - x[C.k20b]*y[V.Sh_G_S]*y[V.RP]
    v[21] = x[C.k21f]*y[V.ShP]*y[V.Grb2] - x[C.k21b]*y[V.Sh_G]
    v[22] = x[C.k22f]*y[V.Sh_G]*y[V.SOS] - x[C.k22b]*y[V.Sh_G_S]
    v[23] = x[C.k23f]*y[V.Sh_G_S] - x[C.k23b]*y[V.ShP]*y[V.G_S]
    v[24] = x[C.k24f]*y[V.R_ShP]*y[V.G_S] - x[C.k24b]*y[V.R_Sh_G_S]
    v[25] = x[C.k25f]*y[V.PLCgP] - x[C.k25b]*y[V.PLCgP_I]

    dydt=[0]*V.len_f_vars

    dydt[V.EGF]      = -v[1]
    dydt[V.R]        = -v[1]
    dydt[V.Ra]       =  v[1]-2*v[2]
    dydt[V.R2]       =  v[2]-v[3]+v[4]
    dydt[V.RP]       =  v[3]-v[4]-v[5]+v[7]-v[9]+v[11]-v[13]+v[15]+v[18]+v[20]
    dydt[V.PLCg]     = -v[5]+v[8]
    dydt[V.R_PL]     =  v[5]-v[6]
    dydt[V.R_PLP]    =  v[6]-v[7]
    dydt[V.PLCgP]    =  v[7]-v[8]-v[25]
    dydt[V.Grb2]     = -v[9]+v[12]-v[17]-v[21]
    dydt[V.R_G]      =  v[9]-v[10]
    dydt[V.SOS]      = -v[10]+v[12]-v[19]-v[22]
    dydt[V.R_G_S]    =  v[10]-v[11]
    dydt[V.G_S]      =  v[11]-v[12]+v[23]-v[24]
    dydt[V.Shc]      = -v[13]+v[16]
    dydt[V.R_Sh]     =  v[13]-v[14]
    dydt[V.R_ShP]    =  v[14]-v[15]-v[17]-v[24]
    dydt[V.ShP]      =  v[15]-v[16]-v[21]+v[23]
    dydt[V.R_Sh_G]   =  v[17]-v[18]-v[19]
    dydt[V.Sh_G]     =  v[18]+v[21]-v[22]
    dydt[V.R_Sh_G_S] =  v[19]-v[20]+v[24]
    dydt[V.Sh_G_S]   =  v[20]+v[22]-v[23]
    dydt[V.PLCgP_I]  =  v[25]

    return dydt