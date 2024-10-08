XSec = {
  #'DYJetsToLL_M-50'             : 6424.0,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYJetsToLL_M-50_TuneCP5"
  #'DY1JetsToLL_M-50'            : 964.0,   # TauFW/PicoProducer/utils/getXSec.sh:  9.640e+02 +- 3.774e-01 pb  using 100 files from /DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM
  #'DY2JetsToLL_M-50'            : 307.5,   # TauFW/PicoProducer/utils/getXSec.sh:  3.075e+02 +- 1.304e-01 pb  using 100 files from /DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM
  #'DY3JetsToLL_M-50'            : 91.27,   # TauFW/PicoProducer/utils/getXSec.sh:  9.127e+01 +- 4.079e-02 pb  using 100 files from /DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM
  #'DY4JetsToLL_M-50'            : 43.87,   # TauFW/PicoProducer/utils/getXSec.sh:  4.387e+01 +- 3.756e-02 pb  using 100 files from /DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM
  'DYJetsToLL_M-50'             : 5379.0,  # LO to be consistent with nJet split samples; https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYJetsToLL_M-50_TuneCP5"
  'DY1JetsToLL_M-50'            : 876.9,   # LO, https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DY1JetsToLL_M-50_TuneCP5"
  'DY2JetsToLL_M-50'            : 306.4,   # LO, https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DY2JetsToLL_M-50_TuneCP5"
  'DY3JetsToLL_M-50'            : 112.0,   # LO, https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DY3JetsToLL_M-50_TuneCP5"
  'DY4JetsToLL_M-50'            : 44.03,   # LO, https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DY4JetsToLL_M-50_TuneCP5"
  'DYJetsToLL_M-10to50'         : 20490.0, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYJetsToLL_M-10to50"
  'DYJetsToLL_M-50_NLO'          : 6077.22, # Actually NNLO, https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z
  'DYJetsToLL_M-50_Pt0-50_NLO'   : 1413.99, # 6077.22 * (nWeighted Pt0-50) / (nWeighted Inclusive)
  'DYJetsToLL_M-50_Pt50-100_NLO' : 378.97,  # 6077.22 * (nWeighted Pt50-100) / (nWeighted Inclusive)
  'DYJetsToLL_M-50_Pt100-250_NLO': 93.145,   # 6077.22 * (nWeighted Pt100-150) / (nWeighted Inclusive)
  'DYJetsToLL_M-50_Pt250-400_NLO': 3.7095,    # 6077.22 * (nWeighted Pt250-400) / (nWeighted Inclusive)
  'DYJetsToLL_M-50_Pt400-650_NLO': 0.51548,    # 6077.22 * (nWeighted Pt400-650) / (nWeighted Inclusive)
  'DYJetsToLL_M-50_Pt650-Inf_NLO': 0.048545,    # 6077.22 * (nWeighted Pt650-Inf) / (nWeighted Inclusive)  
  'WJetsToLNu_LO'               : 61526.7, # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#W_jets , apparently this is NNLO, while LO would be 53870 pb according to https://cms-gen-dev.cern.ch/xsdb/ -> k-factor is 1.1421
  'WJetsToLNu'                  : 61526.7, # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#W_jets , apparently this is NNLO, while NLO would be 67350 pb according to https://cms-gen-dev.cern.ch/xsdb/ -> k-factor is 0.9135 ; BUT, apparently with genXsecAnalyzer 6.043e+04 +- 1.302e+02 pb (https://indico.cern.ch/event/658253/contributions/2683676/attachments/1504862/2344638/20170807_VJets_GenMeeting.pdf), which results in k-factor 1.0181, or 1.0176 according to https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'W0JetsToLNu'                 : 50131.98,       # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'W1JetsToLNu_LO'              : 8927*1.1421,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=W1JetsToLNu"
  'W1JetsToLNu'                 : 8426.09,        # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'W2JetsToLNu_LO'              : 2809*1.1421,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=W2JetsToLNu"
  'W2JetsToLNu'                 : 3172.96,        # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'W3JetsToLNu_LO'              : 826.3*1.1421,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=W3JetsToLNu"
  'W4JetsToLNu_LO'              : 388.0*1.1421,   # TauFW/PicoProducer/utils/getXSec.sh:  3.880e+02 +- 1.727e-01 pb  using 100 files from /W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM
  'WJetsToLNu_HT70to100'        : 1264.0*1.1421,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-70To100"
  'WJetsToLNu_HT100to200'       : 1256.0*1.1421,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-100To200"
  'WJetsToLNu_HT200to400'       : 335.5*1.1421,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-200To400"
  'WJetsToLNu_HT400to600'       : 45.25*1.1421,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-400To600"
  'WJetsToLNu_HT600to800'       : 10.97*1.1421,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-600To800"
  'WJetsToLNu_HT800to1200'      : 4.933*1.1421,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-800To1200"
  'WJetsToLNu_HT1200to2500'     : 1.160*1.1421,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WJetsToLNu_HT-1200To2500"
  'WJetsToLNu_HT2500toInf'      : 0.02624*1.1421, # TauFW/PicoProducer/utils/getXSec.sh:  2.624e-02 +- 1.733e-05 pb  using 94 files from /WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM
  'WJetsToLNu_Pt100to250'       : 689.75,         # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'WJetsToLNu_Pt250to400'       : 24.507,         # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'WJetsToLNu_Pt400to600'       : 3.1101,         # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'WJetsToLNu_Pt600toInf'       : 0.46832,        # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
  'TTbar'                       : 833.90,  # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#TTbar
  'TTTo2L2Nu'                   : 88.51,   # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#TTbar, 833.90 * 0.324 * 0.324
  'TTToSemiLeptonic'            : 366.29,  # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#TTbar, 833.90 * 0.324 * 0.676 * 2
  'TTToHadronic'                : 378.93,  # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#TTbar, 833.90 * 0.676 * 0.676
  'ST_s-channel_leptonDecays'   : 3.344,   # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_s_channel_cross_secti, 10.32 * 0.324
  'ST_s-channel_hadronicDecays' : 6.976,   # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_s_channel_cross_secti, 10.32 * 0.676
  'ST_t-channel_top'            : 134.2,   # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_t_channel_cross
  'ST_t-channel_antitop'        : 80.0,    # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_t_channel_cross
  'ST_tW_top'                   : 39.65,   # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_tW_channel_cros , divided by 2 for top <-> antitop
  'ST_tW_antitop'               : 39.65,   # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_tW_channel_cros , divided by 2 for top <-> antitop
  'QCD_HT50to100'               : 186100000, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT100to200'              : 23630000,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT200to300'              : 1554000,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT300to500'              : 323800,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT500to700'              : 30280,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT700to1000'             : 6392,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT1000to1500'            : 1118,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT1500to2000'            : 108.9,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_HT2000toInf'             : 21.93,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_HT"
  'QCD_Pt15to30'                : 1244000000, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_15to30_TuneCP5"
  'QCD_Pt30to50'                : 106500000,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_30to50_TuneCP5"
  'QCD_Pt50to80'                : 15700000,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_50to80_TuneCP5"
  'QCD_Pt80to120'               : 2346000,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_80to120_TuneCP5"
  'QCD_Pt120to170'              : 407700,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_120to170_TuneCP5"
  'QCD_Pt170to300'              : 103700,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_170to300_TuneCP5"
  'QCD_Pt300to470'              : 6830,       # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_300to470_TuneCP5"
  'QCD_Pt470to600'              : 551.2,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_470to600_TuneCP5"
  'QCD_Pt600to800'              : 156.7,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_600to800_TuneCP5"
  'QCD_Pt800to1000'             : 26.25,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_800to1000_TuneCP5"
  'QCD_Pt1000to1400'            : 7.465,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_1000to1400_TuneCP5"
  'QCD_Pt1400to1800'            : 0.6487,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_1400to1800_TuneCP5"
  'QCD_Pt1800to2400'            : 0.08734,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_1800to2400_TuneCP5"
  'QCD_Pt2400to3200'            : 0.005237,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_2400to3200_TuneCP5"
  'QCD_Pt3200toInf'             : 0.0001352,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_Pt_3200toInf_TuneCP5"
  'WW'                          : 118.7,    # Value from https://arxiv.org/pdf/1408.5243.pdf , would do minus 3.974 from ggWW process if considered separately, which we don't do however (see https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson)
  'WWTo2L2Nu'                   : 12.60,    # 118.7 * (3*0.1086)*(3*0.1086)
  'WWTo1L1Nu2Q'                 : 52.14,    # 118.7 * (3*0.1086)*0.6741 * 2
  'WWTo4Q'                      : 53.94,    # 118.7 * 0.6741*0.6741
  'WZ'                          : 27.55,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZ_TuneCP5_13TeV-pythia8"
  'WZTo3L1Nu'                   : 5.257,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZTo3LNu_TuneCP5"
  'WZTo1L3Nu'                   : 3.414,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZTo1L3Nu"
  'WZTo2L2Q'                    : 6.565,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZTo2Q2L_mllmin4p0"
  'WZTo1L1Nu2Q'                 : 9.119,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZTo1L1Nu2Q"
  'ZZ'                          : 12.14,    # TauFW/PicoProducer/utils/getXSec.sh:  1.214e+01 +- 3.300e-03 pb (LO?) using all 42 files from /ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM (Note: The following ZZ->... values are different from simple XS(ZZ)*BR because it's actually always Z/gamma and includes all interference effects)
  'ZZTo4L'                      : 1.325,    # TauFW/PicoProducer/utils/getXSec.sh:  1.325e+00 +- 1.220e-03 pb (NLO, because XSDB had same value and says it's NLO) using 100 files from /ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM
  'ZZTo2L2Nu'                   : 0.9738,   # TauFW/PicoProducer/utils/getXSec.sh:  9.738e-01 +- 9.971e-04 pb (NLO, because XSDB had same value and says it's NLO) using 20 files (tried 100) from /ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM
  'ZZTo2L2Q'                    : 3.698,    # TauFW/PicoProducer/utils/getXSec.sh:  3.698e+00 +- 2.666e-03 pb (NLO) using 84 files (tried 100) from /ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM
  'ZZTo2Nu2Q'                   : 4.489,    # TauFW/PicoProducer/utils/getXSec.sh:  4.489e+00 +- 6.934e-03 pb (NLO) using 100 files from /ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM
  'ZZTo4Q'                      : 3.306,    # TauFW/PicoProducer/utils/getXSec.sh:  3.306e+00 +- 5.339e-03 pb (NLO) using all 68 files from /ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM
  'WWW'                         : 0.2158,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WWW_4F_TuneCP5"
  'WWZ'                         : 0.1707,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WWZ_4F_TuneCP5"
  'WZZ'                         : 0.05709,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZZ_TuneCP5"
  'ZZZ'                         : 0.01476,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=ZZZ_TuneCP5"
  'TTW'                         : 0.4611,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=ttWJets_TuneCP5" , NOTE: Pre-UL value!
  'TTZ'                         : 0.5407,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=ttZJets_TuneCP5" , NOTE: Pre-UL value!
  'SignalWto3pi'                : 193200*1e-6,  # Cross section: from SMP-20-004, the cross section times the "generic" leptonic branching fraction is 21040. SMP-18-011 measured the generic leptonic branching fractino to be 0.1089 ==> 21040 / 0.1089 = 193204.78 rounded with significant figures to 193200 (NOTE: It's sort of unclear at first whether associated BR is (W->lv) or (W->muv), but it should be the latter, because this gives a comparable result to the W+Jets->LNu cross section. In https://cds.cern.ch/record/2093537/files/SMP-15-004-pas.pdf , "lv" means any SPECIFIC lepton, and note that this value is similar to just the "ev" and "muv" values (Same as in PDG, BR W->lv isn't just the sum of ->ev, ->muv and ->tauv, but is "missing" factor 3)) ;; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'SignalWJetsTo3Pi'            : 193200*1e-6, # same as above ;; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'SignalW0JetsTo3Pi'           : 157419.438*1e-6,  # Full XSec * ( 0J / Inclusive ) ;; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'SignalW1JetsTo3Pi'           : 26458.76649*1e-6, # Full XSec * ( 1J / Inclusive ) ;; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'SignalW2JetsTo3Pi'           : 9963.412177*1e-6, # Full XSec * ( 2J / Inclusive ) ;; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'SignalWJetsTo3Pi_Plus'       : 111400*1e-6, # for NNLO, which is split by W boson charge, from SMP-20-004 (12130 / 0.1089 = 111400 w/ SigFigs);; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'SignalWJetsTo3Pi_Minus'       : 81800*1e-6, # for NNLO, which is split by W boson charge, from SMP-20-004 (8910 / 0.1089 = 81800 w/ SigFigs);; Signal BR: assuming 10^-6 (95% upper limit from first analysis)
  'ggH_TauTau'                  : 48.52*0.06256,  # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'VBF_TauTau'                  : 3.779*0.06256,  # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'WpH_TauTau'                  : 0.8380*0.06256, # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'WmH_TauTau'                  : 0.5313*0.06256, # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'ZH_TauTau'                   : 0.8824*0.06256, # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'ggH_WW'                      : 48.52*0.2152 * 0.324 * 0.324,      # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR , samples are 2L2Nu
  'VBF_WW'                      : 3.779*0.2152 * 0.324 * 0.324,      # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR , samples are 2L2Nu
  'WpH_WW'                      : 0.8380*0.2152,     # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'WmH_WW'                      : 0.5313*0.2152,     # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'ZH_WW'                       : 0.8824*0.2152,     # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'ggZH_WW'                     : 0.1227*0.2152 * 0.324 * 0.324,     # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.00 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR , samples are 2L2Nu
  'ttH_nonbb'                   : 0.5065*(1-0.5809), # XSec: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV , mH = 125.09 GeV ; BR: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'EWK_WplusToLNu'              : 39.13,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=EWKWPlus2Jets_WToLNu"
  'EWK_WminusToLNu'             : 32.05,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=EWKWMinus2Jets_WToLNu"
  'EWK_ZTo2L'                   : 6.214,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=EWKZ2Jets_ZToLL"
  'EWK_ZTo2Nu'                  : 10.68,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=EWKZ2Jets_ZToNuNu"
  'WGToLNuG'                    : 411.2   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WGToLNuG"
}

