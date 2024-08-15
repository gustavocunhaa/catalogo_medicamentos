from pydantic import BaseModel

class ColetaInfo(BaseModel):
    lista_ids: list
    atributos: list

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "lista_ids": [1, 2, 3],
                    "atributos": ['produto', 
                                  'principio_ativo', 'tipo_produto',
                                  'fabricante',
                                  'especialidade', 'classe_terapeutica', 'categoria',
                                  'codigo_barras', 'tipo_receita']
                }
            ]
        }
    }

class BuscaProdutos(BaseModel):
    busca: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "busca": "Losartana"
                }
            ]
        }
    }

class MontaVetor(BaseModel):
    texto: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "texto": "Hipovas Besilato De Anlodipino + Losartana Potássica Genérico Anti-Hipertensivo Antagonistas Da Angiotensina Ii Associados A Antagonistas Do Cálcio Cardiologia Nova Química"
                }
            ]
        }
    }

class DistanciaVetores(BaseModel):
    vetor: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "vetor": "[0.23708826, -0.32627442, 0.47324193, 0.15548621, 0.31450653, 0.02363802, -0.0057975673, -0.1336786, 0.071723044, 0.18438037, 0.32842997, -0.037617132, 0.0059807654, 0.18279044, -0.028794356, -0.3464693, 0.034517214, -0.12728778, -0.22893278, 0.032507002, -0.24024294, 0.16695637, 0.2779869, 0.3303741, 0.00931802, 0.2913501, 0.11965529, 0.21712758, 0.23543745, -0.55104154, 0.18071, 0.040649515, -0.5015423, 0.085133694, 0.24427089, -0.28981432, 0.254373, 0.14992015, 0.14953478, -0.5506154, 0.14639013, -0.11757129, -0.08730194, -0.036250178, -0.07740155, -0.11320681, -0.1828289, 0.30154827, -0.67382586, -0.45088217, -0.24292882, -0.15048067, 0.39149734, 0.26082647, -0.045177486, -0.096804954, 0.04803827, -0.58067, 0.060199976, -0.28723982, 0.019638382, 0.430819, 0.13179646, 0.008581715, 0.1943344, 0.27107146, -0.029202152, -0.38067225, 0.30301493, 0.5541005, 0.13328257, -0.0960926, 0.37251458, -0.17421211, -0.7464069, 0.43515784, 0.026383983, -0.05128073, 0.0021684302, -0.13651732, 0.13489576, 0.13563582, -1.1490874, 0.19058722, -0.32295412, 0.3335422, 0.056296926, -0.23178908, 0.4242868, -0.5415458, 0.29057539, 0.2720803, 0.42676094, -0.17223959, -0.44274268, 0.053436723, 0.016112093, 0.10744391, -0.3233387, 0.028577661, 0.09110943, -0.26912326, 0.70308864, 0.032591864, 0.4425078, -0.17504221, 0.2459512, 0.32574326, -0.21511991, 0.55709285, 0.32388008, 0.64810956, 0.33288518, -0.20113075, 0.22423907, -0.23801325, 5.624471e-05, 0.07289682, 0.50352585, -0.119761296, 0.05392719, -0.23804519, -0.29247075, -0.47516838, 0.03289881, 0.2571852, -0.020365605, 0.025987413, 0.25812206, -0.5385083, -0.30606064, 0.020685025, 0.21605986, 0.27184027, 0.37915337, 0.018341122, 0.3722184, -0.3365043, 0.47798392, 0.22463936, -0.2284866, 0.08345181, -0.41366538, -0.1626695, 0.05221493, -0.0941585, -0.67824906, 0.9124168, -0.30376896, 0.34520498, 0.058182035, 0.062153306, 0.1851208, 0.48878416, 0.05671019, 0.40388158, 0.10209163, -0.36835626, 0.24752274, 0.37614465, -0.041459795, -0.4314821, -0.3217951, -0.21610053, -0.12903409, 0.15907282, 0.13129961, -0.58079135, -0.20462087, -0.04862558, -0.011776869, 0.08047878, -0.12163964, -0.21744105, -0.32568935, 0.06134467, 0.16734454, -0.013049702, -0.22747897, -0.40539584, 0.18966319, -0.038035136, -0.14387254, 0.22644301, 0.19856681, -0.16300991, 0.07512135, -0.24961735, -0.06259157, -0.7120369, -0.07348697, 0.1686982, -0.3925123, 0.01635348, -0.07408328, -0.04080839, 0.015247, -0.26617572, 0.023435049, -0.38968262, 0.19932191, 0.24498814, 0.044985253, -0.37842658, -0.24390434, 0.25143483, 0.21947096, -0.23802221, 0.15778148, 0.05882115, -0.2209919, 0.24148923, -0.07672676, -0.19599527, 1.0642445, 0.18867314, -0.14669447, 0.24195118, 0.36966184, 0.40178663, -0.0041065165, -0.07953142, -0.401135, 0.15024593, -0.015667405, -0.5172006, 0.41225556, 0.14425582, -0.03245587, -0.5958997, -0.4506107, -0.47719446, -0.36641762, 0.26401073, -0.07635944, 0.13650627, 0.032950252, -0.42525733, -0.23491329, 0.0085455, -0.118296824, -0.49889487, -0.09814666, 0.077056915, 0.16232213, -0.211603, -0.8045422, -0.23697852, -0.032237284, -0.18671156, -0.35597053, 0.03590333, 0.14306189, -0.3413553, -0.22811002, -0.07052728, 0.27467343, -0.050930757, 0.2303116, -0.23583294, 0.028909206, -0.21233092, -0.16582191, 0.4753588, 0.25855368, 0.21445726, 0.398328, 0.034316994, 0.21728608, 0.060839847, -0.5466527, 0.3776121, 0.024864443, 0.053209227, -0.13179173, -0.0475061, 0.18575312, 0.025802808, -0.29619214, 0.0586705, 0.41044444, -0.22797184, -0.06106408, 0.26978102, 0.5686601, -0.03423646, 0.061417647, 0.27224404, -0.23067401, -0.09817767, -0.97134346, -0.39387894, 0.12216166, 0.093229495, -0.22230846, -0.47507384, -0.42523536, 0.18570222, 0.21715166, -0.34254584, -0.015783997, 0.29634747, -0.23644578, -0.18585287, 0.4989766, 0.3595489, 0.2813289, -0.36310446, 0.12203246, 0.12243331, -0.13000552, -0.29801747, 0.13759397, 0.14515822, 0.18482012, 0.19845766, 0.54008996, -0.19755423, -0.48409742, 0.24666214, -0.26164335, 0.15795651, 0.3474823, 0.31751132, 0.10660418, 0.4040972, 0.13536063, -0.13398962, 0.061828766, 0.15819557, -0.17109776, -0.08589942, -0.107724875, -0.0010859817, 0.023917453, -0.23197505, -0.013697803, -0.089766115, -0.718347, -0.4321036, -0.2415345, 0.02372896, 0.07011112, -0.011735616, 0.20789017, -0.09028186, -0.12583609, 0.06981349, -0.4507347, -0.5752251, -0.37300402, 0.23748392, -0.08923998, 0.22867282, -0.014215249, 0.15649682, -0.28783375, -0.008039977, 0.07410098, 0.12749362, -0.08540498, 0.34153438, 0.059258915, -0.20294352, -0.397422, 0.033299595, 0.22300223, -0.19839631, 0.40097424, 0.4175607, 0.02502925, -0.03674933, -0.5349395, -0.034100477, -0.018339518, 0.08534723, 0.08237731, -0.16844223, -0.13772015, -0.25541538, 0.30331704, -0.4957589, 0.043665595, -0.3863064, -0.1164014, -0.054808035, -0.09657101, 0.17065871, -0.012102657, 0.22459258, -0.17122088, 0.1201014, 0.07330106, -0.049883556, -0.008927026, -0.19140813, 0.32216853, 0.1773219, -0.2034323, -0.0036978081, -0.27498, 0.15119946, 0.16218711, 0.33588293, -0.048710126, 0.5278526, -0.100032896, 0.29973376, -0.22065149, 0.24985577, -0.16995889, 0.09861959, 0.21488765, -0.023016682, 0.24687138, -0.2935262, 0.040390015, 0.26102433, -0.3669336, 0.5039345, 0.19821419, -0.030506466, 0.28110486, -0.7486115, -0.091148056, -0.2896423, 0.20240599, 0.20992826, -0.6604685, -0.09268937, -0.33703783, 0.20080955, -0.34538573, 0.11668142, -0.110739276, 0.02757944, 0.07358185, -0.34070757, -0.16897929, 0.04152041, 0.39081398, 0.053110104, 0.26999134, 0.22974053, 0.10214391, 0.2117187, 0.32076538, -0.5195101, -0.14451033, 0.095117815, -0.10215104, -0.601609, 0.16372308, 0.69305736, -0.05789485, -0.32886568, -0.21382104, 0.06498229, -0.16263913, -0.3712269, -0.33146435, 0.21131662, 0.00422769, -0.15783402, -0.10540377, 0.015565421, 0.0053850017, 0.13301553, 0.14154159, 0.18782187, -0.7658108, 0.15288836, -0.0909376, -0.14224538, 0.18687238, 0.14173192, -0.090992816, 0.12327961, 0.023085447, -0.2071076, -0.4802236, 0.30508876, -0.06049147, -0.11004569, 0.2207285, 0.55323124, -0.3477218, -0.07947663, 0.5967162, 0.056642737, 0.22898826, 0.38031235, -0.13899069, -0.59815484, -0.13645406, 0.29386467, -0.50186604, -0.30287728, 0.53535193, 1.0143919, -0.36680275, -0.075485505, -0.2224922, 0.44791913, 0.15194328, -0.31545663, -0.57959944, 0.22406913, 0.1449363, -0.2224559, 0.10587015, -0.6749293, 0.4680506, -0.054025993, 0.40741423, 0.19845192, 0.055491403, 0.2581674, -0.10456702, 0.4803955, -0.28279757, 0.120037906, 0.3460327, -0.093381636, -0.60817873, -0.12667166, -0.14013134, -0.46511504, 0.070617825, -0.19130914, -0.25195575, 0.5170426, -0.26054898, 0.09018145, -0.22489977, 0.12416468, 0.15779884, 0.39826158, 0.13044937, 0.49321595, 0.21467048, -0.020294977, -0.05353048, -0.1316613, 0.22671759, -0.13493705, 0.012867945, 0.38292053, 0.27105668, -0.4965247, -0.27868262, -0.1312423, 0.013987768, 0.4000526, 0.020679463, 0.09736982, 0.20204896, -0.64993656, 0.4026737, 0.2244216, -0.16708165, -0.46090552, 0.08087472, 0.10778441, 0.113674946, 0.2402017, 0.26027304, -0.076143846, 0.33798605, 0.46814558, -0.03766144, 0.06732578, -0.38591716, 0.2166013, -0.13857313, 0.055336405, -0.5897128, -0.24988069, -0.043069575, 0.13096279, 0.020324338, 0.026515389, 0.0032396207, -0.20619215, 0.13852562, 0.07428736, 0.25229648, -0.05194616, 0.043907985, 0.014621856, -0.09926458, 0.040950425, 0.27319172, -0.67071074, 0.27489161, 0.061129402, 0.16232729, -0.010567062, 0.26110846, 0.015742956, -0.16150865, -0.00059532456, 0.04949558, -0.5857237, -0.5831193, 0.07759437, -0.107405625, 0.34910887, 0.09643255, -0.05731301, 0.2826325, 0.054149285, 0.14874212, 0.1783775, -0.3414068, -0.1341882, -0.016409209, -0.25070804, -0.32295477, 0.11891951, 0.0664635, 0.41305926, 0.3637678, -0.18654543, 0.12690258, -0.20143877, 0.092189215, 0.04281692, 0.054765984, -0.2752251, -0.03231229, 0.08626482, 0.52275586, -0.18884298, 0.20201948, 0.07927461, -0.10288852, -0.498107, -0.13303986, -0.030437922, -0.2891668, 0.68495625, -0.14221697, -0.15685116, 0.17052716, 0.10395099, 0.154311, 0.01958967, 0.13093437, 0.7002118, 0.08587241, -0.16640504, 0.1497998, -0.28729934, -0.13363634, -0.19278243, 0.34318867, -0.16529058, -0.09103963, 0.6698373, -0.076072685, 0.45462307, 0.6353053, -0.04141167, -0.33407065, 0.4250644, -0.37734607, -0.37926728, 0.12701777, 0.14516555, -0.44319224, -0.25754735, 0.30782992, 0.23412405, 0.117674604, 0.018661097, 0.20446663, -0.5419083, -0.08718959, -0.20271482, -0.4470496, -0.04028585, -0.016339049, -0.07946787, 0.23290774, -0.030418396, 0.018641183, 0.09769708, -0.3165027, 0.10216574, 0.050013136, -0.10109267, -0.28906998, -0.013279343, 0.121244855, -0.04912891, 0.01120432, -0.0050316476, 0.4369797, -0.66780365, -0.07766413, -0.27339023, 0.28085276, -0.3163362, -0.13700996, -0.033809952, -0.09321227, -0.6271666, 0.46582046, -0.22072445, 0.4586615, -0.2136367, -0.4492335, -0.061115973, -0.3101541, -0.6665111, -0.49865302, -0.301436, 0.051809497, 0.24576044, 0.5256011, 0.18155557, -0.11117743, 0.038103763, 0.08068862, 0.00011847858, 0.055680014, 0.15762526, 0.030948566, -0.12787461, 0.2521486, 1.6329974, 0.07152894, 0.15324806, 0.28940558, -0.09116463, 0.29018718, 0.37379888, -0.10981315, 0.21099682, -0.212987, -0.40006012, -0.08082651, -0.20171799, -0.14548099, -0.13456589, 0.1819802, -0.3077599, 0.05467565, -0.18229349, -0.36850777, -0.02184777, -0.28325602, 0.24497956, 0.17446128, 0.073707305, -0.5128194, -0.1886871, 0.31771952, -0.23690861, -0.16871364, -0.3608773, 0.09549455, -0.2343799, 0.096808515, 0.2945182, 0.25306034, -0.48887634]"}
            ]
        }
    }
