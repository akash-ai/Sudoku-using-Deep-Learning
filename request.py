import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'cell_1': 6, 'cell_2': 3, 'cell_3': 0, 'cell_4': 0, 'cell_5': 0, 'cell_6': 0, 'cell_7': 0, 'cell_8': 0, 'cell_9': 0, 'cell_10': 0,
            'cell_11': 2, 'cell_12': 0, 'cell_13': 0, 'cell_14': 0, 'cell_15': 8, 'cell_16': 9, 'cell_17': 0, 'cell_18': 0, 'cell_19': 4, 'cell_20': 8,
            'cell_21': 0, 'cell_22': 6, 'cell_23': 2, 'cell_24': 0, 'cell_25': 0, 'cell_26': 0, 'cell_27': 0, 'cell_28': 2, 'cell_29': 6, 'cell_30': 0,
            'cell_31': 0, 'cell_32': 0, 'cell_33': 0, 'cell_34': 0, 'cell_35': 0, 'cell_36': 0, 'cell_37': 0, 'cell_38': 1, 'cell_39': 4, 'cell_40': 0,
            'cell_41': 0, 'cell_42': 0, 'cell_43': 7, 'cell_44': 6, 'cell_45': 0, 'cell_46': 0, 'cell_47': 0, 'cell_48': 0, 'cell_49': 0, 'cell_50': 0,
            'cell_51': 0, 'cell_52': 0, 'cell_53': 4, 'cell_54': 9, 'cell_55': 0, 'cell_56': 0, 'cell_57': 0, 'cell_58': 0, 'cell_59': 3, 'cell_60': 1,
            'cell_61': 0, 'cell_62': 7, 'cell_63': 8, 'cell_64': 0, 'cell_65': 0, 'cell_66': 1, 'cell_67': 7, 'cell_68': 0, 'cell_69': 0, 'cell_70': 0,
            'cell_71': 3, 'cell_72': 0, 'cell_73': 0, 'cell_74': 0, 'cell_75': 0, 'cell_76': 0, 'cell_77': 0, 'cell_78': 0, 'cell_79': 0, 'cell_80': 9, 'cell_81': 5})

print(r.json())