XSec_Unc = { # [Up, Down]   # References are the same as above, unless noted otherwise
  #'DYJetsToLL_M-50'             : [6424.0  +81.95,     6424.0  -81.95],
  #'DY1JetsToLL_M-50'            : [964.0   +0.3774,    964.0   -0.3774],
  #'DY2JetsToLL_M-50'            : [307.5   +0.1304,    307.5   -0.1304],
  #'DY3JetsToLL_M-50'            : [91.27   +0.04079,   91.27   -0.04079],
  #'DY4JetsToLL_M-50'            : [43.87   +0.03756,   43.87   -0.03756],
  'DYJetsToLL_M-50'             : [5379.0  +40.44,     5379.0  -40.44],
  'DY1JetsToLL_M-50'            : [876.9   +2.322,     876.9   -2.322],
  'DY2JetsToLL_M-50'            : [306.4   +0.8959,    306.4   -0.8959],
  'DY3JetsToLL_M-50'            : [112.0   +0.3402,    112.0   -0.3402],
  'DY4JetsToLL_M-50'            : [44.03   +0.1354,    44.03   -0.1354],
  'DYJetsToLL_M-10to50'         : [20490.0 +182.2,     20490.0 -182.2],
  'WJetsToLNu'                  : [61526.7 +2365.5,    61526.7 -2327.8],
  'W0JetsToLNu'                 : [50131.98+66.0,      50131.98-66.0],  # https://docs.google.com/spreadsheets/d/13wIO_T70JMHGu4lTXR9rRulVur7iqEjXw_V0T3N11TI/edit#gid=0
  'W1JetsToLNu'                 : [8426.09 +18.0,      8426.09 -18.0],  # https://docs.google.com/spreadsheets/d/13wIO_T70JMHGu4lTXR9rRulVur7iqEjXw_V0T3N11TI/edit#gid=0
  'W2JetsToLNu'                 : [3172.96 +12.0,      3172.96 -12.0],  # https://docs.google.com/spreadsheets/d/13wIO_T70JMHGu4lTXR9rRulVur7iqEjXw_V0T3N11TI/edit#gid=0
  #'WJetsToLNu_LO'               : XXX,
  #'W1JetsToLNu_LO'              : XXX,
  #'W2JetsToLNu_LO'              : XXX,
  #'W3JetsToLNu_LO'              : XXX,
  #'W4JetsToLNu_LO'              : XXX,
  #'TTbar'                       : 833.90,
  #'TTTo2L2Nu'                   : 88.51,
  #'TTToSemiLeptonic'            : 366.29,
  #'TTToHadronic'                : 378.93,
  'ST_s-channel_leptonDecays'   : [3.344   +0.087,     3.344   -0.087],
  'ST_s-channel_hadronicDecays' : [6.976   +0.183,     6.976   -0.183],
  'ST_t-channel_top'            : [134.2   +2.6,       134.2   -1.7],
  'ST_t-channel_antitop'        : [80.0    +1.8,       80.0    -1.4],
  'ST_tW_top'                   : [39.65   +1.45,      39.65   -1.40],
  'ST_tW_antitop'               : [39.65   +1.45,      39.65   -1.40],
  'WW'                          : [118.7   *1.025,     118.7   *0.978],
  'WWTo2L2Nu'                   : [12.60   *1.025,     12.60   *0.978],
  'WWTo1L1Nu2Q'                 : [52.14   *1.025,     52.14   *0.978],
  'WWTo4Q'                      : [53.94   *1.025,     53.94   *0.978],
  'WZ'                          : [27.55   +0.1272,    27.55   -0.1272],
  'WZTo3L1Nu'                   : [5.257   +0.04924,   5.257   -0.04924],
  'WZTo1L3Nu'                   : [3.414   +0.0366,    3.414   -0.0366],
  'WZTo2L2Q'                    : [6.565   +0.05904,   6.565   -0.05904],
  'WZTo1L1Nu2Q'                 : [9.119   +0.09682,   9.119   -0.09682],
  'ZZ'                          : [12.14   +0.003300,  12.14   -0.003300],
  'ZZTo4L'                      : [1.325   +0.001220,  1.325   -0.001220],
  'ZZTo2L2Nu'                   : [0.9738  +0.0009971, 0.9738  -0.0009971],
  'ZZTo2L2Q'                    : [3.698   +0.002666,  3.698   -0.002666],
  'ZZTo2Nu2Q'                   : [4.489   +0.006934,  4.489   -0.006934],
  'ZZTo4Q'                      : [3.306   +0.005339,  3.306   -0.005339],
  'WWW'                         : [0.2158  +0.0002479, 0.2158  -0.0002479],
  'WWZ'                         : [0.1707  +0.0001757, 0.1707  -0.0001757],
  'WZZ'                         : [0.05709 +6.213e-05, 0.05709 -6.213e-05],
  'ZZZ'                         : [0.01476 +1.521e-05, 0.01476 -1.521e-05],
  'TTW'                         : [0.4611  +0.001268,  0.4611  -0.001268],
  'TTZ'                         : [0.5407  +0.002541,  0.5407  -0.002541],
  'SignalWto3pi'                : [0.1929  +0.007418,  0.1929  -0.007299],

  # Higgs production cross sections may have special uncertainties; so don't define them here
  #'ggH_TauTau'                  : 3.035,
  #'VBF_TauTau'                  : 0.2364,
  #'WpH_TauTau'                  : 0.05243,
  #'WmH_TauTau'                  : 0.03324,
  #'ZH_TauTau'                   : 0.05520,
  #'ggH_WW'                      : 10.44,
  #'VBF_WW'                      : 0.8132,
  #'WpH_WW'                      : 0.1803,
  #'WmH_WW'                      : 0.1143,
  #'ZH_WW'                       : 0.1899,
  #'ggZH_WW'                     : 0.02641,
  #'ttH_nonbb'                   : 0.2123,
  'EWK_WplusToLNu'              : [39.13   +0.09366,   39.13   -0.09366],
  'EWK_WminusToLNu'             : [32.05   +0.07777,   32.05   -0.07777],
  'EWK_ZTo2L'                   : [6.214   +0.01374,   6.214   -0.01374],
  'EWK_ZTo2Nu'                  : [10.68   +0.02624,   10.68   -0.02624],
  'WGToLNuG'                    : [411.2   +3.101,     411.2   -3.101]
}
XSecRun3 = {
  # keep full terminating intermediate expressions, just like you would in a lab experiment. Error is calculated in final result.
  # Signal
  # XSec : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG136TeVxsec_extrap, mH = 125.09
  # BR   : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'ggH_TauTau'                  : 3.2638,  # 52.17 * 0.06256
  'ggH_TauTau_Filtered'         : 3.2638,  # 52.17 * 0.06256
  'ggH_TauTau_UnFiltered'       : 3.2638,  # 52.17 * 0.06256
  'VBF_TauTau'                  : 0.2549,  # 4.075 * 0.06256
  'VBF_TauTau_Filtered'         : 0.2549,  # 4.075 * 0.06256
  'VBF_TauTau_UnFiltered'       : 0.2549,  # 4.075 * 0.06256
  'WplusH_TauTau_Filtered'      : 0.05549, # 0.88696 * 0.06256
  'WplusH_TauTau_UnFiltered'    : 0.05549, # 0.88696 * 0.06256
  'WminusH_TauTau_Filtered'     : 0.03543, # 0.566359 * 0.06256
  'WminusH_TauTau_UnFiltered'   : 0.03543, # 0.566359 * 0.06256
  'ZH_TauTau_Filtered'          : 0.05894, # 0.9422 * 0.06256
  'ZH_TauTau_UnFiltered'        : 0.05894, # 0.9422 * 0.06256

  # DY
  # https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV , Single Vector Boson Production, pp->e+e- LO
  # extrapolated to nJets based on 2018, see rows 3-7 of this table (using LO):
  # https://docs.google.com/spreadsheets/d/15fB5axUXr8rn6E5lnhZI11Yq35nbsx9X8oe3sq7qMRw/edit#gid=0
  'DYJetsToLL_M-50_LO'          : 5594.7,   # 1864.9 * 3
  'DY1JetsToLL_M-50_LO'         : 911.9361, # 1864.9 * 3 * 0.1630
  'DY2JetsToLL_M-50_LO'         : 318.6741, # 1864.9 * 3 * 0.05696
  'DY3JetsToLL_M-50_LO'         : 116.4817, # 1864.9 * 3 * 0.02082
  'DY4JetsToLL_M-50_LO'         : 45.7982,  # 1864.9 * 3 * 0.008186
  'DYJetsToLL_M-4to50_LO'       : 100800,   # TauFW/PicoProducer/utils/getXSec.sh:  1.008e+05 +- 1.787e+02 pb  using all files from /DYTo2L_MLL-4to50_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM
  'DYJetsToLL_M-10to50_LO'      : 17380,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2L-4Jets_MLL-10to50 && energy=13.6" , postEE value

  # https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV , Single Vector Boson Production, pp->e+e- NLO_QCD + NLO_EW
  # Njet Xsec determined from minimization: Obtaining the fractions of 0J, 1J and 2J in the inclusive sample
  'DYJetsToLL_M-50'             : 6331.5,   # 2110.5 * 3
  'DY0JetsToLL_M-50'            : 5007.8,   # 0.790937 * 6331.5
  'DY1JetsToLL_M-50'            : 955.28,   # 0.150877 * 6331.5
  'DY2JetsToLL_M-50'            : 368.40,   # 0.058186 * 6331.5
  'DYJetsToLL_M-10to50'         : 20950,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2L-2Jets_MLL-10to50 && energy=13.6" , postEE value
  'DYJetsToLL_M-4to10'          : 141500,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2L-2Jets_MLL-4to10 && energy=13.6" , postBPix value
  # Copy values with "_NLO", because things will get confusing once we also consider Powheg NNLO samples
  'DYJetsToLL_M-50_NLO'         : 6331.5,
  'DY0JetsToLL_M-50_NLO'        : 5007.8,
  'DY1JetsToLL_M-50_NLO'        : 955.28,
  'DY2JetsToLL_M-50_NLO'        : 368.40,
  'DYJetsToLL_M-10to50_NLO'     : 20950,

  'DYto2Tau_MLL-10to50_NNLO'     : 6744.0,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-10to50 && energy=13.6" , postEE value
  'DYto2Mu_MLL-10to50_NNLO'      : 6744.0,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-10to50 && energy=13.6" , postEE value
  'DYto2E_MLL-10to50_NNLO'       : 6744.0,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-10to50 && energy=13.6" , postEE value
  'DYto2Tau_MLL-50to120_NNLO'    : 2219.0,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-50to120 && energy=13.6" , postEE value
  'DYto2Mu_MLL-50to120_NNLO'     : 2219.0,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-50to120 && energy=13.6" , postEE value
  'DYto2E_MLL-50to120_NNLO'      : 2219.0,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-50to120 && energy=13.6" , postEE value
  'DYto2Tau_MLL-120to200_NNLO'   : 21.65,         # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-120to200 && energy=13.6" , postEE value
  'DYto2Mu_MLL-120to200_NNLO'    : 21.65,         # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-120to200 && energy=13.6" , postEE value
  'DYto2E_MLL-120to200_NNLO'     : 21.65,         # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Eu_MLL-120to200 && energy=13.6" , postEE value
  'DYto2Tau_MLL-200to400_NNLO'   : 3.058,         # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-200to400 && energy=13.6" , postEE value
  'DYto2Mu_MLL-200to400_NNLO'    : 3.058,         # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-200to400 && energy=13.6" , postEE value
  'DYto2E_MLL-200to400_NNLO'     : 3.058,         # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-200to400 && energy=13.6" , postEE value
  'DYto2Tau_MLL-400to800_NNLO'   : 0.2691,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-400to800 && energy=13.6" , postEE value
  'DYto2Mu_MLL-400to800_NNLO'    : 0.2691,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-400to800 && energy=13.6" , postEE value
  'DYto2E_MLL-400to800_NNLO'     : 0.2691,        # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-400to800 && energy=13.6" , postEE value
  'DYto2Tau_MLL-800to1500_NNLO'  : 0.01915,       # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-800to1500 && energy=13.6" , postEE value
  'DYto2Mu_MLL-800to1500_NNLO'   : 0.01915,       # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-800to1500 && energy=13.6" , postEE value
  'DYto2E_MLL-800to1500_NNLO'    : 0.01915,       # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-800to1500 && energy=13.6" , postEE value
  'DYto2Tau_MLL-1500to2500_NNLO' : 0.001111,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-1500to2500 && energy=13.6" , postEE value
  'DYto2Mu_MLL-1500to2500_NNLO'  : 0.001111,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-1500to2500 && energy=13.6" , postEE value
  'DYto2E_MLL-1500to2500_NNLO'   : 0.001111,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-1500to2500 && energy=13.6" , postEE value
  'DYto2Tau_MLL-2500to4000_NNLO' : 0.00005949,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-2500to4000 && energy=13.6" , postEE value
  'DYto2Mu_MLL-2500to4000_NNLO'  : 0.00005949,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-2500to4000 && energy=13.6" , postEE value
  'DYto2E_MLL-2500to4000_NNLO'   : 0.00005949,    # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-2500to4000 && energy=13.6" , postEE value
  'DYto2Tau_MLL-4000to6000_NNLO' : 0.000001558,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-4000to6000 && energy=13.6" , postEE value
  'DYto2Mu_MLL-4000to6000_NNLO'  : 0.000001558,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-4000to6000 && energy=13.6" , postEE value
  'DYto2E_MLL-4000to6000_NNLO'   : 0.000001558,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-4000to6000 && energy=13.6" , postEE value
  'DYto2Tau_MLL-6000toInf_NNLO'  : 0.00000003519, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Tau_MLL-6000 && energy=13.6" , postEE value
  'DYto2Mu_MLL-6000toInf_NNLO'   : 0.00000003519, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2Mu_MLL-6000 && energy=13.6" , postEE value
  'DYto2E_MLL-6000toInf_NNLO'    : 0.00000003519, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=DYto2E_MLL-6000 && energy=13.6" , postEE value

  # Based on same expolations as above:
  #'DY0JetsToLL_M-50'            : 4754.957, # 2110.5 * 3 * 0.7510
  #'DY1JetsToLL_M-50'            : 1032.035, # 2110.5 * 3 * 0.1630
  #'DY2JetsToLL_M-50'            : 360.6422, # 2110.5 * 3 * 0.05696

  #'DYJetsToLL_M-50'             : 6727.0,   # TauFW/PicoProducer/utils/getXSec.sh:  6.727e+03 +- 6.807e+00 pb (NLO)  using 100 files from /DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM
  #'DY0JetsToLL_M-50'            : 5367.0,   # TauFW/PicoProducer/utils/getXSec.sh:  5.367e+03 +- 3.061e+00 pb (NLO)  using 100 files from /DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM
  #'DY1JetsToLL_M-50'            : 1011.0,   # TauFW/PicoProducer/utils/getXSec.sh:  1.011e+03 +- 1.284e+00 pb (NLO)  using 100 files from /DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM
  #'DY2JetsToLL_M-50'            : 382.9,    # TauFW/PicoProducer/utils/getXSec.sh:  3.829e+02 +- 8.956e-01 pb (NLO)  using 100 files from /DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM

  # TT
  # XSec : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO#Updated_reference_cross_sections, 13.6 TeV
  # BR   : https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#TTbar
  'TTbar'                       : 923.60,
  'TTTo2L2Nu'                   : 96.9558336,   # 923.60 * 0.324 * 0.324
  'TTToSemiLeptonic'            : 404.5811328,  # 923.60 * 0.324 * 0.676 * 2
  'TTToFullyHadronic'           : 422.0630336,  # 923.60 * 0.676 * 0.676

  # ST
  'ST_s-channel_top'            : 2.278, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=TBbartoLplusNuBbar && energy=13.6" , postEE value
  'ST_s-channel_antitop'        : 1.430, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=TbarBtoLminusNuB && energy=13.6" , postEE value
  'ST_t-channel_top'            : 123.8, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=TBbarQ_t-channel && energy=13.6" , postEE value
  'ST_t-channel_antitop'        : 75.47, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=TbarBQ_t-channel && energy=13.6" , postEE value
  #### ST tW 87.9 top and antitop combined 
  # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_tW_channel_cros, 13.6 TeV
  # can figure out with BRs of t, tbar, Wplus, Wminus, or use MiniAOD tool
  # BR values from https://arxiv.org/pdf/2201.07861.pdf table above figure 6, assuming Lepton Flavor Universality (LFU)
  # TWminus   inclusive XSec = 35.99 +- 1.292e-02 pb
  'ST_TWminus_2L2Nu'            : 3.841316711, # 35.99 * 0.3267 * 0.3267
  'ST_TWminus_4Q'               : 16.31060466, # 35.99 * 0.6732 * 0.6732
  'ST_TWminus_LNu2Q'            : 15.83088099, # 35.99 * 0.3267 * 0.6732 * 2 
  # TbarWplus inclusive XSec = 36.05 +- 1.296e-02 pb
  'ST_TbarWplus_2L2Nu'          : 3.847720685, # 36.05 * 0.3267 * 0.3267
  'ST_TbarWplus_4Q'             : 16.33779655, # 36.05 * 0.6732 * 0.6732
  'ST_TbarWplus_LNu2Q'          : 15.85727312, # 36.05 * 0.3267 * 0.6732 * 2

  # WJ
  # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV 
  # Single Vector Boson Production, pp->e+nu and pp-> e-nubar LO
  # extrapolated to nJets based on 2018, see rows 9-13 of this table (using LO)
  'WJetsToLNu_LO'               : 56350.2,
  'W1JetsToLNu_LO'              : 10663.148, # 56350.2 * 0.1893
  'W2JetsToLNu_LO'              : 3355.654,  # 56350.2 * 0.05955
  'W3JetsToLNu_LO'              : 987.256,   # 56350.2 * 0.01752
  'W4JetsToLNu_LO'              : 463.537,   # 56350.2 * 0.008226

  # Using NLO_QCD + NLO_EW
  # Njet Xsec determined from minimization: Obtaining the fractions of 0J, 1J and 2J in the inclusive sample
  'WJetsToLNu'                  : 64451.4,
  'W0JetsToLNu'                 : 52090.5,   # 64451.4 * 0.808213
  'W1JetsToLNu'                 : 8964.29,   # 64451.4 * 0.139086
  'W2JetsToLNu'                 : 3396.65,   # 64451.4 * 0.052701

  #VV
  # from 100 file estimate using getXSec.sh tool unless otherwise stated
  #### WW
  'WW'                          : 122.3, # From TauFW, with NNLO k-factor (https://github.com/cms-tau-pog/TauFW/blob/master/Plotter/config/samples_v12.py)
  'WWTo2L2Nu'                   : 11.79, # +- 4.216e-03 pb
  'WWTo4Q'                      : 50.79, # +- 1.816e-02 pb
  'WWToLNu2Q'                   : 48.94, # +- 1.750e-02 pb

  #### WZ
  'WZ'                          : 41.15, # From TauFW, with NNLO k-factor (https://github.com/cms-tau-pog/TauFW/blob/master/Plotter/config/samples_v12.py)
  'WZTo3LNu'                    : 4.924, # +- 2.370e-03 pb 
  'WZTo2L2Q'                    : 7.568, # +- 3.908e-03 pb 
  'WZToLNu2Q'                   : 15.87, # +- 7.874e-03 pb

  #### ZZ
  'ZZ'                          : 19.43, # From TauFW, with NNLO k-factor (https://github.com/cms-tau-pog/TauFW/blob/master/Plotter/config/samples_v12.py)
  'ZZTo2L2Nu'                   : 1.031, # +- 5.268e-04 pb
  'ZZTo2L2Q'                    : 6.788, # +- 3.501e-03 pb
  'ZZTo2Nu2Q'                   : 4.826, # +- 1.296e-03 pb
  'ZZTo4L'                      : 1.390, # +- 7.001e-04 pb

  #### VVV
  'WWW'                         : 0.2328,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8 && energy=13.6"
  'WWZ'                         : 0.1851,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8 && energy=13.6"
  'WZZ'                         : 0.06206, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8 && energy=13.6"
  'ZZZ'                         : 0.01591, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8 && energy=13.6"

  #### HWW background
  # XSec : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG136TeVxsec_extrap, mH = 125.09
  # BR   : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
  'ggH_WW'                      : 52.17*0.2152 * 0.324 * 0.324, # Samples are 2L2Nu
  'VBF_WW'                      : 4.075 *0.2152 * 0.324 * 0.324, # Samples are 2L2Nu
  'ttH_nonbb'                   : 0.5688*(1-0.5809),

  #### QCD PT
  'QCD_PT-15to20_MuEnrichedPt5'    : 2982000.0, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-15to20_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-20to30_MuEnrichedPt5'    : 2679000.0, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-20to30_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-30to50_MuEnrichedPt5'    : 1497000.0, # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-30to50_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-50to80_MuEnrichedPt5'    : 402900.0,  # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-50to80_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-80to120_MuEnrichedPt5'   : 95130.0,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-80to120_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-120to170_MuEnrichedPt5'  : 22980.0,   # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-120to170_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-170to300_MuEnrichedPt5'  : 7763,      # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-170to300_MuEnrichedPt5 && energy=13.6" , postEE value
  'QCD_PT-300to470_MuEnrichedPt5'  : 699.1,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-300to470_MuEnrichedPt5 && energy=13.6", preEE value
  'QCD_PT-470to600_MuEnrichedPt5'  : 68.24,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-470to600_MuEnrichedPt5 && energy=13.6" , postEE value
  'QCD_PT-600to800_MuEnrichedPt5'  : 21.37,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-600to800_MuEnrichedPt5 && energy=13.6" , postEE value
  'QCD_PT-800to1000_MuEnrichedPt5' : 3.913,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-800to1000_MuEnrichedPt5 && energy=13.6" , preEE value
  'QCD_PT-1000_MuEnrichedPt5'      : 1.323,     # https://cms-gen-dev.cern.ch/xsdb/ , searching for "process_name=QCD_PT-1000_MuEnrichedPt5 && energy=13.6" , postEE value

  # QCD HT - from TauFW/PicoProducer/utils/getXSec.sh for 100 files (unless otherwise noted) on MINIAODSIM parent sample
  'QCD_HT-70to100'             : 58590000,
  'QCD_HT-100to200'            : 25180000,
  'QCD_HT-200to400'            : 1950000,
  'QCD_HT-400to600'            : 96180,
  'QCD_HT-600to800'            : 13500,
  'QCD_HT-800to1000'           : 3013,
  'QCD_HT-1000to1200'          : 881.8,
  'QCD_HT-1200to1500'          : 381.5,
  'QCD_HT-1500to2000'          : 125.7,
  'QCD_HT-2000'                : 26.32,

}
XSec_UncRun3 = {
  'DYJetsToLL_M-4to10'         : [141500 +301.9,     141500 -301.9],
  'DYJetsToLL_M-4to50_LO'      : [100800 +178.7,     100800 -178.7],
  'DYJetsToLL_M-10to50'        : [20950  +183.5,     20950  -183.5],
  'DYJetsToLL_M-10to50_NLO'    : [20950  +183.5,     20950  -183.5],
  'DYJetsToLL_M-10to50_LO'     : [17380  +26.57,     17380  -26.57],

  'DYto2Tau_MLL-10to50_NNLO'     : [6744.0        +1.132,       6744.0     -1.132],
  'DYto2Mu_MLL-10to50_NNLO'      : [6744.0        +1.132,       6744.0     -1.132],
  'DYto2E_MLL-10to50_NNLO'       : [6744.0        +1.132,       6744.0     -1.132],
  'DYto2Tau_MLL-50to120_NNLO'    : [2219.0        +0.2327,      2219.0     -0.2327],
  'DYto2Mu_MLL-50to120_NNLO'     : [2219.0        +0.2327,      2219.0     -0.2327],
  'DYto2E_MLL-50to120_NNLO'      : [2219.0        +0.2327,      2219.0     -0.2327],
  'DYto2Tau_MLL-120to200_NNLO'   : [21.65         +0.003184,    21.65      -0.003184],
  'DYto2Mu_MLL-120to200_NNLO'    : [21.65         +0.003184,    21.65      -0.003184],
  'DYto2E_MLL-120to200_NNLO'     : [21.65         +0.003184,    21.65      -0.003184],
  'DYto2Tau_MLL-200to400_NNLO'   : [3.058         +0.000465,    3.058      -0.000465],
  'DYto2Mu_MLL-200to400_NNLO'    : [3.058         +0.000465,    3.058      -0.000465],
  'DYto2E_MLL-200to400_NNLO'     : [3.058         +0.000465,    3.058      -0.000465],
  'DYto2Tau_MLL-400to800_NNLO'   : [0.2691        +0.00004215,  0.2691     -0.00004215],
  'DYto2Mu_MLL-400to800_NNLO'    : [0.2691        +0.00004215,  0.2691     -0.00004215],
  'DYto2E_MLL-400to800_NNLO'     : [0.2691        +0.00004215,  0.2691     -0.00004215],
  'DYto2Tau_MLL-800to1500_NNLO'  : [0.01915       +0.000003085, 0.01915    -0.000003085],
  'DYto2Mu_MLL-800to1500_NNLO'   : [0.01915       +0.000003085, 0.01915    -0.000003085],
  'DYto2E_MLL-800to1500_NNLO'    : [0.01915       +0.000003085, 0.01915    -0.000003085],
  'DYto2Tau_MLL-1500to2500_NNLO' : [0.001111      +1.787e-7,    0.001111   -1.787e-7],
  'DYto2Mu_MLL-1500to2500_NNLO'  : [0.001111      +1.787e-7,    0.001111   -1.787e-7],
  'DYto2E_MLL-1500to2500_NNLO'   : [0.001111      +1.787e-7,    0.001111   -1.787e-7],
  'DYto2Tau_MLL-2500to4000_NNLO' : [0.00005949    +9.162e-9,    0.00005949 -9.162e-9],
  'DYto2Mu_MLL-2500to4000_NNLO'  : [0.00005949    +9.162e-9,    0.00005949 -9.162e-9],
  'DYto2E_MLL-2500to4000_NNLO'   : [0.00005949    +9.162e-9,    0.00005949 -9.162e-9],
  'DYto2Tau_MLL-4000to6000_NNLO' : [0.000001558   +2.078e-10,   0.000001558 -2.078e-10],
  'DYto2Mu_MLL-4000to6000_NNLO'  : [0.000001558   +2.078e-10,   0.000001558 -2.078e-10],
  'DYto2E_MLL-4000to6000_NNLO'   : [0.000001558   +2.078e-10,   0.000001558 -2.078e-10],
  'DYto2Tau_MLL-6000toInf_NNLO'  : [0.00000003519 +6.811e-12,   0.00000003519 -6.811e-12],
  'DYto2Mu_MLL-6000toInf_NNLO'   : [0.00000003519 +6.811e-12,   0.00000003519 -6.811e-12],
  'DYto2E_MLL-6000toInf_NNLO'    : [0.00000003519 +6.811e-12,   0.00000003519 -6.811e-12],

  'ST_s-channel_top'           : [2.278 +0.0003008,  2.278 -0.0003008],
  'ST_s-channel_antitop'       : [1.430 +0.0001633,  1.430 -0.0001633],
  'ST_t-channel_top'           : [123.8 +0.3709,     123.8 -0.3709],
  'ST_t-channel_antitop'       : [75.47 +0.2361,     75.47 -0.2361],

  'WWTo2L2Nu'                  : [11.79 +0.004216,  11.79 -0.004216],
  'WWTo4Q'                     : [50.79 +0.01816,   50.79 -0.01816],
  'WWToLNu2Q'                  : [48.94 +0.01750,   48.94 -0.01750],
  'WZTo3LNu'                   : [4.924 +0.002370,  4.924 -0.002370],
  'WZTo2L2Q'                   : [7.568 +0.003908,  7.568 -0.003908],
  'WZToLNu2Q'                  : [15.87 +0.007874,  15.87 -0.007874],
  'ZZTo2L2Nu'                  : [1.031 +0.0005268, 1.031 -0.0005268],
  'ZZTo2L2Q'                   : [6.788 +0.003501,  6.788 -0.003501],
  'ZZTo2Nu2Q'                  : [4.826 +0.001296,  4.826 -0.001296],
  'ZZTo4L'                     : [1.390 +0.0007001, 1.390 -0.0007001],

  'WWW'                        : [0.2328  +0.0001247,   0.2328  -0.0001247],
  'WWZ'                        : [0.1851  +0.00009482,  0.1851  -0.00009482],
  'WZZ'                        : [0.06206 +0.00003689,  0.06206 -0.00003689],
  'ZZZ'                        : [0.01591 +0.000007828, 0.01591 -0.000007828],

  'QCD_PT-15to20_MuEnrichedPt5'    : [2982000.0 +28620.0,  2982000.0 -28620.0	],
  'QCD_PT-20to30_MuEnrichedPt5'    : [2679000.0 +26580.0,  2679000.0 -26580.0	],
  'QCD_PT-30to50_MuEnrichedPt5'    : [1497000.0 +14580.0,  1497000.0 -14580.0	],
  'QCD_PT-50to80_MuEnrichedPt5'    : [402900.0  +3936.0,   402900.0  -3936.0	],
  'QCD_PT-80to120_MuEnrichedPt5'   : [95130.0   +933.5,    95130.0   -933.5],
  'QCD_PT-120to170_MuEnrichedPt5'  : [22980.0   +215.1,    22980.0   -215.1],
  'QCD_PT-170to300_MuEnrichedPt5'  : [7763.0    +23.67,    7763.0    -23.67],
  'QCD_PT-300to470_MuEnrichedPt5'  : [699.1     +6.639,    699.1     -6.639],
  'QCD_PT-470to600_MuEnrichedPt5'  : [68.24     +0.2049,   68.24     -0.2049],
  'QCD_PT-600to800_MuEnrichedPt5'  : [21.37     +0.199,    21.37     -0.199],
  'QCD_PT-800to1000_MuEnrichedPt5' : [3.913     +0.03526,  3.913     -0.03526],
  'QCD_PT-1000_MuEnrichedPt5'      : [1.323     +0.003921, 1.323     -0.003921],

  'QCD_HT-70to100'               : [58590000 +18590,   58590000 -18590],
  'QCD_HT-100to200'              : [25180000 +8255,    25180000 -8255],
  'QCD_HT-200to400'              : [1950000  +748.9,   1950000  -748.9],
  'QCD_HT-400to600'              : [96180    +39.19,   96180    -39.19],
  'QCD_HT-600to800'              : [13500    +5.759,   13500    -5.759],
  'QCD_HT-800to1000'             : [3013     +2.388,   3013     -2.388],
  'QCD_HT-1000to1200'            : [881.8    +.04135,  881.8    -.04135],
  'QCD_HT-1200to1500'            : [381.5    +.01811,  381.5    -.01811],
  'QCD_HT-1500to2000'            : [125.7    +.005904, 125.7    -.005904], 
  'QCD_HT-2000'                  : [26.32    +.001469, 26.32    -.001469],

}
