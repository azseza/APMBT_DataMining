import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["daDatabase"]
mycol = mydb["daTable"]
the_dict ={
                "Date",
                "socialVar_1",#Balance Comercial
                "socialVar_2",#Pib par trimestre
                "socialVar_3",#market intrest rate 
                "socialVar_4",#Ipi, indus prod index 
                "socialVar_5",#import/export
                "G11-MONOPRIX-H","G11-MONOPRIX-L","G11-MONOPRIX-Avg",
                "G11-SFBT-H","G11-SFBT-L","G11-SFBT-Avg",
                "G11-TUNISAIR-H","G11-TUNISAIR-L","G11-TUNISAIR-Avg",
                "G11-Attijari_Bank-H","G11-Attijari_Bank-L","G11-Attijari_Bank-Avg",
                "G11-BIAT-H","G11-BIAT-L","G11-BIAT-Avg",
                "G11-BH-H","G11-BH-L","G11-BH-Avg",
                "G11-Tunisie_Leasing_et_Factoring-H","G11-Tunisie_Leasing_et_Factoring-L","G11-Tunisie_Leasing_et_Factoring-Avg",
                "G11-BT-H","G11-BT-L","G11-BT-Avg",
                "G11-STB-H","G11-STB-L","G11-STB-Avg",
                "G11-BNA-H","G11-BNA-L","G11-BNA-Avg",
                "G11-ICF-H","G11-ICF-L","G11-ICF-Avg",
                "G11-AMEN BANK-H","G11-AMEN BANK-L","G11-AMEN BANK-Avg",
                "G11-ATB-H","G11-ATB-L","G11-ATB-Avg",
                "G11-UIB-H","G11-UIB-L","G11-UIB-Avg",
                "G11-SIMPAR-H","G11-SIMPAR-L","G11-SIMPAR-Avg",
                "G11-CIL-H","G11-CIL-L","G11-CIL-Avg",
                "G11-ATL-H","G11-ATL-L","G11-ATL-Avg",
                "G11-PGH-H","G11-PGH-L","G11-PGH-Avg",
                "G11-SOTETEL-H","G11-SOTETEL-L","G11-SOTETEL-Avg",
                "G11-SOTUVER-H","G11-SOTUVER-L","G11-SOTUVER-Avg",
                "G11-SOTUMAG-H","G11-SOTUMAG-L","G11-SOTUMAG-Avg",
                "G11-SIAME-H","G11-SIAME-L","G11-SIAME-Avg",
                "G11-TJL-H","G11-TJL-L","G11-TJL-Avg",
                "G11-ELECTROSTAR-H","G11-ELECTROSTAR-L","G11-ELECTROSTAR-Avg",
                "G11-SOTRAPIL-H","G11-SOTRAPIL-L","G11-SOTRAPIL-Avg",
                "G11-SOMOCER-H","G11-SOMOCER-L","G11-SOMOCER-Avg",
                "G11-GIF FILTER SA-H","G11-GIF FILTER SA-L","G11-GIF FILTER SA-Avg",
                "G11-ASSAD-H","G11-ASSAD-L","G11-ASSAD-Avg",
                "G11-WIFACK INTERNATIONAL BANK-H","G11-WIFACK INTERNATIONAL BANK-L","G11-WIFACK INTERNATIONAL BANK-Avg",
                "G11-Société ESSOUKNA-H","G11-Société ESSOUKNA-L","G11-Société ESSOUKNA-Avg",
                "G11-ADWYA-H","G11-ADWYA-L","G11-ADWYA-Avg",
                "G11-TPR-H","G11-TPR-L","G11-TPR-Avg",
                "G11-SOPAT-H","G11-SOPAT-L","G11-SOPAT-Avg",
                "G11-ARTES-H","G11-ARTES-L","G11-ARTES-Avg",
                "G11-HANNIBAL LEASE-H","G11-HANNIBAL LEASE-L","G11-HANNIBAL LEASE-Avg",
                "G11-TUNIS RE-H","G11-TUNIS RE-L","G11-TUNIS RE-Avg",
                "G11-ENNAKL automobiles-H","G11-ENNAKL automobiles-L","G11-ENNAKL automobiles-Avg",
                "G11-Telnet Holding-H","G11-Telnet Holding-L","G11-Telnet Holding-Avg",
                "G11-OTH-H","G11-OTH-L","G11-OTH-Avg",
                "G11-CITY CARS-H","G11-CITY CARS-L","G11-CITY CARS-Avg"
                "G11-EURO-CYCLES-H","G11-EURO-CYCLES-L","G11-EURO-CYCLES-Avg",
                "G11-CELLCOM-H","G11-CELLCOM-L","G11-CELLCOM-Avg",
                "G11-SAH-H","G11-SAH-L","G11-SAH-Avg",
                "G11-MPBS-H","G11-MPBS-L","G11-MPBS-Avg",
                "G11-SOTIPAPIER-H","G11-SOTIPAPIER-H","G11-SOTIPAPIER-Avg",
                "G11-Société Délice Holding-H","G11-Société Délice Holding-L","G11-Société Délice Holding-Avg",
                "G11-UADH-H","G11-UADH-L","G11-UADH-Avg",
                "G11-UNIMED-H","G11-UNIMED-L","G11-UNIMED-Avg",
                "G11-SAM-H","G11-SAM-L","G11-SAM-Avg",
                "Tunindex-H","Tunidex-L","Tunindex-Avg"
                } 
