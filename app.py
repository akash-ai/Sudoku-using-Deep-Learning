from flask import Flask, request, jsonify, render_template
import keras

from model import *

import sys
sys.setrecursionlimit(5000)

app = Flask(__name__)
model = keras.models.load_model('sudoku_model')


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('sudoku_design_frame.html')


@app.route('/predict', methods=['POST'])
def predict():
    # int_features = np.array([int(x) for x in request.form.values()]).reshape((9, 9, 1))

    cell_1 = int(request.form['cell-0'])
    cell_2 = int(request.form['cell-1'])
    cell_3 = int(request.form['cell-2'])
    cell_4 = int(request.form['cell-3'])
    cell_5 = int(request.form['cell-4'])
    cell_6 = int(request.form['cell-5'])
    cell_7 = int(request.form['cell-6'])
    cell_8 = int(request.form['cell-7'])
    cell_9 = int(request.form['cell-8'])
    cell_10 = int(request.form['cell-9'])
    cell_11 = int(request.form['cell-10'])
    cell_12 = int(request.form['cell-11'])
    cell_13 = int(request.form['cell-12'])
    cell_14 = int(request.form['cell-13'])
    cell_15 = int(request.form['cell-14'])
    cell_16 = int(request.form['cell-15'])
    cell_17 = int(request.form['cell-16'])
    cell_18 = int(request.form['cell-17'])
    cell_19 = int(request.form['cell-18'])
    cell_20 = int(request.form['cell-19'])
    cell_21 = int(request.form['cell-20'])
    cell_22 = int(request.form['cell-21'])
    cell_23 = int(request.form['cell-22'])
    cell_24 = int(request.form['cell-23'])
    cell_25 = int(request.form['cell-24'])
    cell_26 = int(request.form['cell-25'])
    cell_27 = int(request.form['cell-26'])
    cell_28 = int(request.form['cell-27'])
    cell_29 = int(request.form['cell-28'])
    cell_30 = int(request.form['cell-29'])
    cell_31 = int(request.form['cell-30'])
    cell_32 = int(request.form['cell-31'])
    cell_33 = int(request.form['cell-32'])
    cell_34 = int(request.form['cell-33'])
    cell_35 = int(request.form['cell-34'])
    cell_36 = int(request.form['cell-35'])
    cell_37 = int(request.form['cell-36'])
    cell_38 = int(request.form['cell-37'])
    cell_39 = int(request.form['cell-38'])
    cell_40 = int(request.form['cell-39'])
    cell_41 = int(request.form['cell-40'])
    cell_42 = int(request.form['cell-41'])
    cell_43 = int(request.form['cell-42'])
    cell_44 = int(request.form['cell-43'])
    cell_45 = int(request.form['cell-44'])
    cell_46 = int(request.form['cell-45'])
    cell_47 = int(request.form['cell-46'])
    cell_48 = int(request.form['cell-47'])
    cell_49 = int(request.form['cell-48'])
    cell_50 = int(request.form['cell-49'])
    cell_51 = int(request.form['cell-50'])
    cell_52 = int(request.form['cell-51'])
    cell_53 = int(request.form['cell-52'])
    cell_54 = int(request.form['cell-53'])
    cell_55 = int(request.form['cell-54'])
    cell_56 = int(request.form['cell-55'])
    cell_57 = int(request.form['cell-56'])
    cell_58 = int(request.form['cell-57'])
    cell_59 = int(request.form['cell-58'])
    cell_60 = int(request.form['cell-59'])
    cell_61 = int(request.form['cell-60'])
    cell_62 = int(request.form['cell-61'])
    cell_63 = int(request.form['cell-62'])
    cell_64 = int(request.form['cell-63'])
    cell_65 = int(request.form['cell-64'])
    cell_66 = int(request.form['cell-65'])
    cell_67 = int(request.form['cell-66'])
    cell_68 = int(request.form['cell-67'])
    cell_69 = int(request.form['cell-68'])
    cell_70 = int(request.form['cell-69'])
    cell_71 = int(request.form['cell-70'])
    cell_72 = int(request.form['cell-71'])
    cell_73 = int(request.form['cell-72'])
    cell_74 = int(request.form['cell-73'])
    cell_75 = int(request.form['cell-74'])
    cell_76 = int(request.form['cell-75'])
    cell_77 = int(request.form['cell-76'])
    cell_78 = int(request.form['cell-77'])
    cell_79 = int(request.form['cell-78'])
    cell_80 = int(request.form['cell-79'])
    cell_81 = int(request.form['cell-80'])


    game = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10,
            cell_11, cell_12, cell_13, cell_14, cell_15, cell_16, cell_17, cell_18, cell_19, cell_20,
            cell_21, cell_22, cell_23, cell_24, cell_25, cell_26, cell_27, cell_28, cell_29, cell_30,
            cell_31, cell_32, cell_33, cell_34, cell_35, cell_36, cell_37, cell_38, cell_39, cell_40,
            cell_41, cell_42, cell_43, cell_44, cell_45, cell_46, cell_47, cell_48, cell_49, cell_50,
            cell_51, cell_52, cell_53, cell_54, cell_55, cell_56, cell_57, cell_58, cell_59, cell_60,
            cell_61, cell_62, cell_63, cell_64, cell_65, cell_66, cell_67, cell_68, cell_69, cell_70,
            cell_71, cell_72, cell_73, cell_74, cell_75, cell_76, cell_77, cell_78, cell_79, cell_80, cell_81]

    #game = np.array(game).reshape((9, 9, 1))

    # np.array([int(j) for j in game]).reshape((9,9,1))

    #game = norm(game)

    game = solve_sudoku(game)

    return render_template('sudoku_design_frame.html', game_output=game)


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = np.array(list(data.values())).reshape((9, 9, 1))
    prediction = norm(prediction)
    prediction = solve_sudoku(prediction)

    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)
