#!/usr/bin/env python
import sys
import time
import os

def SampleSize():

    m = {}
    m["QCD_bEnriched_HT1000to1500"]                 =  1.352
    m["ZZTo4Q"]                                     = 128.479
    m["QCD_Pt_470to600"]                            =  0.894
    m["QCD_bEnriched_HT700to1000"]                  =  5.030
    m["QCD_bEnriched_HT2000toInf"]                  =  0.161
    m["QCD_Pt_300to470"]                            =  0.583
    m["ChargedHiggs_HplusTB_HplusToTB_M_500"]       =  6.021
    m["QCD_Pt_1000to1400"]                          =  0.288
    m["ChargedHiggs_HplusTB_HplusToTB_M_250"]       =  3.832
    m["QCD_bEnriched_HT100to200"]                   =  20.116
    m["QCD_bEnriched_HT500to700"]                   =  13.044
    m["QCD_Pt_1800to2400"]                          =  0.047
    m["TT_ext3"]                                    =  58.935
    m["QCD_Pt_3200toInf"]                           =  0.039
    m["QCD_Pt_1400to1800"]                          =  0.045
    m["ChargedHiggs_HplusTB_HplusToTB_M_350"]       =  5.315
    m["QCD_Pt_2400to3200"]                          =  0.045
    m["WZ"]                                         =  2.906
    m["ttbb_4FS_ckm_amcatnlo_madspin_pythia8"]      =  10.377
    m["WWTo4Q"]                                     =  7.817
    m["QCD_Pt_600to800"]                            =  0.846
    m["TTZToQQ"]                                    =  3.877
    m["ST_tW_top_5f_inclusiveDecays"]               =  3.646
    m["WJetsToQQ_HT_600ToInf"]                      =  5.666
    m["ChargedHiggs_HplusTB_HplusToTB_M_180"]       =  2.465
    m["ST_t_channel_top_4f_inclusiveDecays"]        = 125.228
    m["ST_tW_antitop_5f_inclusiveDecays"]           =  1.318
    m["QCD_Pt_50to80"]                              =  0.000
    m["ST_t_channel_antitop_4f_inclusiveDecays"]    =  75.175
    m["QCD_bEnriched_HT200to300"]                   =  20.964
    m["ChargedHiggs_HplusTB_HplusToTB_M_220"]       =  3.261
    m["JetHT_Run2016B_PromptReco_v2_273150_275376"] =  14.709
    m["QCD_bEnriched_HT300to500"]                   =  14.008
    m["QCD_Pt_30to50"]                              =  0.000
    m["ZJetsToQQ_HT600toInf"]                       =  1.287 
    m["QCD_Pt_800to1000"]                           =  0.317
    m["JetHT_Run2016E_PromptReco_v2_276824_277420"] =  15.243
    m["ChargedHiggs_HplusTB_HplusToTB_M_200"]       =  2.850
    m["JetHT_Run2016D_PromptReco_v2_276315_276811"] =  13.892
    m["QCD_Pt_80to120"]                             =  0.001
    m["TTTT_ext1"]                                  =  5.235
    m["ChargedHiggs_HplusTB_HplusToTB_M_300"]       =  4.636
    m["ChargedHiggs_HplusTB_HplusToTB_M_400"]       =  5.817
    m["QCD_Pt_170to300"]                            =  0.043
    m["QCD_Pt_120to170"]                            =  0.008
    m["QCD_bEnriched_HT1500to2000"]                 =  0.330
    m["JetHT_Run2016F_PromptReco_v1_277816_278800"] =  9.172
    m["TTJets"]                                     =  34.067
    m["QCD_Pt_15to30"]                              =  0.000
    m["JetHT_Run2016C_PromptReco_v2_275420_276283"] =  7.508
    m["JetHT_Run2016F_PromptReco_v1_278801_278808"] =  1.800
    m["TTWJetsToQQ"]                                =  4.153
    m["JetHT_Run2016G_PromptReco_v1_278816_280385"] =  33.355

    size = 0
    for key, value in m.items():
        size += value

    print str(size) + " GB"
    return


def BasenameList():

    myList = [
        "/Users/attikis/my_work/programming.git/python/miniaod_1.root",
        "/Users/attikis/my_work/programming.git/python/miniaod_2.root",
        "/Users/attikis/my_work/programming.git/python/miniaod_3.root",
        "/Users/attikis/my_work/programming.git/python/miniaod_4.root",
        "/Users/attikis/my_work/programming.git/python/miniaod_5.root"
    ]

    #myList2 = [lambda x:  os.path.basename(x) , myList]
    myList2 = [os.path.basename(d) for d in myList]

    for l in myList2:
        print "\t", l
    return
        
    
def Re():
    import re

    print "=== Re()" 
    exitedJobs = []
    fileName   = "cmsRun_111.log.tar.gz"
    jobId_re   = re.compile("cmsRun_(?P<jobId>\d+)\.log\.tar\.gz")
    exit_match = jobId_re.search(fileName)

    if exit_match:
        exitedJobs.append(int(exit_match.group("jobId")))
    else:
        pass
    print "exitedJobs = ", exitedJobs
    return

    

def Tarball():
    import re
    import tarfile

    print "=== Tarball"
    
    filePath = "cmsRun_112.log.tar.gz"
    exitCode_re = re.compile("process\s+id\s+is\s+\d+\s+status\s+is\s+(?P<exitcode>\d+)")
    
    if tarfile.is_tarfile(filePath):
        # Open the tarball
        fIN = tarfile.open(filePath)
        log_re = re.compile("cmsRun-stdout-(?P<job>\d+)\.log")
        
        # For-loop: All files inside tarball
        for member in fIN.getmembers():
            print "member = ", member

            # Extract the log file
            logfile = fIN.extractfile(member)
            match   = log_re.search(logfile.name)
        
            # Regular Expression match for log-file
            if match:
                # For-loop: All lines of log-file
                for line in reversed(logfile.readlines()):
                
                    # Search for exit code
                    exitMatch = exitCode_re.search(line)
                    
                    # If exit code found, return the value
                    if exitMatch:
                        exitCode = int(exitMatch.group("exitcode"))
                        print "exitCode = ", exitCode
                        return exitCode
    else:
        print "File %s is not a tarfile" % (filePath)
    return


if __name__ == "__main__":

    # Tarball()
    # Re()
    # BasenameList()
    SampleSize()
