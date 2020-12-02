'''
Finalized dataSet Constructer:
Ce fishier va construire le dataset qui sera utilisée par l'algorithme d'apprentissage 
@uthor : AzsezA 
'''
import sys
import csv
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt
import datetime

startDate=datetime.date(2017,01,01)
endDate = datetime.datetime(2020,9,01)
def main(argv):
   print('preparing ... ') 
'''
argv help & check for data files
'''
    print('catching files')
    
    with open('DataSet.csv','w',newline=''):
        headers=['Date',
                'socialVar_1',#Terrorism avg over year
                'socialVar_2',#Tourism avg over year
                'socialVar_3',#agri avg over year 
                'socialVar_4',#indus avg over year 
                'socialVar_5',#romadhan 
                'polVar_1',#movement of panic europe (terror attacks/geopolitical stuff
                'polVar_2',#movement of panic wordwide 
                'polVar_3',#movement of panic tunisian
                'BestIndexAvg',
                'Foreign_investors',
                'Tunindex',
                'G11-MONOPRIX-A','G11-MONOPRIX-B','G11-MONOPRIX-C','G11-MONOPRIX-D',
                'G11-SFBT-A','G11-SFBT-B','G11-SFBT-C','G11-SFBT-D',
                'G11-TUNISAIR-A','G11-TUNISAIR-B','G11-TUNISAIR-C','G11-TUNISAIR-D',
                'G11-Attijari_Bank-A','G11-Attijari_Bank-B','G11-Attijari_Bank-C','G11-Attijari_Bank-D',
                'G11-BIAT-A','G11-BIAT-B','G11-BIAT-C','G11-BIAT-D',
                'G11-BH-A','G11-BH-B','G11-BH-C','G11-BH-D',
                'G11-Tunisie_Leasing_et_Factoring-A','G11-Tunisie_Leasing_et_Factoring-B','G11-Tunisie_Leasing_et_Factoring-C','G11-Tunisie_Leasing_et_Factoring-D',
                'G11-BT-A','G11-BT-B','G11-BT-C','G11-BT-D',
                'G11-STB-A','G11-STB-B','G11-STB-C','G11-STB-D',
                'G11-BNA-A','G11-BNA-B','G11-BNA-C','G11-BNA-D',
                'G11-ICF-A','G11-ICF-B','G11-ICF-C','G11-ICF-D',
                'G11-AMEN BANK-A','G11-AMEN BANK-B','G11-AMEN BANK-C','G11-AMEN BANK-D',
                'G11-ATB-A','G11-ATB-B','G11-ATB-C','G11-ATB-D',
                'G11-UIB-A','G11-UIB-B','G11-UIB-C','G11-UIB-D',
                'G11-SIMPAR-A','G11-SIMPAR-B','G11-SIMPAR-C','G11-SIMPAR-D',
                'G11-CIL-A','G11-CIL-B','G11-CIL-C','G11-CIL-D',
                'G11-ATL-A','G11-ATL-B','G11-ATL-C','G11-ATL-D',
                'G11-PGH-A','G11-PGH-B','G11-PGH-C','G11-PGH-D',
                'G11-SOTETEL-A','G11-SOTETEL-B','G11-SOTETEL-C','G11-SOTETEL-D',
                'G11-SOTUVER-A','G11-SOTUVER-B','G11-SOTUVER-C','G11-SOTUVER-D',
                'G11-SOTUMAG-A','G11-SOTUMAG-B','G11-SOTUMAG-C','G11-SOTUMAG-D',
                'G11-SIAME-A','G11-SIAME-B','G11-SIAME-C','G11-SIAME-D',
                'G11-TJL-A','G11-TJL-B','G11-TJL-C','G11-TJL-D',
                'G11-ELECTROSTAR-A','G11-ELECTROSTAR-B','G11-ELECTROSTAR-C','G11-ELECTROSTAR-D',
                'G11-SOTRAPIL-A','G11-SOTRAPIL-B','G11-SOTRAPIL-C','G11-SOTRAPIL-D',
                'G11-SOMOCER-A','G11-SOMOCER-B','G11-SOMOCER-C','G11-SOMOCER-D',
                'G11-GIF FILTER SA-A','G11-GIF FILTER SA-B','G11-GIF FILTER SA-C','G11-GIF FILTER SA-D',
                'G11-ASSAD-A','G11-ASSAD-B','G11-ASSAD-C','G11-ASSAD-D',
                'G11-WIFACK INTERNATIONAL BANK-A','G11-WIFACK INTERNATIONAL BANK-B','G11-WIFACK INTERNATIONAL BANK-C','G11-WIFACK INTERNATIONAL BANK-D',
                'G11-Société ESSOUKNA-A','G11-Société ESSOUKNA-B','G11-Société ESSOUKNA-C','G11-Société ESSOUKNA-D',
                'G11-ADWYA-A','G11-ADWYA-B','G11-ADWYA-C','G11-ADWYA-D',
                'G11-TPR-A','G11-TPR-B','G11-TPR-C','G11-TPR-D',
                'G11-SOPAT-A','G11-SOPAT-B','G11-SOPAT-C','G11-SOPAT-D',
                'G11-ARTES-A','G11-ARTES-B','G11-ARTES-C','G11-ARTES-D',
                'G11-HANNIBAL LEASE-A','G11-HANNIBAL LEASE-B','G11-HANNIBAL LEASE-C','G11-HANNIBAL LEASE-D',
                'G11-TUNIS RE-A','G11-TUNIS RE-B','G11-TUNIS RE-C','G11-TUNIS RE-D',
                'G11-ENNAKL automobiles-A','G11-ENNAKL automobiles-B','G11-ENNAKL automobiles-C','G11-ENNAKL automobiles-D',
                'G11-Telnet Holding-A','G11-Telnet Holding-B','G11-Telnet Holding-C','G11-Telnet Holding-D',
                'G11-OTH-A','G11-OTH-B','G11-OTH-C','G11-OTH-D',
                'G11-CITY CARS-A','G11-CITY CARS-B','G11-CITY CARS-C','G11-CITY CARS-D',
                'G11-EURO-CYCLES-A','G11-EURO-CYCLES-B','G11-EURO-CYCLES-C','G11-EURO-CYCLES-D',
                'G11-CELLCOM-A','G11-CELLCOM-B','G11-CELLCOM-C','G11-CELLCOM-D',
                'G11-SAH-A','G11-SAH-B','G11-SAH-C','G11-SAH-D',
                'G11-MPBS-A','G11-MPBS-B','G11-MPBS-C','G11-MPBS-D',
                'G11-SOTIPAPIER-A','G11-SOTIPAPIER-B','G11-SOTIPAPIER-C','G11-SOTIPAPIER-D',
                'G11-Société Délice Holding-A','G11-Société Délice Holding-B','G11-Société Délice Holding-C','G11-Société Délice Holding-D',
                'G11-UADH-A','G11-UADH-B','G11-UADH-C','G11-UADH-D',
                'G11-UNIMED-A','G11-UNIMED-B','G11-UNIMED-C','G11-UNIMED-D',
                'G11-SAM-A','G11-SAM-B','G11-SAM-C','G11D',
                '','','','',
                '','','','',
                '','','','',
                '','','','',
                '','','','',
                '','','','',]
        socialData(argrv[0],time)
        


