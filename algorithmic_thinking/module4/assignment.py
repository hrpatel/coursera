__author__ = 'mamaray'

import alg_app4_provided as data
import project as soln


def q1():
    human = data.read_protein(data.HUMAN_EYELESS_URL)
    fly = data.read_protein(data.FRUITFLY_EYELESS_URL)
    scores = data.read_scoring_matrix(data.PAM50_URL)

    a_matrix = soln.compute_alignment_matrix(human, fly, scores, False)
    print soln.compute_local_alignment(human, fly, scores, a_matrix)

    a_matrix = soln.compute_alignment_matrix(human, fly, scores, True)
    print soln.compute_global_alignment(human, fly, scores, a_matrix)

    # local answer
    b = (875,
         'HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ',
         'HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ')

    # global answer
    a = (4,
         'MQN--------------------------------------S--------------HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ--------------------------------------------M------------GA----DG-----MYDKLRMLN-------G--Q----T---G-S---WGTR---P----G------------W----YPG----T--------------SV---------------P---------G-Q---P--T-------Q-DGCQQ-QE-G-G-GENTNSISSN-GEDSDEAQMRLQLKRKLQRNRTSFTQEQIEALEKEFERTHYPDVFARERLAAKIDLPEARIQVWFSNRRAKWRREEKLRNQRR--Q-----A-----S---N-T--P------SH-I------P----I---SS-S-FSTSVYQP-----I--PQ-PT-TP-V-SSFTSGSMLGR-T-D-----T--AL-T----NT-Y--S-------AL-P---P-M---P-SF-TM-AN--N--LPM-Q------P-P------V-----PS----Q---T-SS-YSC-M-L---PTSPS----V--N-GR--------------------S-YD--T-YT--PPHM------Q-------------T--H-M--NS-Q-P-MGTS--GTT-STGL----ISPGV-S---V----P--VQ-V-P----G-S---EPDMSQ------YWPRLQ',
         'MRNLPCLGTAGGSGLGGIAGKPSPTMEAVEASTASHPHSTSSYFATTYYHLTDDECHSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQSTGSGSSSTSAGNSISAKVSVSIGGNVSNVASGSRGTLSSSTDLMQTATPLNSSESGGASNSGEGSEQEAIYEKLRLLNTQHAAGPGPLEPARAAPLVGQSPNHLGTRSSHPQLVHGNHQALQQHQQQSWPPRHYSGSWYPTSLSEIPISSAPNIASVTAYASGPSLAHSLSPPNDIESLASIGHQRNCPVATEDIHLKKELDG-HQSDETGSGEGENSNGGASNIG-NTEDDQARLILKRKLQRNRTSFTNDQIDSLEKEFERTHYPDVFARERLAGKIGLPEARIQVWFSNRRAKWRREEKLRNQRRTPNSTGASATSSSTSATASLTDSPNSLSACSSLLSGSAGGPSVSTINGLSSPSTLSTNVNAPTLGAGIDSSESPTPIPHIRPSCTSDNDNGRQSEDCRRVCSPCPLGVGGHQNTHHIQSNGHAQGHALVPAISPRLNFNSGSFGAMYSNMHHTALSMSDSYGAVTPIPSFNHSAVGPLAPPSPIPQQGDLTPSSLYPCHMTLRPPPMAPAHHHIVPGDGGRPAGVGLGSGQSANLGASCSGSGYEVLSAYALPPPPMASSSAADSSFSAASSASANVTPHHTIAQESCPSPCSSASHFGVAHSSGFSSDPISPAVSSYAHMSYNYASSANTMTPSSASGTSAHVAPGKQQFFASCFYSPWV-')


def q2():
    def q2_helper(str1, str2):
        if len(str1) != len(str2):
            return 0
        else:
            ctr = 0
            for char in range(len(str1)):
                if str1[char] == str2[char]:
                    ctr += 1

        return (ctr * 1.0 / len(str1)) * 100

    human = data.read_protein(data.HUMAN_EYELESS_URL)
    fly = data.read_protein(data.FRUITFLY_EYELESS_URL)
    scores = data.read_scoring_matrix(data.PAM50_URL)
    c_pax = data.read_protein(data.CONSENSUS_PAX_URL)

    # get local alignment of human and fly
    a_matrix = soln.compute_alignment_matrix(human, fly, scores, False)
    l_score, l_h, l_ff = soln.compute_local_alignment(human, fly, scores, a_matrix)

    # removing the dashes
    l_h = l_h.replace("-", "")
    l_ff = l_ff.replace("-", "")

    # get global alignment matrix for each local string and pax
    pax_a_h_matrix = soln.compute_alignment_matrix(l_h, c_pax, scores, True)
    pax_a_ff_matrix = soln.compute_alignment_matrix(l_ff, c_pax, scores, True)

    # compute global alignment
    h_ga = soln.compute_global_alignment(l_h, c_pax, scores, pax_a_h_matrix)
    ff_ga = soln.compute_global_alignment(l_ff, c_pax, scores, pax_a_ff_matrix)

    print "human:\t\t", q2_helper(h_ga[1], h_ga[2])
    print "fruit fly:\t", q2_helper(ff_ga[1], ff_ga[2])


q2()